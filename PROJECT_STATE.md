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
- Работа ведётся большими батчами, но с фиксацией точной точки продолжения.

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

Полностью обработаны `bot/exts/backend/`, `bot/exts/filtering/`, `bot/exts/fun/`, `bot/exts/help_channels/` и `bot/exts/info/`.

В `info/` закрыты codeblock, весь `doc/` (batch parser, Redis cache, doc item, HTML, inventory parser, Markdown, parsing), `code_snippets.py`, `information.py`, `patreon.py`, `pep.py`, `python_news.py`, `tags.py` и ранее просмотренные `help.py`, `resources.py`, `pypi.py`, `stats.py`, `source.py`, `subscribe.py`.

В `moderation/` просмотрены `alts.py`, `clean.py`, `defcon.py`, `dm_relay.py`, `incidents.py`, `metabase.py`, `modlog.py`, `modpings.py`, `silence.py`, `slowmode.py`, `stream.py`, `verification.py`, `voice_gate.py`, а также `infraction/_scheduler.py`, `infraction/_utils.py`, `infraction/_views.py`.

`modpings.py` не породил новый дубль поверх `PDIS-A002`.

Основные дополнительные moderation-идеи находятся в `ideas/PYTHON_DISCORD_MODERATION_2.md` (`PDIS-M2-001`–`PDIS-M2-016`) и `ideas/PYTHON_DISCORD_MODERATION_3.md` (`PDIS-M3-001`–`PDIS-M3-015`).

## Следующая точка

Продолжать **только `python-discord/bot`** и строго внутри `bot/exts/moderation/`.

Следующий крупный батч:
1. оставшиеся root moderation files;
2. `infraction/infractions.py`;
3. `infraction/management.py`;
4. `infraction/superstarify.py`;
5. затем повторно сверить recursive tree на предмет пропущенных файлов.

Не переходить к `ItzSudhan/Discord-MusicBot`, пока весь `python-discord/bot` реально не закрыт.

**Другие источники не трогать.**
