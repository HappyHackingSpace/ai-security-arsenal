# Adding a tool

`README.md` is generated. Edit `data/repos.csv`, then run:

```sh
python3 scripts/build.py          # needs an authenticated `gh` CLI
scripts/preview.sh                # optional: render the README the way GitHub does
```

## Rules

A repo is listed only if **all** of these hold:

1. **It is a tool.** Something you install, run, import or point at a target: CLI, library, framework, server,
   MCP server, plugin, agent skill pack, benchmark or dataset, vulnerable lab, payload collection.
   Not a blog post, paper-only repo, standard, guide, handbook, course or curated list.
2. **It is about AI security**, in one of three directions:
   - **attack AI**: test or red-team LLMs, agents, MCP servers, skills, models
   - **defend AI**: guardrails, detectors, runtime control, model / supply-chain scanning
   - **hack with AI**: an LLM or agent does the security work (pentest, code audit, reversing, recon)

   A generic security tool with no AI angle does not qualify, and neither does a generic AI tool with no security angle.
3. **Open source on GitHub, ≥ 10 stars.** The build enforces this and omits anything below.
4. **No offensive payload builders**: malware, RAT, C2 or phishing kit generators are out, even if AI-powered.
5. **One category per repo**, chosen by primary purpose. No duplicates (the build warns).
6. **Canonical name.** If a repo moved, use the new `owner/repo`. Archived repos may stay; they get 🗄️.
7. **Zero `WARN` lines** from `build.py` before committing.

## Row format: `data/repos.csv`

```
category,repo,name,note
pentest,owner/repo,Display Name,
```

- `category`: a `key` from `data/categories.csv`
- `name`: leave empty to use the repo name
- `note`: leave empty to use the GitHub description; fill it in to override a bad or empty one

## Rejecting a repo

Keep it in the file with category `skip` and the reason in `note`. Skipped rows never render, and
`inbox.py` and future sweeps won't suggest them again.

```
skip,owner/repo,,out of scope: guide/handbook, not a tool
```

## New category: `data/categories.csv`

```
key,title,blurb
my-key,Section Title,One sentence on what belongs here.
```

Row order is the README order. Add a category only when at least 3 tools need it.

## Importing bookmarks

```sh
python3 scripts/inbox.py ~/Downloads/export.csv   # Raindrop export, or any CSV with a `url` column
```

Prints the GitHub repos not yet in `data/repos.csv` as `TODO,owner/repo,,` rows. Replace `TODO` with a category
(or `skip` plus a reason), paste the rows in, then build.
