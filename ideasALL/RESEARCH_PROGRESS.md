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

### Batch 3
- `commands/⚜️ Custom Queue(s)` — ✅ обработано полностью.
- Добавлены `TOM-012–020`.

### Batch 4
- `commands/🎤 Voice` — ✅ обработано полностью.
- Добавлены `TOM-021–033`.

### Batch 5
- `commands/🎮 MiniGames` — ✅ обработано полностью.
- Добавлены `TOM-034–058`.

### Batch 6
- `commands/🎶 Music` — ✅ обработано полностью.
- Добавлены `TOM-059–072`.

### Batch 7
- `commands/🏫 School Commands` — ✅ обработано полностью.
- Добавлены `TOM-073–077`.

### Batch 8
- `commands/👀 Filter` — ✅ обработано полностью.
- Добавлены `TOM-078–092`.

### Batch 9
- `commands/👑 Owner` — ✅ обработано полностью.
- Добавлены `TOM-093–106`.

### Batch 10 — `commands/💪 Setup` — В РАБОТЕ
- Recursive tree директории проверен; содержание ещё не закрыто.
- `TOM-107–116` в `TOMATO_BATCH9.md`.
- `TOM-117–145` в `TOMATO_BATCH9_PART2.md`.
- `TOM-146–171` в `TOMATO_BATCH9_PART3.md`.
- `TOM-146–156`: language, admin command log, member counters, Menu Apply/Ticket, music request panel, Valid-Code, Joinlist, JTC.
- `TOM-157–162`: mute style/default time, level-up reply variant, Server Roster, Report Log.
- `TOM-163–166`: up to 100 Ticket Systems, closed-ticket category, customizable Suggestion texts and voting emojis.
- `TOM-167–171`: TikTok logger, Twitter logger/fallback, Twitch logger with multiple channels and live/ghost-ping roles.
- Проверены дубли: boost, logger, radio, admin, reactionrole, rank; redirects не размножались.

### Текущая точка
`commands/💪 Setup` **НЕ закрыта**. Продолжать с оставшихся файлов Setup после обработанного social block (`setup-tiktok.js` / `setup-twitter.js` / `setup-twitch.js`), затем последовательно закрыть остаток Setup. Не переходить к Economy до полного закрытия Setup.

`bot/main.py` и implementation InsaneBot не изменялись.
