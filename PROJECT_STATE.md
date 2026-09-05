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
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — СЛЕДУЮЩИЙ.**
4. codebymitch/TitanBot — ОЖИДАЕТ.
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `python-discord/bot` — ЗАВЕРШЁН

Полностью закрыт recursive tree.

Проверены:
- весь `bot/exts/*`;
- `bot/utils/*`;
- `bot/resources/*`;
- core/shared infrastructure (`__main__`, `errors`, `pagination`, logging и т. д.);
- `tests/*` и специализированные test helpers/base classes;
- `.github/*` и reusable workflows;
- Docker/deployment/root configuration.

Новые пакеты идей:
- `ideas/PYTHON_DISCORD_RECRUITMENT.md` — `PDIS-R001`–`PDIS-R036`;
- `ideas/PYTHON_DISCORD_UTILS.md` — `PDIS-U001`–`PDIS-U050`;
- `ideas/PYTHON_DISCORD_CORE_UTILS.md` — `PDIS-CU001`–`PDIS-CU040`;
- `ideas/PYTHON_DISCORD_TESTING.md` — `PDIS-T001`–`PDIS-T025`;
- `ideas/PYTHON_DISCORD_DEPLOYMENT.md` — `PDIS-D001`–`PDIS-D038`.

Журнал: `research/python-discord-bot.md` — статус `✅ ЗАВЕРШЁН`.

## Следующая точка

Начать **`ItzSudhan/Discord-MusicBot`** с корневого README/tree и идти по нему целиком, большими батчами, не переходя к следующему источнику до полного закрытия.

**Другие источники до завершения MusicBot не трогать.**
