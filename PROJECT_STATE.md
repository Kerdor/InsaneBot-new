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

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation, Music, Reaction_roles, Search, ServerStats, Ticket и Tools.

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
- `ideas/TITAN_SEARCH.md` — TS-001–TS-080;
- `ideas/TITAN_SERVERSTATS.md` — TSS-001–TSS-170;
- `ideas/TITAN_TICKETS.md` — TT-001–TT-170;
- `ideas/TITAN_TOOLS.md` — TTOOL-001–TTOOL-244.

### `ServerStats` — ЗАКРЫТ

Просмотрены `src/commands/ServerStats/serverstats.js`, все четыре ServerStats modules, `src/services/serverstatsService.js`, `src/handlers/counterButtons.js`, member join/leave paths, scheduler/update path в `src/app.js` и counter config. Зафиксированы TSS-001–TSS-170.

### `Ticket` — ЗАКРЫТ

Просмотрены ticket command/dashboard, service/database/permissions/logging modules, button/modal handlers, feedback persistence и связанные config/transcript paths. Зафиксированы TT-001–TT-170.

### `Search` — ЗАКРЫТ

Зафиксированы TS-001–TS-080 по `src/commands/Search/`.

### `Tools` — ЗАКРЫТ

Просмотрены `src/commands/Tools/baseconvert.js`, `calculate.js`, `countdown.js`, `generatepassword.js`, `hexcolor.js`, `poll.js`, `randomuser.js`, `shorten.js`, `time.js`, `unixtime.js`, `embedbuilder.js` и `src/handlers/countdownButtons.js`. Зафиксированы TTOOL-001–TTOOL-244 в `ideas/TITAN_TOOLS.md`.

Основные блоки: countdown controls/lifecycle/permissions; base conversion с BigInt и Base64/Base58/Base62; безопасный calculator с whitelist, защитой от code-like patterns, history и interactive operations; crypto password generation и strength scoring; HEX color analysis; reaction polls; filtered random-user picker; timezone/Unix utilities; URL shortener; интерактивный Embed Builder с live preview, fields, colors, author/footer/images, timestamp, reorder/reset/post и timeout-safe interactions.

### Точная точка продолжения

**Следующий шаг: `src/commands/Utility/`.**

После следующего крупного батча обновить `research/titanbot.md`, `RESEARCH_PROGRESS.md` и этот файл с точным путём.

**Не переходить к GAwesomeBot до полного закрытия TitanBot.**
