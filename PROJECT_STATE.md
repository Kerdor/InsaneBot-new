# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **максимально глубокий сбор и каталогизация идей/механик из сторонних Discord-ботов.**

## Правила

- Источники исследуются строго по очереди и не переключаются до полного завершения текущего.
- Собираем максимально всё, включая очевидные, маленькие и потенциально бесполезные механики.
- Перед добавлением сверяем банк идей; идентичные дубликаты не размножаем.
- Для существующей системы сохраняем только новые UX, поведение, настройки, ограничения или архитектурные варианты.
- Идеи сразу распределяются по тематическим `ideas/`; новые тематические файлы разрешены.

## Восстановление после смены чата

- `RESEARCH_PROGRESS.md` — глобальная контрольная точка.
- `research/<source>.md` — последовательный журнал источника.
- `✅` означает реальный просмотр и сверку.
- После каждого существенного батча обновляются журнал и `PROJECT_STATE.md`.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — АКТИВЕН.**
3. ItzSudhan/Discord-MusicBot — ОЖИДАЕТ.
4. codebymitch/TitanBot — ОЖИДАЕТ.
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `python-discord/bot` — текущая точка

Полное recursive tree получено на tree SHA `0e4cd5cb46f2239eacccdded8cdf02ba89028ab9`.

Полностью обработаны `bot/exts/backend/` и `bot/exts/filtering/`. Filtering закрыт после проверки engine, lists, filters, anti-spam, unique/security, settings/actions/validations и UI.

`bot/exts/fun/` закрыт: `duck_pond.py` и `off_topic_names.py` просмотрены, добавлены `PDIS-FUN001`–`PDIS-FUN012` в `ideas/PYTHON_DISCORD_FUN.md`.

`bot/exts/help_channels/` закрыт: `_caches.py`, `_channel.py`, `_cog.py`, `_stats.py` просмотрены, добавлены `PDIS-HF001`–`PDIS-HF013` в `ideas/PYTHON_DISCORD_HELP_CHANNELS.md`.

`bot/exts/info/` закрыт по runtime-поверхности: codeblock, doc включая `_cog.py`, `_batch_parser.py`, `_redis_cache.py`, `_doc_item.py`, `_html.py`, `_inventory_parser.py`, `_markdown.py`, `_parsing.py`, а также `code_snippets.py`, `information.py`, `patreon.py`, `pep.py`, `python_news.py`, `tags.py` и ранее просмотренные `help.py`, `resources.py`, `pypi.py`, `stats.py`, `source.py`, `subscribe.py`. Основной банк содержит `PDIS-I001`–`PDIS-I026`; дополнительные уникальные механики вынесены в `ideas/PYTHON_DISCORD_INFO_2.md` (`PDIS-I2-001`–`PDIS-I2-011`).

Начат следующий каталог `bot/exts/moderation/`. Просмотрены `alts.py`, `clean.py`, `defcon.py`, `incidents.py`, `modpings.py`, `stream.py`. Дубликаты из уже существующего банка не размножались; новые аварийные, incident, clean и streaming механики вынесены в `ideas/PYTHON_DISCORD_MODERATION_2.md` (`PDIS-M2-001`–`PDIS-M2-016`). `modpings.py` в основном совпал с ранее зафиксированной механикой scheduled role state и не добавлялся повторно.

## Следующая точка

Продолжать **только `python-discord/bot`** и строго внутри `bot/exts/moderation/`. Не возвращаться к уже закрытым info/fun/help_channels/backend/filtering без появления нового материала.

В moderation ещё остаются остальные файлы и подкаталог `infraction`; их нужно последовательно просмотреть и сверить с уже существующими `MODERATION.md`, `MODERATION_DETAILS.md`, `MODLOG.md` и `PYTHON_DISCORD_MODERATION_2.md`.

После полного завершения python-discord только тогда переходить к `ItzSudhan/Discord-MusicBot`.

**Другие источники не трогать.**
