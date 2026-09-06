# PYTHON-DISCORD — Filtering engine architecture

## PDIS-FE001 — Filtering events as an internal abstraction
- Filtering events do not have to map 1:1 to Discord gateway events.
- An internal event such as `nickname` can be dispatched when another Discord event occurs, allowing the filtering engine to expose a stable semantic event model.
- Filter lists and unique filters explicitly subscribe to the semantic events they support.

## PDIS-FE002 — Filter list defaults inherited by individual filters
- A FilterList contains defaults for both validation and actions.
- Individual filters may leave fields unset and inherit the containing list's value.
- This makes large rule collections compact while still allowing per-rule exceptions.

## PDIS-FE003 — Settings groups represented as typed field bundles
- Related filter settings can be represented as one typed group with named fields.
- The same field structure can be serialized/deserialized between bot and site API.
- Adding a new setting can therefore be isolated to a new action/validation entry and its serialization metadata.

## PDIS-FE004 — Bot/site schema can evolve independently
- The bot-side filter parser can accept a newly added setting before the site UI is updated.
- Unknown/missing settings can be tolerated during staged deployment.
- This permits deploying backend support first and rolling out the configuration UI afterwards.

## PDIS-FE005 — Filtering dispatcher returns structured multi-list results
- Each filter list returns three things: actions to perform, human-readable moderation messages and the exact triggered filters grouped by list type.
- The central filtering cog merges these results before performing side effects.
- New filter lists can therefore be added without rewriting the core action executor.

## Дубликаты

Общие modular architecture и event handlers уже есть в банке; здесь сохранены только специализированные свойства filtering engine.
