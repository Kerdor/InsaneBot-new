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

Repository: `CorwinDev/Discord-Bot`, branch `main`.

Полный recursive Git Tree проверен повторно. Все обнаруженные области и root-level файлы просмотрены и сверены с банком идей.

### Batch'и
- Batch 1: `COR-001–080`.
- Batch 2: `COR-081–125`.
- Batch 3: `COR-126–201`; `src/commands` закрыт.
- Batch 4: `src/events` — `COR-202–248`.
- Batch 5: оставшиеся ветки `src/events` — `COR-249–293`.
- Batch 6: `src/handlers` — `COR-294–314`.
- Batch 7: `src/handlers` — `COR-315–332`.
- Batch 8: `src/interactions` — `COR-333–341`.
- Batch 9: `src/database` — `COR-342`.
- Batch 10: `src/music` — `COR-343–346`.
- Batch 11: `src/packages` — `COR-347–354`.
- Batch 12: root/startup/infrastructure verification — `COR-355–359`.

`CorwinDev/Discord-Bot` **ЗАВЕРШЁН**.

## Tomato6966/Multipurpose-discord-bot — IN PROGRESS

Repository: `Tomato6966/Multipurpose-discord-bot`, branch `new_2025`.

### Batch 1
- `commands/⌨️ Programming` — ✅ обработано.
- Добавлены `TOM-001–005`.

### Batch 2
- `commands/⚙️ Settings` — ✅ обработано полностью.
- Добавлены `TOM-006–011`.
- Дубли и полностью закомментированные команды не учитывались.

### Batch 3
- `commands/⚜️ Custom Queue(s)` — ✅ обработано полностью.
- Добавлены `TOM-012–020`.

### Batch 4
- `commands/🎤 Voice` — ✅ обработано полностью.
- Добавлены `TOM-021–033`.

### Batch 5
- `commands/🎮 MiniGames` — ✅ обработано полностью.
- Добавлены `TOM-034–058`.
- Отключённые `.js.disabled`, `uno.js` и unsupported `poker-night.js` как рабочие механики не учитывались.

### Batch 6 — текущий
- `commands/🎶 Music` — 🔄 в работе.
- Добавлены `TOM-059–071` в `ideasALL/ideas/TOMATO_BATCH5.md`.
- Новые находки: previous/similar track, DM-grab, playtop, moveme, radio catalog/search, radio reconnect, shuffle rollback, queue deduplication, queue status, Music Mix и Song of the Day.
- Базовые music controls проверяются на дубли и новые детали.
- `voteskip.js` / `removevoteskip.js` полностью закомментированы; `lyrics.js` / `searchplaylist.js` не выполняют заявленную механику.

### Текущая точка
`commands/🎶 Music` **ЕЩЁ НЕ ЗАКРЫТА**. Продолжить с оставшихся файлов Music, затем закрыть папку только после полного прохода.

`bot/main.py` и implementation InsaneBot не изменялись.
