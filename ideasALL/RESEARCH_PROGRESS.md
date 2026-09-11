# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения глубокого исследования без потери позиции.

## Правила
- Источники исследуются строго по очереди.
- Внутри активного репозитория фиксируется каждая обработанная папка и файл.
- Переход к следующему источнику разрешён только после `ЗАВЕРШЁН` у текущего.
- `✅` означает реальный просмотр + сверку с банком идей.
- Дубликаты не добавляются; новые детали существующих систем сохраняются.
- На текущем этапе bot implementation не изменяется; исследуются только ideas/research/checkpoints.

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
- `commands/🎤 Voice` — `TOM-021–033`, закрыто.
- `commands/🎮 MiniGames` — `TOM-034–058`, закрыто.
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
- Recursive tree проверен; все 27 command files просмотрены.
- `TOM-185–196` → `TOMATO_BATCH10.md`.
- `TOM-197` → `TOMATO_BATCH11.md`.
- `TOM-185–196`: Black Market, cooldown tiers, bulk buy/sell, sell fee, inventory valuation, combined-capital leaderboard, gambling payout variants, Crime/Rob variants.
- `ecohelp.js` проверен; отдельная help panel зафиксирована как `TOM-197`.

### Batch 12 — `databases/` — ЗАВЕРШЁН
- Дерево `databases/` проверено; runtime-хранилища Enmap/SQLite и placeholder-файлы.
- `handlers/loaddb.js` проверен полностью.
- `TOM-198–200` → `ideasALL/ideas/TOMATO_BATCH12.md`.
- `TOM-198`: domain-separated Enmap storage.
- `TOM-199`: numbered slots до 100 конфигураций одного типа.
- `TOM-200`: ensure/default schema initialization.
- Бинарные SQLite/WAL-файлы не считались отдельными механиками.

### Текущая точка
`databases/` **ЗАВЕРШЁН**.

Следующий проход — следующая функциональная директория Tomato, крупным последовательным батчем.

`bot/main.py` и implementation InsaneBot не изменялись.
