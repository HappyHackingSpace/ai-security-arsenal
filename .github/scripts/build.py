#!/usr/bin/env python3
"""Render README.md from .github/data/*.csv. Fetches live repo metadata via `gh api`.

Usage: python3 .github/scripts/build.py
"""
import csv, json, subprocess, sys, urllib.error, urllib.request
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / ".github" / "data"
MIN_STARS = 10
ISSUE = "https://github.com/HappyHackingSpace/ai-security-arsenal/issues/new?template=add-tool.yml"


def load(name):
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


FIELDS = """full_name:nameWithOwner stargazers_count:stargazerCount archived:isArchived description
  defaultBranchRef{target{...on Commit{committedDate}}}"""


def anonymous_meta(repo):
    """Unauthenticated REST lookup (60 requests/hour), for the few repos a token can't read."""
    try:
        with urllib.request.urlopen(f"https://api.github.com/repos/{repo}", timeout=30) as f:
            d = json.load(f)
    except urllib.error.URLError as e:
        sys.exit(f"{repo}: token access refused and anonymous lookup failed: {e}")
    return {"full_name": d["full_name"], "stargazers_count": d["stargazers_count"], "archived": d["archived"],
            "description": d["description"], "last_commit": d["pushed_at"]}


def meta_batch(repos):
    """Metadata for up to ~50 repos in one GraphQL query (GITHUB_TOKEN allows 1000 points/hour); None if missing."""
    decl, body, args = [], [], []
    for i, repo in enumerate(repos):
        owner, name = repo.split("/")
        decl.append(f"$o{i}:String!,$n{i}:String!")
        body.append(f"r{i}:repository(owner:$o{i},name:$n{i}){{{FIELDS}}}")
        args += ["-f", f"o{i}={owner}", "-f", f"n{i}={name}"]
    query = f"query({','.join(decl)}){{{' '.join(body)}}}"
    r = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}", *args], capture_output=True, text=True)
    resp = json.loads(r.stdout or "{}")
    # Orgs with an IP allow list (e.g. lakeraai) refuse token requests from CI runners; their public repos
    # are still readable anonymously.
    blocked = {e["path"][0] for e in resp.get("errors", []) if e.get("type") == "FORBIDDEN" and e.get("path")}
    errors = [e for e in resp.get("errors", []) if e.get("type") != "NOT_FOUND" and e.get("path", [""])[0] not in blocked]
    if errors or not resp.get("data"):  # never treat an API failure as "repo gone"
        sys.exit(f"gh api graphql failed: {errors or r.stderr.strip()}")
    out = []
    for i in range(len(repos)):
        if f"r{i}" in blocked:
            out.append(anonymous_meta(repos[i])); continue
        m = resp["data"].get(f"r{i}")
        if m:  # empty repos have no default branch
            m["last_commit"] = ((m.pop("defaultBranchRef") or {}).get("target") or {}).get("committedDate", "")
        out.append(m)
    return out


def metas(repos, size=50):
    chunks = [repos[i:i + size] for i in range(0, len(repos), size)]
    with ThreadPoolExecutor(4) as ex:
        return dict(zip(repos, [m for ms in ex.map(meta_batch, chunks) for m in ms]))


def warn(msg):
    print("WARN", msg, file=sys.stderr)


def anchor(title):
    return "#" + "".join(c for c in title.lower().replace(" ", "-") if c.isalnum() or c in "-_")


def short(desc, n=100):
    desc = " ".join((desc or "").split()).replace("|", "/")
    return desc if len(desc) <= n else desc[:n].rsplit(" ", 1)[0].rstrip(",.;:") + "…"


def badges(repo):
    gh, sh = f"https://github.com/{repo}", "https://img.shields.io/github"
    return (f"[![Stars]({sh}/stars/{repo}?style=flat&label=%E2%98%85)]({gh}/stargazers) | "
            f"[![Last commit]({sh}/last-commit/{repo}?style=flat&label=)]({gh}/commits)")


def shield(label, msg, color, link):
    q = lambda t: t.replace("-", "--").replace(" ", "%20")
    return f"[![{label}](https://img.shields.io/badge/{q(label)}-{q(msg)}-{color})]({link})"


def owasp(c):
    if not c["owasp_stage"]:
        return "— (AI for security; outside the OWASP GenAI landscape)"
    parts = [f"stage *{c['owasp_stage']}*", f"landscape *{c['owasp_class']}*"]
    if c["owasp_risks"]:
        parts.append(f"risks {c['owasp_risks']}")
    return " · ".join(parts)


def main():
    cats = load("categories.csv")
    keys = {c["key"] for c in cats} | {"skip"}
    all_rows = load("repos.csv")
    repos = [r for r in all_rows if r["category"] != "skip"]

    seen = {}
    for r in all_rows:
        k = r["repo"].lower()
        if k in seen:
            warn(f"duplicate repo {r['repo']} ({seen[k]} and {r['category']})")
        seen[k] = r["category"]
        if r["category"] not in keys:
            warn(f"unknown category {r['category']!r} for {r['repo']}")

    meta = metas([r["repo"] for r in repos])

    rows = {}
    for r in repos:
        m = meta[r["repo"]]
        if m is None:
            warn(f"{r['repo']}: not found (404) — move to skip"); continue
        if m["full_name"].lower() != r["repo"].lower():
            warn(f"{r['repo']}: moved to {m['full_name']} — update repos.csv")
        if m["stargazers_count"] < MIN_STARS:
            warn(f"{r['repo']}: {m['stargazers_count']} stars < {MIN_STARS} — omitted"); continue
        rows.setdefault(r["category"], []).append((r, m))

    total = sum(map(len, rows.values()))
    groups = list(dict.fromkeys(c["group"] for c in cats))
    out = ['<div align="center">', "", '<img alt="AI Security Arsenal: open source tools to attack, defend and hack with AI" '
           'src=".github/assets/banner.svg" width="100%">', "",
           " ".join([shield("tools", str(total), "blue", anchor(groups[0])),
                     shield("categories", str(len(cats)), "blue", ".github/CONTRIBUTING.md#categories"),
                     shield("updated", date.today().isoformat(), "green", "../../commits/main"),
                     shield("suggest", "a tool", "orange", ISSUE)]), "",
           "</div>", ""]
    out += ["## Contents", ""]
    for g in groups:  # TOC: group → categories, with tool counts
        gc = [c for c in cats if c["group"] == g]
        out.append(f"- **[{g}]({anchor(g)})** `{sum(len(rows.get(c['key'], [])) for c in gc)}`")
        out += [f"  - [{c['title']}]({anchor(c['title'])}) `{len(rows.get(c['key'], []))}`" for c in gc]
    out.append("")

    for c in cats:
        if c["group"] in groups:
            out += [f"## {groups.pop(0)}", ""]
        n = len(rows.get(c["key"], []))
        out += [f"### {c['title']}", "", f"> {c['blurb']}  ", f"> **{n} tools** · OWASP: {owasp(c)}", "",
                "| Project | Description | Stars | Last commit |",
                "| --- | --- | --- | --- |"]
        for r, m in sorted(rows.get(c["key"], []), key=lambda x: (x[1]["stargazers_count"], x[1]["last_commit"]), reverse=True):
            name = r["name"] or m["full_name"].split("/")[1]
            arch = " 🗄️" if m["archived"] else ""
            out.append(f"| [**{name}**](https://github.com/{m['full_name']}){arch} | "
                       f"{short(r['note'] or m['description'])} | {badges(m['full_name'])} |")
        out += ["", '<div align="right"><a href="#top">↑ back to top</a></div>', ""]

    (ROOT / "README.md").write_text("\n".join(out))

    # Data for the search site (.github/site/index.html); generated, not committed.
    site = {"generated": date.today().isoformat(),
            "categories": [{**{k: c[k] for k in ("key", "group", "title", "blurb", "owasp_stage", "owasp_class")},
                            "risks": [x.strip() for x in c["owasp_risks"].split(",") if x.strip()]} for c in cats],
            "tools": [{"name": r["name"] or m["full_name"].split("/")[1], "repo": m["full_name"], "cat": key,
                       "desc": " ".join((r["note"] or m["description"] or "").split()), "stars": m["stargazers_count"],
                       "archived": m["archived"], "pushed": m["last_commit"][:10]}
                      for key, items in rows.items() for r, m in items]}
    (ROOT / ".github" / "site" / "tools.json").write_text(json.dumps(site, ensure_ascii=False, separators=(",", ":")))
    print(f"README.md: {sum(map(len, rows.values()))} repos", file=sys.stderr)

    # Keep the category table in CONTRIBUTING.md in sync with .github/data/categories.csv.
    table = ["| Group | Category |", "| --- | --- |"]
    table += [f"| {c['group']} | {c['title']} |" for c in cats]
    tpl = ROOT / ".github" / "CONTRIBUTING.md"
    text = tpl.read_text()
    start, end = "<!-- categories:start -->", "<!-- categories:end -->"
    if start in text and end in text:
        head, rest = text.split(start, 1)
        tpl.write_text(head + start + "\n" + "\n".join(table) + "\n" + end + rest.split(end, 1)[1])
    else:
        warn("CONTRIBUTING.md: category markers missing — table not updated")


if __name__ == "__main__":
    main()
