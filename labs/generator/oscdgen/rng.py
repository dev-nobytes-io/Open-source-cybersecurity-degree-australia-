"""Seeded sampling helpers, pure standard library.

The lab data must exhibit the statistical properties the curriculum teaches —
log-normal volumes, overdispersed counts, seasonality, heavy tails. Python's
``random`` gives us most of that; Poisson and negative-binomial are built here.

Everything takes an explicit ``random.Random`` so a run is reproducible from a
single seed. Reproducibility is not a nicety: SPL-09's labs compute predictive
values against ground truth, and a grader must be able to regenerate the exact
dataset a learner used.
"""
from __future__ import annotations

import math
import random


def poisson(rng: random.Random, lam: float) -> int:
    """Poisson sample. Knuth for small lambda, normal approximation above 30."""
    if lam <= 0:
        return 0
    if lam < 30.0:
        target = math.exp(-lam)
        k, p = 0, 1.0
        while True:
            p *= rng.random()
            if p <= target:
                return k
            k += 1
    # Normal approximation with continuity correction.
    return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))


def negbin(rng: random.Random, mean: float, dispersion: float) -> int:
    """Negative binomial as a Gamma-mixed Poisson.

    ``dispersion`` > 0 sets the variance-to-mean ratio: var = mean * (1 + mean/d).
    Real security counts are overdispersed; assuming Poisson understates the tail
    and over-alerts (SPL-09 Topic 9).
    """
    if mean <= 0:
        return 0
    if dispersion <= 0:
        return poisson(rng, mean)
    shape = dispersion
    scale = mean / dispersion
    return poisson(rng, rng.gammavariate(shape, scale))


def lognormal(rng: random.Random, median: float, sigma: float) -> float:
    """Log-normal with a given median (not mean) and log-scale sigma."""
    if median <= 0:
        return 0.0
    return rng.lognormvariate(math.log(median), sigma)


def jittered_interval(rng: random.Random, base: float, jitter: float) -> float:
    """Beacon interval: base seconds +/- jitter fraction.

    Beaconing is detected by *low variance* of inter-arrival times, not by volume
    (SPL-09 Topic 9), so the jitter fraction is the difficulty dial.
    """
    return max(1.0, base * (1.0 + rng.uniform(-jitter, jitter)))


def seasonal_factor(ts: float, tz_offset_hours: float = 10.0) -> float:
    """Weekly and daily activity multiplier for Australian business hours.

    Returns roughly 0.05 (deep weekend night) to ~1.6 (weekday mid-morning).
    A threshold fitted to a raw series with this seasonality is simultaneously
    too tight on Monday morning and too loose at 3am Sunday — which is the point
    of SPL-09 Topic 7's deseasonalisation argument.
    """
    local = ts + tz_offset_hours * 3600.0
    hour = (local % 86400.0) / 3600.0
    # Days since Thu 1 Jan 1970; shift so 0 = Monday.
    dow = int((local // 86400.0 + 3) % 7)

    # Twin-peaked working day, minimum around 03:00.
    day = 0.06 + 1.5 * math.exp(-((hour - 10.0) ** 2) / 8.0) \
               + 1.2 * math.exp(-((hour - 15.0) ** 2) / 8.0)
    week = 1.0 if dow < 5 else 0.18
    return day * week


def pick_weighted(rng: random.Random, choices: dict) -> str:
    """Weighted choice from {value: weight}."""
    total = sum(choices.values())
    r = rng.uniform(0, total)
    upto = 0.0
    for value, weight in choices.items():
        upto += weight
        if r <= upto:
            return value
    return next(iter(choices))
