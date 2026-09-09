"""Proxy / DNS / flow events, CIM Web + Network_Traffic + Network_Resolution.

Egress volume is log-normal per host with a per-host median, which is what makes
a global byte threshold wrong and a per-entity robust baseline right
(SPL-09 Topic 8). DGA domains are generated with a distinct character process so
the entropy and n-gram labs have real signal to find.
"""
from __future__ import annotations
import random
import string
from .. import rng as R

TOP_DOMAINS = ["google.com", "microsoft.com", "atlassian.net", "github.com",
               "slack.com", "salesforce.com", "abc.net.au", "news.com.au",
               "aws.amazon.com", "cloudflare.com", "zoom.us", "linkedin.com",
               "splunk.com", "gov.au", "westpac.com.au"]
CATEGORIES = {"business": 0.55, "technology": 0.2, "news": 0.12,
              "social": 0.08, "uncategorised": 0.05}
_VOWELS, _CONSONANTS = "aeiou", "bcdfghjklmnpqrstvwxyz"


def benign_domain(rng):
    if rng.random() < 0.82:
        return rng.choice(TOP_DOMAINS)
    # Pronounceable filler: alternating consonant/vowel keeps entropy moderate,
    # so entropy alone will not separate these from DGA cleanly.
    n = rng.randint(3, 5)
    label = "".join(rng.choice(_CONSONANTS) + rng.choice(_VOWELS) for _ in range(n))
    return f"{label}.{rng.choice(['com', 'net', 'com.au', 'io'])}"


def failed_lookup(rng):
    """A benign name that will not resolve.

    Real estates generate a steady stream of NXDOMAIN — typos, decommissioned
    internal names, and search-domain suffixing. Without these, `reply_code=NXDomain`
    alone identifies the C2 host and SPL-03 Lab 7 collapses into a one-line search
    with no analysis in it. These names are deliberately *low* entropy, so
    NXDOMAIN narrows the candidate set and entropy is still needed to finish the job.
    """
    style = rng.random()
    if style < 0.45:                                    # fat-fingered a real domain
        d = rng.choice(TOP_DOMAINS)
        i = rng.randrange(len(d.split(".")[0]))
        label = list(d.split(".")[0])
        label[i] = rng.choice(_CONSONANTS)
        return ".".join([("".join(label))] + d.split(".")[1:])
    if style < 0.80:                                    # stale internal name
        return "%s%02d.corp.example.com.au" % (
            rng.choice(["print", "fileserv", "oldapp", "wsus", "backup", "vpn"]),
            rng.randint(1, 40))
    return "%s.%s.corp.example.com.au" % (              # search-domain suffixing
        rng.choice(TOP_DOMAINS).split(".")[0],
        rng.choice(["syd", "mel", "bne", "per"]))


def dga_domain(rng, length=None):
    """Uniform random labels: high entropy AND improbable n-grams."""
    n = length or rng.randint(12, 22)
    label = "".join(rng.choice(string.ascii_lowercase) for _ in range(n))
    return f"{label}.{rng.choice(['top', 'xyz', 'info', 'cc', 'su'])}"


def proxy_event(rng, ts, ident, asset, domain=None, bytes_out=None, bytes_in=None):
    d = domain or benign_domain(rng)
    return {
        "_time": ts,
        "sourcetype": "proxy:squid",
        "index": "proxy",
        "user": ident.user,
        "src": asset.ip,
        "src_host": asset.host,
        "dest": d,
        "url": f"https://{d}/",
        "http_method": "GET" if rng.random() < 0.85 else "POST",
        "status": 200 if rng.random() < 0.94 else rng.choice([204, 301, 403, 404, 502]),
        "category": R.pick_weighted(rng, CATEGORIES),
        "bytes_out": int(bytes_out if bytes_out is not None
                         else R.lognormal(rng, 4_000 * ident.activity, 1.15)),
        "bytes_in": int(bytes_in if bytes_in is not None
                        else R.lognormal(rng, 90_000 * ident.activity, 1.3)),
    }


def dns_event(rng, ts, asset, domain, answer=None):
    return {
        "_time": ts,
        "sourcetype": "dns",
        "index": "dns",
        "src": asset.ip,
        "src_host": asset.host,
        "query": domain,
        "query_type": "A",
        "answer": answer or f"104.{rng.randint(16,26)}.{rng.randint(0,255)}.{rng.randint(1,254)}",
        "reply_code": "NoError" if answer is not False else "NXDomain",
    }
