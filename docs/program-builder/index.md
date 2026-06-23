# Program Builder

> Generated examples from `.github/scripts/program_builder.py`. Compose your own program from the designed degrees, one or more majors, or an arbitrary set of courses, and see the education it delivers as NICE/DCWF role completion and KSAT coverage.

## How to build a program

```bash
# A designed degree (shared core + every major in the degree):
python3 .github/scripts/program_builder.py --preset operations-degree

# Shared core + a single major:
python3 .github/scripts/program_builder.py --major TH --name "Threat Hunting"

# Hand-pick individual courses:
python3 .github/scripts/program_builder.py --units F01,F06,OC02,TH03 --no-core
```

## Example programs

- [Bachelor of Cybersecurity Operations (full degree)](operations-degree.md) — Shared core plus all five operational majors — the complete operational degree surface.
- [Bachelor of Cybersecurity Strategy (full degree)](strategy-degree.md) — Shared core plus all three strategic majors — the complete strategic degree surface.
- [Operations + Threat Hunting major](threat-hunting.md) — A realistic single-major program: the 18-unit shared core plus the six Threat Hunting units.
- [Operations + Detection Engineering major](detection-engineering.md) — Shared core plus the six Detection Engineering units.
- [Strategy + Leadership & CISO major](ciso-leadership.md) — Shared core plus the six Leadership & CISO units.
- [Strategy + GRC major](grc.md) — Shared core plus the six Governance, Risk & Compliance units.

