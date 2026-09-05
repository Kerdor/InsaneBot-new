# PYTHON-DISCORD — Specialized filtering

## PDIS-FS001 — Attachment extension allowlist with contextual guidance
- Unknown/disallowed extensions are blocked.
- `.py` receives a paste-service recommendation.
- `.txt/.csv/.json` get a separate explanation for Discord long-message conversion.
- Other blocked extensions show allowed types and an appeal/meta-channel hint.

## PDIS-FS002 — Perceptual image-hash filtering
- Images can be matched by perceptual hash rather than text/URL.
- Only suitable image MIME types and files below a size limit are processed.
- External hashing failures/timeouts are isolated from the filtering pipeline.
- Alerts include matched rule ID, hash distance and rule description.

## PDIS-FS003 — Invite filtering with anti-obfuscation and trusted-server exceptions
- Invite codes are extracted and normalized to handle obfuscation.
- Unknown invites can be treated as potential phishing under an allowlist policy.
- Explicit deny rules take precedence.
- Verified/Partnered guilds are allowed unless explicitly denied.
- Alerts can include guild name, ID and approximate member/presence counts.

## PDIS-FS004 — Regex token filtering through spoiler expansion
- Token rules can use regex.
- Discord spoiler blocks are expanded into multiple interpretations before matching so hidden text is also inspected.
- The same token pipeline can cover messages, edits, nicknames, thread names and Snekbox output.

## PDIS-FS005 — Delayed anti-spam incident aggregation
- Multiple spam violations from one user are collected into one deletion context.
- A short delay allows related messages, channels, actions and attachments to be merged into one moderation alert.
- Repeated actions are aggregated with counts.
- The strongest infraction in the configured hierarchy becomes the primary infraction.

## PDIS-FS006 — Potential-phishing signal separate from final action
- Unknown/unapproved URLs and invites can be stored as a separate `potential_phish` signal.
- Moderation can consume that signal independently from the immediate filter action.

## PDIS-FS007 — Per-filter validation/action overrides
- Filter-list defaults apply to all filters unless an individual filter overrides them.
- A filter-specific validation can override a failed default validation.
- Actions from multiple triggered filters are merged with list defaults as fallback.

## PDIS-FS008 — Suppress repeated deny triggers on message edits
- Previously triggered deny filters are stored with message metadata.
- On edit, filters that already triggered on the previous version are not repeatedly actioned.
- The stored trigger set is replaced with the current result for the next edit.
