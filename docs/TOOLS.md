# Answering service connector: tool reference

Connector address: `https://mcp.kauneonga.com/api/v2/mcp`

This page documents every tool the connector offers, for the people who use it and for
AI directory reviewers. Each tool is classified as:

- **Read**: returns information and changes nothing.
- **Write**: changes data in a routine, recoverable way.
- **Sensitive write**: sends a real call, text or email, changes who receives urgent
  calls, or deletes something permanently. Your AI app should ask you to approve each one.

63 tools: 36 read, 6 write, 21 sensitive write.

## Sign-in and permissions

- Sign in with your own client portal login. OAuth 2.1 authorization code with PKCE (S256);
  the AI app registers itself (RFC 7591) and finds the endpoints through
  `/.well-known/oauth-protected-resource` and `/.well-known/oauth-authorization-server`.
- You see only the accounts your login belongs to. Asking for another account's records
  by ID returns an error, not data.
- Changing the on-call calendar needs **Calendar Management** access on that account.
  Without it the server refuses the change and says why.
- Platform administration, phone line settings, call scripts and AI answering settings
  are not available through this connector.
- Disconnect at any time from your AI app's connector settings. Revoking access ends the
  session; later calls return 401 and the app must sign in again.

## Tools

| Tool | What it does | Class | Who can use it | Side effect |
|---|---|---|---|---|
| `list_messages` | List messages on the accounts you can see, newest first, with filters. | Read | Account member | None |
| `list_recent_messages` | List the most recent messages. | Read | Account member | None |
| `search_messages` | Search messages by caller, date or content. | Read | Account member | None |
| `get_message` | Open one message in full. | Write | Account member | Marks the message read, as opening it in the portal does |
| `get_message_by_short_code` | Find a message by the short code shown in alerts. | Read | Account member | None |
| `list_message_activities` | Show a message's delivery and activity history. | Read | Account member | None |
| `list_message_notes` | List the notes on a message. | Read | Account member | None |
| `list_message_call_recording` | Show call details linked to a message (time, caller number, line). No audio is returned. | Read | Account member | None |
| `mark_message_read` | Mark a message read. | Write | Account member | Changes the read flag only |
| `mark_message_unread` | Mark a message unread. | Write | Account member | Changes the read flag only |
| `create_message_note` | Add a note to a message. | Write | Account member | Adds a note visible to others on the account |
| `delete_message_note` | Delete a note from a message. | Sensitive write | Account member | Permanent |
| `acknowledge_message` | Acknowledge a new message so it counts as picked up. | Sensitive write | Account member | Stops further escalation to on-call contacts |
| `update_message` | Change a message's read flag or status (delivered, archived, acknowledged). | Sensitive write | Account member | Acknowledging stops escalation; a message cannot go back to new |
| `create_message` | Add a message to a line, for example a test alert. | Sensitive write | Account member | Delivered to the line's on-call contacts like a real message |
| `list_to_dos` | List scheduled follow-up To Dos. | Read | Account member | None |
| `create_to_do` | Schedule a follow-up call, text or email, once or on a repeating schedule. | Sensitive write | Account member | Sends real calls, texts or emails at the scheduled times |
| `delete_to_do` | Delete a scheduled To Do. | Sensitive write | Account member | Permanent; future sends are cancelled |
| `list_accounts` | List the accounts your login belongs to. | Read | Account member | None |
| `search_accounts` | Search the accounts your login belongs to. | Read | Account member | None |
| `get_account` | Get one account. | Read | Account member | None |
| `list_account_phones` | List an account's phone lines. | Read | Account member | None |
| `get_account_phone` | Get one phone line. | Read | Account member | None |
| `list_account_user_access` | List an account's users and what each may change. | Read | Account member | None |
| `list_account_contacts` | List an account's contacts. | Read | Account member | None |
| `search_account_contacts` | Search an account's contacts. | Read | Account member | None |
| `get_account_contact` | Get one account contact. | Read | Account member | None |
| `list_account_contacts_alphabetical_index_count` | Count contacts by first letter. | Read | Account member | None |
| `list_account_contacts_alphabetical_index_bucket` | List contacts under one letter. | Read | Account member | None |
| `list_phone_events_on_call` | Show who is on call for a line at a given time. | Read | Account member | None |
| `list_escalation_levels` | List a line's escalation levels (who is tried first, second, and so on). | Read | Account member | None |
| `get_escalation_level` | Get one escalation level. | Read | Account member | None |
| `list_escalation_level_dependents` | Show what depends on an escalation level before changing it. | Read | Account member | None |
| `list_escalation_level_reference_data` | Look up valid options before changing an escalation level. | Read | Account member | None |
| `list_calendar_events` | List on-call shifts for one escalation level. | Read | Account member | None |
| `get_calendar_event` | Get one on-call shift. | Read | Account member | None |
| `list_calendar_event_reference_data` | Look up valid options before changing a shift. | Read | Account member | None |
| `list_calendar_contacts` | List a line's on-call contacts. | Read | Account member | None |
| `get_calendar_contact` | Get one on-call contact. | Read | Account member | None |
| `list_calendar_contact_reference_data` | Look up valid options before changing a contact. | Read | Account member | None |
| `list_delivery_methods` | List how an on-call contact is reached (call, text, email). | Read | Account member | None |
| `get_delivery_method` | Get one delivery method. | Read | Account member | None |
| `list_delivery_method_reference_data` | Look up valid options before changing a delivery method. | Read | Account member | None |
| `build_on_call_calendar` | Draft a complete on-call calendar from a plain description. Saves nothing. | Read | Account member | None; returns a plan to review |
| `create_calendar_contact` | Add an on-call contact to a line. | Write | Calendar Management access | Not on call until given a shift |
| `update_calendar_contact` | Edit an on-call contact's details. | Write | Calendar Management access | Changes the contact record |
| `create_delivery_method` | Add a way to reach an on-call contact. | Sensitive write | Calendar Management access | Changes who receives alerts and how |
| `update_delivery_method` | Change how an on-call contact is reached. | Sensitive write | Calendar Management access | Changes who receives alerts and how |
| `delete_delivery_method` | Remove a way to reach an on-call contact. | Sensitive write | Calendar Management access | Permanent; the contact may stop receiving alerts |
| `delete_calendar_contact` | Remove an on-call contact. | Sensitive write | Calendar Management access | Permanent; removes them from coverage |
| `merge_phone_calendar_contacts` | Merge duplicate on-call contacts into one. | Sensitive write | Calendar Management access | Permanent |
| `create_calendar_event` | Add an on-call shift. | Sensitive write | Calendar Management access | Changes who receives urgent calls |
| `update_calendar_event` | Change an on-call shift. | Sensitive write | Calendar Management access | Changes who receives urgent calls |
| `copy_calendar_event` | Copy an on-call shift to another time or level. | Sensitive write | Calendar Management access | Changes who receives urgent calls |
| `delete_calendar_event` | Delete an on-call shift. | Sensitive write | Calendar Management access | Permanent; may leave a gap in coverage |
| `delete_calendar_events` | Delete several on-call shifts at once. | Sensitive write | Calendar Management access | Permanent; may leave gaps in coverage |
| `create_escalation_level` | Add an escalation level to a line. | Sensitive write | Calendar Management access | Changes the order contacts are tried |
| `update_escalation_level` | Change an escalation level. | Sensitive write | Calendar Management access | Changes the order contacts are tried |
| `clone_phone_escalation_level` | Copy one escalation level's shifts to another. | Sensitive write | Calendar Management access | Changes who receives urgent calls |
| `delete_escalation_level_events` | Delete every shift on one escalation level. | Sensitive write | Calendar Management access | Permanent; that level has no coverage until shifts are added |
| `delete_escalation_level` | Not available to client logins. The server refuses it and explains why. | Sensitive write | Calendar Management access | None (always refused) |
| `search_resources` | Search the help articles your provider set up. | Read | Account member | None |
| `read_resource_page` | Read one help article. | Read | Account member | None |

## Errors and status

- A refused call returns a tool error that starts with what was not done and why, for
  example a missing permission. Nothing is changed when a call is refused.
- Writes return the record as saved. Read it back before telling someone a change is done.
- `create_to_do` and `create_message` send real communications. Confirm the recipient,
  channel and timing with the person first.
- An expired or revoked sign-in returns HTTP 401 with a `WWW-Authenticate` header that
  points to the protected-resource metadata, so the app can sign in again.

## Rate limits

By default, 60 tool calls per minute per signed-in person. Over the limit, the call
returns an error saying the limit was reached; wait a minute and retry.

## Data handling

- The connector reads and changes data only when the person signed in asks their AI app
  to. Every tool call is logged with who made it.
- Messages can contain personal and health information from callers. Use the connector
  only with an AI app and plan your organization has approved for that data.

## Help

your answering service, or [support@kauneonga.com](mailto:support@kauneonga.com)
