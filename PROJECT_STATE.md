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
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `codebymitch/TitanBot` — АКТИВЕН

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation, Music, Reaction_roles и Search.

Пакеты TitanBot:
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

Search закрыт по `src/commands/Search/` и трём модулям: `define`, `google`, `urban`. Зафиксированы единый search router, раздельные lookup modules, внешние Dictionary/Urban API, Google URL generation, URL encoding, input validation, HTTP timeout, deferred interaction lifecycle, dictionary meanings/phonetics/examples formatting, Urban cleanup/stats/author/permalink, 404/429/error classification, centralized user errors, logging и расширяемая module architecture.

Reaction_roles закрыт по command/service/handler/status/database-key paths: setup/dashboard, role safety, 5-panel guild limit, 25-role panel limit, self-assignment через select menu, add/remove/edit/repost/delete lifecycle, deleted-message recovery, message-ID migration, reconciliation, persistence, typed errors, audit logging и isolated partial failures.

### Точная точка продолжения

**Следующий раздел: `src/commands/ServerStats/`.**

После закрытия `ServerStats/` продолжать строго по порядку дерева `src/commands/`.

**Не переходить к GAwesomeBot до полного закрытия TitanBot.**
