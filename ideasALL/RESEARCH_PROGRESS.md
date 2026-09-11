# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения глубокого исследования без потери позиции.

## Правила
- Источники исследуются строго по очереди.
- Внутри активного репозитория фиксируется каждая обработанная папка и файл.
- Переход к следующему источнику разрешён только после `ЗАВЕРШЁН` у текущего.
- `✅` означает реальный просмотр + сверку с банком идей.
- Дубликаты не добавляются; новые детали существующих систем сохраняются.
- На текущем этапе bot implementation не изменяется; исследуются только ideas/research/checkpoints.
- Работа ведётся большими батчами, но с фиксацией точной точки продолжения.

## Источники
| № | Репозиторий | Статус | Журнал |
|---|---|---|---|
| 1 | `Cog-Creators/Red-DiscordBot` | ✅ ЗАВЕРШЁН | `research/red-discord-bot.md` |
| 2 | `python-discord/bot` | ✅ ЗАВЕРШЁН | `research/python-discord-bot.md` |
| 3 | `ItzSudhan/Discord-MusicBot` | ✅ ЗАВЕРШЁН | `research/discord-music-bot.md` |
| 4 | `codebymitch/TitanBot` | ✅ ЗАВЕРШЁН | `research/titanbot.md` |
| 5 | `GAwesomeBot/bot` | ✅ ЗАВЕРШЁН | `research/gawesomebot.md` |
| 6 | `CorwinDev/Discord-Bot` | ✅ ЗАВЕРШЁН | `research/corwindev.md` |
| 7 | `Tomato6966/Multipurpose-discord-bot` | 🔄 В РАБОТЕ | `research/tomato6966.md` |

## CorwinDev/Discord-Bot — COMPLETE
Полный recursive Git Tree проверен повторно. Все обнаруженные области и root-level файлы просмотрены и сверены с банком идей.

Batch 1: `COR-001–080`.
Batch 2: `COR-081–125`.
Batch 3: `COR-126–201`; `src/commands` закрыт.
Batch 4: `src/events` — `COR-202–248`.
Batch 5: `src/events` — `COR-249–293`.
Batch 6: `src/handlers` — `COR-294–314`.
Batch 7: `src/handlers` — `COR-315–332`.
Batch 8: `src/interactions` — `COR-333–341`.
Batch 9: `src/database` — `COR-342`.
Batch 10: `src/music` — `COR-343–346`.
Batch 11: `src/packages` — `COR-347–354`.
Batch 12: root/startup/infrastructure — `COR-355–359`.

`CorwinDev/Discord-Bot` **ЗАВЕРШЁН**.

## Tomato6966/Multipurpose-discord-bot — IN PROGRESS
Ветка: `new_2025`.

### Batch 1–9
- `commands/⌨️ Programming` — `TOM-001–005`, закрыто.
- `commands/⚙️ Settings` — `TOM-006–011`, закрыто.
- `commands/⚜️ Custom Queue(s)` — `TOM-012–020`, закрыто.
- `commands/🎮 MiniGames` — `TOM-034–058`, закрыто.
- `commands/🎤 Voice` — `TOM-021–033`, закрыто.
- `commands/🎶 Music` — `TOM-059–072`, закрыто.
- `commands/🏫 School Commands` — `TOM-073–077`, закрыто.
- `commands/👀 Filter` — `TOM-078–092`, закрыто.
- `commands/👑 Owner` — `TOM-093–106`, закрыто.

### Batch 10 — `commands/💪 Setup` — ЗАВЕРШЁН
- `TOM-107–116` → `TOMATO_BATCH9.md`.
- `TOM-117–145` → `TOMATO_BATCH9_PART2.md`.
- `TOM-146–171` → `TOMATO_BATCH9_PART3.md`.
- `TOM-172–184` → `TOMATO_BATCH9_PART4.md`.
- Recursive Setup перепроверен; redirects/дубли не размножены.

### Batch 11 — `commands/💸 Economy` — ЗАВЕРШЁН
- Recursive Economy tree проверен; все 27 command files просмотрены.
- `TOM-185–196` → `TOMATO_BATCH10.md`.
- `TOM-197` → `TOMATO_BATCH11.md`.
- Зафиксированы Black Market, cooldown tiers, bulk buy/sell, sell fee, inventory valuation, combined-capital leaderboard, gambling payout variants, Crime/Rob variants и Economy help panel.

### Batch 12 — `databases/` — ЗАВЕРШЁН
- Дерево `databases/` проверено; runtime-хранилища Enmap/SQLite и placeholder-файлы.
- `handlers/loaddb.js` проверен полностью.
- `TOM-198–200` → `TOMATO_BATCH12.md`.
- `TOM-198`: domain-separated Enmap storage.
- `TOM-199`: numbered slots до 100 конфигураций.
- `TOM-200`: ensure/default schema initialization.
- Бинарные SQLite/WAL-файлы не считались отдельными механиками.

### Batch 13 — `events/` — ЗАВЕРШЁН
- Проверены `events/client` и `events/guild`.
- `TOM-201–216` → `TOMATO_BATCH13.md`.
- Зафиксированы auto-clean bot-channel IDs, music request channel isolation, Bot Permission preflight, thread auto-join, unified command gateway, synthetic Message adapter, music self-healing/preconditions, dynamic status placeholders/rotation, startup diagnostics, lazy databasing, partial fetch, temporary error replies и shard lifecycle logging.
- Базовые diagnostic/lifecycle hooks, пустые handlers и уже существующие механики не размножены.

### Batch 14 — `handlers/` — первая крупная часть
- `TOM-217–227` → `TOMATO_BATCH14.md`.
- Проверены крупные functional handlers; дубли Setup/Logger/helper-систем не размножены.

### Batch 15 — `handlers/playermanagers/` + `handlers/erela_events/`
- `TOM-228–230` → `TOMATO_BATCH15.md`.
- Обе вложенные директории проверены рекурсивно.
- Зафиксированы timed messages, единая Music Control Panel и voice preflight.

### Batch 16 — root-level handlers
- `TOM-231–240` → `TOMATO_BATCH16.md`.
- Проверены основные оставшиеся root-level handlers.
- Зафиксированы giveaway DM notifications, JTC ownership transfer/cleanup, ticket confirmation/close behavior, CAPTCHA quarantine role, leveling anti-farm, level role rewards, reversible suggestion votes/voter list и declarative slash builder.

### Batch 17 — финальный recursive контроль `handlers/` — ЗАВЕРШЁН
- `TOM-241–242` → `TOMATO_BATCH17.md`.
- Root-level handlers из `index.js` сверены с журналом; вложенные `playermanagers/` и `erela_events/` закрыты ранее.
- `handlers/` **ПОЛНОСТЬЮ ЗАВЕРШЁН**.

### Batch 18 — `botconfig/` + `social_log/` — ЗАВЕРШЁН
- `TOM-243–245`: Twitch Live Logger, live-role + temporary ping, автоматическое обновление Twitch OAuth.
- `TOM-246`: Twitter Feed с фильтрацией reply/retweet и дедупликацией.
- `TOM-247`: YouTube Feed с несколькими каналами и историей отправленных видео.
- TikTok Logger не добавлен как рабочая система, потому что в текущей ветке он отключён; закомментированная `twitterfeed2` также не учитывалась.
- Статические botconfig JSON не считаются самостоятельными механиками.
- `botconfig/` и `social_log/` **ЗАВЕРШЕНЫ**.

### Batch 19 — `slashCommands/` — ЗАВЕРШЁН
- `TOM-248–254` → `ideasALL/ideas/TOMATO_BATCH19.md`.
- Рекурсивно проверены `Admin`, `Fun`, `Info`, `Music`, `NSFW` и root-level `chat.js`.
- Большинство slash-команд оказались альтернативными интерфейсами уже исследованных систем и не были размножены.
- Новые идеи: replay текущего трека, modstats, source-size diagnostics, расширенная invite statistics card, интерактивный FAQ, SoundCloud play+skip и общий слой image/meme generators.
- `Info/translate.js` исключён как нерабочий в текущем виде.

`bot/main.py` и implementation InsaneBot не изменялись.
