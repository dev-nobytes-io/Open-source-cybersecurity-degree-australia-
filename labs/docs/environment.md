# Lab environment

## Single instance (Splunk Free)

```bash
python3 generator/generate.py --days 14
cd docker && docker compose -f compose.single.yml up -d
```

Splunk Web: <http://localhost:8000>. First start takes 2–4 minutes.

**The Free licence has no authentication** — you are dropped in as an
admin-level user with no login. That is why the compose file binds to
`127.0.0.1` only. Never expose this port, and never load real data into it.
This is not a lab quirk: it is the reason SPL-06 Topic 9 says a Free instance
holding real personal information is a notifiable-breach problem.

### Confirming ingestion

```
| tstats count where index=* by index
```

Expect roughly (14-day default, seed 1337):

| Index | Events |
|---|---|
| `proxy` | ~30,000 |
| `sysmon` | ~28,000 |
| `wineventlog` | ~21,000 |
| `dns` | ~13,500 |
| `cloud` | ~8,600 |
| `risk` | ~760 |

If an index is empty, check the container can read `/data` and that
`data/events/<index>.json` exists on the host.

## Distributed (trial licence required)

```bash
cd docker && docker compose -f compose.distributed.yml up -d
```

One search head, two indexers. **This will not work on the Free licence** —
Free has no distributed search. That constraint is examined in the Enterprise
Admin blueprint at 10% and is the subject of SPL-06 Lab 8.

## Resetting

```bash
docker compose -f compose.single.yml down -v   # -v drops indexed data
python3 generator/generate.py --days 14        # regenerate
docker compose -f compose.single.yml up -d
```

Because the generator is seeded, a reset returns you to a byte-identical
dataset. Nothing is lost by starting over.

## What is deliberately absent

| Capability | Why |
|---|---|
| Enterprise Security | Premium licensed app. Cannot be shipped. The `risk` index is synthesised instead, which is enough for the RBA labs and gives you ground truth ES would not. |
| Splunk SOAR | Separate licensed product; availability for learning use is unverified. |
| Real malware / live C2 | Never appropriate in a teaching lab. Scenarios are synthetic log records only. |
| Internet egress from the container | Not needed. Keeps the lab safe to run on a work laptop. |
