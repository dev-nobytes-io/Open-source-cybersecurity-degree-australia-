"""Sysmon-style process creation, CIM Endpoint/Processes model."""
from __future__ import annotations
import random
from .. import rng as R

BENIGN = {
    "chrome.exe": 0.24, "outlook.exe": 0.18, "teams.exe": 0.12, "explorer.exe": 0.10,
    "code.exe": 0.08, "excel.exe": 0.08, "svchost.exe": 0.07, "python.exe": 0.05,
    "git.exe": 0.04, "powershell.exe": 0.04,
}
PARENTS = {"chrome.exe": "explorer.exe", "outlook.exe": "explorer.exe",
           "teams.exe": "explorer.exe", "explorer.exe": "userinit.exe",
           "code.exe": "explorer.exe", "excel.exe": "explorer.exe",
           "svchost.exe": "services.exe", "python.exe": "cmd.exe",
           "git.exe": "code.exe", "powershell.exe": "explorer.exe"}

# Living-off-the-land binaries. Present benignly at low rate so the labs cannot
# be solved by "any LOLBin = bad" — the signal is context, not the binary.
LOLBINS = ["certutil.exe", "bitsadmin.exe", "rundll32.exe", "regsvr32.exe",
           "mshta.exe", "wmic.exe", "cscript.exe"]


def event(rng, ts, ident, asset, name=None, parent=None, cmdline=None):
    proc = name or R.pick_weighted(rng, BENIGN)
    par = parent or PARENTS.get(proc, "explorer.exe")
    return {
        "_time": ts,
        "sourcetype": "XmlWinEventLog:Sysmon",
        "index": "sysmon",
        "EventCode": 1,
        "user": ident.user,
        "dest": asset.host,
        "process_name": proc,
        "parent_process_name": par,
        "process": cmdline or f"C:\\Windows\\System32\\{proc}",
        "process_id": rng.randint(600, 32000),
    }


def benign(rng, ts, ident, asset):
    if rng.random() < 0.012:
        lol = rng.choice(LOLBINS)
        return event(rng, ts, ident, asset, name=lol, parent="cmd.exe",
                     cmdline=f"C:\\Windows\\System32\\{lol} /benign-maintenance")
    return event(rng, ts, ident, asset)
