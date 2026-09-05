# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **максимально глубокий сбор и каталогизация идей/механик из сторонних Discord-ботов.**

## Правила

- Источники исследуются строго по очереди и не переключаются до полного завершения текущего.
- Собираем максимально всё, включая очевидные, маленькие и потенциально бесполезные механики.
- Перед добавлением сверяем банк идей; идентичные дубликаты не размножаем.
- Для существующей системы сохраняем только новые UX, поведение, настройки, ограничения или архитектурные варианты.
- Проверяем исходники, команды, handlers, конфиги, утилиты, API, deployment, тесты и документацию.
- Идеи сразу распределяются по тематическим `ideas/`; при необходимости создаются новые тематические файлы.

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

Обработаны core/utility/info/moderation surfaces предыдущих батчей, а также весь `bot/exts/backend/`:
- branding repository/cog;
- config verifier;
- error handler;
- logging;
- security;
- sync cog/syncers.

Созданы source-specific idea files:
- `ideas/PYTHON_DISCORD.md`;
- `ideas/PYTHON_DISCORD_ADVANCED.md`;
- `ideas/PYTHON_DISCORD_BACKEND.md`;
- `ideas/PYTHON_DISCORD_BACKEND_2.md`.

В них записаны только новые механики, а не прямые дубликаты общего банка.

Некоторые filtering-файлы были дополнительно просмотрены заранее для глубокого анализа: antispam, domain, extension, image_hash, invite, token, unique, filter_list. Они отмечены в исследовательском журнале как отдельный предварительный просмотр и будут сверены во время последовательного filtering pass.

**Следующая последовательная точка:** `bot/exts/filtering/FILTERS-DEVELOPMENT.md`.

**Источник не завершён. Следующие репозитории не трогать.**
