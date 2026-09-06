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

## PDIS-FS009 — Multi-dimensional anti-spam signal library
- Anti-spam can measure different abuse dimensions independently instead of relying only on raw message rate.
- Attachment-volume threshold: count attachments from one user over a configurable time window.
- Character-volume threshold: count total characters sent by one user over a short window.
- Emoji-volume threshold: count Unicode/custom emoji while ignoring fenced code blocks.
- Link-volume threshold: count URLs across recent messages, with an additional requirement that links occur in more than one message to avoid one-message bursts.
- Mention-volume threshold: count actual Discord-resolved user mentions while excluding bots, self-mentions and the replied-to author.
- Role-mention threshold: independently count role mentions.
- Newline threshold supports both total newlines and a separate consecutive-newline limit.
- Duplicate-message threshold detects repeated identical content from the same user.
- Burst threshold counts messages from one user in a rolling interval.
- Each detector records the exact measured quantity in the moderation context, making alerts explainable.

## PDIS-FS010 — Normalization layer for anti-filter bypasses
- Normalize filtered text before matching by removing invisible/control/format characters and Zalgo-style combining marks.
- URL-percent-decoded content is inspected so encoded links cannot trivially bypass filters.
- Backslashes and filter-bypassing newlines can be normalized away.
- Keep normalization separate from the original message so moderation can still inspect/display the original content.

## PDIS-FS011 — Secret/webhook leak interception with safe logging
- Detect seemingly valid Discord bot/user tokens using structural checks rather than a naive substring search.
- Validate the encoded user ID, timestamp and non-dummy HMAC before treating a token as real-looking.
- Replace only the sensitive HMAC portion with a redacted form while retaining enough suffix for diagnostics.
- Prevent the normal deletion logger from creating a second sensitive-data log entry.
- Detect Discord webhook URLs and immediately revoke/delete the webhook through the API.
- Redact webhook secrets from moderation output before logging.

## PDIS-FS012 — Semantic filter events independent of gateway events
- A filtering system can expose semantic events such as `NICKNAME` or `SNEKBOX` instead of coupling every rule directly to Discord gateway event types.
- This lets one filter engine process messages, edits, nicknames, thread names and generated code-execution output through a common pipeline.

## Дубликаты

Общие anti-spam, keyword filtering, mention limits и moderation alerts уже есть в банке; здесь сохранены именно отдельные detection dimensions, normalization/security rules и их специальные counting/handling rules.
