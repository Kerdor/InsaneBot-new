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
- Birthday; Community; Core; Economy; Fun; Giveaway; JoinToCreate; Leveling; Logging; Moderation; Music; Reaction_roles; Search; ServerStats; Ticket; Tools; Utility; Config; Events; Handlers; Interactions; Services.

### Handlers — ЗАКРЫТ

Проверена фактическая директория `src/handlers/` и вложенные каталоги `help/`, `interactionHandlers/`, `loaders/`.

Проверены 16 обнаруженных файлов. Зафиксировано **TH-001–TH-320** в `ideas/TITAN_HANDLERS.md`.

### Interactions — ЗАКРЫТ

По фактическому дереву `src/interactions/` проверены все обнаруженные definition-файлы в `buttons/`, `modals/` и `selectMenus/`.

Зафиксировано **TI-001–TI-160** в `ideas/TITAN_INTERACTIONS.md`.

### Services — ЗАКРЫТ

Проверен фактический `src/services/` и его вложенные каталоги.

Проверены/перекрёстно сверены:
- `applicationService.js`;
- `birthdayService.js`;
- `commandAccessService.js`;
- `config/guildConfig.js`;
- `config/configService.js`;
- `countingGameService.js`;
- `economyService.js`;
- `giveawayService.js`;
- `joinToCreateService.js`;
- `leveling/levelRoleSyncService.js`;
- `leveling/leveling.js`;
- `leveling/xpSystem.js`;
- `loggingService.js`;
- `moderation/moderationService.js`;
- `moderation/warningService.js`;
- `music/musicActions.js`;
- `music/musicEmbeds.js`;
- `music/musicVoiceState.js`;
- `music/permissions.js`;
- `music/playerHandler.js`;
- `music/playerStore.js`;
- `music/prefixSupport.js`;
- `music/riffySetup.js`;
- `panelHealthService.js`;
- `reactionRoleService.js`;
- `serverstatsService.js`;
- `ticket.js`;
- `verificationService.js`.

Новые service-layer детали после сверки с уже существующими тематическими пакетами зафиксированы в `ideas/TITAN_SERVICES.md` — **TSVC-001–TSVC-190**.

Ключевые блоки: service boundaries и typed errors; bounded in-memory state; application validation/cooldowns; guild config normalization/patching/legacy migration/history; command registry/access snapshots; counting state normalization; economy transaction safety/rollback; giveaway validation and background processing; JoinToCreate template sanitization; verification cooldown/attempt tracking and auto-verify criteria; panel health reconciliation and message-ID recovery; startup level-role synchronization; cross-service cache/DB fallbacks and resilience.

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
- `ideas/TITAN_UTILITY.md` — TUTILITY-001–TUTILITY-240;
- `ideas/TITAN_HANDLERS.md` — TH-001–TH-320;
- `ideas/TITAN_INTERACTIONS.md` — TI-001–TI-160;
- `ideas/TITAN_SERVICES.md` — TSVC-001–TSVC-190.

## Точная точка продолжения

`src/commands/`, `src/config/`, `src/events/`, `src/handlers/`, `src/interactions/` и `src/services/` полностью просмотрены по фактическому дереву.

Следующий необработанный top-level каталог по фактическому дереву `src/`: **`src/utils/`**.

Продолжать строго по порядку. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
