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
| 3 | `ItzSudhan/Discord-MusicBot` | 🔵 АКТИВЕН | `research/discord-music-bot.md` |
| 4 | `codebymitch/TitanBot` | ⏳ ОЖИДАЕТ | — |
| 5 | `GAwesomeBot/bot` | ⏳ ОЖИДАЕТ | — |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | — |
| 7 | `Tomato6966/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | — |

## `ItzSudhan/Discord-MusicBot` — АКТИВЕН

Ветка: `v5`.

### Закрыто

- root README/tree/config/index/package;
- `commands/slash/` — все команды из recursive tree;
- `commands/context/play.js`;
- все 6 файлов `events/`;
- `lib/DiscordMusicBot.js` — дочитан полностью;
- `lib/SlashCommand.js`, `lib/EpicPlayer.js`;
- весь `util/`: `Controller.js`, `db.js`, `getChannel.js`, `getConfig.js`, `getLavalink.js`, `guildDb.js`, `loadCommands.js`;
- весь исходный `api/`: `index.js`, `middlewares/auth.js`, `router.js`, `routes/dashboard.js`, `routes/data.js`;
- исходный `dashboard/`: страницы, components и utils, включая динамическую `pages/servers/[id].tsx`.

### Идеи

- `ideas/MUSIC.md` — MUSIC-001–042;
- `ideas/MUSIC_COMMANDS.md` — MUSIC-C001–055;
- `ideas/MUSIC_CONTEXT.md` — MUSIC-X001–007;
- `ideas/MUSIC_EVENTS.md` — MUSIC-E001–025;
- `ideas/MUSIC_STORAGE.md` — MUSIC-S001–018;
- `ideas/MUSIC_CORE.md` — MUSIC-K001–018;
- `ideas/MUSIC_WEB.md` — MUSIC-W001–031.

### Последний батч

Проверен весь `util/` и закрыт `api/`. В `api/` найдены Express-сервер, Passport Discord OAuth, session auth middleware, динамическое подключение route-файлов, защищённые dashboard endpoints и public data endpoint с динамическим invite URL. Затем дочитан исходный `dashboard/`: NextUI dark theme, typed API helpers, dashboard stat cards, server selector/avatar UI, общий navbar/layout, login/logout redirects и модель состояния сервера с queue/loop/playing.

Скомпилированный `dashboard/out/` зафиксирован как build artifact и не используется как отдельный источник новых механик поверх исходного TypeScript-кода.

## Следующая точка

Продолжить строго по recursive tree `v5`: сначала `deploy/`, затем `docker/`, `.github/`, затем оставшиеся root-файлы и любые ещё не закрытые исходные каталоги/файлы. Скомпилированные `dashboard/out/_next` не дублировать после анализа исходников.

**`ItzSudhan/Discord-MusicBot` НЕ ЗАВЕРШЁН. Следующие источники не трогать.**
