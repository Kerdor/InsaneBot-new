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

Help-идеи покрывают native Forum lifecycle, inactivity watchdog/rescheduling, разные причины закрытия, opener guidance, starter pinning, claimant/staff close semantics, title editing, owner-departure notification, answered/unanswered analytics, load/duration metrics, deleted-starter fallback, participant-aware closure ping и graceful failure.

## Следующая точка

Продолжать **только `python-discord/bot`**. Следующий каталог по recursive tree — `bot/exts/info/`; ранее просмотренные `help`, `resources`, `pypi`, `stats`, `source`, `subscribe` повторно не считать новыми без обнаружения дополнительного материала. В первую очередь разбирать ещё не закрытые `info/codeblock/`, `info/doc/`, `code_snippets.py`, `information.py`, `patreon.py`, `pep.py`, `python_news.py`, `tags.py`.

После полного завершения python-discord только тогда переходить к `ItzSudhan/Discord-MusicBot`.

**Другие источники не трогать.**
