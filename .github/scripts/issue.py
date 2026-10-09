#!/usr/bin/env python3
"""Turn an "Add a tool" issue form into a repos.csv row. Used by .github/workflows/issue-to-pr.yml.

Reads the issue body from $ISSUE_BODY (untrusted: never pass it through a shell).
On success: appends the row to .github/data/repos.csv, writes the PR body to $RUNNER_TEMP/body.md
and `repo=`/`key=` to $GITHUB_OUTPUT. On rejection: writes the reason to $RUNNER_TEMP/body.md, exits 1.

Usage: ISSUE_BODY="$(cat body.md)" python3 .github/scripts/issue.py
"""
import csv, os, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build import DATA, MIN_STARS, load, metas, short

REPO = re.compile(r"^(?:https?://github\.com/)?([A-Za-z0-9-]{1,39})/([A-Za-z0-9._-]{1,100}?)(?:\.git)?/?$")
OUT = Path(os.environ.get("RUNNER_TEMP", ".")) / "body.md"


def field(body, label):
    m = re.search(rf"^### {re.escape(label)}\s*\n+(.+?)\s*(?=^### |\Z)", body, re.M | re.S)
    return m.group(1).strip() if m else ""


def reject(msg):
    OUT.write_text(f"🤖 Couldn't turn this into a pull request: {msg}\n\nEdit the issue to fix it and I'll try again.\n")
    print("REJECT", msg, file=sys.stderr)
    sys.exit(1)


def main():
    body = os.environ.get("ISSUE_BODY", "")
    m = REPO.match(field(body, "GitHub repo"))
    if not m or m.group(2) in (".", ".."):
        reject("the **GitHub repo** field must be `owner/repo` or `https://github.com/owner/repo`.")
    repo = asked = f"{m.group(1)}/{m.group(2)}"

    keys = {c["key"]: c["title"] for c in load("categories.csv")}
    k = re.match(r"^[^/]+/ ([a-z-]+):", field(body, "Category"))
    if not k or k.group(1) not in keys:
        reject("pick one of the listed categories.")
    key = k.group(1)

    meta = metas([repo])[repo]
    if meta is None:
        reject(f"`{repo}` was not found on GitHub (private, deleted or misspelled).")
    repo = meta["full_name"]  # canonical name if moved
    known = {r["repo"].lower(): r for r in load("repos.csv")}
    for name in {asked.lower(), repo.lower()} & known.keys():
        r = known[name]
        reject(f"`{repo}` is already listed ({r['category']})." if r["category"] != "skip"
               else f"`{repo}` was reviewed before and left out: {r['note'] or 'no reason given'}.")
    if meta["stargazers_count"] < MIN_STARS:
        reject(f"`{repo}` has {meta['stargazers_count']} stars; the list needs at least {MIN_STARS}.")

    with open(DATA / "repos.csv", "a", newline="") as f:
        csv.writer(f, lineterminator="\n").writerow([key, repo, "", ""])
    desc = short(meta["description"], 200).replace("@", "@​")  # no mentions from third-party text
    archived = " · 🗄️ archived" if meta["archived"] else ""
    OUT.write_text(f"Adds [`{repo}`](https://github.com/{repo}) to **{keys[key]}** (`{key}`).\n\n"
                   f"★ {meta['stargazers_count']}{archived}\n\n> {desc or '(no description)'}\n\n"
                   "Merging this updates README.md automatically.\n")
    with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as f:
        f.write(f"repo={repo}\nkey={key}\n")
    print("OK", key, repo, file=sys.stderr)


if __name__ == "__main__":
    main()
