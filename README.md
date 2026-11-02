# Kauneonga

Work with your answering service from Claude.

This plugin connects Claude to the client connector your answering service runs on
Kauneonga, and adds skills for the everyday work clients do: reading and acting on the
messages the service took, keeping the on-call schedule right, and keeping on-call
people reachable.

## Install

Install from the Claude Directory after publication. For a local development test, clone this repository and run `claude --plugin-dir .`.

On first use you sign in at your answering service's client portal. Enter the web address
you use to sign in and sign in with your own login. Your password is never seen by Claude
or by the connector. You see and change only what your login can in the client portal: the
accounts and lines you belong to, and the calendar of lines where you have Calendar
Management access.

## Customer capabilities

The customer connector supports authorized message review and updates,
follow-up to-dos, and on-call calendar and escalation-level management.
Access depends on the signed-in user's active memberships, granted OAuth
scopes, and Calendar Management permission for the affected phone.
Before changes that send calls, SMS or email or change coverage, ask for
confirmation and verify the tool result.

Kauneonga does not expose billing, card collection, or payment tools through
this plugin. Those features are specific to Answering Service Care.

## Skills

| Skill | What it does |
|---|---|
| `kauneonga` | Picks the right skill for a request, and the order when a job needs several |
| `message-triage` | Separate the messages that need action now from the ones that can wait, and record what you did |
| `oncall-changes` | Cover time off, swap or move shifts, and answer who's on call |
| `contact-delivery` | Update how on-call people are reached: numbers, texts, email |

The skills only guide the order of the work. Every rule is enforced by the connector, which
also works without this plugin in ChatGPT and other AI apps that support MCP.
