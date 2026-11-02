---
name: contact-delivery
description: Change who receives a client's messages and how they are reached - a new cell number, texts instead of calls, adding an email, stopping one method, or merging a person listed twice. Use when you want to update an on-call person's contact details or how messages reach them.
---

# Contacts and how they're reached

A calendar contact is a person. A delivery method is one way to reach them: call, SMS,
email, fax, app and others. One person can have several. A delivery method belongs to the
person, so changing it changes how they're reached on every shift and every level they're
on. Say that when you propose a change.

## Before any change

1. `list_calendar_contacts` for the line to find the person. If two people share a name,
   ask which one.
2. `list_delivery_method_reference_data` for that person. It returns the valid method
   types, the fields each type needs, and the methods they already have. Check it so you
   don't create a duplicate.
3. Say the change in plain words ("Dr. Lee will get messages by text at (555) 123-4567
   instead of a phone call") and wait for a yes.
4. Make it, then read the person's methods again with `list_delivery_methods` and confirm.

## Common changes

| Request | How |
|---|---|
| New number or email | `update_delivery_method` on the existing method, not a second one alongside it |
| Add a way to reach someone | `create_delivery_method`, with the fields the reference data lists for that type |
| Stop reaching someone a certain way | `delete_delivery_method`. Check they still have at least one method left, or anything sent to them goes nowhere |
| Rename a person | `update_calendar_contact` |
| Same person listed twice | `merge_phone_calendar_contacts` with both records and the name to keep. It can't be undone here, so read back exactly which two records merge |
| Remove a person | `delete_calendar_contact` removes every shift they have. Prefer ending their shifts (`oncall-changes`) unless the user is sure |

## Read numbers back

Repeat every phone number back in full before saving it. A wrong digit means a missed
page, and nothing will flag it.

## Who can change what

You can make these changes on lines where your login has Calendar Management access. If a
change is refused, say which access it needs rather than trying another way.
