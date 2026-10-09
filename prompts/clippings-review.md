# Clippings review prompt

Used to triage GitHub repos pre-filtered from the Obsidian `Clippings/` folder (or any bookmark dump)
before they go into `data/repos.csv`. Category keys come from `data/categories.csv`; scope rules mirror `TEMPLATE.md`.

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

**Categories:** `scanners` (LLM scanners & red teaming), `agents` (agent/MCP/skill security), `guardrails`,
`discovery` (finding exposed AI services), `model` (model/ML supply chain), `adversarial-ml` (adversarial example /
robustness libraries), `pentest` (AI pentest agents & assistants), `code-audit` (AI code auditing & vuln discovery),
`reversing` (LLM/MCP integrations for IDA, Ghidra, radare2, JADX, Frida…), `skills` (security skills/plugins for
coding agents), `payloads` (payloads, TTPs, research PoCs), `labs` (vulnerable apps/playgrounds),
`benchmarks` (datasets/benchmarks).

**Output** one CSV row per input item, no header, no commentary:
`category,owner/repo,Display Name,confidence,reason`

`confidence` is `high` / `medium` / `low`. `reason` ≤ 12 words, no commas. Quote any field that contains a comma.
Use the item's real `owner/repo` (as given, after redirects).
