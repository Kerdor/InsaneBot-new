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
- ServerStats;
- Ticket;
- Tools;
- Utility.

### ServerStats
Просмотрены command/modules/service/handlers/events/scheduler/config paths. Зафиксировано TSS-001–TSS-170.

### Search
Просмотрены command и search modules. Зафиксировано TS-001–TS-080.

### Ticket
Просмотрены ticket command/dashboard, service/database/permissions/logging modules, handlers, feedback persistence и связанные config/transcript paths. Зафиксировано TT-001–TT-170.

### Tools — ЗАКРЫТ

Просмотрены:
- `src/commands/Tools/baseconvert.js`;
- `src/commands/Tools/calculate.js`;
- `src/commands/Tools/countdown.js`;
- `src/handlers/countdownButtons.js`;
- `src/commands/Tools/embedbuilder.js`;
- `src/commands/Tools/generatepassword.js`;
- `src/commands/Tools/hexcolor.js`;
- `src/commands/Tools/poll.js`;
- `src/commands/Tools/randomuser.js`;
- `src/commands/Tools/shorten.js`;
- `src/commands/Tools/time.js`;
- `src/commands/Tools/unixtime.js`.

Зафиксировано TTOOL-001–TTOOL-244.

### Utility — ЗАКРЫТ

Просмотрены:
- `src/commands/Utility/avatar.js`;
- `src/commands/Utility/firstmsg.js`;
- `src/commands/Utility/report.js`;
- `src/commands/Utility/serverinfo.js`;
- `src/commands/Utility/todo.js`;
- `src/commands/Utility/userinfo.js`;
- `src/commands/Utility/weather.js`;
- `src/commands/Utility/wipedata.js`;
- `src/commands/Utility/modules/report.js`;
- `src/commands/Utility/modules/report_setchannel.js`;
- `src/handlers/todoButtons.js`.

Зафиксировано TUTILITY-001–TUTILITY-240.

### Config — ЗАКРЫТ

Полностью проверен `src/config/` по фактическому дереву:
- `src/config/application.js`;
- `src/config/bot.js`;
- `src/config/commands/commandAliases.js`;
- `src/config/commands/commandCategories.js`;
- `src/config/commands/prefixRestrictions.js`;
- `src/config/database/postgres.js`;
- `src/config/database/schemaVersion.js`;
- `src/config/guild/guildConfigDefaults.js`;
- `src/config/music/lavalink.js`;
- `src/config/shop/index.js`;
- `src/config/shop/items.js`.

Зафиксировано в `ideas/TITAN_CONFIG.md` — TITAN-G001–TITAN-G232.

Существенные новые блоки: production/development config behavior, centralized embed branding, application retention, verification safety/audit limits, welcome/goodbye templates, counter resolver configuration, global feature flags, command/subcommand alias resolution, protected commands, granular prefix restrictions, PostgreSQL connection/SSL/pool/TTL/health/migration configuration, schema version contract, multi-source Lavalink node loading, API/CORS/rate-limit settings и декларативная shop pricing/transaction/event configuration.

## Уже зафиксировано в ideas
- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md` — TITAN-G001–TITAN-G232;
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
- `ideas/TITAN_TICKETS.md` — TT-001–TT-170;
- `ideas/TITAN_TOOLS.md` — TTOOL-001–TTOOL-244;
- `ideas/TITAN_UTILITY.md` — TUTILITY-001–TUTILITY-240.

## Точная точка продолжения

`src/commands/` и `src/config/` — полностью закрыты.

Следующий необработанный top-level каталог по фактическому дереву `src/`: **`src/events/`**.

Продолжать строго по порядку. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
