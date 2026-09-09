"""Windows-style authentication events, CIM Authentication model."""
from __future__ import annotations
import random
from .. import rng as R

LOGON_TYPES = {"2": 0.10, "3": 0.55, "10": 0.20, "5": 0.10, "11": 0.05}
FAIL_REASONS = {"0xC000006A": 0.62, "0xC0000064": 0.24, "0xC0000234": 0.09,
                "0xC000006F": 0.05}


def event(rng, ts, ident, asset, success=True, src_ip=None, logon_type=None):
    lt = logon_type or R.pick_weighted(rng, LOGON_TYPES)
    e = {
        "_time": ts,
        "sourcetype": "WinEventLog:Security",
        "index": "wineventlog",
        "EventCode": 4624 if success else 4625,
        "action": "success" if success else "failure",
        "app": "win:remote" if lt in ("3", "10") else "win:local",
        "user": ident.user,
        "src": src_ip or asset.ip,
        "dest": asset.host,
        "dest_ip": asset.ip,
        "Logon_Type": lt,
        "user_category": ident.category,
        "dest_priority": asset.priority,
    }
    if not success:
        e["Failure_Reason"] = R.pick_weighted(rng, FAIL_REASONS)
    return e


def benign_burst(rng, ts, ident, asset):
    """A normal login session: usually success, occasionally a fat-fingered fail."""
    out = []
    if rng.random() < 0.07:
        for i in range(rng.randint(1, 2)):
            out.append(event(rng, ts + i * rng.uniform(2, 20), ident, asset, success=False))
    out.append(event(rng, ts + rng.uniform(0, 40), ident, asset, success=True))
    return out
