"""The synthetic organisation.

Entities are stable for a given seed, so a lookup generated today matches the
events generated tomorrow. Asset and identity data is emitted alongside the
events because half the curriculum's point is that an alert without business
context is not actionable (SPL-03 Topic 5).
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field, asdict
from typing import List

DEPARTMENTS = {
    "finance": 0.14, "engineering": 0.30, "sales": 0.18,
    "operations": 0.16, "hr": 0.07, "executive": 0.03, "it": 0.12,
}
PRIVILEGED_DEPTS = {"it", "executive"}

# Where people actually work. Sign-ins are drawn from the identity's home city,
# not uniformly across the country: without this every user appears to teleport
# between capitals and a geo-velocity detection returns thousands of findings
# that are all artefacts of the generator (SPL-03 Lab 5).
HOME_CITIES = [
    ("Sydney", -33.87, 151.21, 0.38),
    ("Melbourne", -37.81, 144.96, 0.28),
    ("Brisbane", -27.47, 153.03, 0.18),
    ("Perth", -31.95, 115.86, 0.16),
]


@dataclass
class Identity:
    user: str
    full_name: str
    department: str
    priority: str          # low | medium | high | critical
    privileged: bool
    category: str          # employee | service_account | contractor
    workstation: str
    activity: float        # per-user volume multiplier (log-normal)
    home_city: str = "Sydney"
    home_lat: float = -33.87
    home_long: float = 151.21


@dataclass
class Asset:
    host: str
    ip: str
    role: str              # workstation | server | domain_controller | jump_host
    department: str
    priority: str
    is_crown_jewel: bool


@dataclass
class Org:
    identities: List[Identity] = field(default_factory=list)
    assets: List[Asset] = field(default_factory=list)

    def user_names(self):
        return [i.user for i in self.identities]

    def hosts_by_role(self, role):
        return [a for a in self.assets if a.role == role]


_FIRST = ["alice", "ben", "chloe", "dan", "eve", "finn", "grace", "hugo", "isla",
          "jack", "kira", "liam", "mia", "noah", "olive", "pete", "quinn", "ruby",
          "sam", "tara", "umar", "vera", "will", "xena", "yusuf", "zara"]
_LAST = ["nguyen", "smith", "patel", "brown", "wilson", "taylor", "chen", "murphy",
         "kaur", "jones", "lee", "walker", "ryan", "hall", "singh", "obrien"]


def build_org(rng: random.Random, n_users: int = 220, n_servers: int = 40) -> Org:
    org = Org()
    seen = set()
    for i in range(n_users):
        first = rng.choice(_FIRST)
        last = rng.choice(_LAST)
        user = f"{first}.{last}"
        n = 2
        while user in seen:
            user = f"{first}.{last}{n}"
            n += 1
        seen.add(user)

        dept = _weighted(rng, DEPARTMENTS)
        privileged = dept in PRIVILEGED_DEPTS and rng.random() < 0.55
        priority = ("critical" if dept == "executive" else
                    "high" if privileged or dept == "finance" else
                    "medium" if rng.random() < 0.3 else "low")
        home = _pick_home(rng)
        org.identities.append(Identity(
            user=user,
            full_name=f"{first.capitalize()} {last.capitalize()}",
            department=dept,
            priority=priority,
            privileged=privileged,
            category="employee" if rng.random() > 0.08 else "contractor",
            workstation=f"WS-{dept[:3].upper()}-{i:04d}",
            # Log-normal activity: a few people generate far more than the median.
            # This is what makes a global threshold wrong (SPL-09 Topic 8).
            activity=rng.lognormvariate(0.0, 0.55),
            home_city=home[0], home_lat=home[1], home_long=home[2],
        ))

    # Service accounts: low count, high volume, and the usual blind spot.
    for i in range(max(4, n_users // 30)):
        org.identities.append(Identity(
            user=f"svc-{rng.choice(['backup','sql','scan','deploy','monitor'])}{i:02d}",
            full_name="Service Account", department="it", priority="high",
            privileged=True, category="service_account",
            workstation="-", activity=rng.lognormvariate(1.2, 0.4),
        ))

    for ident in org.identities:
        if ident.workstation != "-":
            org.assets.append(Asset(
                host=ident.workstation,
                ip=f"10.20.{rng.randint(1, 60)}.{rng.randint(2, 254)}",
                role="workstation", department=ident.department,
                priority=ident.priority, is_crown_jewel=False,
            ))

    roles = {"server": 0.72, "domain_controller": 0.10, "jump_host": 0.18}
    for i in range(n_servers):
        role = _weighted(rng, roles)
        crown = role in ("domain_controller", "jump_host") or rng.random() < 0.15
        org.assets.append(Asset(
            host=f"SRV-{role[:3].upper()}-{i:03d}",
            ip=f"10.30.{rng.randint(1, 20)}.{rng.randint(2, 254)}",
            role=role,
            department=rng.choice(["it", "engineering", "finance", "operations"]),
            priority="critical" if crown else "high",
            is_crown_jewel=crown,
        ))
    return org


def _pick_home(rng):
    r = rng.uniform(0, sum(c[3] for c in HOME_CITIES))
    upto = 0.0
    for city in HOME_CITIES:
        upto += city[3]
        if r <= upto:
            return city
    return HOME_CITIES[0]


def _weighted(rng, choices):
    total = sum(choices.values())
    r = rng.uniform(0, total)
    upto = 0.0
    for value, weight in choices.items():
        upto += weight
        if r <= upto:
            return value
    return next(iter(choices))


def asset_rows(org: Org):
    return [asdict(a) for a in org.assets]


def identity_rows(org: Org):
    return [asdict(i) for i in org.identities]
