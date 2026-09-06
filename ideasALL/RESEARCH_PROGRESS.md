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
| 7 | `Tomato6969/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | — |

## `codebymitch/TitanBot` — АКТИВЕН

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation, Music, Reaction_roles, Search, ServerStats, Ticket, Tools, Utility, Config, Events, Handlers, Interactions и Services.

Пакеты идей:
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

### `Handlers` — ЗАКРЫТ

Проверена фактическая `src/handlers/` и вложенные `help/`, `interactionHandlers/`, `loaders/`: 16 обнаруженных файлов. Зафиксировано TH-001–TH-320.

### `Interactions` — ЗАКРЫТ

Проверена фактическая `src/interactions/` во всех трёх ветках `buttons/`, `modals/`, `selectMenus/`. Проверены все обнаруженные definition-файлы. Зафиксировано TI-001–TI-160.

### `Services` — ЗАКРЫТ

Проверен фактический `src/services/` и вложенные `config/`, `leveling/`, `moderation/`, `music/`. Все обнаруженные service-файлы просмотрены и сверены с уже существующими тематическими пакетами. Зафиксировано TSVC-001–TSVC-190 в `ideas/TITAN_SERVICES.md`.

### Точная точка продолжения

**`src/commands/`, `src/config/`, `src/events/`, `src/handlers/`, `src/interactions/` и `src/services/` полностью закрыты.** Следующий необработанный top-level каталог по фактическому дереву `src/`: **`src/utils/`**.

Продолжать строго по порядку. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
