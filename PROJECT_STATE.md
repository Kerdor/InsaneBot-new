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

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — АКТИВНО ИССЛЕДУЕТСЯ.**
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `codebymitch/TitanBot` — АКТИВЕН

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation, Music, Reaction_roles, Search, ServerStats и Ticket.

Пакеты TitanBot:
- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md`;
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065;
- `ideas/TITAN_JOINTOCREATE.md` — TJ-001–TJ-080;
- `ideas/TITAN_LEVELING.md` — TL-001–TL-100;
- `ideas/TITAN_LOGGING.md` — TLOG-001–TLOG-100;
- `ideas/MODERATION.md` — MOD-001–MOD-135;
- `ideas/TITAN_MUSIC.md` — TM-001–TM-154;
- `ideas/TITAN_REACTION_ROLES.md` — TRR-001–TRR-170;
- `ideas/TITAN_SEARCH.md` — TS-001–TS-080;
- `ideas/TITAN_SERVERSTATS.md` — TSS-001–TSS-170;
- `ideas/TITAN_TICKETS.md` — TT-001–TT-170.

### `ServerStats` — ЗАКРЫТ

Просмотрены `src/commands/ServerStats/serverstats.js`, все четыре ServerStats modules, `src/services/serverstatsService.js`, `src/handlers/counterButtons.js`, member join/leave paths, scheduler/update path в `src/app.js` и counter config. Зафиксированы TSS-001–TSS-170: три типа member counters, voice/text variants, category placement, duplicate protection, creation rollback, persistent guild records, sanitization/legacy DB formats, member counting/fallbacks, configurable channel-name templates, 15-minute cron, immediate join/leave updates, orphan cleanup, list/update/delete UX, destructive confirmation, initiator-only controls, DB-first deletion, audit logging и error isolation.

### `Ticket` — ЗАКРЫТ

Просмотрены `src/commands/Ticket/ticket.js`, `ticket_dashboard.js`, ticket service/database/permissions/logging modules, button/modal handlers, feedback persistence и связанные config/transcript paths. Зафиксированы TT-001–TT-170: persistent panel/dashboard, staff role и open/closed categories, open-ticket limits, ticket numbering/persistence, creator/staff permissions, claim/unclaim, priority, pin/unpin, close/archive, transcript/delete flow, ticket logging, feedback, guild statistics и изолированная service/database/interaction архитектура.

### `Search` — ЗАКРЫТ

Зафиксированы TS-001–TS-080 по `src/commands/Search/`.

### Точная точка продолжения

**Следующий шаг: `src/commands/Tools/`.**

После каждого следующего крупного батча обновлять этот файл и `research/titanbot.md` с точным путём.

**Не переходить к GAwesomeBot до полного закрытия TitanBot.**
