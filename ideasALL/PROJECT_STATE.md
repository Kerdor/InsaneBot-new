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
- На текущем этапе не изменяем bot implementation; работаем только с ideas/research/checkpoints.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — ЗАВЕРШЁН.**
5. **GAwesomeBot/bot — АКТИВНО ИССЛЕДУЕТСЯ СЛЕДУЮЩИМ.**
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6969/Multipurpose-discord-bot — ОЖИДАЕТ.

## `codebymitch/TitanBot` — ЗАВЕРШЁН

Recursive tree `main` проверен полностью (`truncated=false`). Полностью закрыты все обнаруженные top-level каталоги `src/`, включая `src/utils/` и вложенные `database/`, `logging/`, `ticket/`.

Пакеты идей TitanBot включают все ранее созданные каталоги плюс:
- `ideas/TITAN_SERVICES.md` — TSVC-001–TSVC-190;
- `ideas/TITAN_UTILS.md` — TU-001–TU-292;
- `ideas/TITAN_UTILS_PRESENTATION.md` — TUP-001–TUP-076;
- `ideas/TITAN_UTILS_ERRORS.md` — TUE-001–TUE-060.

### `Utils` — ЗАКРЫТ

Проверены utility-файлы `src/utils/` и вложенные `database/`, `logging/`, `ticket/`.

Зафиксированы механики command/prefix pipeline, interaction response coordination, safe interaction lifecycle, dashboard collectors, reusable components, validation/sanitization, abuse protection, rate limiting, mutex/state storage, trace logging, structured embeds, panel recovery, welcome formatting, giveaway helpers, PostgreSQL abstraction/retry/schema/migration, canonical key system, ticket permissions/logging и safe math parser.

### Точная точка продолжения

**TitanBot полностью закрыт по фактическому `src/` дереву.**

Следующий источник по строгому порядку: **GAwesomeBot/bot**.

До полного завершения GAwesomeBot не переходить к CorwinDev/Discord-Bot или Tomato6969/Multipurpose-discord-bot.
