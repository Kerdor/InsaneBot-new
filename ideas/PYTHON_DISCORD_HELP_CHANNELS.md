# PYTHON-DISCORD — Help forum / support workflow

## PDIS-HF001 — Automatic inactivity closure with rescheduling
- Help posts calculate a future close time from the latest activity and schedule a task for that exact post.
- A periodic watchdog checks all currently open posts and recreates missing scheduled tasks.
- If the post becomes active again, the previous task is cancelled and rescheduled.

## PDIS-HF002 — Multiple distinct closure reasons
- Help sessions distinguish manual close, inactivity, native Discord archive, deletion and cleanup after the owner leaves.
- The reason is retained in analytics and can change the wording of the closing message.

## PDIS-HF003 — Native forum lifecycle integration
- The bot builds on Discord Forum/Thread native open/archive/delete events instead of implementing a parallel ticket system.
- Native archive actions are detected separately so the bot does not double-apply its own close logic.

## PDIS-HF004 — Automatic opener guidance
- Every new help post receives a standardized embedded checklist explaining how to ask a good question, what information to include and a safety warning about untrusted package installation.
- The opener is explicitly mentioned and the message has a footer describing the inactivity/close behavior.

## PDIS-HF005 — Starter-message pinning
- The original forum starter message is automatically pinned so the question remains easy to find while the thread grows.
- Missing/deleted starter messages and already-deleted posts are handled without crashing the lifecycle handler.

## PDIS-HF006 — Claimant-only close plus silent permission failure
- The post owner can close their own help post, while configured staff roles can also close it.
- The close check intentionally fails silently outside help posts or for unauthorized users, avoiding noisy permission errors.

## PDIS-HF007 — Dedicated help-post title editing
- Authorized helpers can rename a help forum post directly with a lightweight command.
- The command is intentionally inert outside the help forum and for non-helper users.

## PDIS-HF008 — Owner-departure notification
- When a help-post owner leaves the server, every still-open post they own receives a warning message.
- Archived posts are ignored and missing/deleted threads are safely suppressed.

## PDIS-HF009 — Answered/unanswered session analytics
- A lightweight Redis marker records whether anyone other than the claimant/bot replied.
- Completed sessions are classified as answered or unanswered and combined with total in-use duration.

## PDIS-HF010 — Separate total-open gauge and lifecycle timings
- The system reports the current number of open help posts as a gauge.
- Completed sessions report how long each post remained active, allowing both current load and historical workload analysis.

## PDIS-HF011 — Deleted-starter idle fallback
- If the starter message disappeared, the system examines recent messages to decide whether the post should still be treated as inactive/deleted-idle.
- If the owner never posted again, closure timing can fall back to the thread creation timestamp rather than failing due to missing starter data.

## PDIS-HF012 — Participant-aware inactivity closure message
- On inactivity closure, the bot checks recent non-bot participants.
- If only the original poster ever participated, the closure can mention them directly to draw attention to the guidance for asking better questions.

## PDIS-HF013 — Graceful closure under API failure
- Failure to send the closing message does not prevent the thread from being archived/locked.
- Lifecycle correctness is prioritized over auxiliary notification delivery.

## Дубликаты

Общие tickets/helpdesk уже есть в банке, поэтому здесь сохранены именно специализированные свойства Discord Forum-based support workflow: lifecycle, inactivity scheduler, claimant semantics и support analytics.
