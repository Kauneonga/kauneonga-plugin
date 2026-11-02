---
name: oncall-changes
description: Make day-to-day changes to who is on call - cover someone's time off, swap two shifts, add or move a shift, change a repeating shift, copy a week, or answer "who's on call tonight". Use when you want to change your on-call schedule or check who is covering.
---

# Change the on-call schedule

This skill covers everyday on-call shifts and escalation-level management
where a customer's membership grants Calendar Management access. Changes to
escalation timing or level order can affect real calls. Show the current
configuration, explain the impact, obtain confirmation, and verify the result.

## Who's on call

1. Find the line. If the account has several, ask which one.
2. `list_escalation_levels` for the line, then `list_calendar_events` with the line's
   phone and a start and end around the time asked about. Pass each escalation level's id
   in turn: without it the calendar returns the first level only, so backup coverage goes
   missing from the answer.
3. Answer with names, levels and times in the line's time zone.

## Making a change

Always in this order:

1. **Reference data first.** `list_calendar_event_reference_data` for shifts and
   `list_calendar_contact_reference_data` for people. Use only ids these return; ids
   belong to one phone line and mean nothing on another.
2. **Read the current shifts** for the dates involved, so you change the right one.
3. **Say the change in plain words**: who, which level, from when to when, and whether it
   is one shift or the whole repeating series. Wait for a yes.
4. **Make it**, then read the calendar again for that window and confirm it shows what
   was asked.

| Request | How |
|---|---|
| Cover time off | Add a shift for the person covering with `create_calendar_event`. To take one occurrence out of a repeating series, detach that occurrence first, then change the detached copy |
| Swap two shifts | Two changes. Confirm both before making either, so a swap never ends half done |
| Change a repeating shift | `update_calendar_event`, for one occurrence or the whole series. Ask which; never assume the series |
| Copy a week | `copy_calendar_event` |
| Remove shifts | `delete_calendar_event` for one, `delete_calendar_events` for several. Read back exactly what will go |
| Add a person | `create_calendar_contact`, at least one way to reach them (see `contact-delivery`), then give them shifts |
| Edit escalation levels | Check `list_escalation_levels`, confirm the plan, then use `create_escalation_level`, `update_escalation_level` or `delete_escalation_level` where authorized. Read back the level order |

## "The wrong person got called"

Escalation-level configuration differs from the delivery sequence for contacts
within a level. Do not change either as a troubleshooting shortcut. Never
delete and re-add a person to change order: removing a contact removes all
their shifts. If calls are not arriving, ask the answering service to
investigate delivery beyond what the portal tools can verify.

## Who can change what

You can change the calendar of lines where your login has Calendar Management access.
Customers with Calendar Management access may edit escalation levels.
Some contact-delivery ordering settings still need the answering service.
If access is refused, explain the required permission; do not bypass it.
