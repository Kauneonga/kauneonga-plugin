# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Cursor, Copilot and others)
working in this repository.

## What this repository is

The official Kauneonga agent plugin. It packages skills and one MCP connector for
clients of answering services that run on Kauneonga, so they can
work with their messages, To Dos and on-call schedules from Claude, ChatGPT and other
agents. There is no application code here: the package is manifests, Markdown skills,
one logo, a packaging script and offline checks.

- Website: https://www.kauneonga.com/
- MCP connector: `https://mcp.kauneonga.com/api/v2/mcp` (Streamable HTTP, OAuth 2.0)
- How agents authenticate: https://www.kauneonga.com/auth.md
- Product documentation: https://www.kauneonga.com/docs/

## Layout

| Path | Purpose |
|---|---|
| `plugin.json` | Portable Agent Plugins manifest (agent-plugins.org), including the ChatGPT listing |
| `mcp.json` | Portable connector configuration with the sign-in declaration |
| `.claude-plugin/plugin.json` | Claude plugin manifest |
| `.claude-plugin/marketplace.json` | Claude marketplace entry for this repository |
| `.mcp.json` | Claude connector configuration |
| `skills/<name>/SKILL.md` | Skills, one shared source for every agent |
| `assets/logo.png` | Listing logo |
| `scripts/build_chatgpt_package.py` | Builds the ChatGPT upload ZIP into `dist/` |
| `tests/test_package.py` | Offline structure and safety checks |
| `docs/MAINTAINING.md` | Maintainer guide; read it before changing manifests |

## Checks

Run before every commit. CI runs the first one on every push and pull request.

```bash
python3 tests/test_package.py
claude plugin validate --strict .
```

## Rules

- Keep one shared `skills/` tree for every agent. Don't add per-app copies of a skill.
- Skills are for clients of the answering service. They may name only tools the client
  connector actually serves, never tools meant for answering service staff. If you
  rename or remove a tool reference, update every skill that mentions it.
- A tool that is announced but not yet served may be named only with a one-line
  fallback saying what to do when it isn't in the tool list.
- The connector enforces access. Skills confirm changes with the user, call out cost and
  effects that can't be undone, verify the result before saying it's done, and never
  work around a refusal.
- Never fabricate account, phone, calendar or message ids: use only ids the tools
  return for the signed-in login.
- Clients can't delete an escalation level. Skills never offer to.
- This plugin has no billing or payment tools. Never collect card, bank or payment
  details through an AI chat.
- Keep the version identical in `plugin.json`, `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and the connector URL identical in `mcp.json` and
  `.mcp.json`.
- Never add credentials, API keys, `headers` blocks, reviewer logins or real client data
  to any file. Examples use made-up names such as Dr. Lee and Northwind.
- Public text (README, manifests, skills) must not name internal systems, vendors,
  staff-only roles or other brands. `tests/test_package.py` checks the public files.
- Write for the end user: plain language, no internal jargon, no em dashes. Prices and
  plan details come from https://www.kauneonga.com/pricing/, never from memory.
- Don't add new skills to `skills/` without also adding them to `EXPECTED_SKILLS` in
  `tests/test_package.py` and to the skills table in `README.md`.
- Preserve the MIT copyright notice in `LICENSE`.
