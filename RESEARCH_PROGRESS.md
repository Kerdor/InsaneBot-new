# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения глубокого исследования в новом чате без потери позиции.

## Правила

- Источники исследуются строго по очереди.
- Внутри активного репозитория фиксируется каждая обработанная папка и файл в порядке фактического обхода.
- Переход к следующему источнику разрешён только после `ЗАВЕРШЁН` у текущего.
- `✅` означает реальный просмотр + сверку с банком идей.
- Дубликаты не добавляются; новые детали существующих систем сохраняются.
- После каждого существенного батча обновляются журнал и `PROJECT_STATE.md`.

## Источники

| № | Репозиторий | Статус | Журнал |
|---|---|---|---|
| 1 | `Cog-Creators/Red-DiscordBot` | ✅ ЗАВЕРШЁН | `research/red-discord-bot.md` |
| 2 | `python-discord/bot` | ✅ ЗАВЕРШЁН | `research/python-discord-bot.md` |
| 3 | `ItzSudhan/Discord-MusicBot` | ✅ ЗАВЕРШЁН | `research/discord-music-bot.md` |
| 4 | `codebymitch/TitanBot` | 🔵 АКТИВЕН | `research/titanbot.md` |
| 5 | `GAwesomeBot/bot` | ⏳ ОЖИДАЕТ | — |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | — |
| 7 | `Tomato6966/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | — |

## `codebymitch/TitanBot` — АКТИВЕН

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation, Music, Reaction_roles, Search, ServerStats и Ticket.

Пакеты идей:
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

Просмотрены command, все четыре modules, service, counter button handler, member join/leave event paths, scheduler в `src/app.js` и counter config. Зафиксированы TSS-001–TSS-170: типы счётчиков, создание voice/text channels в category, duplicate protection, persistence/sanitization, member counting, configurable names, cron + event-driven updates, orphan cleanup, list/update/delete UX, destructive confirmation, initiator-only buttons, DB-first deletion и error isolation.

### `Ticket` — ЗАКРЫТ

Просмотрены ticket command/dashboard, service, database helpers, permissions/logging utilities, button/modal handlers, feedback persistence и связанные config/transcript paths. Зафиксированы TT-001–TT-170: panel/dashboard, persistent guild config, role/category selectors, open-ticket limits, ticket lifecycle/counter, permissions, claim/unclaim, priorities, pin/unpin, close/archive, transcript/delete flow, ticket logging, feedback и guild statistics, а также service-layer/error-isolation архитектура.

### Точная точка продолжения

**Следующий шаг: `src/commands/Tools/`.**

Продолжать строго по порядку дерева `src/commands/`. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
