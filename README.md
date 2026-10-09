<div align="center">

# AI Security Arsenal

Open source tools for AI security.<br>
**Attack AI · Defend AI · Hack with AI**

[![tools](https://img.shields.io/badge/tools-362-blue)](#contents) [![categories](https://img.shields.io/badge/categories-14-blue)](TEMPLATE.md#categories-fixed) [![updated](https://img.shields.io/badge/updated-2026--10--09-green)](../../commits/main) [![suggest](https://img.shields.io/badge/suggest-a%20tool-orange)](https://github.com/omarkurt/ai-security-arsenal/issues/new?template=add-tool.yml)

[Attack AI](#attack-ai) · [Defend AI](#defend-ai) · [Hack with AI](#hack-with-ai) · [Practice & Measure](#practice--measure)

</div>

Tools only, no articles or standards. GitHub repos with at least 10 stars, each category sorted by last commit; 🗄️ = archived. Missing one? [Suggest it](https://github.com/omarkurt/ai-security-arsenal/issues/new?template=add-tool.yml).

## Contents

| Group | Category | Tools |
| --- | --- | --: |
| Attack AI | [LLM Red Teaming & Scanners](#llm-red-teaming--scanners) | 37 |
|  | [Agent & MCP Security Testing](#agent--mcp-security-testing) | 18 |
|  | [Adversarial ML](#adversarial-ml) | 6 |
|  | [Jailbreak & Injection Payloads](#jailbreak--injection-payloads) | 14 |
|  | [AI Asset Discovery](#ai-asset-discovery) | 4 |
| Defend AI | [Guardrails & AI Firewalls](#guardrails--ai-firewalls) | 24 |
|  | [Agent & MCP Runtime Security](#agent--mcp-runtime-security) | 15 |
|  | [Model & Supply-Chain Security](#model--supply-chain-security) | 6 |
| Hack with AI | [AI Pentest Agents](#ai-pentest-agents) | 63 |
|  | [AI Code Auditing](#ai-code-auditing) | 42 |
|  | [AI Reverse Engineering](#ai-reverse-engineering) | 21 |
|  | [Security Skills for Coding Agents](#security-skills-for-coding-agents) | 50 |
| Practice & Measure | [Vulnerable AI Labs](#vulnerable-ai-labs) | 16 |
|  | [Benchmarks & Datasets](#benchmarks--datasets) | 46 |

## Attack AI

### LLM Red Teaming & Scanners

Probe LLMs and LLM apps for jailbreaks, prompt injection, data leakage and unsafe output.

<sub>OWASP: stage *Test & Evaluate* · landscape *Red Teaming* · risks LLM01, LLM02, LLM05, LLM07, LLM10</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Promptfoo**](https://github.com/promptfoo/promptfoo) | Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare… | ⭐&nbsp;25.8k | 2026-10-09 |
| [**Giskard**](https://github.com/Giskard-AI/giskard-oss) | 🐢 Open-Source Evaluation & Testing library for LLM Agents | ⭐&nbsp;5.9k | 2026-10-09 |
| [**PyRIT**](https://github.com/microsoft/PyRIT) | The Python Risk Identification Tool for generative AI (PyRIT) is an open source framework built to… | ⭐&nbsp;4.6k | 2026-10-09 |
| [**hackmyagent**](https://github.com/opena2a-org/hackmyagent) | Metasploit for AI agents: scan, attack, and fix AI agents and MCP servers. Open source security… | ⭐&nbsp;83 | 2026-10-09 |
| [**garak**](https://github.com/NVIDIA/garak) | the LLM vulnerability scanner | ⭐&nbsp;9.5k | 2026-10-08 |
| [**AI-Infra-Guard**](https://github.com/Tencent/AI-Infra-Guard) | A full-stack AI Red Teaming platform securing AI ecosystems via Agent Scan, Skills Scan, MCP scan… | ⭐&nbsp;6.8k | 2026-10-08 |
| [**nuguard**](https://github.com/NuGuardAI/nuguard) | AI red-teaming tool and LLM security framework to evaluate agentic AI applications. Tests prompt… | ⭐&nbsp;61 | 2026-10-07 |
| [**augustus**](https://github.com/praetorian-inc/augustus) | LLM security testing framework for detecting prompt injection, jailbreaks, and adversarial attacks… | ⭐&nbsp;301 | 2026-10-03 |
| [**AI Scanner**](https://github.com/0din-ai/ai-scanner) | AI model safety scanner built on NVIDIA garak | ⭐&nbsp;674 | 2026-10-02 |
| [**humanbound**](https://github.com/humanbound/humanbound) | Open-source adversarial testing engine, SDK, and CLI for AI agents. Runs locally or against the… | ⭐&nbsp;166 | 2026-10-02 |
| [**DeepTeam**](https://github.com/confident-ai/deepteam) | DeepTeam is a framework to red team LLMs and AI agents. | ⭐&nbsp;3k | 2026-10-01 |
| [**RAGdrag**](https://github.com/itsbroken-ai/RAGdrag) | RAG pipeline security testing toolkit - 27 techniques across 6 kill chain phases, mapped to MITRE… | ⭐&nbsp;42 | 2026-09-30 |
| [**PIForge**](https://github.com/albert-y1n/PIForge) | PIForge: An Open Framework for RL-based Prompt Injection Red Teaming. | ⭐&nbsp;35 | 2026-09-30 |
| [**Purple Llama**](https://github.com/meta-llama/PurpleLlama) | Set of tools to assess and improve LLM security. | ⭐&nbsp;4.4k | 2026-09-29 |
| [**Agentic Security**](https://github.com/msoedov/agentic_security) | Agentic LLM Vulnerability Scanner / AI red teaming kit 🧪 | ⭐&nbsp;2k | 2026-09-22 |
| [**hackagent**](https://github.com/AISecurityLab/hackagent) | HackAgent is an open-source security toolkit to detect vulnerabilities of your AI Agents | ⭐&nbsp;521 | 2026-09-21 |
| [**spikee**](https://github.com/ReversecLabs/spikee) | Simple Prompt Injection Kit for Evaluation and Exploitation | ⭐&nbsp;264 | 2026-09-11 |
| [**Jailbreaker-CE**](https://github.com/SpecterOps/Jailbreaker-CE) | Jailbreaker is a local evaluation tool for testing chatbot and agent-style systems against… | ⭐&nbsp;111 | 2026-09-08 |
| [**EasyJailbreak**](https://github.com/EasyJailbreak/EasyJailbreak) | An easy-to-use Python framework to generate adversarial jailbreak prompts. | ⭐&nbsp;921 | 2026-09-01 |
| [**agentfence**](https://github.com/haggaishachar/agentfence) | AgentFence is an open-source platform for automatically testing AI agent security. It identifies… | ⭐&nbsp;61 | 2026-08-06 |
| [**cryptex-oss**](https://github.com/m4xx101/cryptex-oss) | Open-source LLM red-teaming technique toolkit (162 transforms, 36 mutators, 25 tool surfaces). MIT. | ⭐&nbsp;336 | 2026-06-09 |
| [**LLMInjector**](https://github.com/anmolksachan/LLMInjector) | Burp Suite Extension for LLM Prompt Injection Testing | ⭐&nbsp;50 | 2026-04-06 |
| [**LangBiTe**](https://github.com/SOM-Research/LangBiTe) | A Bias Tester framework for LLMs | ⭐&nbsp;26 | 2026-03-25 |
| [**CEREBRO-RED v2**](https://github.com/Leviticus-Triage/cerebro-red-v2) | CEREBRO-RED v2: Advanced LLM Red Team Research Platform with PAIR Algorithm and LLM-as-a-Judge… | ⭐&nbsp;16 | 2026-03-21 |
| [**FuzzyAI**](https://github.com/cyberark/FuzzyAI) | A powerful tool for automated LLM fuzzing. It is designed to help developers and security… | ⭐&nbsp;1.6k | 2026-02-06 |
| [**EvoSynth**](https://github.com/dongdongunique/EvoSynth) | EvoSynth is a SOTA automated LLM red-teaming framework that evolves executable, code-level… | ⭐&nbsp;60 | 2026-02-04 |
| [**LLAMATOR**](https://github.com/LLAMATOR-Core/llamator) | Red Teaming python-framework for testing chatbots and GenAI systems. | ⭐&nbsp;223 | 2026-01-15 |
| [**promptmap2**](https://github.com/utkusen/promptmap) | a security scanner for custom LLM applications | ⭐&nbsp;1.3k | 2025-12-01 |
| [**Whistleblower**](https://github.com/Repello-AI/whistleblower) | Whistleblower is a offensive security tool for testing against system prompt leakage and capability… | ⭐&nbsp;178 | 2025-10-27 |
| [**counterfit**](https://github.com/Azure/counterfit) | a CLI that provides a generic automation layer for assessing the security of ML models | ⭐&nbsp;942 | 2025-07-18 |
| [**injectlab**](https://github.com/ahow2004/injectlab) | An open-source ATT&CK-style framework and test suite for adversarial LLM security research | ⭐&nbsp;10 | 2025-04-13 |
| [**kereva-scanner**](https://github.com/kereva-dev/kereva-scanner) | Code scanner to check for issues in prompts and LLM calls | ⭐&nbsp;78 | 2025-04-06 |
| [**artkit**](https://github.com/BCG-X-Official/artkit) | Automated prompt-based testing and evaluation of Gen AI applications | ⭐&nbsp;172 | 2025-02-18 |
| [**HouYi**](https://github.com/LLMSecurity/HouYi) | The automated prompt injection framework for LLM-integrated applications. | ⭐&nbsp;276 | 2024-09-12 |
| [**LLMFuzzer**](https://github.com/mnns/LLMFuzzer) | 🧠 LLMFuzzer - Fuzzing Framework for Large Language Models 🧠 LLMFuzzer is the first open-source… | ⭐&nbsp;382 | 2024-02-12 |
| [**PromptInject**](https://github.com/agencyenterprise/PromptInject) | PromptInject is a framework that assembles prompts in a modular fashion to provide a quantitative… | ⭐&nbsp;529 | 2022-11-18 |
| [**deep-pwning**](https://github.com/cchio/deep-pwning) | Metasploit for machine learning. | ⭐&nbsp;570 | 2022-05-17 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### Agent & MCP Security Testing

Scan, audit and pentest AI agents, MCP / A2A servers, agent skills and agent configs.

<sub>OWASP: stage *Test & Evaluate* · landscape *Agentic* · risks ASI01, ASI02, ASI03, ASI04, ASI05</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**SkillSpector**](https://github.com/NVIDIA/SkillSpector) | Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks… | ⭐&nbsp;19.7k | 2026-10-09 |
| [**Skill Scanner**](https://github.com/cisco-ai-defense/skill-scanner) | Security Scanner for Agent Skills | ⭐&nbsp;2.6k | 2026-10-09 |
| [**MCP Scanner**](https://github.com/cisco-ai-defense/mcp-scanner) | Scan MCP servers for potential threats & security findings. | ⭐&nbsp;1.1k | 2026-10-07 |
| [**Agent Scan (ex mcp-scan)**](https://github.com/snyk/agent-scan) | Security scanner for AI agents, MCP servers and agent skills. | ⭐&nbsp;3.1k | 2026-10-06 |
| [**MCPwned**](https://github.com/FenriskSecurity/MCPwned) | MCPwned is a companion extension that enables pentesters to effectively test MCP servers. It… | ⭐&nbsp;20 | 2026-09-28 |
| [**repo-forensics**](https://github.com/alexgreensh/repo-forensics) | Offline security scanner for AI-agent repos, skills, plugins, and MCP servers. | ⭐&nbsp;188 | 2026-09-27 |
| [**inkog**](https://github.com/inkog-io/inkog) | Static security scanner for AI agents. Catches prompt injection, runaway loops, missing oversight… | ⭐&nbsp;30 | 2026-09-16 |
| [**aguara**](https://github.com/garagon/aguara) | The open source security engine for AI agent and supply-chain trust. | ⭐&nbsp;93 | 2026-09-10 |
| [**AgentShield**](https://github.com/affaan-m/agentshield) | AI agent security scanner. Detect vulnerabilities in agent configurations, MCP servers, and tool… | ⭐&nbsp;1.3k | 2026-09-10 |
| [**agent-opfor**](https://github.com/KeyValueSoftwareSystems/agent-opfor) | Open-source adversary emulation for AI agents and MCP servers. | ⭐&nbsp;582 | 2026-08-13 |
| [**AgentSeal**](https://github.com/getagentseal/agentseal) | Security toolkit for AI agents. Scan your machine for dangerous skills and MCP configs, monitor for… | ⭐&nbsp;377 | 2026-06-11 |
| [**A2A Scanner**](https://github.com/cisco-ai-defense/a2a-scanner) | Scan A2A agents for potential threats and security issues | ⭐&nbsp;167 | 2026-04-16 |
| [**MCP Client and Proxy**](https://github.com/appsecco/mcp-client-and-proxy) | A universal MCP client with proxying feature to interact with MCP Servers which support STDIO… | ⭐&nbsp;23 | 2026-04-15 |
| [**MCP-ASD**](https://github.com/hoodoer/MCP-ASD) | MCP Attack Surface Detector - Burp plugin to make manual testing of MCP servers easier in Burp Suite | ⭐&nbsp;33 | 2026-02-26 |
| [**skillguard**](https://github.com/LLMSecurity/skillguard) | Agent Skill Security Auditor — Audit agent skills against OWASP Agentic Top 10 & MITRE ATLAS before… | ⭐&nbsp;11 | 2026-02-25 |
| [**cc-safe**](https://github.com/ykdojo/cc-safe) | Security scanner for Claude Code settings files. Scans for dangerous patterns in your approved… | ⭐&nbsp;60 | 2025-12-10 |
| [**Agentic Radar**](https://github.com/splx-ai/agentic-radar) | A security scanner for your LLM agentic workflows | ⭐&nbsp;1.1k | 2025-11-27 |
| [**MCP Safety Scanner**](https://github.com/johnhalloran321/mcpSafetyScanner) | MCPSafetyScanner - Automated MCP safety auditing and remediation using Agents. More info… | ⭐&nbsp;180 | 2025-04-10 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### Adversarial ML

Craft adversarial examples and measure model robustness.

<sub>OWASP: stage *Test & Evaluate* · landscape *GenAI LLM* · risks LLM04</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Adversarial Robustness Toolbox**](https://github.com/Trusted-AI/adversarial-robustness-toolbox) | Adversarial Robustness Toolbox (ART) - Python Library for Machine Learning Security - Evasion… | ⭐&nbsp;6.3k | 2026-10-08 |
| [**TextAttack**](https://github.com/QData/TextAttack) | TextAttack 🐙 is a Python framework for adversarial attacks, data augmentation, and model training… | ⭐&nbsp;3.5k | 2026-08-15 |
| [**foolbox**](https://github.com/bethgelab/foolbox) | A Python toolbox to create adversarial examples that fool neural networks in PyTorch, TensorFlow… | ⭐&nbsp;3k | 2024-03-04 |
| [**cleverhans**](https://github.com/cleverhans-lab/cleverhans) | An adversarial example library for constructing attacks, building defenses, and benchmarking both | ⭐&nbsp;6.5k | 2023-01-31 |
| [**AdvBox**](https://github.com/advboxes/AdvBox) | Advbox is a toolbox to generate adversarial examples that fool neural networks in… | ⭐&nbsp;1.4k | 2022-08-08 |
| [**advertorch**](https://github.com/BorealisAI/advertorch) | A Toolbox for Adversarial Robustness Research | ⭐&nbsp;1.4k | 2022-05-29 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### Jailbreak & Injection Payloads

Payload collections, attack techniques and proof-of-concept code.

<sub>OWASP: stage *Test & Evaluate* · landscape *Red Teaming* · risks LLM01, LLM07</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Model Inversion Attack ToolBox**](https://github.com/ffhibnese/Model-Inversion-Attack-ToolBox) | A comprehensive toolbox for model inversion attacks and defenses, which is easy to get started. | ⭐&nbsp;197 | 2026-09-15 |
| [**code-review-prompts**](https://github.com/Sw4mpf0x/code-review-prompts) | A collection of useful prompts and system prompts for security-oriented code reviews | ⭐&nbsp;40 | 2026-08-26 |
| [**Arcanum Prompt Injection Taxonomy**](https://github.com/Arcanum-Sec/arc_pi_taxonomy) | The Arcanum Prompt Injection Taxonomy | ⭐&nbsp;777 | 2026-06-29 |
| [**Prompt Injection as Role Confusion**](https://github.com/role-confusion/prompt-injection-as-role-confusion) | Prompt Injection as Role Confusion | ⭐&nbsp;134 | 2026-05-31 |
| [**ChatGPT_DAN**](https://github.com/0xk1h0/ChatGPT_DAN) | ChatGPT DAN, Jailbreaks prompt | ⭐&nbsp;12.6k | 2026-03-02 |
| [**pallms**](https://github.com/mik0w/pallms) | Payloads for Attacking Large Language Models | ⭐&nbsp;149 | 2026-01-13 |
| [**GenAI Attacks (TTPs)**](https://github.com/mbrg/genai-attacks) | A knowledge source about TTPs used to target GenAI-based systems, copilots and agents | ⭐&nbsp;149 | 2025-12-22 |
| [**ChatGPT DAN**](https://github.com/alexisvalentino/Chatgpt-DAN) | DAN - The ‘JAILBREAK’ Version of ChatGPT and How to Use it. (update: this was 3 years ago, might… | ⭐&nbsp;236 | 2025-09-10 |
| [**AI red teaming payloads**](https://github.com/joey-melo/payloads) | Payloads for AI Red Teaming and beyond | ⭐&nbsp;324 | 2025-08-28 |
| [**WideOpenAI**](https://github.com/grepstrength/WideOpenAI) | Short list of indirect prompt injection attacks for OpenAI-based models. | ⭐&nbsp;40 | 2025-08-27 |
| [**llm-security (greshake)**](https://github.com/greshake/llm-security) | New ways of breaking app-integrated LLMs | ⭐&nbsp;2.1k | 2025-07-17 |
| [**AI Exploits**](https://github.com/protectai/ai-exploits) | A collection of real world AI/ML exploits for responsibly disclosed vulnerabilities | ⭐&nbsp;1.8k | 2024-10-23 |
| [**BadDiffusion**](https://github.com/IBM/BadDiffusion) | Official repo to reproduce the paper "How to Backdoor Diffusion Models?" published at CVPR 2023 | ⭐&nbsp;97 | 2024-09-10 |
| [**Basic ML Prompt Injections**](https://github.com/Zierax/Basic-ML-prompt-injections) | llm attacks basic payloads | ⭐&nbsp;11 | 2024-04-15 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### AI Asset Discovery

Find and inventory exposed LLM services, inference servers, MCP endpoints and agents.

<sub>OWASP: stage *Scope & Plan, Govern* · landscape *GenAI LLM, Agentic*</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Julius**](https://github.com/praetorian-inc/julius) | Simple LLM service identification - translate IP:Port to Ollama, vLLM, LiteLLM, or 60+ other AI… | ⭐&nbsp;244 | 2026-10-03 |
| [**Agent Discover Scanner**](https://github.com/Defend-AI-Tech-Inc/agent-discover-scanner) | The industry-standard Agentic Identity & Inventory Scanner. Automatically inventory autonomous… | ⭐&nbsp;21 | 2026-07-28 |
| [**AI OSINT**](https://github.com/7WaySecurity/ai_osint) | 🤖 Curated AI OSINT resources — Google dorks, Shodan queries, GitHub dorks, and techniques to… | ⭐&nbsp;166 | 2026-06-19 |
| [**Knostic MCP-Scanner**](https://github.com/knostic/MCP-Scanner) | Advanced Shodan-based scanner for discovering, verifying, and enumerating Model Context Protocol… | ⭐&nbsp;57 | 2025-07-06 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

## Defend AI

### Guardrails & AI Firewalls

Input / output filtering, prompt-injection and jailbreak detection, LLM firewalls and gateways.

<sub>OWASP: stage *Deploy, Operate* · landscape *GenAI LLM* · risks LLM01, LLM02, LLM05, LLM07</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Secretless AI**](https://github.com/opena2a-org/secretless-ai) | One command to keep secrets out of AI (LLMs). Works with Claude Code, Cursor, Copilot, Windsurf… | ⭐&nbsp;26 | 2026-10-09 |
| [**piighost**](https://github.com/Athroniaeth/piighost) | Reversible PII masking for LLM agents: piighost replaces personal data with placeholders before the… | ⭐&nbsp;14 | 2026-10-08 |
| [**NeMo Guardrails**](https://github.com/NVIDIA-NeMo/Guardrails) | NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based… | ⭐&nbsp;7.3k | 2026-10-07 |
| [**Arcjet**](https://github.com/arcjet/arcjet-js) | Runtime security for AI apps and agents: prompt injection detection, tool-call authorization… | ⭐&nbsp;689 | 2026-10-07 |
| [**TrustGate**](https://github.com/NeuralTrust/TrustGate) | Open-source AI gateway for LLM and agent traffic — multi-provider routing, guardrails, semantic… | ⭐&nbsp;11 | 2026-10-07 |
| [**shellward**](https://github.com/jnMetaCode/shellward) | AI 应用合规网关 · 一行命令体检 AI 项目的「数据出境 / 硬编码密钥 /… | ⭐&nbsp;140 | 2026-09-28 |
| [**prompt-shield**](https://github.com/mthamil107/prompt-shield) | Prompt-injection firewall for LLM applications — 33 input detectors, 9 output scanners, federated… | ⭐&nbsp;17 | 2026-09-26 |
| [**Kiji Proxy**](https://github.com/dataiku/kiji-proxy) | Privacy proxy for your OpenAI requests | ⭐&nbsp;437 | 2026-09-14 |
| [**Armorer Guard**](https://github.com/ArmorerLabs/Armorer-Guard) | Public SDKs and integration contracts for Armorer Guard. | ⭐&nbsp;43 | 2026-08-27 |
| [**Guardrails AI**](https://github.com/guardrails-ai/guardrails) | Adding guardrails to large language models. | ⭐&nbsp;7.5k | 2026-08-26 |
| [**Superagent**](https://github.com/superagent-ai/superagent) | Superagent protects your AI applications against prompt injections, data leaks, and harmful… | ⭐&nbsp;6.8k | 2026-08-25 |
| [**LLM Guard**](https://github.com/protectai/llm-guard) 🗄️ | The Security Toolkit for LLM Interactions | ⭐&nbsp;3.2k | 2026-07-08 |
| [**AgentDoG**](https://github.com/AI45Lab/AgentDoG) | A Diagnostic Guardrail Framework for AI Agent Safety and Security | ⭐&nbsp;700 | 2026-06-08 |
| [**Sentinel AI**](https://github.com/MaxwellCalkin/sentinel-ai) | Real-time AI safety guardrails for LLM apps. 10 scanners: prompt injection, PII, harmful content… | ⭐&nbsp;24 | 2026-03-09 |
| [**hai-guardrails**](https://github.com/presidio-oss/hai-guardrails) | A TypeScript library providing a set of guards for LLM (Large Language Model) applications | ⭐&nbsp;52 | 2026-02-06 |
| [**ZenGuard**](https://github.com/ZenGuard-AI/fast-llm-security-guardrails) | The fastest Trust Layer for AI Agents | ⭐&nbsp;155 | 2026-02-03 |
| [**gpt-oss-safeguard**](https://github.com/openai/gpt-oss-safeguard) |  | ⭐&nbsp;60 | 2026-01-14 |
| [**PIGuard**](https://github.com/leolee99/PIGuard) | [ACL 2025] The official implementation of the paper "PIGuard: Prompt Injection Guardrail via… | ⭐&nbsp;87 | 2025-12-04 |
| [**Trylon Gateway**](https://github.com/trylonai/gateway) | The Open Source Firewall for LLMs. A self-hosted gateway to secure and control AI applications with… | ⭐&nbsp;181 | 2025-06-25 |
| [**CaMeL**](https://github.com/google-research/camel-prompt-injection) | Code for the paper "Defeating Prompt Injections by Design" | ⭐&nbsp;403 | 2025-06-20 |
| [**LangKit**](https://github.com/whylabs/langkit) | 🔍 LangKit: An open-source toolkit for monitoring Large Language Models (LLMs). 📚 Extracts signals… | ⭐&nbsp;998 | 2024-11-22 |
| [**last_layer**](https://github.com/arekusandr/last_layer) | Ultra-fast, low latency LLM prompt injection/jailbreak detection ⛓️ | ⭐&nbsp;136 | 2024-04-28 |
| [**Vigil**](https://github.com/deadbits/vigil-llm) | ⚡ Vigil ⚡ Detect prompt injections, jailbreaks, and other potentially risky Large Language Model… | ⭐&nbsp;505 | 2024-01-31 |
| [**Rebuff**](https://github.com/protectai/rebuff) 🗄️ | LLM Prompt Injection Detector | ⭐&nbsp;1.5k | 2024-01-25 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### Agent & MCP Runtime Security

Runtime control for agents: MCP gateways and firewalls, sandboxes, agent identity, detection rules.

<sub>OWASP: stage *Deploy, Operate, Monitor* · landscape *Agentic* · risks ASI02, ASI03, ASI05, ASI06, ASI10</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**NemoClaw**](https://github.com/NVIDIA/NemoClaw) | Run agents like Hermes, LangChain Deep Agents, and OpenClaw more securely inside NVIDIA OpenShell… | ⭐&nbsp;22.7k | 2026-10-09 |
| [**Agent Identity Management**](https://github.com/opena2a-org/agent-identity-management) | The IAM layer for AI agents: cryptographic identity, capability authorization, and audit trails for… | ⭐&nbsp;67 | 2026-10-09 |
| [**OpenShell**](https://github.com/NVIDIA/OpenShell) | OpenShell is the safe, private runtime for autonomous AI agents. | ⭐&nbsp;15.5k | 2026-10-09 |
| [**Pipelock**](https://github.com/luckyPipewrench/pipelock) | Open-source AI agent firewall for MCP security and agent egress. Scans mediated HTTP, MCP, A2A, and… | ⭐&nbsp;921 | 2026-10-09 |
| [**Agent Threat Rules**](https://github.com/Agent-Threat-Rule/agent-threat-rules) | Open detection-rule standard for AI agent security threats — like Sigma, but for AI agents… | ⭐&nbsp;408 | 2026-10-08 |
| [**agentguard**](https://github.com/GoPlusSecurity/agentguard) | Security guard for AI agents — blocks malicious skills, prevents data leaks, protects secrets. 24… | ⭐&nbsp;467 | 2026-10-08 |
| [**ironcurtain**](https://github.com/provos/ironcurtain) | A secure* runtime for autonomous AI agents. Policy from plain-English constitutions… | ⭐&nbsp;612 | 2026-10-07 |
| [**clawvisor**](https://github.com/clawvisor/clawvisor) | API gateway for purpose-based authorization for AI agents. Human approval for tasks, AI-native… | ⭐&nbsp;283 | 2026-10-03 |
| [**Brood Box**](https://github.com/stacklok/brood-box) | CLI tool for running coding agents inside hardware-isolated microVMs | ⭐&nbsp;75 | 2026-09-16 |
| [**Adrian**](https://github.com/secureagentics/Adrian) | Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious… | ⭐&nbsp;580 | 2026-09-15 |
| [**Claude Code Devcontainer**](https://github.com/trailofbits/claude-code-devcontainer) | Sandboxed devcontainer for running Claude Code in bypass mode safely. Built for security audits and… | ⭐&nbsp;950 | 2026-08-28 |
| [**MCP-Defender**](https://github.com/MCP-Defender/MCP-Defender) | Desktop app that automatically scans and blocks malicious MCP traffic in AI apps like Cursor… | ⭐&nbsp;256 | 2026-06-05 |
| [**MCP Armor (ex mcp-checkpoint)**](https://github.com/aira-security/mcp-armor) | MCP Armor continuously secures and monitors Model Context Protocol operations through static and… | ⭐&nbsp;124 | 2026-03-27 |
| [**secureclaw**](https://github.com/adversa-ai/secureclaw) | SecureClaw - Security Plugin and Skill for OpenClaw OWASP-Aligned | ⭐&nbsp;347 | 2026-02-28 |
| [**Lasso MCP Gateway**](https://github.com/lasso-security/mcp-gateway) | A plugin-based gateway that orchestrates other MCPs and allows developers to build upon it… | ⭐&nbsp;395 | 2026-01-22 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### Model & Supply-Chain Security

Scan model artifacts (pickle, PyTorch, Keras, …) for malicious code.

<sub>OWASP: stage *Develop & Experiment, Release* · landscape *GenAI LLM* · risks LLM03, LLM04, ASI04</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Activation Model Scanner**](https://github.com/GoogleCloudPlatform/activation-model-scanner) | Verify language model safety before deployment by analyzing activation patterns | ⭐&nbsp;33 | 2026-10-07 |
| [**Fickling**](https://github.com/trailofbits/fickling) | A Python pickling decompiler and static analyzer | ⭐&nbsp;670 | 2026-10-01 |
| [**aisbom**](https://github.com/Lab700xOrg/aisbom) | Static security scanner for ML model files — detects pickle bombs, Keras Lambda RCE and GGUF… | ⭐&nbsp;81 | 2026-09-19 |
| [**picklescan**](https://github.com/mmaitre314/picklescan) | Security scanner detecting Python Pickle files performing suspicious actions | ⭐&nbsp;427 | 2026-09-01 |
| [**ModelScan**](https://github.com/protectai/modelscan) | Protection against Model Serialization Attacks | ⭐&nbsp;782 | 2026-02-18 |
| [**AIShield Watchtower**](https://github.com/bosch-aisecurity-aishield/watchtower) | AIShield Watchtower: Dive Deep into AI's Secrets! 🔍 Open-source tool by AIShield for AI model… | ⭐&nbsp;202 | 2025-03-24 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

## Hack with AI

### AI Pentest Agents

LLM agents and assistants that test web apps, APIs and infrastructure.

<sub>OWASP: — (AI for security; outside the OWASP GenAI landscape)</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**CyberStrikeAI**](https://github.com/AIPentest/CyberStrikeAI) | The system of action for AI-native cybersecurity—where intent becomes governed execution, evidence… | ⭐&nbsp;7.2k | 2026-10-09 |
| [**Strix**](https://github.com/usestrix/strix) | Open-source AI penetration testing tool to find and fix your app’s vulnerabilities. | ⭐&nbsp;67.4k | 2026-10-08 |
| [**Nebula**](https://github.com/berylliumsec/nebula) | AI-powered penetration testing assistant for automating recon, note-taking, and vulnerability… | ⭐&nbsp;1.1k | 2026-10-08 |
| [**RedAmon**](https://github.com/samugit83/redamon) | Open-source, self-hosted AI penetration testing framework: maps your attack surface into a graph… | ⭐&nbsp;3k | 2026-10-08 |
| [**CyberStrike**](https://github.com/CyberStrikeus/CyberStrike) | Open-source AI-powered offensive security harness for automated penetration testing. | ⭐&nbsp;3.1k | 2026-10-08 |
| [**Agentic Bug Hunter**](https://github.com/awarexone/Agentic-Bug-Hunter) | AI-powered bug bounty hunting toolkit that works with or without subscription. | ⭐&nbsp;5.3k | 2026-10-08 |
| [**HackGpt**](https://github.com/yashab-cyber/HackGpt) | HackGPT Enterprise is a production-ready, cloud-native AI-powered penetration testing platform… | ⭐&nbsp;1.3k | 2026-10-08 |
| [**RAPTOR**](https://github.com/gadievron/raptor) | Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By using… | ⭐&nbsp;3.9k | 2026-10-08 |
| [**Shannon**](https://github.com/KeygraphHQ/shannon) | Shannon is an AI pentester for web applications and APIs. It analyzes your source code, identifies… | ⭐&nbsp;48.7k | 2026-10-08 |
| [**BugTraceAI-WEB**](https://github.com/BugTraceAI/BugTraceAI-WEB) | Real-time web dashboard for BugTraceAI — scan monitoring, 20+ security tools, and AI-powered… | ⭐&nbsp;26 | 2026-10-07 |
| [**BugTraceAI-CLI**](https://github.com/BugTraceAI/BugTraceAI-CLI) | Autonomous AI-powered security scanner — multi-agent vulnerability detection, exploitation, and… | ⭐&nbsp;185 | 2026-10-07 |
| [**xalgorix**](https://github.com/xalgorix/xalgorix) | Autonomous AI pentesting agents — real-time reconnaissance, vulnerability detection, and… | ⭐&nbsp;1.2k | 2026-10-07 |
| [**pentest-ai**](https://github.com/0xSteph/pentest-ai) | Open-source AI pentester that proves every finding. Machine oracles re-run each exploit; verified… | ⭐&nbsp;1.7k | 2026-10-07 |
| [**Obsius-AI**](https://github.com/ILOVCTRY/Obsius-AI) | AI驱动的智能体协作工具，用于逆向，渗透测试等。 | ⭐&nbsp;12 | 2026-10-07 |
| [**shiftgrid**](https://github.com/BuFuuu/shiftgrid) | More than just an agent harness for pentesting, yet lightweight and transparent. | ⭐&nbsp;41 | 2026-10-07 |
| [**NeuroSploit**](https://github.com/JoasASantos/NeuroSploit) | NeuroSploit is an advanced, AI-powered penetration testing framework designed to automate and… | ⭐&nbsp;1.4k | 2026-10-06 |
| [**Google MCP Security**](https://github.com/google/mcp-security) |  | ⭐&nbsp;531 | 2026-10-06 |
| [**BugTraceAI**](https://github.com/BugTraceAI/BugTraceAI) | Autonomous AI-powered security scanning platform — CLI scanner, web dashboard, and one-command… | ⭐&nbsp;353 | 2026-10-06 |
| [**RedCell**](https://github.com/martian56/redcell) | AI red-team platform. Autonomous LLM agents run a penetration test end to end inside a Kali… | ⭐&nbsp;331 | 2026-10-06 |
| [**Reconner**](https://github.com/rootdr-backup/Reconner) | Self-hosted bug-bounty platform — verification-first recon & DAST, continuous monitoring. Your data… | ⭐&nbsp;129 | 2026-10-06 |
| [**Deep Eye**](https://github.com/zakirkun/deep-eye) | Deep Eye orchestrates multiple AI providers (OpenAI, Claude, Grok, Gemini, OLLAMA, Groq, Mistral… | ⭐&nbsp;2.3k | 2026-10-06 |
| [**PentAGI**](https://github.com/vxcontrol/pentagi) | Fully autonomous AI Agents system capable of performing complex penetration testing tasks | ⭐&nbsp;25.4k | 2026-10-03 |
| [**AI-OPS**](https://github.com/antoninoLorenzo/AI-OPS) | Penetration Testing AI Assistant based on open source LLMs. | ⭐&nbsp;165 | 2026-10-03 |
| [**Dark-Moon**](https://github.com/ASCIT31/Dark-Moon) | Open-source autonomous AI penetration testing. 50 specialist agents across web, API, cloud, Active… | ⭐&nbsp;1k | 2026-10-01 |
| [**Pentest Swarm AI**](https://github.com/Armur-Ai/Pentest-Swarm-AI) | Autonomous penetration testing using a swarm of AI agents. Orchestrates recon, classification… | ⭐&nbsp;2.8k | 2026-10-01 |
| [**violin**](https://github.com/Strategic-Automation/violin) | Supervised, Hermes-native penetration testing profile with 35 routed playbooks, guarded target… | ⭐&nbsp;148 | 2026-09-23 |
| [**pentestagent**](https://github.com/GH05TCREW/pentestagent) | PentestAgent is an AI agent framework for black-box security testing, supporting bug bounty… | ⭐&nbsp;3.2k | 2026-09-21 |
| [**BlacksmithAI**](https://github.com/yohannesgk/blacksmith) | BlacksmithAI is an OPEN-SOURCE advanced penetration testing framework that leverages multiple AI… | ⭐&nbsp;250 | 2026-09-20 |
| [**Cybermes**](https://github.com/Zyrexnn/Cybermes) | Autonomous Offensive Security, Bug Bounty & Red Teaming Agent Framework powered by Hermes Agent… | ⭐&nbsp;926 | 2026-09-16 |
| [**OpenHunterAI**](https://github.com/LumosLab-Innovation/OpenHunterAI) | Local-first AI red team for web, API, and LLM application security. Attacker-style reasoning… | ⭐&nbsp;330 | 2026-09-14 |
| [**hackingBuddyGPT**](https://github.com/ipa-lab/hackingBuddyGPT) | Helping Ethical Hackers use LLMs in 50 Lines of Code or less.. | ⭐&nbsp;1.3k | 2026-09-13 |
| [**mcp-virustotal**](https://github.com/w0h1v/mcp-virustotal) | MCP server for VirusTotal API — analyze URLs, files, IPs, and domains with comprehensive security… | ⭐&nbsp;150 | 2026-09-08 |
| [**PentesterFlow Agent**](https://github.com/PentesterFlow/agent) | Agentic offensive-security in your terminal | ⭐&nbsp;1.4k | 2026-08-31 |
| [**Burp AI Agent**](https://github.com/six2dez/burp-ai-agent) | Burp Suite extension that adds built-in MCP tooling, AI-assisted analysis, privacy controls… | ⭐&nbsp;1.5k | 2026-08-31 |
| [**cyberful**](https://github.com/cyberful/cyberful) | Cyberful is an open-source AI Red Team for discovering, exploiting, verifying, and remediating… | ⭐&nbsp;135 | 2026-08-24 |
| [**CAI**](https://github.com/aliasrobotics/cai) 🗄️ | Cybersecurity AI (CAI), the framework for AI Security | ⭐&nbsp;9.8k | 2026-08-22 |
| [**Pentest AI Agents**](https://github.com/0xSteph/pentest-ai-agents) | Turn Claude Code into your offensive security research assistant. Specialized AI subagents for… | ⭐&nbsp;2.3k | 2026-08-16 |
| [**Pentest Copilot**](https://github.com/bugbasesecurity/pentest-copilot) | Pentest Copilot is an AI-powered browser based ethical hacking assistant tool designed to… | ⭐&nbsp;1.5k | 2026-08-14 |
| [**Burp MCP Server**](https://github.com/PortSwigger/mcp-server) | MCP Server for Burp | ⭐&nbsp;1.2k | 2026-08-12 |
| [**HexStrike AI**](https://github.com/0x4m4/hexstrike-ai) | HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.)… | ⭐&nbsp;12.5k | 2026-08-03 |
| [**cochise**](https://github.com/andreashappe/cochise) | Autonomous Assumed Breach Penetration-Testing Active Directory Networks | ⭐&nbsp;140 | 2026-08-03 |
| [**PentestGPT**](https://github.com/GreyDGL/PentestGPT) | Automated Penetration Testing Agentic Framework Powered by Large Language Models | ⭐&nbsp;15.8k | 2026-07-14 |
| [**Guardian CLI**](https://github.com/zakirkun/guardian-cli) | Guardian is a production-ready AI-powered penetration testing automation CLI tool that leverages… | ⭐&nbsp;1.9k | 2026-06-27 |
| [**AdStrike**](https://github.com/capture0x/AdStrike) | AI-powered modular Active Directory red-team framework for authorized penetration testing, AD… | ⭐&nbsp;356 | 2026-06-11 |
| [**Bug-Bounty-Agents**](https://github.com/matty69v/Bug-Bounty-Agents) | AI-Powered Agents for Bub-Bounty Pentesting and Red-Teaming purposes | ⭐&nbsp;443 | 2026-04-30 |
| [**MCP Security Hub**](https://github.com/FuzzingLabs/mcp-security-hub) | A growing collection of MCP servers bringing offensive security tools to AI assistants. Nmap… | ⭐&nbsp;802 | 2026-04-08 |
| [**h1-brain**](https://github.com/PatrikFehrenbach/h1-brain) | MCP server that connects AI assistants to HackerOne for bug bounty hunting | ⭐&nbsp;356 | 2026-04-07 |
| [**Operant MCP**](https://github.com/operantlabs/operant-mcp) | Turn your AI agent into a hacker by plugging in this MCP | ⭐&nbsp;25 | 2026-04-01 |
| [**Reaper**](https://github.com/ghostsecurity/reaper) | Live validation proxy tool for testing web app vulnerabilities | ⭐&nbsp;886 | 2026-03-24 |
| [**BugTrace-AI**](https://github.com/yz9yt/BugTrace-AI) 🗄️ | [ARCHIVED] Evolved into BugTraceAI v2 — github.com/BugTraceAI/BugTraceAI | ⭐&nbsp;253 | 2026-02-11 |
| [**Cyber-AutoAgent**](https://github.com/westonbrown/Cyber-AutoAgent) 🗄️ | AI agent for autonomous cyber operations | ⭐&nbsp;550 | 2025-11-29 |
| [**Crossbow Agent**](https://github.com/harishsg993010/crossbow-agent) | world's first Opensource fully Autonomous AI Security Engineer | ⭐&nbsp;245 | 2025-11-18 |
| [**Nuclei MCP**](https://github.com/addcontent/nuclei-mcp) | An implementation of a Model Context Protocol (MCP) for the Nuclei scanner. This tool enables… | ⭐&nbsp;49 | 2025-08-04 |
| [**Rogue**](https://github.com/faizann24/rogue) | Automated web vulnerability scanning with LLM agents | ⭐&nbsp;483 | 2025-06-18 |
| [**BloodHound-MCP-AI**](https://github.com/MorDavid/BloodHound-MCP-AI) | BloodHound-MCP-AI is integration that connects BloodHound with AI through Model Context Protocol… | ⭐&nbsp;379 | 2025-06-02 |
| [**FAAST**](https://github.com/yacwagh/FAAST) | Prototype of Full Agentic Application Security Testing, FAAST = SAST + DAST + LLM agents | ⭐&nbsp;69 | 2025-05-01 |
| [**VulnBot**](https://github.com/KHenryAegis/VulnBot) | The repository of VulnBot: Autonomous Penetration Testing for A Multi-Agent Collaborative Framework. | ⭐&nbsp;198 | 2025-04-07 |
| [**mcp-shodan**](https://github.com/ADEOSec/mcp-shodan) | The Shodan MCP Server by ADEO Cybersecurity Services provides cybersecurity professionals with… | ⭐&nbsp;25 | 2025-03-22 |
| [**mythic_mcp**](https://github.com/xpn/mythic_mcp) | A simple POC to expose Mythic as a MCP server | ⭐&nbsp;78 | 2025-03-20 |
| [**mcp-dnstwist**](https://github.com/w0h1v/mcp-dnstwist) | MCP server for dnstwist, a powerful DNS fuzzing tool that helps detect typosquatting, phishing, and… | ⭐&nbsp;51 | 2025-03-03 |
| [**AICA Agent**](https://github.com/aica-iwg/aica-agent) | This project will work towards a fully-functional autonomous intelligent cyberdefense agent with… | ⭐&nbsp;45 | 2024-11-12 |
| [**BurpGPT**](https://github.com/aress31/burpgpt) | A Burp Suite extension that integrates OpenAI's GPT to perform an additional passive scan for… | ⭐&nbsp;2.4k | 2024-06-09 |
| [**Cyber Security LLM Agents**](https://github.com/NVISOsecurity/cyber-security-llm-agents) | A collection of agents that use Large Language Models (LLMs) to perform tasks common on our day to… | ⭐&nbsp;396 | 2024-05-07 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### AI Code Auditing

LLM-driven source code review, variant hunting and vulnerability discovery.

<sub>OWASP: — (AI for security; outside the OWASP GenAI landscape)</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**scrutineer**](https://github.com/alpha-omega-security/scrutineer) | Security through scrutiny | ⭐&nbsp;239 | 2026-10-09 |
| [**argo**](https://github.com/gigioneggiando/argo) | LLM-native static vulnerability detection: point it at a repo and get a reviewable vuln report, the… | ⭐&nbsp;63 | 2026-10-08 |
| [**VulnHunter (Capital One)**](https://github.com/capitalone/VulnHunter) | Agentic AI security tool that applies proactive, attacker-first analysis directly to source code. | ⭐&nbsp;1.1k | 2026-10-07 |
| [**VulnHunter (nealbridges)**](https://github.com/nealbridges/VulnHunter) | Agentic AI security scanner that hunts exploitable vulnerabilities like an adversary, proves them… | ⭐&nbsp;665 | 2026-10-06 |
| [**codecrucible**](https://github.com/block/codecrucible) | A purpose-built Go CLI tool that analyses Git repositories for security vulnerabilities using… | ⭐&nbsp;117 | 2026-10-01 |
| [**grimoire**](https://github.com/JoranHonig/grimoire) | An agentic auditing stack | ⭐&nbsp;88 | 2026-10-01 |
| [**seclab-taskflow-agent**](https://github.com/GitHubSecurityLab/seclab-taskflow-agent) | GitHub Security Lab Taskflow Agent | ⭐&nbsp;263 | 2026-09-28 |
| [**hound**](https://github.com/scabench-org/hound) | Language-agnostic AI auditor that autonomously builds and refines adaptive knowledge graphs for… | ⭐&nbsp;819 | 2026-09-17 |
| [**open-kritt**](https://github.com/Kritt-ai/open-kritt) | Open-source, self-hosted AI vulnerability research tool that orchestrates agents to find and… | ⭐&nbsp;2.2k | 2026-09-15 |
| [**DeepZero**](https://github.com/416rehman/DeepZero) | Find zero-days while you sleep. DeepZero is an automated vulnerability research framework that… | ⭐&nbsp;736 | 2026-09-10 |
| [**Local Vuln Research Pipeline**](https://github.com/theteatoast/local-vuln-research-pipeline) | Fully local vulnerability research pipeline - 14B code-specialized LLM reviews every source file… | ⭐&nbsp;170 | 2026-09-05 |
| [**AutoCVE**](https://github.com/larlarua/AutoCVE) | Agent-driven automated CVE discovery platform for source code auditing, vulnerability verification… | ⭐&nbsp;1.4k | 2026-09-03 |
| [**vulnerability-spoiler-alert**](https://github.com/spaceraccoon/vulnerability-spoiler-alert) | A monitoring hub that watches popular open-source repositories and uses AI to detect when commits… | ⭐&nbsp;161 | 2026-09-01 |
| [**Droid LLM Hunter**](https://github.com/roomkangali/droid-llm-hunter) | Droid LLM Hunter is a tool to scan for vulnerabilities in Android applications using Large Language… | ⭐&nbsp;204 | 2026-08-28 |
| [**Bastet**](https://github.com/OneSavieLabs/Bastet) | Bastet is a comprehensive dataset of common smart contract vulnerabilities in DeFi along with an… | ⭐&nbsp;122 | 2026-08-18 |
| [**SecAuditAI**](https://github.com/tgllsy/SecAuditAI) | 一款集成 CodeQL 静态分析和 LLM (大语言模型) 智能验证的半自动化代码审计工具 | ⭐&nbsp;34 | 2026-08-14 |
| [**defending-code-reference-harness**](https://github.com/anthropics/defending-code-reference-harness) | Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can… | ⭐&nbsp;7.6k | 2026-08-06 |
| [**plamen**](https://github.com/PlamenTSV/plamen) | Autonomous Web3 security audit agent for Claude Code | ⭐&nbsp;303 | 2026-07-15 |
| [**medusa**](https://github.com/Pantheon-Security/medusa) | AI-first security scanner. NEW in v2026.7: Claude Code compromise detection — vet .claude/ hooks… | ⭐&nbsp;1k | 2026-06-24 |
| [**GPT-3 Security Vulnerability Scanner**](https://github.com/chris-koch-penn/gpt3_security_vulnerability_scanner) | GPT-3 found hundreds of security vulnerabilities in this repo - (this was the first real LLM… | ⭐&nbsp;603 | 2026-06-09 |
| [**VulTriage**](https://github.com/vinsontang1/VulTriage) | The code of VulTriage: Triple-Path Context Augmentation for LLM-Based Vulnerability Detection | ⭐&nbsp;10 | 2026-05-10 |
| [**OpenVul**](https://github.com/youpengl/OpenVul) | OpenVul: An Open-Source Post-Training Framework for LLM-Based Vulnerability Detection | ⭐&nbsp;52 | 2026-05-02 |
| [**aether**](https://github.com/l33tdawg/aether) | AI Smart Contract Security Analysis and PoC Generation Framework | ⭐&nbsp;67 | 2026-04-27 |
| [**redai**](https://github.com/kpolley/redai) | AI-driven vulnerability discovery and live validation | ⭐&nbsp;349 | 2026-04-27 |
| [**nano-analyzer**](https://github.com/weareaisle/nano-analyzer) | A minimal LLM-powered zero-day vulnerability scanner by AISLE. | ⭐&nbsp;365 | 2026-04-14 |
| [**ai-sast**](https://github.com/rivian/ai-sast) | AI-powered SAST accelerator built to speed up secure development. | ⭐&nbsp;93 | 2026-03-23 |
| [**Nemesis Auditor**](https://github.com/0xiehnnkta/nemesis-auditor) | The Inescapable Auditor -- iterative deep-logic security audit agent for Claude Code | ⭐&nbsp;243 | 2026-03-16 |
| [**ChiefWiggum**](https://github.com/ant4g0nist/ChiefWiggum) | A Ralph Wiggum-style Claude Code plugin for iterative vulnerability hunting... | ⭐&nbsp;15 | 2026-02-20 |
| [**Slither MCP**](https://github.com/trailofbits/slither-mcp) | MCP server for Slither static analysis of Solidity smart contracts | ⭐&nbsp;97 | 2026-02-13 |
| [**Claude Code Security Review**](https://github.com/anthropics/claude-code-security-review) | An AI-powered security review GitHub Action using Claude to analyze code changes for security… | ⭐&nbsp;6.3k | 2026-02-11 |
| [**xvulnhuntr**](https://github.com/CompassSecurity/xvulnhuntr) 🗄️ | Zero shot vulnerability discovery using LLMs | ⭐&nbsp;12 | 2026-02-03 |
| [**Anamnesis**](https://github.com/SeanHeelan/anamnesis-release) | Automatic Exploit Generation with LLMs | ⭐&nbsp;634 | 2026-01-30 |
| [**BinAIVulHunter**](https://github.com/ke0z/BinAIVulHunter) | Use IDA PRO HexRays decompiler with OpenAI(ChatGPT) to find possible vulnerabilities in binaries | ⭐&nbsp;373 | 2025-11-10 |
| [**Semgrep MCP**](https://github.com/semgrep/mcp) 🗄️ | A MCP server for using Semgrep to scan code for security vulnerabilities. | ⭐&nbsp;687 | 2025-10-28 |
| [**LLMDFA**](https://github.com/chengpeng-wang/LLMDFA) | LLMDFA: Analyzing Dataflow in Code with Large Language Models (NeurIPS 2024) | ⭐&nbsp;215 | 2025-10-24 |
| [**LLMSAN**](https://github.com/chengpeng-wang/LLMSAN) | LLMSAN: Sanitizing Large Language Models in Bug Detection with Data-Flow (EMNLP Findings 2024) | ⭐&nbsp;88 | 2025-10-24 |
| [**slice**](https://github.com/noperator/slice) | SAST + LLM Interprocedural Context Extractor | ⭐&nbsp;210 | 2025-08-20 |
| [**LLM-SmartAudit**](https://github.com/LLMAudit/LLMSmartAuditTool) | LLM-SmartAudit is a cutting-edge tool designed to revolutionize smart contract auditing using… | ⭐&nbsp;77 | 2025-08-17 |
| [**vulnhuntr**](https://github.com/protectai/vulnhuntr) | Zero shot vulnerability discovery using LLMs | ⭐&nbsp;2.8k | 2025-02-06 |
| [**GPTScan**](https://github.com/GPTScan/GPTScan) | ICSE'24 GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program… | ⭐&nbsp;106 | 2024-12-11 |
| [**LLift**](https://github.com/seclab-ucr/LLift) | The source code of project "LLift" (Enhancing static analysis with LLM) | ⭐&nbsp;88 | 2024-03-05 |
| [**audit_gpt**](https://github.com/fuzzland/audit_gpt) | Fine-tuning GPT for Smart Contract Auditing | ⭐&nbsp;165 | 2023-04-23 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### AI Reverse Engineering

LLM / MCP integrations for IDA, Ghidra, Binary Ninja, radare2, JADX, Frida and friends.

<sub>OWASP: — (AI for security; outside the OWASP GenAI landscape)</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**kuna**](https://github.com/Noelo-Lab/kuna) | An agent-first decompiler designed to be refined by other agents. Kuna is written in Rust and was… | ⭐&nbsp;572 | 2026-10-08 |
| [**radare2 MCP**](https://github.com/radareorg/radare2-mcp) | MCP stdio server for radare2 | ⭐&nbsp;318 | 2026-10-05 |
| [**IDA Pro MCP**](https://github.com/mrexodia/ida-pro-mcp) | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. | ⭐&nbsp;12.6k | 2026-09-26 |
| [**pyghidra-mcp**](https://github.com/clearbluejar/pyghidra-mcp) | Python Command-Line Ghidra MCP | ⭐&nbsp;437 | 2026-09-25 |
| [**JADX MCP Server**](https://github.com/zinja-coder/jadx-mcp-server) | MCP server for JADX-AI Plugin | ⭐&nbsp;792 | 2026-09-23 |
| [**JADX AI MCP**](https://github.com/zinja-coder/jadx-ai-mcp) | Plugin for JADX to integrate MCP server | ⭐&nbsp;2.9k | 2026-09-23 |
| [**Kunglao Agent**](https://github.com/amd2g2zz/kunglao-agent) | The reverse-engineering expert agent: plans its own analysis path, derives every fact from raw… | ⭐&nbsp;51 | 2026-09-19 |
| [**OGhidra**](https://github.com/llnl/OGhidra) | OGhidra bridges Large Language Models (LLMs) via Ollama with the Ghidra reverse engineering… | ⭐&nbsp;452 | 2026-09-16 |
| [**ghidra-rpc**](https://github.com/cellebrite-labs/ghidra-rpc) | A Ghidra agentic reverse engineering skill. | ⭐&nbsp;362 | 2026-09-16 |
| [**Android Reverse Engineering Skill**](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Claude Code skill to support Android app's reverse engineering | ⭐&nbsp;8k | 2026-09-08 |
| [**Gepetto**](https://github.com/JusticeRage/Gepetto) | IDA plugin which queries language models to speed up reverse-engineering | ⭐&nbsp;3.5k | 2026-08-15 |
| [**GhidrAssistMCP**](https://github.com/symgraph/GhidrAssistMCP) | An native MCP server extension for Ghidra | ⭐&nbsp;764 | 2026-08-02 |
| [**GhidraGPT**](https://github.com/weirdmachine64/GhidraGPT) | Integrate LLM models directly into Ghidra for AI-enhanced reverse engineering. | ⭐&nbsp;822 | 2026-07-22 |
| [**Apktool MCP Server**](https://github.com/zinja-coder/apktool-mcp-server) | A MCP Server for APK Tool (Part of Android Reverse Engineering MCP Suites) | ⭐&nbsp;667 | 2026-07-02 |
| [**x64dbg MCP**](https://github.com/bromoket/x64dbg_mcp) | Drive x64dbg with your AI. MCP server: 23 mega-tools / 153 endpoints for breakpoints, memory… | ⭐&nbsp;132 | 2026-06-08 |
| [**Reverse Engineering Skills**](https://github.com/hackersifu/reverse-engineering-skills) | Skills related to reverse engineering malware, for various AIs | ⭐&nbsp;38 | 2026-03-12 |
| [**LLM4Decompile**](https://github.com/albertan017/LLM4Decompile) | Reverse Engineering: Decompiling Binary Code with Large Language Models | ⭐&nbsp;7.1k | 2026-02-12 |
| [**Kahlo MCP**](https://github.com/FuzzySecurity/kahlo-mcp) | A Frida MCP server to enable autonomous AI assistance for Android instrumentation | ⭐&nbsp;135 | 2026-02-08 |
| [**GhidraMCP**](https://github.com/LaurieWired/GhidraMCP) | MCP Server for Ghidra | ⭐&nbsp;10.7k | 2025-06-23 |
| [**binaryninja-mcp**](https://github.com/MCPPhalanx/binaryninja-mcp) | Another™ MCP Server for Binary Ninja with superpower 🥵 | ⭐&nbsp;50 | 2025-05-13 |
| [**Frida MCP**](https://github.com/dnakov/frida-mcp) | MCP stdio server for frida | ⭐&nbsp;437 | 2025-05-12 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### Security Skills for Coding Agents

Skill packs and plugins that turn Claude Code, Codex & co. into security assistants.

<sub>OWASP: — (AI for security; outside the OWASP GenAI landscape)</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Security Audit Skill**](https://github.com/netresearch/security-audit-skill) | Agent Skill for PHP security audits - OWASP patterns, vulnerability detection / Claude Code… | ⭐&nbsp;44 | 2026-10-08 |
| [**Claude-BugHunter**](https://github.com/elementalsouls/Claude-BugHunter) | A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash… | ⭐&nbsp;4.8k | 2026-10-08 |
| [**Pashov audit skills**](https://github.com/pashov/skills) | Pashov Audit Group Skills | ⭐&nbsp;1.2k | 2026-10-05 |
| [**forefy-context**](https://github.com/forefy/.context) | AI Agent Skills, Goals and Dynamic Workflows for Security Auditing, Pentesting and Research | ⭐&nbsp;152 | 2026-10-04 |
| [**AI Web3 Security**](https://github.com/pashov/ai-web3-security) |  | ⭐&nbsp;589 | 2026-10-02 |
| [**project-codeguard**](https://github.com/cosai-oasis/project-codeguard) | Project CodeGuard is an open-source, model-agnostic security framework that embeds… | ⭐&nbsp;351 | 2026-09-29 |
| [**Trail of Bits Skills**](https://github.com/trailofbits/skills) | Trail of Bits Claude Code skills for security research, vulnerability detection, and audit workflows | ⭐&nbsp;7.4k | 2026-09-28 |
| [**Ghost Security Skills**](https://github.com/ghostsecurity/skills) | Ghost Security's collection of AppSec skills for AI coding agents | ⭐&nbsp;409 | 2026-09-28 |
| [**reverse-skill**](https://github.com/zhaoxuya520/reverse-skill) | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack… | ⭐&nbsp;40.3k | 2026-09-22 |
| [**web3-bug-bounty-hunting-ai-skills**](https://github.com/awarexone/web3-bug-bounty-hunting-ai-skills) | 18 Claude Code skill files for smart contract security — built from 2,749 Immunefi reports, 681… | ⭐&nbsp;162 | 2026-09-21 |
| [**Public Skills Builder**](https://github.com/awarexone/public-skills-builder) | Generate Claude Code bug bounty skills from public HackerOne reports and GitHub writeups — 18 vuln… | ⭐&nbsp;246 | 2026-09-21 |
| [**Claude-Red**](https://github.com/SnailSploit/Claude-Red) | claude-red is a curated library of offensive security skills designed for the Claude skills system… | ⭐&nbsp;7.4k | 2026-09-19 |
| [**secscan-skill**](https://github.com/atgreen/secscan-skill) | Mirror of https://cave.moxielogic.com/atgreen/secscan-skill | ⭐&nbsp;50 | 2026-09-17 |
| [**bountyforge**](https://github.com/Gabson0x/bountyforge) | all round pentest skill | ⭐&nbsp;442 | 2026-09-16 |
| [**secure-supply-chain-skills**](https://github.com/latiotech/secure-supply-chain-skills) | A set of tools for claude code to fix insecure software supply chain configurations | ⭐&nbsp;29 | 2026-09-15 |
| [**security-audit-skill**](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine-readable… | ⭐&nbsp;26.7k | 2026-09-14 |
| [**ctf-skills**](https://github.com/ljagiello/ctf-skills) | Agent skills for solving CTF challenges - web exploitation, binary pwn, crypto, reverse… | ⭐&nbsp;3.4k | 2026-09-13 |
| [**Claude-Code-CyberSecurity-Skill**](https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill) | 22 production-quality Claude Code Skills for cybersecurity professionals — covering offensive… | ⭐&nbsp;469 | 2026-09-07 |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 817 structured cybersecurity skills for AI agents · Mapped to 6 frameworks: MITRE ATT&CK, NIST CSF… | ⭐&nbsp;34k | 2026-08-31 |
| [**Claude-OSINT**](https://github.com/elementalsouls/Claude-OSINT) | 8 Claude skills · 100+ recon capabilities · 80 secret-regex patterns · 80+ dorks · 9 read-only… | ⭐&nbsp;2.8k | 2026-08-30 |
| [**Claude-AD**](https://github.com/ADScanPro/Claude-AD) | Active Directory pentest methodology for Claude Code: skills, agents and slash commands for… | ⭐&nbsp;211 | 2026-08-24 |
| [**llm-sast-scanner**](https://github.com/SunWeb3Sec/llm-sast-scanner) | A SAST skill that gives AI coding agents structured vulnerability detection across 34 vulnerability… | ⭐&nbsp;287 | 2026-08-22 |
| [**caido-skills**](https://github.com/caido/skills) | 🤹 Caido AI Skills | ⭐&nbsp;279 | 2026-08-13 |
| [**threat-model**](https://github.com/alpha-omega-security/threat-model) | Agent skill for producing threat models for open-source projects | ⭐&nbsp;58 | 2026-08-11 |
| [**secskills**](https://github.com/trilwu/secskills) | Transform Claude Code into your personal security engineer | ⭐&nbsp;157 | 2026-08-06 |
| [**semgrep-skills**](https://github.com/semgrep/skills) | A collection of skills for AI coding agents from Semgrep | ⭐&nbsp;322 | 2026-07-28 |
| [**Web3 Skills**](https://github.com/DarkNavySecurity/web3-skills) | Web3 security skills kit — smart contract auditing, blockchain client analysis, and on-chain… | ⭐&nbsp;114 | 2026-07-21 |
| [**Trail of Bits skills-curated**](https://github.com/trailofbits/skills-curated) | Curated, community-vetted Claude Code plugin marketplace | ⭐&nbsp;513 | 2026-07-14 |
| [**DeepBits Claude Plugins**](https://github.com/DeepBitsTechnology/claude-plugins) | This project equips Claude Code with advanced binary analysis capabilities for tasks such as… | ⭐&nbsp;49 | 2026-07-13 |
| [**SecuritySkills**](https://github.com/UnitOneAI/SecuritySkills) | Open-source security skills for AI coding agents. Grounded in OWASP, NIST, MITRE ATT&CK, CIS. Works… | ⭐&nbsp;79 | 2026-06-18 |
| [**audit-skills**](https://github.com/RuoJi6/audit-skills) | 专注于代码审计skill，最小化轻量化skill，只负责安全边界。 | ⭐&nbsp;1k | 2026-06-16 |
| [**claude-pentest**](https://github.com/Stickman230/claude-pentest) | An open source plugin for enabeling claude to gain offensive pentesting capabilities | ⭐&nbsp;114 | 2026-06-08 |
| [**Awesome Skills Security**](https://github.com/Eyadkelleh/awesome-skills-security) | Security testing toolkit for AI Agent: curated SecLists wordlists, injection payloads, and expert… | ⭐&nbsp;388 | 2026-06-08 |
| [**Hacktron Skills**](https://github.com/HacktronAI/skills) | This repository consists of extensions, that hacktron uses to execute specific workflows in CLI. | ⭐&nbsp;115 | 2026-06-04 |
| [**Claude Secure Coding Rules**](https://github.com/TikiTribe/claude-secure-coding-rules) | Secure Coding Rules for Claude Code with a particular emphasis on AIML projects | ⭐&nbsp;142 | 2026-05-02 |
| [**security-skills**](https://github.com/eth0izzle/security-skills) | A collection of Claude Code skills that help security teams stay secure | ⭐&nbsp;58 | 2026-04-27 |
| [**SlowMist Agent Security**](https://github.com/slowmist/slowmist-agent-security) | SlowMist Agent Security Skill: A comprehensive security review framework for AI agents operating in… | ⭐&nbsp;508 | 2026-04-17 |
| [**SecOpsAgentKit**](https://github.com/AgentSecOps/SecOpsAgentKit) | Security operations toolkit for AI coding agents. Give Claude Code 25+ skills to catch… | ⭐&nbsp;220 | 2026-04-15 |
| [**CD Security Skills**](https://github.com/CDSecurity/cdsecurity-skills) | Claude Code skills for smart contract security — by CD Security | ⭐&nbsp;54 | 2026-04-08 |
| [**red-run**](https://github.com/blacklanternsecurity/red-run) | Offensive security toolkit for Claude Code | ⭐&nbsp;287 | 2026-04-01 |
| [**QuillShield Skills**](https://github.com/quillai-network/quillshield_skills) | Structured skills for smart contract security audits. Infers state invariants, detects semantic… | ⭐&nbsp;130 | 2026-03-30 |
| [**move-auditor-skills**](https://github.com/sanbir/move-auditor-skills) | AI-powered Sui Move security skills for auditing packages that live in an object-centric runtime… | ⭐&nbsp;39 | 2026-03-23 |
| [**scv-scan**](https://github.com/kadenzipfel/scv-scan) | A Claude Code skill that scans Solidity codebases for security vulnerabilities by referencing 36… | ⭐&nbsp;109 | 2026-03-11 |
| [**sec-context**](https://github.com/Arcanum-Sec/sec-context) | AI Code Security Anti-Patterns distilled from 150+ sources to help LLMs generate safer code. | ⭐&nbsp;600 | 2026-02-24 |
| [**bug-reaper**](https://github.com/shaniidev/bug-reaper) | Web2 bug bounty Agent Skill — evidence-based, no AI slop. Covers 18 vulnerability classes across… | ⭐&nbsp;73 | 2026-02-21 |
| [**VibeSec Skill**](https://github.com/BehiSecc/VibeSec-Skill) | This skill helps Claude write secure code and prevent common vulnerabilities. | ⭐&nbsp;1.3k | 2026-02-17 |
| [**claude-skill-security-auditor**](https://github.com/wrsmith108/claude-skill-security-auditor) | Claude Code skill for running structured security audits with actionable remediation plans | ⭐&nbsp;34 | 2026-02-10 |
| [**Supabase Pentest Skills**](https://github.com/yoanbernabeu/supabase-pentest-skills) | 24 AI Agent Skills for professional security auditing of Supabase applications. Detection, key… | ⭐&nbsp;69 | 2026-01-31 |
| [**ffuf Claude Skill**](https://github.com/jthack/ffuf_claude_skill) | This is a "skill" for claude to use FFUF. | ⭐&nbsp;213 | 2025-10-16 |
| [**Cursor Security Rules**](https://github.com/matank001/cursor-security-rules) | This repository contains Cursor Security Rules designed to improve the security of both development… | ⭐&nbsp;380 | 2025-08-27 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

## Practice & Measure

### Vulnerable AI Labs

Deliberately vulnerable LLM apps, agents and MCP servers to practice against.

<sub>OWASP: stage *Test & Evaluate* · landscape *Red Teaming*</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**Damn Vulnerable AI Agent**](https://github.com/opena2a-org/damn-vulnerable-ai-agent) | Damn Vulnerable AI Agent is a deliberately vulnerable AI agent platform for security testing and… | ⭐&nbsp;141 | 2026-10-08 |
| [**Fabraix Playground**](https://github.com/fabraix/playground) | A live environment to stress-test AI agent defenses through adversarial play 🧠 | ⭐&nbsp;76 | 2026-10-06 |
| [**LLMVault**](https://github.com/CyberSunil/LLMVault) | An intentionally vulnerable OWASP LLM Top 10 training platform for AI Security, Prompt Injection… | ⭐&nbsp;336 | 2026-09-28 |
| [**secure-code-game**](https://github.com/skills/secure-code-game) | Learn to code securely while having fun through our popular open source in-editor experience… | ⭐&nbsp;2.8k | 2026-08-13 |
| [**ai-prompt-ctf**](https://github.com/c-goosen/ai-prompt-ctf) | Agentic LLM CTF to test prompt injection attacks and preventions | ⭐&nbsp;38 | 2026-07-29 |
| [**AIGoat**](https://github.com/AISecurityConsortium/AIGoat) | AIGoat - Open-source AI security playground for LLM red teaming. AI Goat provides hands-on labs… | ⭐&nbsp;99 | 2026-04-24 |
| [**Vulnerable MCP Servers Lab**](https://github.com/appsecco/vulnerable-mcp-servers-lab) | A collection of servers which are deliberately vulnerable to learn Pentesting MCP Servers. | ⭐&nbsp;278 | 2025-12-18 |
| [**Damn Vulnerable MCP Server**](https://github.com/harishsg993010/damn-vulnerable-MCP-server) | Damn Vulnerable MCP Server | ⭐&nbsp;1.4k | 2025-12-08 |
| [**AI Red Teaming Playground Labs**](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) | AI Red Teaming playground labs to run AI Red Teaming trainings including infrastructure. | ⭐&nbsp;2.1k | 2025-10-07 |
| [**Damn Vulnerable LLM Agent**](https://github.com/ReversecLabs/damn-vulnerable-llm-agent) |  | ⭐&nbsp;529 | 2025-06-25 |
| [**Tensor Trust**](https://github.com/HumanCompatibleAI/tensor-trust) | A prompt injection game to collect data for robust ML research | ⭐&nbsp;78 | 2024-12-27 |
| [**ScottLogic prompt-injection**](https://github.com/ScottLogic/prompt-injection) | Application which investigates defensive measures against prompt injection attacks on an LLM, with… | ⭐&nbsp;35 | 2024-10-23 |
| [**local-llm-ctf**](https://github.com/BishopFox/local-llm-ctf) | A small go harness that uses Ollama to orchestrate LLMs in a restricted process flow | ⭐&nbsp;19 | 2024-09-10 |
| [**AI Goat**](https://github.com/dhammon/ai-goat) | Learn AI security through a series of vulnerable LLM CTF challenges. No sign ups, no cloud fees… | ⭐&nbsp;368 | 2024-08-22 |
| [**Damn Vulnerable LLM Project**](https://github.com/harishsg993010/DamnVulnerableLLMProject) | A LLM explicitly designed for getting hacked | ⭐&nbsp;178 | 2023-08-02 |
| [**fml-security**](https://github.com/EthicalML/fml-security) | Practical examples of "Flawed Machine Learning Security" together with ML Security best practice… | ⭐&nbsp;125 | 2022-06-06 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

### Benchmarks & Datasets

Datasets and benchmarks for measuring attacks, defenses and AI security agents.

<sub>OWASP: stage *Test & Evaluate* · landscape *Red Teaming*</sub>

| Project | Description | Stars | Last commit |
| --- | --- | --: | --- |
| [**VulnGym**](https://github.com/Tencent/VulnGym) | VulnGym: A Real-World, Project-Level Vulnerability Benchmark for White-Box Vulnerability-Hunting… | ⭐&nbsp;260 | 2026-10-08 |
| [**Bug Hunt Bench**](https://github.com/phuryn/bug-hunt-bench) | Bug Hunt Bench: 105 real bugs in two production repos, frontier coding models (GPT-6, Claude, Grok… | ⭐&nbsp;131 | 2026-10-08 |
| [**Agent Security Bench**](https://github.com/agiresearch/ASB) | Agent Security Bench (ASB) | ⭐&nbsp;310 | 2026-09-30 |
| [**FORGE**](https://github.com/shenyimings/FORGE-Artifacts) | [ICSE'26] FORGE: An LLM-driven Framework for Large-Scale Smart Contract Vulnerability Dataset… | ⭐&nbsp;43 | 2026-09-30 |
| [**Open-Prompt-Injection**](https://github.com/liu00222/Open-Prompt-Injection) | This repository provides a benchmark for prompt injection attacks and defenses in LLMs | ⭐&nbsp;504 | 2026-09-27 |
| [**Vibe Security Radar**](https://github.com/HQ1995/vibe-security-radar) | Tracking vulnerabilities contributed by AI-written code | ⭐&nbsp;112 | 2026-09-26 |
| [**evmbench**](https://github.com/paradigmxyz/evmbench) | Collab with OpenAI. A benchmark and harness for finding and exploiting smart contract bugs | ⭐&nbsp;460 | 2026-09-18 |
| [**CyberGym**](https://github.com/sunblaze-ucb/cybergym) | CyberGym is a large-scale, high-quality cybersecurity evaluation framework designed to rigorously… | ⭐&nbsp;942 | 2026-08-28 |
| [**socbench**](https://github.com/DeepTempo/socbench) | An Open Harness and Benchmark for AI in Cybersecurity Operations. | ⭐&nbsp;66 | 2026-08-25 |
| [**CleanVul**](https://github.com/yikun-li/CleanVul) | CleanVul: Automatic Function-Level Vulnerability Detection in Code Commits Using LLM Heuristics | ⭐&nbsp;23 | 2026-08-20 |
| [**BoxPwnr Traces**](https://github.com/0ca/BoxPwnr-Traces) | LLM agent solving traces, leaderboards, and benchmark results across security CTF and hacking… | ⭐&nbsp;80 | 2026-07-29 |
| [**BoxPwnr**](https://github.com/0ca/BoxPwnr) | A modular framework for benchmarking LLMs and agentic strategies on security challenges across… | ⭐&nbsp;459 | 2026-07-22 |
| [**CWEval**](https://github.com/Co1lin/CWEval) | Simultaneous evaluation on both functionality and security of LLM-generated code. | ⭐&nbsp;47 | 2026-07-20 |
| [**CASTLE Benchmark**](https://github.com/CASTLE-Benchmark/CASTLE-Benchmark) | The CASTLE Benchmark is a modern micro-benchmarking solution to test Static Analyzers and LLMs in… | ⭐&nbsp;30 | 2026-07-20 |
| [**PentestEval**](https://github.com/Richael-y/PentestEval) | A demo of PentestEval, for automated model evaluation in stage-level penetration testing tasks. | ⭐&nbsp;18 | 2026-06-25 |
| [**SecCodeBench**](https://github.com/alibaba/sec-code-bench) | SecCodeBench is a benchmark suite focusing on evaluating the security of code generated by large… | ⭐&nbsp;135 | 2026-06-10 |
| [**AgentDojo**](https://github.com/ethz-spylab/agentdojo) | A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. | ⭐&nbsp;898 | 2026-06-02 |
| [**CyberMetric**](https://github.com/cybermetric/CyberMetric) | CyberMetric dataset | ⭐&nbsp;126 | 2026-05-27 |
| [**AICGSecEval**](https://github.com/Tencent/AICGSecEval) | A.S.E (AICGSecEval) is a repository-level AI-generated code security evaluation benchmark developed… | ⭐&nbsp;663 | 2026-05-25 |
| [**seclens**](https://github.com/mattersec-labs/seclens) | Role-Specific Evaluation of LLMs for Security Vulnerability Detection | ⭐&nbsp;41 | 2026-04-16 |
| [**PINT Benchmark**](https://github.com/lakeraai/pint-benchmark) 🗄️ | A benchmark for prompt injection detection systems. | ⭐&nbsp;199 | 2026-04-02 |
| [**CTFTiny**](https://github.com/NYU-LLM-CTF/CTFTiny) | Official repository for CTFTiny | ⭐&nbsp;20 | 2026-03-10 |
| [**BinaryAudit**](https://github.com/QuesmaOrg/BinaryAudit) | An open-source benchmark for evaluating AI agents' ability to find backdoors hidden in compiled… | ⭐&nbsp;101 | 2026-02-27 |
| [**SCAM**](https://github.com/1Password/SCAM) | SCAM - Security Comprehension Awareness Measure / Open-source benchmark that tests AI agents'… | ⭐&nbsp;136 | 2026-02-12 |
| [**AutoPenBench**](https://github.com/lucagioacchini/auto-pen-bench) | This repo contains the codes of the penetration test benchmark for Generative Agents presented in… | ⭐&nbsp;103 | 2025-10-28 |
| [**baxbench**](https://github.com/logic-star-ai/baxbench) |  | ⭐&nbsp;105 | 2025-10-22 |
| [**scabench**](https://github.com/scabench-org/scabench) | A framework for evaluating AI audit agents using recent real-world data | ⭐&nbsp;118 | 2025-10-04 |
| [**NYU CTF Bench**](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) |  | ⭐&nbsp;179 | 2025-09-22 |
| [**Agentic Misalignment**](https://github.com/anthropic-experimental/agentic-misalignment) |  | ⭐&nbsp;658 | 2025-06-19 |
| [**R-Judge**](https://github.com/Lordog/R-Judge) | R-Judge: Benchmarking Safety Risk Awareness for LLM Agents (EMNLP Findings 2024) | ⭐&nbsp;114 | 2025-05-15 |
| [**wasp**](https://github.com/facebookresearch/wasp) 🗄️ | Official implementation of the WASP web agent security benchmark | ⭐&nbsp;97 | 2025-05-14 |
| [**SecLLMHolmes**](https://github.com/ai4cloudops/SecLLMHolmes) | SecLLMHolmes is a generalized, fully automated, and scalable framework to systematically evaluate… | ⭐&nbsp;68 | 2025-05-04 |
| [**VulDetectBench**](https://github.com/Sweetaroo/VulDetectBench) | A Novel Benchmark evaluating the Deep Capability of Vulnerability Detection with Large Language… | ⭐&nbsp;38 | 2025-04-25 |
| [**JailBreakV_28K**](https://github.com/SaFo-Lab/JailBreakV_28K) | [COLM 2024] JailBreakV-28K: A comprehensive benchmark designed to evaluate the transferability of… | ⭐&nbsp;99 | 2025-04-21 |
| [**jailbreakbench**](https://github.com/JailbreakBench/jailbreakbench) | JailbreakBench: An Open Robustness Benchmark for Jailbreaking Language Models [NeurIPS 2024… | ⭐&nbsp;687 | 2025-03-31 |
| [**robustbench**](https://github.com/RobustBench/robustbench) | RobustBench: a standardized adversarial robustness benchmark [NeurIPS 2021 Benchmarks and Datasets… | ⭐&nbsp;788 | 2025-03-31 |
| [**sorry-bench**](https://github.com/SORRY-Bench/sorry-bench) | Benchmark evaluation code for "SORRY-Bench: Systematically Evaluating Large Language Model Safety… | ⭐&nbsp;87 | 2025-03-01 |
| [**jailbreak_llms**](https://github.com/verazuo/jailbreak_llms) | [CCS'24] A dataset consists of 15,140 ChatGPT prompts from Reddit, Discord, websites, and… | ⭐&nbsp;3.8k | 2024-12-24 |
| [**CS-Eval**](https://github.com/CS-EVAL/CS-Eval) | CS-Eval is a comprehensive evaluation suite for fundamental cybersecurity models or large language… | ⭐&nbsp;67 | 2024-11-27 |
| [**CyberBench**](https://github.com/jpmorganchase/CyberBench) 🗄️ | CyberBench: A Multi-Task Cyber LLM Benchmark | ⭐&nbsp;36 | 2024-11-19 |
| [**VulBench**](https://github.com/Hustcw/VulBench) | This is a benchmark for evaluating the vulnerability discovery ability of automated approaches… | ⭐&nbsp;83 | 2024-11-18 |
| [**strongreject**](https://github.com/alexandrasouly/strongreject) | Repository for "StrongREJECT for Empty Jailbreaks" paper | ⭐&nbsp;161 | 2024-11-03 |
| [**AI-Pentest-Benchmark**](https://github.com/isamu-isozaki/AI-Pentest-Benchmark) | The goal of this repo is to become a benchmark for pentesting | ⭐&nbsp;24 | 2024-10-25 |
| [**ToolSword**](https://github.com/Junjie-Ye/ToolSword) | [ACL 2024] ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across… | ⭐&nbsp;15 | 2024-09-12 |
| [**SECURE**](https://github.com/aiforsec/SECURE) | SECURE: Benchmarking Generative Large Language Models as a Cyber Advisory | ⭐&nbsp;17 | 2024-08-28 |
| [**do-not-answer**](https://github.com/Libr-AI/do-not-answer) | Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs | ⭐&nbsp;347 | 2024-06-07 |

<div align="right"><a href="#contents">↑ back to contents</a></div>

## Contribute

Suggest a tool with the [Add a tool](https://github.com/omarkurt/ai-security-arsenal/issues/new?template=add-tool.yml) issue form, or open a PR: add a row to `data/repos.csv` and run `python3 scripts/build.py`. Details in [TEMPLATE.md](TEMPLATE.md).
