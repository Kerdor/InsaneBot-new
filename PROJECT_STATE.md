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

Полностью обработаны `bot/exts/backend/` и `bot/exts/filtering/`. Filtering закрыт после последовательной проверки engine, lists, filters, anti-spam, unique/security, settings/actions/validations и UI.

В filtering добавлены последние UI-идеи `PDIS-FU009`–`PDIS-FU014`: type-aware setting editor, sequence/list editor, interactive search builder, state-copy views, author-bound controls и compact embed rendering.

Начат `bot/exts/fun/`.

Создан source-specific файл `ideas/PYTHON_DISCORD_FUN.md`. Из `duck_pond.py` и `off_topic_names.py` добавлены `PDIS-FUN001`–`PDIS-FUN012`: threshold reaction relay, unique-user threshold, trusted-role restrictions, idempotent marker + lock, manual bypass, attachment-preserving webhook relay, marker restoration, scheduled random channel rotation, active/inactive pool, fuzzy similarity guard, normalized fuzzy search, rate-limit-aware deferred rename, pool exhaustion handling.

## Следующая точка

Продолжать **только `python-discord/bot`**, после `bot/exts/fun/` идти дальше по recursive tree. После полного завершения python-discord только тогда переходить к `ItzSudhan/Discord-MusicBot`.

**Другие источники не трогать.**
