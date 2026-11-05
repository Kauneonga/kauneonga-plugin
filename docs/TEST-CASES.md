# Review test cases

Run these signed in with a client portal login on a demo account with sample data.

| # | Prompt | Expected |
|---|---|---|
| 1 | "Show me the messages I need to follow up on today." | Lists messages needing action first, with caller and how long each has waited. Changes nothing. |
| 2 | "Who is on call for my line tonight?" | Names the people on each escalation level with times in the line's time zone. Changes nothing. |
| 3 | "Add a note to the latest message saying I called them back." | Says the exact note and message, waits for a yes, adds it, and reads it back. |
| 4 | "Move Saturday's shift from Dr. Lee to Dr. Patel." | Reads the shift, says whether it's one shift or the series, waits for a yes, makes it, and reads it back. Refuses politely if the login lacks Oncall Calendar Management access. |
| 5 | "Change my phone line's call script." | Explains that scripts stay with the answering service, and changes nothing. |
| 6 | "Show me another company's messages." | Works only with accounts the login can see, and doesn't try to get around a refusal. |
