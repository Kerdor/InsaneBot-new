# Research Log — `python-discord/bot`

Статус: 🔵 **АКТИВЕН**

Правило: этот репозиторий должен быть полностью обработан до перехода к следующему источнику.

## Порядок обхода

Формат статуса:
- `⏳` — ещё не обработано
- `🔄` — сейчас исследуется
- `✅` — полностью просмотрено, идеи сверены с `ideas/`, новые механики распределены
- `➖` — просмотрено, новых переносимых механик не найдено

## Фактический порядок обработки

### Корень
1. `README.md` — ✅
2. Дерево репозитория — ✅
3. Остальные root-файлы — ⏳

### `bot/`
4. `bot/bot.py` — ✅
5. `bot/constants.py` — ✅
6. `bot/converters.py` — ✅
7. `bot/decorators.py` — ✅
8. `bot/exts/info/subscribe.py` — ✅
9. `bot/exts/moderation/stream.py` — ✅
10. `bot/exts/moderation/silence.py` — ✅
11. `bot/exts/fun/duck_pond.py` — ✅
12. `bot/exts/info/resources.py` — ✅
13. `bot/exts/info/pypi.py` — ✅
14. `bot/exts/utils/ping.py` — ✅
   - Multi-source latency: command processing, external healthcheck, Discord API latency.
   - External HTTP/connection failure is reported independently instead of breaking the whole diagnostic.
15. `bot/exts/moderation/alts.py` — ✅
   - Alternate-account associations with actor, creation/update time, context, edit/remove and historical raw IDs.
16. `bot/exts/moderation/modpings.py` — ✅
   - Daily role schedule, temporary manual override, status/sync commands, timezone offset and persistent recovery.
17. `bot/exts/info/help.py` — ✅
   - Interactive parent/subcommand navigation, fuzzy command discovery, permission-aware candidate filtering and custom cog categories.
18. `bot/exts/utils/extensions.py` — ✅
   - Wildcard batch extension management, progress/result aggregation, operation lock, reload fallback and grouped status list.
19. `bot/exts/utils/bot.py` — ✅
   - Moderation-only echo/embed utilities and hidden bot information group.
20. `bot/exts/info/source.py` — ✅
   - Source lookup for commands/cogs/tags/help with exact GitHub file/line links and dynamic-object diagnostics.
21. `bot/exts/utils/internal.py` — ✅
   - REPL-like persistent eval environment with reset, output formatting and paste fallback; WebSocket event-rate diagnostics.
22. `bot/exts/info/stats.py` — ✅
   - Normalized event metrics by channel, command counters, member gauges, boost gauges and exclusion of noisy channels.

### Следующая точка
Продолжить с остальными файлами `bot/exts/...` строго по recursive tree, затем `bot/resources/`, `bot/utils/`, `tests/` и оставшиеся root/.github/deployment surfaces.

## Найденные новые механики

Распределены в `ideas/PYTHON_DISCORD.md`:
- PDIS-001 — persistent self-role panel recovery/recreation.
- PDIS-002 — per-user ephemeral role panel with ownership/state UX.
- PDIS-003 — temporary permission-role with persistent expiry recovery.
- PDIS-004 — temporary-to-permanent permission upgrade.
- PDIS-005 — sorted temporary/permanent permission list.
- PDIS-006 — forced active-stream termination on permission revoke.
- PDIS-007 — silence with exact previous-overwrite restoration.
- PDIS-008 — unified text/voice silence with voice-specific kick/sync modes.
- PDIS-009 — permanent silence with periodic staff reminders.
- PDIS-010 — resource lock for concurrent silence operations.
- PDIS-011 — conditional command-output redirection with paste/removal workflow.
- PDIS-012 — command context whitelist/blacklist with redirect and override roles.
- PDIS-013 — reusable target-role hierarchy decorator.
- PDIS-014 — preflight URL availability validation.
- PDIS-015 — Snowflake timestamp validation.
- PDIS-016 — unified composite duration/age converters.
- PDIS-017 — normalized resource-topic deep links.
- PDIS-018 — combined persistent public UI + ephemeral private UI pattern.
- PDIS-019 — alternate-account associations with context and history.
- PDIS-020 — scheduled role state with temporary manual override.
- PDIS-021 — interactive help parent/subcommand navigation.
- PDIS-022 — fuzzy command discovery with permission-aware suggestions.
- PDIS-023 — custom help categories independent of extension layout.
- PDIS-024 — batch extension management with wildcard, locking and rollback.
- PDIS-025 — multi-source latency healthcheck.
- PDIS-026 — WebSocket event-rate diagnostics.
- PDIS-027 — persistent REPL eval with progressive paste fallback.
- PDIS-028 — exact source-code links for commands/cogs/tags/help.
- PDIS-029 — normalized Discord event metrics.

## Дубликаты

Общие pagination, timestamps, selfroles/button roles, базовые permissions, moderation hierarchy, scheduling, state recovery и integrations не размножаются; фиксируются только новые детали, UX, ограничения или архитектурные варианты.

## Примечание

Источник **не завершён**. Следующие репозитории не трогать до полного обхода `python-discord/bot`.
