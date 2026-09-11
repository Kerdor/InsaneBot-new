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
- Зафиксированы Black Market boost/multiplier, разные cooldown tiers, bulk buy/sell, sell fee, inventory valuation, combined-capital leaderboard, Coinflip/Dice/Slots payout variants, Crime и Rob variants.
- Economy help panel зафиксирован отдельно; дубли не размножены.

### Batch 12 — `databases/` — ЗАВЕРШЁН
- Дерево `databases/` проверено; это runtime-хранилища Enmap/SQLite и placeholder-файлы.
- `handlers/loaddb.js` проверен полностью.
- `TOM-198`: разделение Enmap-баз по доменам и отдельным каталогам.
- `TOM-199`: numbered slots для масштабирования до 100 независимых конфигураций одного типа.
- `TOM-200`: инициализация обязательной структуры данных через `ensure`/default records.
- Бинарные SQLite/WAL-артефакты отдельно как идеи не учитывались.

## Текущая точка

`databases/` **ЗАВЕРШЁН**.

Следующий этап: определить следующую функциональную директорию Tomato и обработать её **крупным последовательным батчем**, сразу записывая новые идеи и обновляя checkpoints. Не переходить к следующему источнику — Tomato ещё не закрыт.

`bot/main.py` и другая реализация InsaneBot не изменялись.
