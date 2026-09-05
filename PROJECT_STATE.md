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

Полностью обработан весь `bot/exts/backend/`. Далее начат `bot/exts/filtering/`.

В filtering уже просмотрены development overview и основные специализированные surfaces: `filtering.py`, `antispam.py`, `domain.py`, `extension.py`, `image_hash.py`, `invite.py`, `token.py`, `unique.py`, `filter_list.py`.

Созданы source-specific файлы:
- `ideas/PYTHON_DISCORD.md`;
- `ideas/PYTHON_DISCORD_ADVANCED.md`;
- `ideas/PYTHON_DISCORD_BACKEND.md`;
- `ideas/PYTHON_DISCORD_BACKEND_2.md`;
- `ideas/PYTHON_DISCORD_FILTERING_ENGINE.md`;
- `ideas/PYTHON_DISCORD_FILTERING_UI.md`;
- `ideas/PYTHON_DISCORD_FILTERING_SPECIAL.md`.

Записаны только отличающиеся механики: event-branding/asset rotation, API reconciliation, global command guards, interactive error help, filtering UI/templates, image hashes, invite anti-obfuscation/trusted-server handling, spoiler-aware tokens, per-filter overrides, edit-trigger suppression, delayed anti-spam aggregation и другие специализированные варианты.

**Следующая точка:** продолжать `bot/exts/filtering/` по recursive tree, сверяя уже предварительно просмотренные файлы и добирая остальные.

**Источник не завершён. Следующие репозитории не трогать.**
