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
_B32 = "abcdefghijklmnopqrstuvwxyz234567"
_HEX = "0123456789abcdef"

# Ordinary English words, for the dictionary DGA. Wordlist DGAs are the case
# character entropy is structurally blind to: `correcthorsebattery` is
# maximally malicious and entirely unremarkable to an entropy threshold.
_WORDS = ["correct", "horse", "battery", "staple", "harbour", "summer", "copper",
          "silver", "market", "garden", "window", "planet", "forest", "river",
          "stone", "bridge", "candle", "pepper", "yellow", "orange", "velvet",
          "packet", "router", "cotton", "anchor", "lantern", "meadow", "quarry"]


def high_entropy_benign(rng):
    """Benign hostnames that look exactly like a DGA to an entropy threshold.

    These are the false positives entropy actually produces in a real estate,
    and without them SPL-09 Lab 5 measures entropy against a straw man: the
    generator's uniform-random DGA is precisely the distribution entropy is
    optimal for, so it scores 100% precision and teaches nothing.

    All four kinds are long, so they land in the same `len >= 12` band the
    detection uses and cannot be separated by length alone.
    """
    kind = rng.random()
    if kind < 0.35:                                     # CDN / object-store hash
        return "%s.cdn.example-media.net" % "".join(
            rng.choice(_HEX) for _ in range(rng.randint(24, 32)))
    if kind < 0.60:                                     # DKIM selector
        return "%s._domainkey.%s" % (
            "".join(rng.choice(_B32) for _ in range(rng.randint(16, 24))),
            rng.choice(TOP_DOMAINS))
    if kind < 0.85:                                     # UUID subdomain
        u = "".join(rng.choice(_HEX) for _ in range(32))
        return "%s-%s-%s-%s-%s.telemetry.example-saas.com" % (
            u[:8], u[8:12], u[12:16], u[16:20], u[20:])
    return "%s.token.example-auth.io" % "".join(        # base32 token
        rng.choice(_B32) for _ in range(rng.randint(20, 28)))


def benign_domain(rng):
    roll = rng.random()
    if roll < 0.80:
        return rng.choice(TOP_DOMAINS)
    if roll < 0.815:
        # A modest slice, deliberately. These are the false positives entropy
        # produces, and real estates have them — but spread thinly across many
        # hosts, which is what makes a *per-host* view recover the signal a
        # per-domain view loses (SPL-09 Lab 5).
        return high_entropy_benign(rng)
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


def dga_domain(rng, length=None, style=None):
    """An algorithmically generated domain, in one of two families.

    ``uniform`` draws characters uniformly: high entropy and improbable n-grams,
    the textbook case. ``wordlist`` concatenates dictionary words, which has
    *low* character entropy and is invisible to an entropy threshold at any
    cut-point — the failure mode entropy cannot be tuned out of.

    Both families appear in the data, so SPL-09 Lab 5 can measure a detector
    against the case it handles and the case it does not, rather than only the
    former.
    """
    style = style or "uniform"
    tld = rng.choice(["top", "xyz", "info", "cc", "su"])
    if style == "wordlist":
        label = "".join(rng.sample(_WORDS, rng.randint(2, 3)))
        return f"{label}.{tld}"
    n = length or rng.randint(12, 22)
    label = "".join(rng.choice(string.ascii_lowercase) for _ in range(n))
    return f"{label}.{tld}"


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
