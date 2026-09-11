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
- На текущем этапе не изменяем bot implementation; работаем только с ideas/research/checkpoints.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — ЗАВЕРШЁН.**
5. **GAwesomeBot/bot — ЗАВЕРШЁН.**
6. **CorwinDev/Discord-Bot — ЗАВЕРШЁН.**
7. **Tomato6966/Multipurpose-discord-bot — В РАБОТЕ.**

## CorwinDev/Discord-Bot — COMPLETE

Ветка: `main`.

Полный recursive Git Tree проверен повторно. Закрыты `src/commands`, `src/events`, `src/handlers`, `src/interactions`, `src/config`, `src/database`, `src/music`, `src/packages`, а также root-level и startup/infrastructure файлы.

### Batch'и
- Batch 1: `ideasALL/ideas/CORWIN_BATCH1.md` — `COR-001–080`.
- Batch 2: `ideasALL/ideas/CORWIN_BATCH2.md` — `COR-081–125`.
- Batch 3: `ideasALL/ideas/CORWIN_BATCH3.md` — `COR-126–201`.
- Batch 4: `ideasALL/ideas/CORWIN_BATCH4.md` — `COR-202–248`.
- Batch 5: `ideasALL/ideas/CORWIN_BATCH5.md` — `COR-249–293`.
- Batch 6: `ideasALL/ideas/CORWIN_BATCH6.md` — `COR-294–314`.
- Batch 7: `ideasALL/ideas/CORWIN_BATCH7.md` — `COR-315–332`.
- Batch 8: `ideasALL/ideas/CORWIN_BATCH8.md` — `COR-333–341`.
- Batch 9: `ideasALL/ideas/CORWIN_BATCH9.md` — `COR-342`.
- Batch 10: `ideasALL/ideas/CORWIN_BATCH10.md` — `COR-343–346`.
- Batch 11: `ideasALL/ideas/CORWIN_BATCH11.md` — `COR-347–354`.
- Batch 12: `ideasALL/ideas/CORWIN_BATCH12.md` — `COR-355–359`.

`CorwinDev/Discord-Bot` **ПОЛНОСТЬЮ ЗАВЕРШЁН**.

## Tomato6966/Multipurpose-discord-bot — IN PROGRESS

Ветка: `new_2025`.

### Batch 1
`commands/⌨️ Programming` обработано полностью: `coliru.js`, `compile.js`, `github.js`, `httpstatus.js`, `npm.js`, `npmpkgsize.js`.

Зафиксированы `TOM-001–005` в `ideasALL/ideas/TOMATO_BATCH1.md`.

### Batch 2
`commands/⚙️ Settings` обработано полностью: просмотрены все 20 файлов.

Зафиксированы `TOM-006–011` в `ideasALL/ideas/TOMATO_BATCH2.md`.

### Batch 3
`commands/⚜️ Custom Queue(s)` обработано полностью: `TOM-012–020`.

### Batch 4
`commands/🎤 Voice` обработано полностью: `TOM-021–033`.

### Batch 5
`commands/🎮 MiniGames` обработано полностью: `TOM-034–058`.

### Batch 6
`commands/🎶 Music` обработано полностью: `TOM-059–072` в `ideasALL/ideas/TOMATO_BATCH5.md`.

### Batch 7
`commands/🏫 School Commands` обработано полностью: `TOM-073–077` в `ideasALL/ideas/TOMATO_BATCH6.md`.

### Batch 8
`commands/👀 Filter` обработано полностью: `TOM-078–092` в `ideasALL/ideas/TOMATO_BATCH7.md`.

### Batch 9
`commands/👑 Owner` обработано полностью: `TOM-093–106` в `ideasALL/ideas/TOMATO_BATCH8.md`.

Зафиксированы owner-инструменты для управления ботом, конфигурацией, статусом, owner list, slash deploy, reload/restart, reset данных, рекламой и диагностикой. Дубли экономики не добавлялись; отключённые/нерабочие команды помечены и не считались рабочими механиками.

### Batch 10 — `commands/💪 Setup` — В РАБОТЕ

Recursive tree директории проверен; содержание ещё не закрыто.

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

## Текущая точка
`commands/💪 Setup` **НЕ закрыта**.

Продолжить с оставшихся файлов Setup после `setup-antinuke.js`. Не переходить к Economy до полного закрытия Setup.

`bot/main.py` и другая реализация InsaneBot не изменялись.
