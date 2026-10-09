#!/usr/bin/env python3
"""Render README.md from data/*.csv. Fetches live repo metadata via `gh api`.

Usage: python3 scripts/build.py
"""
import csv, json, subprocess, sys
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MIN_STARS = 10
ISSUE = "https://github.com/omarkurt/ai-security-arsenal/issues/new?template=add-tool.yml"


def load(name):
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


QUERY = """query($o:String!,$n:String!){repository(owner:$o,name:$n){
  full_name:nameWithOwner stargazers_count:stargazerCount archived:isArchived description
  defaultBranchRef{target{...on Commit{committedDate}}}}}"""


def meta(repo):
    owner, name = repo.split("/")
    r = subprocess.run(["gh", "api", "graphql", "-f", f"query={QUERY}", "-f", f"o={owner}", "-f", f"n={name}"],
                       capture_output=True, text=True)
    m = (json.loads(r.stdout or "{}").get("data") or {}).get("repository")
    if m:  # empty repos have no default branch
        m["last_commit"] = ((m.pop("defaultBranchRef") or {}).get("target") or {}).get("committedDate", "")
    return m


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

    with ThreadPoolExecutor(8) as ex:
        metas = dict(zip([r["repo"] for r in repos], ex.map(meta, [r["repo"] for r in repos])))

    rows = {}
    for r in repos:
        m = metas[r["repo"]]
        if m is None:
            warn(f"{r['repo']}: not found (404) — move to skip"); continue
        if m["full_name"].lower() != r["repo"].lower():
            warn(f"{r['repo']}: moved to {m['full_name']} — update repos.csv")
        if m["stargazers_count"] < MIN_STARS:
            warn(f"{r['repo']}: {m['stargazers_count']} stars < {MIN_STARS} — omitted"); continue
        rows.setdefault(r["category"], []).append((r, m))

    total = sum(map(len, rows.values()))
    groups = list(dict.fromkeys(c["group"] for c in cats))
    out = ['<div align="center">', "", "<picture>",
           '  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">',
           '  <img alt="AI Security Arsenal: open source tools to attack, defend and hack with AI" '
           'src="assets/banner-light.svg" width="100%">',
           "</picture>", "",
           " ".join([shield("tools", str(total), "blue", anchor(groups[0])),
                     shield("categories", str(len(cats)), "blue", "TEMPLATE.md#categories-fixed"),
                     shield("updated", date.today().isoformat(), "green", "../../commits/main"),
                     shield("suggest", "a tool", "orange", ISSUE)]), "",
           "</div>", ""]
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

    out += ["## Contribute", "", f"Suggest a tool with the [Add a tool]({ISSUE}) issue form, or open a PR: "
            "add a row to `data/repos.csv` and run `python3 scripts/build.py`. Details in [TEMPLATE.md](TEMPLATE.md).", ""]
    (ROOT / "README.md").write_text("\n".join(out))
    print(f"README.md: {sum(map(len, rows.values()))} repos", file=sys.stderr)

    # Keep the category table in TEMPLATE.md in sync with data/categories.csv.
    table = ["| Group | Key | Category | OWASP mapping |", "| --- | --- | --- | --- |"]
    table += [f"| {c['group']} | `{c['key']}` | {c['title']} | {owasp(c)} |" for c in cats]
    tpl = ROOT / "TEMPLATE.md"
    text = tpl.read_text()
    start, end = "<!-- categories:start -->", "<!-- categories:end -->"
    if start in text and end in text:
        head, rest = text.split(start, 1)
        tpl.write_text(head + start + "\n" + "\n".join(table) + "\n" + end + rest.split(end, 1)[1])
    else:
        warn("TEMPLATE.md: category markers missing — table not updated")


if __name__ == "__main__":
    main()
