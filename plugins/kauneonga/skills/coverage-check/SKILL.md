---
name: coverage-check
description: Check a line's on-call coverage for gaps before they cause a missed call - hours with nobody on a level, people on shift with no way to reach them, and uncovered time within the requested period. Use for "are we covered this weekend", "any gaps next week" or before a holiday.
---

# Check on-call coverage

This only reads. Fixes go through `oncall-changes` and `contact-delivery`, with a yes
first.

1. Find the line. If the account has several, ask which one. Establish the period's
   start and end in the line's time zone.
2. `list_escalation_levels` for the line.
3. `list_calendar_events` for the period asked about (the next 7 days if they didn't
   say), once for each escalation level's id. Without the level id the calendar returns
   the first level only.
4. For each person on a shift in that window, `list_delivery_methods`: they need at least
   one way to be reached.

## Report

State the exact period checked, with times in the line's time zone. Lead with the gaps
inside that period:
- hours with nobody on the first level,
- backup levels that are empty while the first level is covered,
- people on shift with no way to reach them,
- coverage that ends before the checked period ends, leaving time uncovered within it,
- overlaps that look unintended, such as two people on the same level at the same time
  when that isn't how the line normally runs.

Then one line on what is covered. If there are no gaps inside the checked period, say
so plainly. A shift ending at the period's end is not a gap within that period: say
"covered through [end time]", not "nothing is scheduled afterward". Do not infer
anything about coverage after the queried end time. If the user asks what follows,
read an additional, explicitly bounded period for every level and state that range
before reporting its coverage.
