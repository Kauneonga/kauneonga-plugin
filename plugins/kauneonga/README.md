# Kauneonga plugin for Claude

For clients of answering services that run on Kauneonga. Connect Claude to your
account with your own client portal login, then ask about your messages, To Dos
and who's on call, and make the changes your login allows.

Try asking: "What came in overnight that needs action?", "Who's on call
tonight?" or "Move Saturday's shift from Dr. Lee to Dr. Patel."

## What's included

- **The Kauneonga connector** at `https://mcp.kauneonga.com/api/v2/mcp`. When you
  connect, enter the web address where you sign in to your client portal, then sign
  in there as usual, with your two-step code if your login uses one.
- **Skills** that guide Claude through common jobs:

| Skill | What it does |
|---|---|
| `kauneonga` | Picks the right skill for a request, and the order when a job needs several |
| `setup` | Connects your account and checks what your login can reach |
| `message-triage` | Separates the messages that need action now from the ones that can wait, acknowledges them, and records notes |
| `follow-ups` | Lists, adds and closes To Dos, and finds out why a follow-up or callback didn't happen |
| `oncall-changes` | Covers time off, swaps or moves shifts, adds many shifts at once, and answers who's on call |
| `contact-delivery` | Updates how on-call people are reached: numbers, texts, email |
| `message-delivery` | Traces a message that didn't arrive and finds the cause |
| `coverage-check` | Finds gaps in upcoming on-call coverage |
| `account-and-access` | Shows who has portal access, the contacts directory and the account's lines |

## Your data and permissions

- Each person connects with their own login and gets the same access they have in
  the client portal. Approving a change in Claude never gives your login more access.
- Before a change, the skills show you exactly what will change and ask first.
- It never asks for card or bank details, and it has no billing or payment tools.
- You can disconnect at any time from Claude's connector settings.
- See Kauneonga's [privacy policy](https://www.kauneonga.com/privacy-policy/) and
  [terms](https://www.kauneonga.com/terms-and-conditions/).

## Help

Documentation: https://www.kauneonga.com/docs/. For account questions, contact your
answering service.

Licensed under the MIT License.
