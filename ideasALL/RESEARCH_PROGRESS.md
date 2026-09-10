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
- Файлы: `coliru.js`, `compile.js`, `github.js`, `httpstatus.js`, `npm.js`, `npmpkgsize.js`.
- Добавлены `TOM-001–005` в `ideasALL/ideas/TOMATO_BATCH1.md`.
- `compile.js` и `coliru.js` признаны дублем одной механики и объединены.

### Batch 2
- `commands/⚙️ Settings` — ✅ обработано полностью.
- Просмотрены все 20 файлов области.
- Добавлены `TOM-006–011` в `ideasALL/ideas/TOMATO_BATCH2.md`.
- Дубли сверены с `CORE`, `ECONOMY`, `SOCIAL` и `MUSIC`; закомментированные `toggledjonly.js` / `togglerequestonly.js` не учитывались как рабочие механики.

### Batch 3
- `commands/⚜️ Custom Queue(s)` — ✅ обработано полностью.
- Просмотрен единственный файл `savedqueue.js` целиком.
- Добавлены `TOM-012–020` в `ideasALL/ideas/TOMATO_BATCH3.md`.
- Зафиксирована система персональных именованных сохранённых музыкальных очередей и отдельные операции её редактирования, просмотра и воспроизведения.

### Batch 4
- `commands/🎤 Voice` — ✅ обработано полностью.
- Просмотрен единственный файл `voice.js` целиком по всем веткам команд.
- Добавлены `TOM-021–033` в `ideasALL/ideas/TOMATO_BATCH3.md`.
- Зафиксированы lock/unlock, stage/unstage, kick, invite, ban/unban, trust/untrust, user limit, bitrate и передача ownership для временных Join-to-Create voice-каналов.

### Batch 5
- `commands/🎮 MiniGames` — ✅ обработано полностью.
- Проверена вся директория, включая 25 рабочих файлов и 7 `.js.disabled` файлов.
- Добавлены `TOM-034–058` в `ideasALL/ideas/TOMATO_BATCH4.md`.
- Зафиксированы 2048, Connect4, Snake, Tic-Tac-Toe, RPS, Hangman, Guess The Number, Guess The Pokémon, ChaosWords, Lie Swatter, Will You Press The Button, Would You Rather, FastType, текстовые эффекты и Discord Activities (Betrayal.io, Chess, Fishington.io, YouTube Together).
- `uno.js` и `poker-night.js` не учитывались как рабочие механики; `.js.disabled` файлы не учитывались.

### Текущая точка
`commands/🎮 MiniGames` закрыта. Следующая область определяется по дереву `commands` ветки `new_2025`.

`bot/main.py` и implementation InsaneBot не изменялись.
