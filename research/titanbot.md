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
- Search.

### Search
Просмотрены:
- `src/commands/Search/search.js`;
- `src/commands/Search/modules/search_define.js`;
- `src/commands/Search/modules/search_google.js`;
- `src/commands/Search/modules/search_urban.js`.

Зафиксировано в `ideas/TITAN_SEARCH.md` — TS-001–TS-080.

Существенные находки: единый `/search` router с `define/google/urban`; отдельные modules; Dictionary API, Urban Dictionary API и Google URL generation; обязательные query fields; minimum length 2; URL encoding; HTTP timeout 5 секунд; safe defer; Urban defer fallback через 1.5 секунды; Dictionary meanings/phonetics/examples formatting; лимиты meanings/definitions; Urban cleanup, 2000-char definition и 500-char example; stats/author/permalink; 404/429 classification; centralized user errors; structured error logging; source footers; module-level extensibility и отсутствие необходимости в БД для Search.

### Уже зафиксировано в ideas
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
- `ideas/TITAN_SEARCH.md` — TS-001–TS-080.

## Точная точка продолжения

`src/commands/Search/` и связанные Search modules — **ЗАКРЫТЫ**.

Следующий каталог по фактическому recursive tree `src/commands/`:
**`src/commands/ServerStats/`**.

Продолжать строго по порядку дерева `src/commands/`. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
