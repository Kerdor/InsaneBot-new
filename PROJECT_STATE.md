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

`bot/exts/info/codeblock/` закрыт: `_cog.py`, `_instructions.py`, `_parsing.py` просмотрены. Извлечены механики автоматического ревью Markdown code blocks, контекстных инструкций, повторной проверки после edit, Python/REPL detection, антиобхода tick-символами и cooldown по каналам.

`bot/exts/info/doc/` просмотрен по основным runtime-файлам `_cog.py`, `_batch_parser.py`, `_redis_cache.py` и структуре каталога. Извлечены documentation inventories/Intersphinx, разрешение конфликтов символов, lazy batch parsing страниц, приоритет пользовательского запроса, stale-inventory warnings, Redis TTL cache, retry/reschedule inventory и diff refresh.

Также просмотрены `code_snippets.py`, `patreon.py`, `pep.py`, `python_news.py`, `tags.py`. Добавлен новый тематический файл `ideas/PYTHON_DISCORD_INFO.md` с `PDIS-I001`–`PDIS-I020`.

## Следующая точка

Продолжать **только `python-discord/bot`**. Каталог `bot/exts/info/` ещё не закрыт полностью: после просмотренного info-батча необходимо добрать оставшиеся/непросмотренные файлы и затем последовательно пройти следующие каталоги recursive tree, включая root/.github/deployment, пока весь источник не будет реально закрыт.

Уже просмотренные `help`, `resources`, `pypi`, `stats`, `source`, `subscribe`, а также текущие `codeblock`, `doc`, `code_snippets`, `information`, `patreon`, `pep`, `python_news`, `tags` не считать заново без обнаружения дополнительного материала.

После полного завершения python-discord только тогда переходить к `ItzSudhan/Discord-MusicBot`.

**Другие источники не трогать.**
