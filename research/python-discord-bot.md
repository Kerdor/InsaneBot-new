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
- `alts.py` — ✅
- `clean.py` — ✅
- `defcon.py` — ✅
- `dm_relay.py` — ✅
- `incidents.py` — 🔎 runtime workflow просмотрен; основной material уже занесён в банк
- `modlog.py` — ✅
- `modpings.py` — ✅; новые идеи не добавлялись поверх `PDIS-A002`
- `silence.py` — ✅
- `slowmode.py` — ✅
- `stream.py` — ✅
- `verification.py` — ✅
- `voice_gate.py` — ✅
- `metabase.py` — ✅
- `infraction/_scheduler.py` — ✅
- `infraction/_utils.py` — ✅
- `infraction/_views.py` — ✅
- `infraction/infractions.py` — 🔎 просмотрен основной command/apply/pardon surface
- `infraction/management.py` — 🔎 просмотрен основной management/search/edit surface
- `infraction/superstarify.py` — 🔎 просмотрен полностью
- Остальные root moderation files — ⏳

## Извлечённые идеи

### Moderation
`ideas/PYTHON_DISCORD_MODERATION_2.md` содержит `PDIS-M2-001`–`PDIS-M2-016`.

`ideas/PYTHON_DISCORD_MODERATION_3.md` содержит `PDIS-M3-001`–`PDIS-M3-015`.

`ideas/PYTHON_DISCORD_MODERATION_4.md` содержит `PDIS-M4-001`–`PDIS-M4-011`: комбинированный clean-ban, compromise-response preset, shadow infractions, contextual last/recent selector, resend DM, regex search, actor audit search, state markers, deterministic forced nickname и активный nickname enforcement.

## Следующая точка

Продолжать **только `python-discord/bot`**. Сначала закрыть оставшиеся части `bot/exts/moderation/` и проверить, не остались ли вложенные файлы/строки в moderation tree. Затем пройти оставшиеся root/.github/deployment части репозитория, если они входят в выбранный полный проход. Только после полного завершения python-discord переходить к `ItzSudhan/Discord-MusicBot`.

**Другие источники не трогать.**
