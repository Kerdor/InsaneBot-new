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
- `__init__.py` — ✅ (пустой)
- `duck_pond.py` — ✅
- `off_topic_names.py` — ✅

### `bot/exts/help_channels/`
- `__init__.py` — ✅
- `_caches.py` — ✅
- `_channel.py` — ✅
- `_cog.py` — ✅
- `_stats.py` — ✅

### `bot/exts/info/`
- Весь runtime-каталог — ✅
- codeblock + весь `doc/` включая batch parser/cache/doc item/HTML/inventory/Markdown/parsing — ✅
- `code_snippets.py`, `information.py`, `patreon.py`, `pep.py`, `python_news.py`, `tags.py` — ✅
- ранее просмотренные `help.py`, `resources.py`, `pypi.py`, `stats.py`, `source.py`, `subscribe.py` — ✅

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
- Остальные root moderation files — ⏳
- `infraction/_scheduler.py` — ✅
- `infraction/_utils.py` — ✅
- `infraction/_views.py` — ✅
- `infraction/infractions.py` — ⏳
- `infraction/management.py` — ⏳
- `infraction/superstarify.py` — ⏳

## Извлечённые идеи

### Info
`ideas/PYTHON_DISCORD_INFO.md` содержит `PDIS-I001`–`PDIS-I026`; `ideas/PYTHON_DISCORD_INFO_2.md` содержит `PDIS-I2-001`–`PDIS-I2-011`. Сюда входят codeblock automation, documentation/inventory pipeline, PEP/news/Patreon, tag UX, raw API inspection и дополнительные documentation/source механики.

### Moderation
`ideas/PYTHON_DISCORD_MODERATION_2.md` содержит `PDIS-M2-001`–`PDIS-M2-016`: DEFCON account-age gate, emergency lockdown, incident workflow/catch-up/archive safety, clean composite filters и 14-day deletion strategy, cancellable cleanup и persisted temporary streaming permissions.

`ideas/PYTHON_DISCORD_MODERATION_3.md` содержит `PDIS-M3-001`–`PDIS-M3-015`: suppression tokens для служебных audit events, permission-aware modlog blacklist, role/reply/voice audit details, infraction active/history lifecycle, отдельный pardon/user reason, автоматический tidy-up, scheduler resync, callable actions и timeout boundary handling.

`modpings.py` дополнительно проверен на scheduled pingable-role behavior; отдельные идеи не дублировались, потому что ключевая схема уже была зафиксирована как `PDIS-A002`.

## Следующая точка

Продолжать **только `python-discord/bot`** и строго внутри `bot/exts/moderation/`. Следующий крупный батч — оставшиеся root moderation files, затем `infraction/infractions.py`, `management.py`, `superstarify.py` и любые вложенные материалы.

После полного завершения python-discord только тогда переходить к `ItzSudhan/Discord-MusicBot`.

**Другие источники не трогать.**
