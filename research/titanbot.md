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
- Tools.

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

### Search
Просмотрены:
- `src/commands/Search/search.js`;
- `src/commands/Search/modules/search_define.js`;
- `src/commands/Search/modules/search_google.js`;
- `src/commands/Search/modules/search_urban.js`.

Зафиксировано в `ideas/TITAN_SEARCH.md` — TS-001–TS-080.

### Ticket
Просмотрены:
- `src/commands/Ticket/ticket.js`;
- `src/commands/Ticket/modules/ticket_dashboard.js`;
- `src/services/ticket.js`;
- `src/utils/database/tickets.js`;
- `src/utils/ticket/ticketPermissions.js`;
- `src/utils/ticket/ticketLogging.js`;
- `src/handlers/ticketButtons.js`;
- `src/interactions/buttons/ticket/ticketFeedback.js`;
- `src/interactions/modals/ticket/ticketFeedbackComment.js`;
- `src/utils/database/ticketFeedback.js`;
- ticket-related configuration in `src/config/bot.js`;
- ticket feedback/transcript/logging paths.

Зафиксировано в `ideas/TITAN_TICKETS.md` — TT-001–TT-170.

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

Зафиксировано в `ideas/TITAN_TOOLS.md` — TTOOL-001–TTOOL-244.

Существенные находки: countdown с pause/resume/cancel, 24h cap, runtime lifecycle и permission gate; конвертация BIN/OCT/DEC/HEX/Base36/Base58/Base62/Base64 через BigInt; безопасный калькулятор с whitelist и защитой от code-like syntax, историей последних 5 вычислений и интерактивными арифметическими операциями; криптографическая генерация паролей 8–50 символов с гарантией классов и оценкой силы; HEX→RGB/HSL/brightness/name/closest-color; poll 2–10 вариантов с anonymous режимом и reactions; random user с role/bot/online/mention фильтрами и повторным выбором; timezone/Unix timestamp utilities; URL shortener с custom suffix, timeout и API error parsing; интерактивный Embed Builder с live preview, полями, цветами, author/footer/images/timestamp, JSON/raw data, reorder/reset/post и timeout-safe modal/select lifecycle.

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
- `ideas/TITAN_SERVERSTATS.md` — TSS-001–TSS-170;
- `ideas/TITAN_TICKETS.md` — TT-001–TT-170;
- `ideas/TITAN_TOOLS.md` — TTOOL-001–TTOOL-244.

## Точная точка продолжения

`src/commands/Tools/` и связанные countdown handler — **ЗАКРЫТЫ**.

Следующий каталог по фактическому recursive tree `src/commands/`:
**`src/commands/Utility/`**.

Продолжать строго по порядку дерева `src/commands/`. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
