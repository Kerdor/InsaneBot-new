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
- Просмотрены все 5 файлов.
- Добавлены `TOM-073–077` в `ideasALL/ideas/TOMATO_BATCH6.md`.
- Зафиксированы текстовый калькулятор, интерактивный calculator UI, вывод числа e, вывод числа π и пользовательские отложенные напоминания.

### Batch 8
- `commands/👀 Filter` — ✅ обработано полностью.
- Просмотрены все 16 файлов.
- Добавлены `TOM-078–092` в `ideasALL/ideas/TOMATO_BATCH7.md`.
- Зафиксированы 8D rotation, Bass Boost, Equalizer presets, reset EQ/filter, готовые voice/timescale эффекты и ручные pitch/speed/rate.
- `cleareq.js` сверён с `clearfilter.js` и не добавлен отдельно.

### Batch 9
- `commands/👑 Owner` — ✅ обработано полностью.
- Просмотрены все 19 файлов.
- Добавлены `TOM-093–106` в `ideasALL/ideas/TOMATO_BATCH8.md`.
- Зафиксированы owner-инструменты для управления ботом, конфигурацией, статусом, owner list, slash deploy, reload/restart, reset данных, рекламой и диагностикой.
- `addmoney.js` / `removemoney.js` сверены с существующей экономикой; `stopbot.js` и отключённый `reloadbot.js` не считались рабочими командами.

### Batch 10 — `commands/💪 Setup` — В РАБОТЕ
- Recursive tree директории проверен; содержание ещё не закрыто.
- Первая часть Setup добавлена как `TOM-107–116` в `ideasALL/ideas/TOMATO_BATCH9.md`.
- Вторая проверенная часть добавлена как `TOM-117–127` в `ideasALL/ideas/TOMATO_BATCH9_PART2.md`.
- `TOM-117`: AI-Chat channel.
- `TOM-118`: Anti-Caps с процентным порогом, whitelist каналов и mute threshold.
- `TOM-119`: Anti-Discord Links с whitelist каналов/серверов и mute threshold.
- `TOM-120`: Anti-Mention с лимитом member/role mentions и whitelist каналов.
- `TOM-121`: автоматические backup сервера раз в 2 дня с удалением старых backup.
- `TOM-122`: Auto-Delete с отдельной задержкой для каждого канала, 3–3600 секунд.
- `TOM-123`: Auto-Embed для нескольких выбранных каналов.
- `TOM-124`: Auto-Meme раз в минуту.
- `TOM-125`: Auto-NSFW раз в минуту только в NSFW-канале.
- `TOM-126`: массовое переключение Auto-Warn правил через multi-select.
- `TOM-127`: Anti-Nuke с модульными защитами, per-module whitelist, дневными/недельными/месячными/all-time thresholds, несколькими наказаниями, quarantine и Suggested Settings.
- `setup-blacklist.js` повторно не добавлялся как отдельная система: базовая blacklist уже есть; batch-add через запятые и reset отмечены как проверенные детали без отдельного ID.
- Redirect-файлы `setup-antimassmention.js`, `setup-antimasspings.js`, `setup-antipings.js`, `setup-auditlog.js` отдельно не считаются.

### Текущая точка
`commands/💪 Setup` **НЕ закрыта**. Продолжить с оставшихся файлов Setup после уже проверенных `setup-autowarn.js` / `setup-antinuke.js`; не переходить к Economy до полного закрытия Setup.

`bot/main.py` и implementation InsaneBot не изменялись.
