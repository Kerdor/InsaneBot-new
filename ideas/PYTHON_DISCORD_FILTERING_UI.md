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
