# Adding a tool

Not a maintainer? Open an [Add a tool](https://github.com/HappyHackingSpace/ai-security-arsenal/issues/new?template=add-tool.yml) issue instead.

`README.md` is generated. Edit `.github/data/repos.csv`, then run:

```sh
python3 .github/scripts/build.py          # needs an authenticated `gh` CLI
.github/scripts/preview.sh                # optional: render the README the way GitHub does
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

## Row format: `.github/data/repos.csv`

```
category,repo,name,note
pentest,owner/repo,Display Name,
```

- `category`: a `key` from `.github/data/categories.csv`
- `name`: leave empty to use the repo name
- `note`: leave empty to use the GitHub description; fill it in to override a bad or empty one

## Rejecting a repo

Keep it in the file with category `skip` and the reason in `note`. Skipped rows never render, and
`inbox.py` and future sweeps won't suggest them again.

```
skip,owner/repo,,out of scope: guide/handbook, not a tool
```

## Categories (fixed)

Pick the **group** first (what the tool is for), then the **category** (what it does). Every tool fits one of these;
if it seems to fit two, use its primary purpose: a scanner that also blocks goes where most of its features are.

The table is written by `build.py` from `.github/data/categories.csv`, so don't edit it by hand.

<!-- categories:start -->
| Group | Key | Category | OWASP mapping |
| --- | --- | --- | --- |
| Attack AI | `scanners` | LLM Red Teaming & Scanners | stage *Test & Evaluate* · landscape *Red Teaming* · risks LLM01, LLM02, LLM05, LLM07, LLM10 |
| Attack AI | `agent-testing` | Agent & MCP Security Testing | stage *Test & Evaluate* · landscape *Agentic* · risks ASI01, ASI02, ASI03, ASI04, ASI05 |
| Attack AI | `adversarial-ml` | Adversarial ML | stage *Test & Evaluate* · landscape *GenAI LLM* · risks LLM04 |
| Attack AI | `payloads` | Jailbreak & Injection Payloads | stage *Test & Evaluate* · landscape *Red Teaming* · risks LLM01, LLM07 |
| Attack AI | `discovery` | AI Asset Discovery | stage *Scope & Plan, Govern* · landscape *GenAI LLM, Agentic* |
| Defend AI | `guardrails` | Guardrails & AI Firewalls | stage *Deploy, Operate* · landscape *GenAI LLM* · risks LLM01, LLM02, LLM05, LLM07 |
| Defend AI | `agent-runtime` | Agent & MCP Runtime Security | stage *Deploy, Operate, Monitor* · landscape *Agentic* · risks ASI02, ASI03, ASI05, ASI06, ASI10 |
| Defend AI | `model` | Model & Supply-Chain Security | stage *Develop & Experiment, Release* · landscape *GenAI LLM* · risks LLM03, LLM04, ASI04 |
| Hack with AI | `pentest` | AI Pentest Agents | — (AI for security; outside the OWASP GenAI landscape) |
| Hack with AI | `code-audit` | AI Code Auditing | — (AI for security; outside the OWASP GenAI landscape) |
| Hack with AI | `reversing` | AI Reverse Engineering | — (AI for security; outside the OWASP GenAI landscape) |
| Hack with AI | `skills` | Security Skills for Coding Agents | — (AI for security; outside the OWASP GenAI landscape) |
| Practice & Measure | `labs` | Vulnerable AI Labs | stage *Test & Evaluate* · landscape *Red Teaming* |
| Practice & Measure | `benchmarks` | Benchmarks & Datasets | stage *Test & Evaluate* · landscape *Red Teaming* |
<!-- categories:end -->

How the mapping works:
- **stage** is the nearest lifecycle stage in the [OWASP GenAI Security Solutions Landscape](https://genai.owasp.org/ai-security-solutions-landscape)
  (Scope & Plan, Augm & Fine Tune Data, Develop & Experiment, Test & Evaluate, Release, Deploy, Operate, Monitor, Govern)
- **landscape** is the landscape's solution class: GenAI LLM, Agentic or Red Teaming
- **risks** are the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) (`LLM01`–`LLM10`) and the
  OWASP Top 10 for Agentic Applications 2026 (`ASI01`–`ASI10`) items the category mainly addresses
- **Hack with AI** categories have no OWASP GenAI equivalent: they use AI *for* security instead of securing AI

**The category list is frozen.** Do not add, rename or split categories when adding tools. A change needs all of:
an OWASP stage + class it maps to (or a clear AI-for-security purpose), at least 10 listed tools that fit no existing
category, and an explicit decision recorded in the commit message.

## Importing bookmarks

```sh
python3 .github/scripts/inbox.py ~/Downloads/export.csv   # Raindrop export, or any CSV with a `url` column
```

Prints the GitHub repos not yet in `.github/data/repos.csv` as `TODO,owner/repo,,` rows. Replace `TODO` with a category
(or `skip` plus a reason), paste the rows in, then build.
