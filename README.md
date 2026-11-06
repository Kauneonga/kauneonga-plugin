# Kauneonga for Claude

For clients of answering services that run on Kauneonga. Connect Claude to your
account with your own client portal login, then ask about your messages, To Dos
and who's on call, and make the changes your login allows.

## What you can do

- **Catch up on messages.** See what needs action first, add or delete a note,
  mark a message read or unread, acknowledge it, change its status, or add a
  new message.
- **Follow up.** Set up a To Do (a call, text or email, now or on a schedule),
  or delete one.
- **Check and change who's on call.** See who's on call tonight and who backs
  them up. If your login has **Oncall Calendar Management** access, cover time
  off, swap or move shifts, change escalation levels, and update your on-call
  contacts and how each one is reached.

Try asking: "What came in overnight that needs action?", "Who's on call
tonight?" or "Move Saturday's shift from Dr. Lee to Dr. Patel."

Before any change, Claude tells you exactly what it will do and asks you to
confirm.

## What it won't do

- It never asks for card or bank details, and it has no billing or payment
  tools.
- It works only with the accounts your client portal login can see.
- Phone lines, scripts and AI answering settings stay with your answering
  service. If you ask for one of these, it tells you and suggests contacting
  them.

## Install

### Claude

**Your whole team (Claude Team or Enterprise):** an owner of your Claude
organization opens **Organization settings > Plugins & skills** and adds this
repository, `Kauneonga/kauneonga-plugin`.

**Claude Code:**

```
/plugin install kauneonga --marketplace Kauneonga/kauneonga-plugin
```

On Claude Code older than 2.1.275, add the marketplace first:

```
/plugin marketplace add Kauneonga/kauneonga-plugin
/plugin install kauneonga@kauneonga
```

**Just the connector:** in Claude, open **Settings > Connectors** and add a
custom connector with this address:
`https://mcp.kauneonga.com/api/v2/mcp`.

### ChatGPT

Add a custom connector in ChatGPT with the address
`https://mcp.kauneonga.com/api/v2/mcp`. The skills come with the plugin once it
is listed in ChatGPT.

### Codex, Cursor and other agents

Install the skills:

```bash
npx skills add Kauneonga/kauneonga-plugin
```

Then add the connector address, `https://mcp.kauneonga.com/api/v2/mcp`, in the
agent's MCP settings. It's a Streamable HTTP server that signs you in with
OAuth.

### Sign in

The first time Claude uses the connector, it opens a sign-in page. Enter the
web address you use to sign in to your client portal, then sign in with your
own login, enter your two-factor code if you use one, and allow access. Your
password is never seen by Claude or by the connector.

## Your data and permissions

- Each person connects with their own login, and gets the same access they
  have in the client portal: the accounts and lines they belong to, and the
  on-call calendar of lines where they have Oncall Calendar Management access.
  Approving a change in the app never gives your login more access.
- You can disconnect at any time from your AI app's connector settings.
- See Kauneonga's [privacy policy](https://www.kauneonga.com/privacy-policy/)
  and [terms](https://www.kauneonga.com/terms-and-conditions/).

## Skills

| Skill | What it does |
|---|---|
| `kauneonga` | Picks the right skill for a request, and the order when a job needs several |
| `setup` | Connects your account and checks what your login can reach |
| `message-triage` | Separates the messages that need action now from the ones that can wait, and records what you did |
| `oncall-changes` | Covers time off, swaps or moves shifts, and answers who's on call |
| `contact-delivery` | Updates how on-call people are reached: numbers, texts, email |

The skills only guide the order of the work. Every rule is enforced by the
connector, which also works without this plugin.

## Help

Contact your answering service.

---

Maintaining this plugin? See [docs/MAINTAINING.md](docs/MAINTAINING.md). AI coding
agents: see [AGENTS.md](AGENTS.md).
Licensed under the [MIT License](LICENSE).
