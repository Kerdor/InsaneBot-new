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

### Services — ЗАКРЫТ
Проверен фактический `src/services/` и вложенные каталоги; новые service-layer детали зафиксированы в `ideas/TITAN_SERVICES.md` — TSVC-001–TSVC-190.

### Utils — ЗАКРЫТ
Проверен фактический `src/utils/` и вложенные каталоги `database/`, `logging/`, `ticket/`.

Проверены utility-файлы:
- `abuseProtection.js`
- `collectorComponents.js`
- `commandInputValidation.js`
- `commandPipeline.js`
- `components.js`
- `constants.js`
- `dashboardSession.js`
- `database.js`
- `economy.js`
- `embeds.js`
- `errorHandler.js`
- `errorRegistry.js`
- `helpers.js`
- `interactionHelper.js`
- `interactionValidator.js`
- `logger.js`
- `memoryStorage.js`
- `messageAdapter.js`
- `moderation.js`
- `mutex.js`
- `panelStatus.js`
- `prefixParser.js`
- `rateLimiter.js`
- `safeMathParser.js`
- `schemas.js`
- `serviceErrorBoundary.js`
- `sqlIdentifiers.js`
- `validation.js`
- `welcome.js`
- `giveaways.js`
- `responseCoordinator.js`
- `permissionGuard.js`

Проверены вложенные database-файлы:
- `database/guildConfigStorage.js`
- `database/keyMigration.js`
- `database/keyParser.js`
- `database/keys.js`
- `database/schema.js`
- `database/tickets.js`
- `database/wrapper.js`

Проверены вложенные logging-файлы:
- `logging/logEmbeds.js`
- `logging/loggingUi.js`

Проверены вложенные ticket-файлы:
- `ticket/ticketLogging.js`
- `ticket/ticketPermissions.js`

Новые utility-layer детали зафиксированы в:
- `ideas/TITAN_UTILS.md` — TU-001–TU-292;
- `ideas/TITAN_UTILS_PRESENTATION.md` — TUP-001–TUP-076;
- `ideas/TITAN_UTILS_ERRORS.md` — TUE-001–TUE-060.

Ключевые utility-блоки: единый command/prefix pipeline; quoted prefix parsing; slash/prefix response coordination; safe interaction lifecycle; dashboard collector ownership/timeouts; reusable Discord components; validation и context-specific sanitization; risky-command abuse protection/anomaly detection; rate limiting и keyed mutex; AsyncLocalStorage trace IDs; structured rotating logs; standardized embeds/log fields; panel message recovery; welcome placeholder formatting; giveaway storage/fallbacks; PostgreSQL connection retry/backoff/schema ledger; canonical/legacy key migration; structured storage plans; ticket permission/logging helpers; safe math parser; SQL identifier allowlists.

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
- `ideas/TITAN_SERVICES.md` — TSVC-001–TSVC-190;
- `ideas/TITAN_UTILS.md` — TU-001–TU-292;
- `ideas/TITAN_UTILS_PRESENTATION.md` — TUP-001–TUP-076;
- `ideas/TITAN_UTILS_ERRORS.md` — TUE-001–TUE-060.

## Точная точка продолжения

`src/commands/`, `src/config/`, `src/events/`, `src/handlers/`, `src/interactions/`, `src/services/` и `src/utils/` полностью просмотрены по фактическому дереву.

**TitanBot: `src/` закрыт полностью.**

Следующий этап по строгому порядку источников: **GAwesomeBot/bot**.

Не переходить к CorwinDev/Discord-Bot или Tomato6969/Multipurpose-discord-bot до полного завершения GAwesomeBot.
