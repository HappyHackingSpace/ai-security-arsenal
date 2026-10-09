# ai-security-arsenal

- Scope: AI security **tools** only (attack AI / defend AI / hack with AI). No articles, standards, guides, handbooks or curated lists. Full rules: `TEMPLATE.md` → Rules.
- Categories are **frozen** (4 groups / 14 categories, each mapped to OWASP GenAI landscape stage + class + Top 10 risks in `data/categories.csv`). Don't add or split categories while adding tools; see `TEMPLATE.md` → Categories.
- `README.md` is generated — never edit it by hand. Source of truth: `data/categories.csv`, `data/repos.csv`; render with `python3 scripts/build.py`.
- Update flow: `python3 scripts/inbox.py <raindrop.csv>` → categorize the `TODO` rows → build → fix every `WARN`.
- Obsidian `Clippings/` sweep: keyword pre-filter + `gh` metadata (≥10★, not already in `data/`), then classify with `prompts/clippings-review.md`. high/medium → listed; low → `skip` with note `clippings low-confidence <cat>: …` (candidates to promote by hand).
- Rejected / moved / duplicate repos stay in `repos.csv` with category `skip` and a reason in `note`, so the inbox doesn't resurface them.
- Stdlib-only Python + `gh` CLI; no new dependencies.
