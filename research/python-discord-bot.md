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
- `__init__.py`, `__main__.py`, `errors.py`, `log.py`, `pagination.py` — просмотрены в финальном проходе; идеи из инфраструктуры извлечены.
- Utility/info/moderation/fun surfaces из предыдущих батчей — ✅

### `bot/utils/`
- Весь каталог — ✅
- `channel.py`, `checks.py`, `function.py`, `helpers.py`, `lock.py`, `message_cache.py`, `messages.py`, `modlog.py`, `time.py`, `webhooks.py` просмотрены и сверены.

### `bot/resources/`
- `foods.json` — просмотрен; это статический список данных без отдельной механики.
- `stars.json` — просмотрен; это статический список данных без отдельной механики.
- `media/print-return.gif` — ресурс без отдельной механики.
- `tags/` — каталог статических учебных tag-файлов; отдельные runtime-механики уже покрыты info/tag исследованием.

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
- `snekbox/` — весь runtime-каталог ✅

## Извлечённые идеи

### Recruitment / Talent Pool
`ideas/PYTHON_DISCORD_RECRUITMENT.md` содержит `PDIS-R001`–`PDIS-R036`.

### Utilities
`ideas/PYTHON_DISCORD_UTILS.md` содержит `PDIS-U001`–`PDIS-U050`.

### Core / shared infrastructure
`ideas/PYTHON_DISCORD_CORE_UTILS.md` содержит `PDIS-CU001`–`PDIS-CU040`: resource locks и wait/raise режимы, bounded message cache, context whitelists и redirects, role cooldown bypass, reaction/deletion workflows, attachment relay, unique voter counting, webhook sanitization, централизованный logging/archive, reply-aware responses, timestamp/duration helpers, expiration UX, paginator restrictions, startup dependency handling, intent/mention safety, semantic exceptions и decorator global handling.

## Следующая точка

Продолжать строго по оставшейся части recursive tree: прежде всего `tests/`, `.github/`, deployment/root config и любые ещё не закрытые runtime-каталоги. `bot/utils/` и `bot/resources/` больше не являются следующей точкой. После закрытия всех содержательных файлов можно пометить `python-discord/bot` полностью завершённым.

**Другие источники не трогать.**
