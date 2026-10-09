#!/usr/bin/env python3
"""Print GitHub repos from a Raindrop CSV export (or any CSV with a `url` column)
that are not yet in .github/data/repos.csv, as ready-to-paste rows.

Usage: python3 .github/scripts/inbox.py ~/Downloads/AI.csv
"""
import csv, re, sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / ".github" / "data"
GH = re.compile(r"https?://github\.com/([^/#?]+/[^/#?]+)")

with open(DATA / "repos.csv", newline="") as f:
    known = {r["repo"].lower() for r in csv.DictReader(f)}

new = []
with open(sys.argv[1], newline="") as f:
    for r in csv.DictReader(f):
        m = GH.match(r["url"].strip())
        if m:
            repo = m.group(1).removesuffix(".git")
            if repo.lower() not in known:
                known.add(repo.lower())
                new.append(f"TODO,{repo},,")

print(f"# repos.csv — {len(new)} new", *new, sep="\n")
