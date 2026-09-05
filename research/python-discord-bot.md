# Research Log — `python-discord/bot`

Статус: 🔵 **АКТИВЕН**

Правило: этот репозиторий должен быть полностью обработан до перехода к следующему источнику.

## Порядок обхода

Формат статуса:
- `⏳` — ещё не обработано
- `🔄` — сейчас исследуется
- `✅` — полностью просмотрено, идеи сверены с `ideas/`, новые механики распределены
- `➖` — просмотрено, новых переносимых механик не найдено

## Зафиксированная структура источника

Полное recursive tree репозитория получено на commit/tree SHA `0e4cd5cb46f2239eacccdded8cdf02ba89028ab9`. В дереве присутствуют root, `bot/`, `bot/exts/`, `bot/resources/`, `bot/utils/`, `tests/` и вложенные директории. Обход продолжается строго по порядку дерева; получение полного дерева само по себе не считается обработкой файлов.

## Фактический порядок обработки

### Корень
1. `README.md` — ✅
2. Дерево репозитория — ✅
3. Остальные root-файлы — ⏳

### `bot/`
4. `bot/bot.py` — ✅
   - Lifecycle Bot, extension-load performance transaction, startup API healthcheck с retry/cooldown, централизованный event error handling и special handling Forbidden/block.
5. `bot/constants.py` — ✅
   - Env-based nested configuration, scoped channel/role/category settings, event enums и thread archive periods.
6. `bot/converters.py` — ✅
   - Extension special `*`/`**`, ValidURL reachability, Inventory validation, Snowflake timestamp validation, composite duration/age parsing.
7. `bot/decorators.py` — ✅
   - Whitelist/blacklist checks, redirect-output с paste fallback, hierarchy decorator и debug short-circuit.
8. `bot/exts/info/subscribe.py` — ✅
   - Persistent public self-role entry point, ephemeral per-user panel, ownership check, dynamic button state, sorting, startup recovery/recreation.
9. `bot/exts/moderation/stream.py` — ✅
   - Temporary/permanent streaming permissions, persistent expiry cache, temp→permanent upgrade, active-stream suspension, sorted access list.
10. `bot/exts/moderation/silence.py` — ✅
   - Text/voice silence, exact previous-overwrite restoration, timed/permanent silence, notifier, voice kick/sync, thread restriction, resource locks.
11. `bot/exts/fun/duck_pond.py` — ✅
   - Reaction-threshold relay, staff-only counting, channel blacklist, webhook/attachment fallback, idempotency, relay lock, checkmark restoration, admin bypass.
12. `bot/exts/info/resources.py` — ✅
   - Topic deep-linking and kebab-case normalization.
13. `bot/exts/info/pypi.py` — ✅
   - PyPI package lookup, input validation, release timestamp, rotating response styling, temporary invalid-input/error cleanup.
14. `bot/exts/utils/ping.py` — ⏳

### Следующая точка
`bot/exts/utils/ping.py` → затем остальные `bot/exts/...` строго по recursive tree.

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
- PDIS-009 — permanent silence notifier with periodic staff reminders.
- PDIS-010 — resource lock for concurrent silence operations.
- PDIS-011 — conditional command-output redirection with paste/removal workflow.
- PDIS-012 — command context whitelist/blacklist with redirect and override roles.
- PDIS-013 — reusable target-role hierarchy decorator.
- PDIS-014 — preflight URL availability validation.
- PDIS-015 — Snowflake timestamp validation.
- PDIS-016 — unified composite duration/age converters.
- PDIS-017 — normalized resource-topic deep links.
- PDIS-018 — combined persistent public UI + ephemeral private UI pattern.

## Дубликаты, которые сознательно не размножались

Общие pagination, timestamps, selfroles/button roles, базовые permissions, moderation hierarchy, scheduling, state recovery и integrations уже есть в банке; из текущих файлов фиксируются только новые детали, UX, ограничения или архитектурные варианты.

## Примечания для продолжения

- Не переходить к `ItzSudhan/Discord-MusicBot`, пока этот документ не будет помечен `ЗАВЕРШЁН`.
- Перед каждой новой записью сверять найденное с существующим банком идей.
- После каждого существенного батча обновлять этот журнал и `PROJECT_STATE.md`.
