---
name: setup
description: Help a client connect Claude, ChatGPT or another AI app to their answering service account with their own client portal login, and check which accounts and lines it can reach. Use after installing the plugin, when the connection fails, or when the client asks what the plugin can access.
---

# Connect your answering service account

1. Ask the user to connect the **Kauneonga** connector through the app's own sign-in
   flow. The connector address is `https://mcp.kauneonga.com/api/v2/mcp`. Never ask for a
   portal password, access token or API key in chat.
2. On the sign-in page they enter the web address they use for their client portal, sign
   in with their own login, enter their two-factor code if they use one, and allow
   access.
3. Run a harmless read first: `list_accounts`, and show only the accounts returned for
   this login. If there are several, ask which one to use for the current request.
4. Explain that Oncall Calendar Management is a separate permission on each account. A
   successful sign-in doesn't by itself allow changing the on-call calendar, every line,
   or the line's phone settings, scripts and AI answering, which stay with their
   answering service.

## When it doesn't work

- **Sign-in fails:** have them disconnect and reconnect the connector in the app's
  settings, then sign in again.
- **Nothing comes back:** their login may not belong to any account yet. Their answering
  service can check. Never try another login or look for hidden ids.
