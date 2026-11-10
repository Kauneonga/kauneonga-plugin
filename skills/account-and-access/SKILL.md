---
name: account-and-access
description: See who has access to the client portal and what each person can do, look up someone in the account's contacts directory, and list the account's lines. Use for "who can change our on-call", "does Sam have access to reports" or "find Dr. Lee's number in our contacts".
---

# Account, access and contacts

This only reads.

- **The account and its lines:** `list_accounts`, `get_account`, `list_account_phones`
  and `get_account_phone`.
- **Who has access:** `list_account_user_access` lists each portal user on the account
  and what they may do: billing, account management, on-call calendar management,
  reports and the rest. Use it to answer whether someone can make or request a change.
  This plugin can't add or remove portal users; the account owner or the answering
  service does that.
- **Contacts directory:** `search_account_contacts` by name or number, or
  `list_account_contacts`; `get_account_contact` for one person. For a long directory,
  page by letter with `list_account_contacts_alphabetical_index_count` and
  `list_account_contacts_alphabetical_index_bucket`.

The directory is separate from the people on the on-call calendar. To change how an
on-call person is reached, use `contact-delivery`.

Contact details are personal information. Share only what was asked for.
