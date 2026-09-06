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
- Utility;
- Config.

### Events — ЗАКРЫТ

Полностью проверен `src/events/` по фактическому дереву:
- `channelDelete.js`;
- `guildCreate.js`;
- `guildMemberAdd.js`;
- `guildMemberRemove.js`;
- `guildMemberUpdate.js`;
- `interactionCreate.js`;
- `messageCreate.js`;
- `messageDelete.js`;
- `messageUpdate.js`;
- `ready.js`;
- `roleCreate.js`;
- `roleDelete.js`;
- `userUpdate.js`;
- `voiceStateUpdate.js`.

Зафиксировано **TE-001–TE-280** в `ideas/TITAN_EVENTS.md`.

Основные блоки: event-module architecture, isolated error boundaries, guild initialization, welcome/goodbye join-leave pipelines, delayed auto-role, auto-verification, realtime counter updates, birthday preserve/restore lifecycle, application/level cleanup, nickname/username auditing, prefix/counting/leveling message pipeline, message delete/edit audit limits, unified interaction dispatcher with trace context, command/access/cooldown/permission gates, autocomplete/button/select/modal routing, startup reconciliation, role auditing, channel-deletion self-healing, temporary voice lifecycle/ownership transfer, music voice integration и cross-event resilience.

## Уже зафиксировано в ideas
- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md` — TITAN-G001–TITAN-G232;
- `ideas/TITAN_EVENTS.md` — TE-001–TE-280;
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

`src/commands/`, `src/config/` и `src/events/` — полностью закрыты.

Следующий необработанный top-level каталог по фактическому дереву `src/`: **`src/handlers/`**.

Продолжать строго по порядку. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
