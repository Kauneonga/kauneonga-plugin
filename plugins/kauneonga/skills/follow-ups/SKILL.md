---
name: follow-ups
description: List, add and close follow-up To Dos, and work out why a follow-up or callback didn't happen. Use for "what follow-ups are still open", "text Sam Lee every weekday at 8", "cancel the Friday reminder" or "the callback to that caller never happened".
---

# Follow-ups: To Dos and callbacks

A To Do is a follow-up your answering service sends for you: a text, an email, or a call
the answering service places and handles with your instructions. It goes out once or on
a schedule, and it reaches real people, so confirm every one before saving it. To Do
times follow the account's time zone.

## What's open

`list_to_dos` lists the To Dos on the accounts this login can see, newest first, 25 to a
page. When the total says there are more, ask for the next `page`. Keep only the ones on
the account or line the user asked about.

For each one, say what it sends, to whom, how, and when it next goes out. Show numbers
and emails only when the user needs them.

## Add one

1. `list_to_dos` first, so you don't add a second copy of one that already exists.
2. Collect what's missing:
   - **which line** it runs on: the account number `get_account` lists for that line;
   - **how:** text, email or call;
   - **to whom:** the number or email address;
   - **what it says**, or for a call, the instructions for whoever places it;
   - **when:** right away, at set times today, or daily, weekly or monthly at set times.
     Weekly and monthly need the days.
3. A text goes out from one of the account's own texting numbers. Ask which one if you
   don't know; never guess. If the save is refused because of that number, say so.
4. When the follow-up is about a message, refer to the message (its short code) instead
   of copying the caller's details into the To Do.
5. Read it all back in plain words, for example "A text from (555) 010-2000 to Sam Lee at
   (555) 123-4567 saying 'Please check the overnight messages', every weekday at 8:00
   AM." Repeat every number in full. Wait for a yes.
6. `create_to_do`, then `list_to_dos` again and confirm it's there with the right
   schedule.

Never use a To Do to test whether messages reach someone: it sends from the account's
own number, not the way messages are delivered. Use a test message instead (see
`message-triage`).

## Close or change one

There's no "done" status here: closing a To Do deletes it. `delete_to_do` cancels
everything it would still send, and it can't be undone. Say exactly which To Do (what, to
whom, when) and wait for a yes. For several, list them all first and get one yes for
that list. Then `list_to_dos` to confirm they're gone.

To change the time, wording or recipient, there's no edit: add the corrected To Do, check
it saved, then delete the old one. Confirm both steps as one plan. If either step fails,
tell the user right away which To Do is in place now.

## Why a follow-up or callback didn't happen

1. **Find it.**
   - A To Do: `list_to_dos`. If it isn't there, it was deleted or never saved. Say so.
   - A callback on a message: `search_messages` or `list_messages`. Don't open it with
     `get_message`: that marks it read and changes the record you're looking into.
2. **Check the To Do's setup** against what the user expected:
   - the days and times, in the account's time zone; a weekly or monthly To Do without
     the right days, or a one-time send whose time had already passed;
   - the recipient's number or email, digit by digit;
   - how it was sent: texts stop reaching someone who replied STOP, until they text
     START to that number; an email can bounce or land in a spam or filtered folder.
3. **Read the message's history.** `list_message_activities` shows each delivery, read,
   pickup and status change. `list_message_notes` shows what the answering service or
   your team noted, such as a callback attempt. Lay it out as a timeline in the line's
   time zone.
4. **Report** what the records show, then the likely cause, kept apart.

These tools don't show each send of a To Do. If the To Do is set up right and the records
don't explain what happened, your answering service can check the send. Don't create test
To Dos to find out: they reach real people.

To fix a wrong To Do, replace it as above, with a yes. If an on-call person's number or
email is wrong, use `contact-delivery`.

## Who can do this

The connector enforces what this login may do. If adding or deleting a To Do is refused,
say what was refused and that the account owner or the answering service can help; never
try another way.
