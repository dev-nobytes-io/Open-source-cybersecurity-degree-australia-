"""Cloud control-plane audit events (Entra-like), CIM Authentication/Change.

Identity is the perimeter in a cloud estate, so these carry the impossible-travel
and legacy-auth signals the SPL-03 investigation topics reference.
"""
from __future__ import annotations
import random

GEO = {
    "AU": [("Sydney", -33.87, 151.21), ("Melbourne", -37.81, 144.96),
           ("Brisbane", -27.47, 153.03), ("Perth", -31.95, 115.86)],
    "NZ": [("Auckland", -36.85, 174.76)],
    "SG": [("Singapore", 1.35, 103.82)],
    "RU": [("Moscow", 55.75, 37.61)],
    "NG": [("Lagos", 6.52, 3.37)],
}


# How often a domestic sign-in comes from somewhere other than the person's home
# city. Real interstate travel exists and should generate a handful of genuine
# geo-velocity hits; if it were zero the lab would have no false positives to
# reason about, and if it were uniform the detection would be pure noise.
DOMESTIC_TRAVEL_RATE = 0.015


def signin(rng, ts, ident, country="AU", success=True, legacy_auth=False, ip=None):
    home = getattr(ident, "home_city", None)
    if country == "AU" and home and rng.random() > DOMESTIC_TRAVEL_RATE:
        city, lat, lon = home, ident.home_lat, ident.home_long
    else:
        city, lat, lon = rng.choice(GEO[country])
    return {
        "_time": ts,
        "sourcetype": "azure:aad:signin",
        "index": "cloud",
        "user": ident.user,
        "action": "success" if success else "failure",
        "src": ip or f"{rng.randint(1,223)}.{rng.randint(0,255)}."
                     f"{rng.randint(0,255)}.{rng.randint(1,254)}",
        "src_country": country,
        "src_city": city,
        "src_lat": lat,
        "src_long": lon,
        "app": "Office365" if not legacy_auth else "IMAP4",
        "authentication_method": "legacy" if legacy_auth else "modern",
        "mfa_result": "satisfied" if success and not legacy_auth else "not_required",
        "signature": "UserLoggedIn" if success else "UserLoginFailed",
    }
