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
- Birthday; Community; Core; Economy; Fun; Giveaway; JoinToCreate; Leveling; Logging; Moderation; Music; Reaction_roles; Search; ServerStats; Ticket; Tools; Utility; Config; Events; Handlers; Interactions.

### Handlers — ЗАКРЫТ

Проверена фактическая директория `src/handlers/` и вложенные каталоги `help/`, `interactionHandlers/`, `loaders/`.

Проверены 16 обнаруженных файлов: calculateModals.js, countdownButtons.js, counterButtons.js, giveawayButtons.js, loggingButtons.js, musicButtons.js, ticketButtons.js, todoButtons.js, verificationButtons.js, warningHandlers.js, wipedataButtons.js, help/helpButtons.js, help/helpSelectMenus.js, interactionHandlers/reactionRolesSelectMenu.js, loaders/events.js, loaders/interactions.js.

Зафиксировано **TH-001–TH-320** в `ideas/TITAN_HANDLERS.md`.

### Interactions — ЗАКРЫТ

По фактическому дереву `src/interactions/` проверены все обнаруженные definition-файлы в `buttons/`, `modals/` и `selectMenus/`.

Buttons: countdown/countdown.js; counter/counterDelete.js; giveaway/giveaway.js; help/help.js; logging/logging.js; music/music.js; ticket/ticket.js; ticket/ticketFeedback.js; todo/todoShared.js; verification/verification.js; warnings/warnings.js; wipedata/wipedata.js.

Modals: calculate/calculate.js; config/config_modal.js; ticket/ticket.js; ticket/ticketFeedbackComment.js; todo/todoShared.js; warnings/warningDelete.js.

Select menus: help/helpCategory.js; logging/logging.js; reactionRoles/reaction_roles.js; ticket/ticketFeedback.js.

Зафиксировано **TI-001–TI-160** в `ideas/TITAN_INTERACTIONS.md`.

Основные блоки: декларативная регистрация interaction definitions, object/array export normalization, повторное использование одного execute, customId context, config modal parsing, ticket feedback rating/comment/decline, shared todo modal pipeline, destructive warning workflow, logging selector→modal цепочки, music queue/pagination controls, countdown controls, verification adapter и reaction-role select adapter.

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
- `ideas/TITAN_INTERACTIONS.md` — TI-001–TI-160.

## Точная точка продолжения

`src/commands/`, `src/config/`, `src/events/`, `src/handlers/` и `src/interactions/` полностью просмотрены по фактическому дереву.

**Следующий необработанный top-level каталог `src/`: `src/services/`.**

Продолжать строго по порядку. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
