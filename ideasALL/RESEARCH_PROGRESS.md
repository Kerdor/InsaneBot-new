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

### Batch 6
- `commands/🎶 Music` — ✅ обработано полностью.
- Добавлены `TOM-059–072` в `ideasALL/ideas/TOMATO_BATCH5.md`.
- Новые находки: previous/similar track, DM-grab, playtop, moveme, radio catalog/search, radio reconnect, shuffle rollback, queue deduplication, queue status, Music Mix, Song of the Day и отдельный searchsimilar.
- Базовые music controls проверены на дубли; нерабочие/закомментированные варианты не учитывались.

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
- Первая часть: `TOM-107–116` в `ideasALL/ideas/TOMATO_BATCH9.md`.
- Вторая часть: `TOM-117–127` в `ideasALL/ideas/TOMATO_BATCH9_PART2.md`.
- Текущий проход добавил `TOM-128–145` в `ideasALL/ideas/TOMATO_BATCH9_PART2.md`.
- `TOM-128–135`: многоэкземплярная Application-система, автосоздание application-раздела, кастомный дизайн, анкета, отдельные accept/deny/ticket сообщения, временная/accept роли, пять вариантов результата с собственными ролями/сообщениями/изображениями и Last Verify.
- `TOM-136–139`: многоэкземплярный Auto-Support, до 25 вариантов, индивидуальный Embed/обычный ответ, повторная публикация панели в выбранный канал.
- `TOM-140–141`: Custom Commands до 25 на сервер и выбор Embed/обычного ответа.
- `TOM-142–145`: глобальный цвет Embed, footer icon из URL/вложения, footer text и toggle thumbnail.
- `TOM-146–156` добавлены в `ideasALL/ideas/TOMATO_BATCH9_PART3.md`.
- `TOM-146`: интерактивная смена языка с reset/status и несколькими языками.
- `TOM-147`: отдельный канал для логирования выполнения административных команд.
- `TOM-148–149`: до 25 Member Counter систем и расширенные placeholders серверной статистики для имён каналов.
- `TOM-150`: Menu Apply с до 100 конфигураций и до 25 вариантов в панели.
- `TOM-151–152`: Menu Ticket до 100 конфигураций, до 25 вариантов, general access/closed category и per-system claim с кастомными сообщениями.
- `TOM-153`: постоянная Music Request панель с кнопками управления.
- `TOM-154`: toggle Valid-Code системы.
- `TOM-155`: Joinlist с шестью типами условий и четырьмя действиями при join.
- `TOM-156`: до 100 независимых JTC конфигураций, создание trigger или использование текущего VC и кастомное имя временных комнат.
- Проверены и сверены дубли: `setup-boost.js`, `setup-logger.js`, `setup-radio.js`, `setup-admin.js`; `setup-serverstats.js` — redirect на membercount.

### Текущая точка
`commands/💪 Setup` **НЕ закрыта**. Следующий участок — продолжать с оставшихся файлов Setup после уже обработанного блока (ориентир: следующие файлы после `setup-membercount.js` / `setup-menuticket.js` / `setup-music.js`). Не переходить к Economy до полного закрытия Setup.

`bot/main.py` и implementation InsaneBot не изменялись.
