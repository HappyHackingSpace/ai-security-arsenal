# Clippings review prompt

Used to triage GitHub repos pre-filtered from the Obsidian `Clippings/` folder (or any bookmark dump)
before they go into `.github/data/repos.csv`. Category keys come from `.github/data/categories.csv`; scope rules mirror `CONTRIBUTING.md`.

---

You are curating **ai-security-arsenal**: a list of open source **AI security tools**. Attack AI. Defend AI. Hack with AI.

**In scope**: the repo is a **tool** (CLI, library, framework, server, MCP server, plugin, agent skill pack,
benchmark or dataset, vulnerable lab, payload collection) whose *primary purpose* is one of:
- attacking, testing or red-teaming LLMs, AI agents, MCP servers, agent skills or ML models
- defending them (guardrails, prompt-injection detection, agent/MCP runtime control, model scanning)
- using LLMs/agents to do offensive or defensive security work (pentest, code audit, reverse engineering, recon)

**Out of scope** (`skip`): blog posts, paper-only repos, standards, guides, handbooks, courses, curated/awesome lists;
general LLM/agent frameworks, apps, prompt libraries, coding assistants, inference servers; generic security tools
with no AI angle; malware/RAT/C2/phishing builders; anything you cannot judge from the given data.
When in doubt, `skip`, because precision beats recall.

**Categories** (fixed; see the table in `CONTRIBUTING.md`). Pick the group, then the category:
- Attack AI: `scanners` (LLM red teaming & scanners), `agent-testing` (scan/audit/pentest agents, MCP/A2A, skills),
  `adversarial-ml`, `payloads` (jailbreak & injection payloads, PoCs), `discovery` (find/inventory exposed AI services and agents)
- Defend AI: `guardrails` (filters, injection detectors, LLM firewalls), `agent-runtime` (MCP gateways, agent sandboxes,
  agent identity, detection rules), `model` (model / ML supply-chain scanning)
- Hack with AI: `pentest`, `code-audit`, `reversing`, `skills` (security skills/plugins for coding agents)
- Practice & Measure: `labs` (vulnerable apps/playgrounds), `benchmarks` (datasets/benchmarks)

Never invent a category; if nothing fits, `skip`.

**Output** one CSV row per input item, no header, no commentary:
`category,owner/repo,Display Name,confidence,reason`

`confidence` is `high` / `medium` / `low`. `reason` ≤ 12 words, no commas. Quote any field that contains a comma.
Use the item's real `owner/repo` (as given, after redirects).
