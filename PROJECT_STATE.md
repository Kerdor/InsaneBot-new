# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **максимально глубокий сбор и каталогизация идей/механик из сторонних Discord-ботов.**

## Правила

- Источники исследуются строго по очереди и не переключаются до полного завершения текущего.
- Собираем максимально всё, включая очевидные, маленькие и потенциально бесполезные механики.
- Перед добавлением сверяем банк идей; идентичные дубликаты не размножаем.
- Для существующей системы сохраняем только новые UX, поведение, настройки, ограничения или архитектурные варианты.
- Идеи сразу распределяются по тематическим `ideas/`; новые тематические файлы разрешены.
- Работа ведётся большими батчами, но с фиксацией точной точки продолжения.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — АКТИВНО ИССЛЕДУЕТСЯ.**
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6969/Multipurpose-discord-bot — ОЖИДАЕТ.

## `codebymitch/TitanBot` — АКТИВЕН

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation, Music, Reaction_roles, Search, ServerStats, Ticket, Tools, Utility, Config, Events и Handlers.

Пакеты TitanBot:
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
- `ideas/TITAN_HANDLERS.md` — TH-001–TH-320.

### `Events` — ЗАКРЫТ

Просмотрены все 14 файлов `src/events/` и зафиксировано TE-001–TE-280.

### `Handlers` — ЗАКРЫТ

Проверена фактическая директория `src/handlers/` со всеми обнаруженными файлами и вложенными каталогами:
- `calculateModals.js`;
- `countdownButtons.js`;
- `counterButtons.js`;
- `giveawayButtons.js`;
- `loggingButtons.js`;
- `musicButtons.js`;
- `ticketButtons.js`;
- `todoButtons.js`;
- `verificationButtons.js`;
- `warningHandlers.js`;
- `wipedataButtons.js`;
- `help/helpButtons.js`;
- `help/helpSelectMenus.js`;
- `interactionHandlers/reactionRolesSelectMenu.js`;
- `loaders/events.js`;
- `loaders/interactions.js`.

Зафиксировано **TH-001–TH-320** в `ideas/TITAN_HANDLERS.md`.

### Точная точка продолжения

**`src/commands/`, `src/config/`, `src/events/` и `src/handlers/` полностью закрыты.**

Следующий необработанный top-level каталог по фактическому дереву `src/`: **`src/interactions/`**.

Продолжать строго по порядку дерева. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
