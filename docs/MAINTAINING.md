# Maintaining this plugin

One package serves Claude, ChatGPT and other agents, using the client connector:
`https://mcp.kauneonga.com/api/v2/mcp`.

## Layout

| Path | Purpose |
|---|---|
| `.claude-plugin/plugin.json` | Claude plugin identity and metadata |
| `.claude-plugin/marketplace.json` | Claude marketplace listing this plugin, so people can install it from this repository |
| `.mcp.json` | Claude connector configuration |
| `plugin.json` | Portable Agent Plugins manifest, including the ChatGPT listing |
| `mcp.json` | Portable connector configuration with the sign-in declaration |
| `skills/` | One shared source of skills for every app |
| `assets/logo.png` | ChatGPT listing logo: the 512 px icon the connector already serves |
| `scripts/build_chatgpt_package.py` | Builds the ChatGPT upload ZIP |
| `docs/TEST-CASES.md` | Review test cases |
| `tests/` | Offline structure and safety checks |

## Rules

- Skills name only tools the client connector serves. When a tool is renamed or removed,
  update every skill that mentions it.
- The connector enforces access. Skills confirm changes, call out cost, live-call and
  can't-be-undone effects, and never work around a refusal.
- Public-facing material never names internal systems, vendors or restricted internal roles.
- Keep the version the same in `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json` and `plugin.json`, and the connector the same in
  `.mcp.json` and `mcp.json`.
- Never commit keys, reviewer credentials or real client data.

## Checks

```bash
python3 tests/test_package.py
claude plugin validate --strict .
claude plugin validate --strict .claude-plugin/plugin.json
```

The offline checks also build the ChatGPT ZIP. Build it on its own with
`python3 scripts/build_chatgpt_package.py` (written to `dist/`), and submit it with the
**With MCP** flow.

## Before listing in a directory

- A live sign-in test with a real client portal login.
- A reviewer client portal login on a demo account with sample data and no two-factor
  sign-in.
- ChatGPT: a demo video, and the domain-check token served at
  `https://mcp.kauneonga.com/.well-known/openai-apps-challenge` (already served).
