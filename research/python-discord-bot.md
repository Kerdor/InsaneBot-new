# Research Log — `python-discord/bot`

Статус: 🔵 **АКТИВЕН**

`✅` = реально просмотрено и сверено с банком; `⏳` = ещё не обработано; `🔎` = предварительно просмотрено до последовательного прохода.

## Фактический журнал

### Корень
- `README.md` — ✅
- Recursive tree — ✅
- Остальные root/.github/deployment files — ⏳

### `bot/`
- Core: `bot.py`, `constants.py`, `converters.py`, `decorators.py` — ✅
- Utility/info/moderation/fun surfaces из предыдущих батчей — ✅

### `bot/exts/backend/`
- Весь каталог — ✅

### `bot/exts/filtering/`
- Весь каталог — ✅
- Engine, lists, filters, anti-spam, unique/security, settings/actions/validations и UI — просмотрены и сверены.

### `bot/exts/fun/`
- Весь каталог — ✅

### `bot/exts/help_channels/`
- Весь каталог — ✅

### `bot/exts/info/`
- Весь runtime-каталог — ✅
- `doc/` включая batch parser/cache/doc item/HTML/inventory/Markdown/parsing — ✅
- Основные info-команды — ✅

### `bot/exts/moderation/`
- Все root-файлы moderation — ✅
- `watchchannels/` — ✅
- `infraction/` — ✅

### `bot/exts/recruitment/`
- `__init__.py` — ✅ (пустой)
- `talentpool/__init__.py` — ✅
- `talentpool/_api.py` — ✅
- `talentpool/_cog.py` — ✅
- `talentpool/_review.py` — ✅

### `bot/exts/utils/`
- `__init__.py` — ✅ (пустой)
- `attachment_pastebin_uploader.py` — ✅
- `bot.py` — ✅
- `extensions.py` — ✅
- `internal.py` — ✅
- `ping.py` — ✅
- `reminders.py` — ✅
- `thread_bumper.py` — ✅
- `utils.py` — ✅
- `snekbox/__init__.py` — ✅
- `snekbox/_constants.py` — ✅
- `snekbox/_cog.py` — ✅
- `snekbox/_eval.py` — ✅
- `snekbox/_io.py` — ✅

## Извлечённые идеи

### Recruitment / Talent Pool
`ideas/PYTHON_DISCORD_RECRUITMENT.md` содержит `PDIS-R001`–`PDIS-R036`: context-menu nominations, optional context modal, source attribution, private/public confirmation, relay в review thread, force nomination, persistent autoreview, execution lock, eligibility gates, weighted priority, review capacity/interval, inactivity pruning, grouped queue, nomination cooldown bucket, evidence batching/pinning, dedicated voting threads, review/archive statistics, lifecycle metadata, typed API и bulk activity lookup.

### Utilities
`ideas/PYTHON_DISCORD_UTILS.md` содержит `PDIS-U001`–`PDIS-U050`: consent-gated attachment paste, delete workflow, reminder opt-in/quotas/permissions/persistence/recovery/editing/locking, extension wildcard/batch management и rollback-safe semantics, multi-dimensional ping, WebSocket diagnostics, persistent REPL, Snekbox per-user locking, multi-version rerun, edit-and-react reruns, multi-codeblock/timeit semantics, mention/escape protection, output/file limits, filename normalization, shared output budget, output filtering и routing.

## Следующая точка

`bot/exts/recruitment/` и `bot/exts/utils/` закрыты. Следующий этап — продолжить строго по оставшейся части recursive tree: другие `bot/exts/*`, `bot/resources/`, `bot/utils/`, `tests/`, root/.github/deployment и прочие файлы, которые ещё не отмечены `✅`.

**Другие источники не трогать.**
