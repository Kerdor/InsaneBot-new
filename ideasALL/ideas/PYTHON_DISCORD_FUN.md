# PYTHON-DISCORD — Fun / community mechanics

## PDIS-FUN001 — Threshold-triggered reaction relay
- A message can be automatically relayed to a dedicated showcase channel after it receives a configurable number of qualifying reactions.
- The threshold counts unique users rather than raw reaction events, preventing one user from satisfying the threshold repeatedly.

## PDIS-FUN002 — Restricted reaction-driven promotion
- A community mechanic can require both the message author and reactors to belong to a trusted/staff role set.
- The source channel can also be filtered through a blacklist and visibility/permission checks.

## PDIS-FUN003 — Idempotent reaction relay marker
- After a message is relayed, the bot adds a marker reaction and checks for that marker before relaying again.
- A lock is acquired around the final check + relay + marker operation to avoid duplicate relays from concurrent reaction events.

## PDIS-FUN004 — Manual bypass of an automatic fun trigger
- A privileged command can invoke the same relay path without waiting for the reaction threshold.
- The manual action uses the same duplicate-prevention logic as the automatic trigger.

## PDIS-FUN005 — Attachment-preserving webhook relay with graceful degradation
- A relay preserves message text, author display name/avatar, and attachments through a webhook.
- If an attachment cannot be fetched, the destination receives an explicit failure notice instead of silently losing the message.

## PDIS-FUN006 — Protected marker reaction restoration
- When users remove the bot's completion marker from an already-triggered message, the bot can restore it while the trigger condition remains satisfied.

## PDIS-FUN007 — Scheduled random channel-name rotation
- A set of community channels can receive randomized names on a daily scheduled task, with a configurable formatter and remote name source.
- The feature can be manually re-rolled for one selected channel and temporarily deactivate the previous name.

## PDIS-FUN008 — Active/deactivated pool for rotating content
- Rotating names are stored as a pool with an explicit active flag.
- Moderators can activate/deactivate entries without deleting them, and list active versus inactive pools separately.

## PDIS-FUN009 — Similarity guard for user-submitted rotating content
- New candidate names are compared against existing names with fuzzy similarity and rejected when they are too close to an existing entry.
- A privileged force-add path can deliberately bypass the similarity guard.

## PDIS-FUN010 — Fuzzy search over normalized community content
- Search normalizes stored values before matching, combines substring matches with fuzzy close matches, and maps results back to their original display forms.

## PDIS-FUN011 — Rate-limit-aware deferred fun operation
- If a channel rename hits a rate limit, the bot can ask the moderator whether to schedule the operation within the current process instead of failing outright.
- The retry choice is protected so only the original requester can control the interactive prompt.

## PDIS-FUN012 — Safe exhaustion handling for finite random pools
- When a reroll pool has no active entries left, the command reports that the pool is exhausted and asks moderators to add new entries instead of producing an invalid result.

## Дубликаты

Общие giveaways, lottery, random utilities, GIF/image fun и games уже есть в общем FUN-банке; здесь сохранены специализированные community mechanics из `python-discord`.
