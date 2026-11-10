---
name: coverage-check
description: Check a line's on-call coverage for gaps before they cause a missed call - hours with nobody on a level, people on shift with no way to reach them, and coverage that ends with nothing after it. Use for "are we covered this weekend", "any gaps next week" or before a holiday.
---

# Check on-call coverage

This only reads. Fixes go through `oncall-changes` and `contact-delivery`, with a yes
first.

1. Find the line. If the account has several, ask which one.
2. `list_escalation_levels` for the line.
3. `list_calendar_events` for the period asked about (the next 7 days if they didn't
   say), once for each escalation level's id. Without the level id the calendar returns
   the first level only.
4. For each person on a shift in that window, `list_delivery_methods`: they need at least
   one way to be reached.

## Report

Times in the line's time zone. Lead with the gaps:
- hours with nobody on the first level,
- backup levels that are empty while the first level is covered,
- people on shift with no way to reach them,
- coverage that ends with nothing scheduled after it,
- overlaps that look unintended, such as two people on the same level at the same time
  when that isn't how the line normally runs.

Then one line on what is covered. If there are no gaps, say so plainly.
