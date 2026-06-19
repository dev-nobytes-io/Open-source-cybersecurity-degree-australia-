#!/usr/bin/env python3
"""
Stage all markdown files into wiki_src/ for the MkDocs build.

MkDocs requires docs_dir to be a child of the config directory, so this script
copies every .md file from the repo root into wiki_src/ preserving directory
structure. wiki_src/ is ephemeral — generated at build time and gitignored.

Note: the repo's templates/ directory is copied to resources/ because MkDocs
always excludes a directory named templates/ (reserved for Jinja2 theme overrides).
"""
import shutil
import pathlib

ROOT = pathlib.Path(".")
DEST = pathlib.Path("wiki_src")
SKIP = {"wiki_src", "site", ".git", "node_modules"}
RENAMES = {"templates": "resources"}

if DEST.exists():
    shutil.rmtree(DEST)

count = 0
for path in sorted(ROOT.rglob("*.md")):
    if set(path.parts) & SKIP:
        continue
    # Apply top-level directory renames
    parts = list(path.parts)
    if len(parts) > 1 and parts[0] in RENAMES:
        parts[0] = RENAMES[parts[0]]
    target = DEST / pathlib.Path(*parts)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)
    count += 1

# Fix markdown links in staged files: replace renamed directory references
# so that links like [foo](templates/bar.md) become [foo](resources/bar.md)
for old, new in RENAMES.items():
    for staged in DEST.rglob("*.md"):
        text = staged.read_text(encoding="utf-8")
        if f"({old}/" in text or f"]({old})" in text:
            staged.write_text(text.replace(f"({old}/", f"({new}/"), encoding="utf-8")

print(f"Staged {count} markdown files into {DEST}/")
