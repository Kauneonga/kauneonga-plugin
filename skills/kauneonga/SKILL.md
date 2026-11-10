---
name: kauneonga
description: Pick the right skill for a request about your answering service and say what this plugin can do. Use when a request is broad or unclear, when someone asks what you can help with, or when a job spans more than one skill.
---

# Pick the right skill

Match the request to one skill below, say which one you're using, then follow it. When
nothing fits, use the connector's tools directly. You see and change only what your login
can in the client portal, with or without a skill.

| The request | Skill |
|---|---|
| Connect the account, or check what this login can reach | `setup` |
| Catch up on messages, find anything urgent, work through unread ones | `message-triage` |
| Create and track follow-up to-dos or update message status | `message-triage` |
| Cover time off, swap or move a shift, who's on call tonight | `oncall-changes` |
| Review or change escalation levels, if authorized | `oncall-changes` |
| A new cell number, texts instead of calls, add or stop an email | `contact-delivery` |
| Someone didn't get a message, got it late, or the wrong person got it | `message-delivery` |
| Any gaps in on-call coverage this week, this weekend or over a holiday | `coverage-check` |
| Who has portal access, the contacts directory, the account's lines | `account-and-access` |

**Someone wasn't reached:** start with `message-delivery`. It checks the message's
history, who was on call and how they're reached, then hands the fix to
`oncall-changes` or `contact-delivery`.

## When the question is how something works

Search the help center with `search_resources`, read the page with `read_resource_page`,
and link it in the answer.

When a task needs something the connector doesn't offer, say so and point the user to the
client portal rather than trying a workaround.

## Access

Use only accounts, phones and records the connector returns for the signed-in login.
The connector enforces account memberships and line permissions; a skill never grants
access. Never pick another account or identity to get around a refusal. Changes to phone
lines, scripts or AI answering settings go to the user's answering service.
