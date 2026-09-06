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

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation, Music, Reaction_roles, Search, ServerStats, Ticket, Tools, Utility и Config.

Пакеты TitanBot:
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

### `Tools` — ЗАКРЫТ

Просмотрены все Tool command/handler files. Зафиксированы TTOOL-001–TTOOL-244.

### `Utility` — ЗАКРЫТ

Просмотрены все файлы `src/commands/Utility/`, `src/commands/Utility/modules/report.js`, `report_setchannel.js` и связанный `src/handlers/todoButtons.js`. Зафиксированы TUTILITY-001–TUTILITY-240.

### `Config` — ЗАКРЫТ

Полностью проверены все элементы `src/config/`: `application.js`, `bot.js`, `commands/commandAliases.js`, `commands/commandCategories.js`, `commands/prefixRestrictions.js`, `database/postgres.js`, `database/schemaVersion.js`, `guild/guildConfigDefaults.js`, `music/lavalink.js`, `shop/index.js`, `shop/items.js`.

Зафиксированы **TITAN-G001–TITAN-G232**. Основные блоки: централизованный runtime config, environment validation/defaults, embed branding, application retention, economy/shop pricing and transaction policies, verification safety/audit controls, welcome/goodbye templates, counter resolvers, global feature flags, command aliases/categories, protected commands, granular prefix restrictions, PostgreSQL pooling/SSL/TTL/health/migrations, schema version contract, multi-source Lavalink configuration и API/CORS/logging runtime settings.

### Точная точка продолжения

**`src/commands/` и `src/config/` полностью закрыты.**

Следующий необработанный top-level каталог по фактическому дереву `src/`: **`src/events/`**.

Продолжать строго по порядку дерева. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
