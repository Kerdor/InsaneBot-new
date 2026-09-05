# PYTHON-DISCORD — Filtering UI

## PDIS-FU001 — UI-assisted filter creation
- Filter add/edit can open an interactive editor before confirmation.
- `noui` provides direct non-interactive operation.

## PDIS-FU002 — Filter templates
- A new/edited filter can copy overrides from an existing filter by ID before applying explicit overrides.

## PDIS-FU003 — Explainable filter/setting discovery
- Commands can list loaded filter types and setting types or show a detailed description for one type.
- Filter-specific settings use `filter/setting` notation.
- Filter inspection marks fields that override the containing filter-list defaults.

## PDIS-FU004 — Interactive destructive confirmation
- Deleting a filter requires an explicit confirmation view owned by the invoking moderator.
- The deletion callback executes only after confirmation.

## PDIS-FU005 — Image-hash closest-match utility
- A moderator can hash an attached image and receive its normalized hexadecimal perceptual hash.
- Existing denied image-hash rules are searched for the closest match and the distance is displayed.
- The result distinguishes a hash inside the capture threshold from an unmatched image.

## PDIS-FU006 — Message content assembled from attachments and snapshots
- Text attachments can be decoded and a bounded amount of their content fed into the same filtering context as the message.
- Forwarded message snapshots are also included.

## PDIS-FU007 — Persistent scheduled-deletion recovery
- Pending offensive-message deletion records are loaded from the API on cog startup.
- Expired records are deleted immediately; future records are re-scheduled.

## PDIS-FU008 — Central filtering webhook alerts
- Filtering uses a dedicated webhook for moderation alerts.
- Alerts can contain rich embeds and interactive components without cluttering the original channel.

## PDIS-FU009 — Type-aware setting editor
- Interactive setting editing derives the input control from the declared setting type.
- Booleans use a constrained True/False selector instead of free-form text.
- Other values use a modal with type conversion and validation feedback.

## PDIS-FU010 — Sequence/list setting editor with duplicate suppression
- List-like settings can be edited through a dedicated UI that supports removing one item, adding one item, or replacing the whole list.
- New items already present in the list are ignored rather than duplicated.
- Large lists are bounded to Discord select-menu capacity while preserving the underlying list.

## PDIS-FU011 — Search criteria as an interactive query builder
- Filter searches can be composed through a UI: add/edit criteria, remove criteria, select filter type, apply a saved filter as a template, then execute.
- Changing filter type clears criteria belonging to the previous filter type to prevent invalid cross-type searches.

## PDIS-FU012 — Single-use interaction views with reusable state copies
- After an interaction changes state, the view is rebuilt from current state and the old view is stopped.
- This avoids stale component/select state while keeping the edit operation visually continuous.

## PDIS-FU013 — Author-bound interactive controls
- Interactive argument completion verifies that only the original command author can use the dropdown.
- Unauthorized users receive an ephemeral explanation instead of being allowed to mutate or re-run the command.

## PDIS-FU014 — Compact embed field rendering for configuration UIs
- Configuration values are rendered from structured dictionaries into embed fields automatically.
- Empty values become a visible placeholder, sequences are rendered compactly, long values are truncated, and short values are made inline.
- Internal/private fields can be hidden from the UI based on naming convention.

## Дубликаты

Общие paginator/menu/modal/confirmation UX уже есть в банке; здесь сохранены только специализированные свойства filtering UI.
