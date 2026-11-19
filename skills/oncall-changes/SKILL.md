---
name: oncall-changes
description: Make day-to-day changes to who is on call - cover time off, swap two shifts, add or move a shift, change one date or every date of a repeating shift, add many shifts at once, set the line's standard shift times, and see, copy or edit escalation levels. Also answers "who's on call tonight". Use when you want to change your on-call schedule or check who is covering.
---

# Change the on-call schedule

This skill covers everyday on-call shifts and escalation-level management
where a customer's membership grants Calendar Management access. Changes to
escalation timing or level order can affect real calls. Show the current
configuration, explain the impact, obtain confirmation, and verify the result.

## Who's on call

1. Find the line. If the account has several, ask which one.
2. **Right now:** `list_phone_events_on_call` for the line shows who is covering now on
   each escalation level.
3. **Another time:** `list_escalation_levels` for the line, then `list_calendar_events`
   with the line's phone and a start and end around the time asked about. Pass each
   escalation level's id in turn: without it the calendar returns the first level only,
   so backup coverage goes missing from the answer.
4. Answer with names, levels and times in the line's time zone.

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
| Cover time off | One date of a repeating shift: change only that date (see below). Otherwise add a shift for the person covering with `create_calendar_event` |
| Swap two shifts | Confirm both changes before making either. If only one succeeds, tell the user immediately and do not imply the swap is complete |
| Change a repeating shift | Ask whether it's only that date or every date, then follow "One date of a repeating shift" below. Never assume the series |
| Put the same shift on another level | `copy_calendar_event` with the levels to copy it to |
| Repeat a week, or add many shifts | See "Several shifts at once" below |
| Remove shifts | `delete_calendar_event` for one, `delete_calendar_events` for several. Read back exactly what will go |
| Add a person | `create_calendar_contact`, at least one way to reach them (see `contact-delivery`), then give them shifts |
| Set up on-call from scratch | `build_on_call_calendar` drafts the levels, people and shifts from a plain description and saves nothing. Show the plan, get a yes, then create the levels, the people, how they're reached, and the shifts, in that order |
| Escalation levels | See "Escalation levels" below |

## One date of a repeating shift

"Move Saturday's shift to Dr. Patel" can mean this Saturday or every Saturday. Ask which
before changing anything, unless the person already said ("only this Saturday", "every
Saturday").

- **Only that date:** `create_calendar_event` with action `detach`. `parent_id` is the
  repeating shift, `original_start_date` is that date's start as the calendar shows it
  (for example `2026-11-21 08:00`), and `start_date`, `end_date`, `contact_id` and
  `delivery_method_ids` are what that date becomes. Leave `schedule` out. Every other
  date stays as it was.
- **Take one date off:** `update_calendar_event` with action `delete` and that date's
  start as `start_date`.
- **Every date:** `update_calendar_event` with action `update` on the repeating shift.
  Leave `schedule` out so it keeps repeating. If the tool says `schedule` is missing,
  send the shift's current `schedule` from `get_calendar_event`, unchanged. A repeating
  shift holds only its current and upcoming dates (past ones roll off), so this is also
  "from now on".
- **From a later date on** ("starting December 5"): changing every date would also change
  the dates before it. Say so and ask how to handle those dates; don't pick for them.

`update_calendar_event` on a repeating shift changes every date of it. Never send
`schedule` "null" to change one date: that stops the shift repeating and removes every
later date. Send it only when the person asks for the shift to stop repeating, together
with `stop_repeating` set to true.

## Several shifts at once

For more than a few shifts, such as a month of nights or next week's copy of this week:

1. Build the list: who, which level, and each shift's start and end in the line's time
   zone. A shift named after one of the line's standard shifts takes that shift's hours.
2. `preview_calendar_events` shows the list day by day for each level and saves nothing.
   If the person saves it from the preview, it's done: don't save it again.
3. On a yes in the chat, `create_calendar_events` with the same list. It saves all of
   them or none: if any shift is refused, fix those and send the whole list again.
4. Read the calendar back for the first and last days, for every level involved.

If `preview_calendar_events` or `create_calendar_events` isn't in your tool list yet,
show the list in the chat, get one yes, and add the shifts one at a time with
`create_calendar_event`.

## Standard shift times

`list_calendar_time_frames` shows the line's standard shifts, such as "Weeknight, 5:00
PM to 8:00 AM the next day", so "Dr. Lee on weeknights December 1 to 4" gets the right
hours. To change them, read the current list, edit it, and send the whole list back with
`update_calendar_time_frames`: it replaces the saved list, so anything left out is
removed. Show the old and new times and get a yes first. Shifts already on the calendar
keep their times.

If these tools aren't in your tool list yet, ask the user for each shift's hours instead.

## Escalation levels

Levels set who is tried first and how long to wait before trying the next level. A change
here affects every call on the line.

- **See them:** `list_escalation_levels` for the line, `get_escalation_level` for one,
  and `list_escalation_level_reference_data` for the current order and valid options.
- **What relies on a level:** `list_escalation_level_dependents` lists the shifts, people
  and other levels that point to it. Check it before changing a level, and say what the
  change would affect.
- **Add or edit a level:** `create_escalation_level`, or `update_escalation_level` for
  its name, its wait time or which level comes next. Show the full order with wait times
  before and after, get a yes, then read it back with `list_escalation_levels`.
- **Copy a level's schedule to another level:** `clone_phone_escalation_level` copies
  every shift on one level onto another level of the same line. It first removes every
  shift already on the level it copies to, and that can't be undone, so list those
  shifts and get a yes. To give another line the same schedule, read this line's shifts
  and add them on the other line with its own reference data (see "Several shifts at
  once").
- **Clear a level's shifts:** `delete_escalation_level_events` removes every shift on one
  level and keeps the level. It can't be undone: list what will go and get a yes.
- **Remove a level:** clients can't. If they want one removed, say their answering
  service can remove it.

## "The wrong person got called"

Escalation-level configuration differs from the delivery sequence for contacts
within a level. Do not change either as a troubleshooting shortcut. Never
delete and re-add a person to change order: removing a contact removes all
their shifts. If calls are not arriving, ask the answering service to
investigate delivery beyond what the portal tools can verify.

When two or more people are on the same level at the same time, texts, emails and app
alerts go to all of them at once, but calls go one at a time in the order set on their
shifts (`position`, lowest first). Shifts with no order set are called in the order they
were added. To change who is called first, `update_calendar_event` with a new `position`
on that shift, after a yes.

## Who can change what

You can change the calendar of lines where your login has Calendar Management access.
Customers with Calendar Management access may edit escalation levels.
Some contact-delivery ordering settings still need the answering service.
If access is refused, explain the required permission; do not bypass it.
