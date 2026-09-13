#!/usr/bin/env python3
"""Stream auditd-format events into a file at a controllable rate.

Containers cannot run the real auditd (it needs the kernel audit socket), so
the SA-05 relay lab tails a file that *looks* like /var/log/audit/audit.log:
the record types, field order and msg=audit(ts:serial) framing follow the real
format closely enough that the same rsyslog and Splunk parsing applies.

Pure standard library, no arguments required:

    python3 auditd_stream.py --out /var/log/audit/audit.log --rate 20
    python3 auditd_stream.py --out audit.log --burst 50000     # Lab 3 step 5
    python3 auditd_stream.py --out audit.log --noise debug.log # local7 stream

Each line carries a monotonically increasing serial, so gaps and reordering
are provable at the central store (Lab 3 step 6). The serial is the only
state; stopping and restarting the streamer restarts it at 1 unless --start
is given.
"""
from __future__ import annotations

import argparse
import os
import random
import sys
import time

USERS = [("alice", 1001), ("bob", 1002), ("svc-backup", 1500), ("root", 0), ("carol", 1003)]
SRC_IPS = ["10.20.3.14", "10.20.7.201", "10.20.12.9", "10.20.44.67", "203.0.113.5"]
EXES = ["/usr/bin/sudo", "/usr/bin/passwd", "/usr/bin/chmod", "/usr/bin/cat", "/usr/bin/vi"]
FILES = ["/etc/shadow", "/etc/sudoers", "/var/log/audit/audit.log", "/home/alice/.ssh/authorized_keys",
         "/etc/ssh/sshd_config", "/opt/app/config.yml"]


def _rec(ts, serial, typ, body):
    return f"type={typ} msg=audit({ts:.3f}:{serial}): {body}"


def event(rng, ts, serial):
    """One auditd record chosen from the kinds Lab 4's active checks look for:
    remote logon, privilege escalation, and a file permission change."""
    user, uid = rng.choice(USERS)
    roll = rng.random()
    if roll < 0.35:                                   # remote logon (sshd)
        res = "success" if rng.random() < 0.93 else "failed"
        return _rec(ts, serial, "USER_LOGIN",
                    f"pid={rng.randint(800, 60000)} uid=0 auid={uid} ses={rng.randint(1, 900)} "
                    f"msg='op=login id={uid} exe=\"/usr/sbin/sshd\" hostname={rng.choice(SRC_IPS)} "
                    f"addr={rng.choice(SRC_IPS)} terminal=ssh res={res}'")
    if roll < 0.55:                                   # privilege escalation (sudo)
        cmd = rng.choice(["/usr/bin/systemctl restart rsyslog", "/usr/bin/cat /etc/shadow",
                          "/usr/sbin/useradd deploy", "/usr/bin/apt-get update"])
        return _rec(ts, serial, "USER_CMD",
                    f"pid={rng.randint(800, 60000)} uid={uid} auid={uid} ses={rng.randint(1, 900)} "
                    f"msg='cwd=\"/home/{user}\" cmd={cmd.encode().hex()} exe=\"/usr/bin/sudo\" "
                    f"terminal=pts/0 res=success'")
    if roll < 0.80:                                   # syscall on a watched file
        f = rng.choice(FILES)
        return _rec(ts, serial, "SYSCALL",
                    f"arch=c000003e syscall={rng.choice([2, 90, 257])} success=yes exit=0 "
                    f"a0=7ffd a1=1c1 a2=0 a3=0 items=1 ppid={rng.randint(1, 900)} pid={rng.randint(800, 60000)} "
                    f"auid={uid} uid={uid} gid={uid} euid={uid} tty=pts0 ses={rng.randint(1, 900)} "
                    f"comm=\"{os.path.basename(rng.choice(EXES))}\" exe=\"{rng.choice(EXES)}\" key=\"watch:{f}\"")
    if roll < 0.90:                                   # permission change
        return _rec(ts, serial, "PATH",
                    f"item=0 name=\"{rng.choice(FILES)}\" inode={rng.randint(10000, 999999)} dev=fd:01 "
                    f"mode=0100{rng.choice(['600', '644', '777'])} ouid={uid} ogid={uid} rdev=00:00 nametype=NORMAL")
    return _rec(ts, serial, "CRED_ACQ",
                f"pid={rng.randint(800, 60000)} uid=0 auid={uid} ses={rng.randint(1, 900)} "
                f"msg='op=PAM:setcred grantors=pam_unix acct=\"{user}\" exe=\"/usr/sbin/sshd\" "
                f"hostname={rng.choice(SRC_IPS)} addr={rng.choice(SRC_IPS)} terminal=ssh res=success'")


def main():
    ap = argparse.ArgumentParser(description="Stream auditd-format events into a file.")
    ap.add_argument("--out", required=True, help="file to append audit records to")
    ap.add_argument("--rate", type=float, default=20.0, help="steady events per second")
    ap.add_argument("--burst", type=int, default=0,
                    help="write this many events as fast as possible, then exit")
    ap.add_argument("--noise", help="also append a debug line (local7 stream) here at 5x the rate")
    ap.add_argument("--start", type=int, default=1, help="first serial number")
    ap.add_argument("--seed", type=int, default=1337)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    serial = args.start
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    noise = open(args.noise, "a", buffering=1) if args.noise else None

    with open(args.out, "a", buffering=1) as fh:
        if args.burst:
            t0 = time.time()
            for _ in range(args.burst):
                fh.write(event(rng, time.time(), serial) + "\n"); serial += 1
            print(f"burst: {args.burst} events in {time.time() - t0:.1f}s, last serial {serial - 1}",
                  file=sys.stderr)
            return
        interval = 1.0 / max(args.rate, 0.01)
        while True:
            fh.write(event(rng, time.time(), serial) + "\n"); serial += 1
            if noise:
                for _ in range(5):
                    noise.write(f"debug serial={serial} module=cache hit_ratio={rng.random():.3f}\n")
            time.sleep(interval)


if __name__ == "__main__":
    main()
