# Kauneonga: connect your AI assistant

For clients of answering services that run on Kauneonga. Connect a supported AI assistant to your
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

Before any change, your AI assistant should tell you what it proposes and ask you to
confirm. Review changes before approving them.

## What it won't do

- It never asks for card or bank details, and it has no billing or payment
  tools.
- It works only with the accounts your client portal login can see.
- Phone lines, scripts and AI answering settings stay with your answering
  service. If you ask for one of these, it tells you and suggests contacting
  them.

## Choose your AI assistant

You can use your Client Portal account with several AI assistants. **Claude installs the complete guided plugin.** ChatGPT, Gemini, and other assistants can connect to the same MCP server where supported, but **the MCP connection alone does not automatically install the plugin's guided skills**.

| AI assistant | Setup | Availability |
| --- | --- | --- |
| **Claude** | Install the `kauneonga` plugin and sign in | Full plugin with guided skills and MCP tools |
| **ChatGPT** | Use an approved workspace MCP plugin (or ask a workspace admin to add it) | MCP tools; additional skills require separate distribution |
| **Gemini Enterprise** | Ask your organization's Gemini Enterprise administrator to add the custom MCP server | MCP tools, after OAuth and tool compatibility are configured and tested |
| **Personal Gemini** | Eligible users may connect a custom MCP app | MCP tools only; eligibility and data-handling restrictions apply |
| **Gemini CLI, Claude Code, Codex, Cursor and other tools** | Configure the MCP server and any separately supported skills | Technical setup, varies by product |

**MCP connection URL:** `https://mcp.kauneonga.com/api/v2/mcp`

Use **your own Client Portal login**. Each person can only see and change what that login is permitted to access. Billing and payments are **not** available through the Kauneonga client connector.

### Claude: install the full plugin

1. Open [Claude](https://claude.ai) and sign in to an account with plugin access.
2. Open **Customize > Plugins**.
3. Choose **Add > Add marketplace > Add from a repository** and paste:

   `Kauneonga/kauneonga-plugin`

4. Find the **kauneonga** plugin in the marketplace and click **Add**. If your organization's Claude admin has already distributed it, look under **Discover** instead.
5. Start a chat and ask, **"What messages came in overnight that need action?"**
6. When Claude asks to connect, enter your usual Client Portal web address if prompted, then sign in on the secure portal page. Complete two-factor authentication if applicable and approve access.

If your organization wants to distribute this plugin to staff, its Claude owner can upload a reviewed plugin ZIP in **Organization settings > Plugins & skills**. **Public GitHub repositories cannot be directly synced to Claude organization marketplaces**; organization owners may alternatively maintain a private/internal marketplace copy for syncing.

[Claude plugin help](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) · [Claude organization distribution](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)

### ChatGPT: connect through a workspace plugin

If your organization has already published an approved **Kauneonga** plugin, open **Settings > Plugins** in [ChatGPT](https://chatgpt.com), enable it, and choose it when asking a question. Sign in with your own Client Portal account when prompted.

If it isn't listed, a **ChatGPT Business, Enterprise or Edu workspace administrator** needs to set it up on the web:

1. Open **Plugins**, select **+ > Add custom MCP server**.
2. Set the name to **Kauneonga** and paste `https://mcp.kauneonga.com/api/v2/mcp` as the HTTPS server address.
3. Configure OAuth sign-in, review the connection warning, then choose **Create as a plugin**.
4. Review and test the discovered tools and permitted actions before publishing it to the appropriate workspace members.

Once available, choose the plugin when composing a message and ask **"Who is on call tonight?"**. A custom MCP plugin exposes the server's tools; importing the separate guided skills requires a compatible plugin distribution process.



[ChatGPT custom MCP setup](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt) · [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)

### Gemini: connect with Google

**Gemini Enterprise (managed business use):** A Gemini Enterprise or Google Cloud administrator can configure a **custom MCP server data store** using `https://mcp.kauneonga.com/api/v2/mcp`. The administrator must supply supported **OAuth 2.0** connection details, verify authentication, explicitly enable permitted tools, and test the experience before giving staff access. This is **not a one-click plugin installation**, and the integration has not been independently validated for this server.

[Gemini Enterprise custom MCP documentation](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server)

**Personal Gemini:** Google also supports custom MCP apps for eligible adults in the US using a **personal Google account**, with **Keep Activity** enabled. Work or school Google accounts are not eligible for this personal custom-app feature. If you are eligible and have confirmed that your organization's/client's privacy policy permits using the account, open [Gemini](https://gemini.google.com) on the web, go to **Settings > Connected Apps > Add a custom app**, enter `https://mcp.kauneonga.com/api/v2/mcp`, and follow the sign-in steps.

**Do not use a personal AI account for client messages, medical information, or other confidential data without appropriate authorization.** The Gemini connection exposes MCP tools, not the repository's bundled skills. Actual OAuth support still needs testing.

[Google's custom-app instructions](https://support.google.com/gemini/answer/17209137)

### Other assistants (technical setup)

For **Claude Code**, use the plugin marketplace command:

```text
/plugin marketplace add Kauneonga/kauneonga-plugin
/plugin install kauneonga@kauneonga
```

For **Gemini CLI**, configure the remote MCP server:

```bash
gemini mcp add -t http -s user kauneonga https://mcp.kauneonga.com/api/v2/mcp
```

Then follow Gemini CLI's authorization instructions. For **Codex, Cursor and other MCP-compatible agents**, add a remote Streamable HTTP MCP server with the same HTTPS address. If the tool supports importing skills, you can separately install compatible workflows from this repository's `skills/` directory.

[Gemini CLI MCP documentation](https://geminicli.com/docs/tools/mcp-server/)

### Troubleshooting

- **Plugin missing:** Your AI account may not support custom plugins or your organization's admin may need to enable it.
- **Sign-in not working:** Make sure you enter the normal Client Portal address when asked. Use the secure authorization page, not a chat message, for passwords and two-factor codes.
- **Can't access an account or action:** Your Client Portal permissions apply in every AI assistant.
- **A skill isn't available in ChatGPT or Gemini:** Those apps may have the MCP tools without the guided skills included with the Claude package. That is expected unless the skills were installed separately.
- **Asked to confirm a change:** Check exactly what will change before approving. Do not share card or bank details with the AI assistant.

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

Maintaining this plugin? See [docs/MAINTAINING.md](docs/MAINTAINING.md).
Licensed under the [MIT License](LICENSE).
