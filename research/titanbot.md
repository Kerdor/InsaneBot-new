# Research Journal — codebymitch/TitanBot

Источник: `codebymitch/TitanBot`
Ветка: `main`
Статус: 🔵 АКТИВЕН

## Просмотрено

### Root / Bootstrap
- recursive tree `main` (`truncated=false`);
- `README.md`;
- `src/app.js`;
- `src/handlers/loaders/commandLoader.js`.

### Уже закрытые каталоги
- Birthday;
- Community;
- Core;
- Economy;
- Fun;
- Giveaway;
- JoinToCreate;
- Leveling;
- Logging;
- Moderation;
- Music;
- Reaction_roles;
- Search;
- ServerStats.

### ServerStats
Просмотрены:
- `src/commands/ServerStats/serverstats.js`;
- `src/commands/ServerStats/modules/serverstats_create.js`;
- `src/commands/ServerStats/modules/serverstats_list.js`;
- `src/commands/ServerStats/modules/serverstats_update.js`;
- `src/commands/ServerStats/modules/serverstats_delete.js`;
- `src/services/serverstatsService.js`;
- `src/handlers/counterButtons.js`;
- `src/events/guildMemberAdd.js`;
- `src/events/guildMemberRemove.js`;
- counter scheduler/update path in `src/app.js`;
- counter configuration path in `src/config/bot.js`.

Зафиксировано в `ideas/TITAN_SERVERSTATS.md` — TSS-001–TSS-170.

Существенные находки: три типа member counters (members+bots / humans / bots); voice/text channel variants; обязательная категория; Manage Channels; duplicate type protection; channel creation rollback при DB save failure; Counter ID и persistent guild-scoped records; enabled/createdAt/updatedAt; DB format compatibility и sanitization; full member fetch с cache fallback; memberCount fallback; configurable `{name}-{count}` channel template; 15-minute cron; immediate join/leave updates; orphan cleanup; missing-channel fetch; no-op rename optimization; counter update audit logging; list dashboard/status heuristic; update с old→new diff; destructive deletion confirmation; initiator-only buttons; DB-first deletion safety; already-deleted channel handling; service-boundary errors; centralized interaction lifecycle.

### Search
Просмотрены:
- `src/commands/Search/search.js`;
- `src/commands/Search/modules/search_define.js`;
- `src/commands/Search/modules/search_google.js`;
- `src/commands/Search/modules/search_urban.js`.

Зафиксировано в `ideas/TITAN_SEARCH.md` — TS-001–TS-080.

## Уже зафиксировано в ideas
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
- `ideas/TITAN_SERVERSTATS.md` — TSS-001–TSS-170.

## Точная точка продолжения

`src/commands/ServerStats/` и связанные ServerStats service/handler/event/scheduler paths — **ЗАКРЫТЫ**.

Следующий каталог по фактическому recursive tree `src/commands/`:
**проверить следующий элемент дерева после `ServerStats/` перед переходом дальше.**

Продолжать строго по порядку дерева `src/commands/`. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
