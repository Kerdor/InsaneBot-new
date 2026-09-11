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
7. **Tomato6966/Multipurpose-discord-bot — ЗАВЕРШЁН.**

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

## Tomato6966/Multipurpose-discord-bot — COMPLETE

Ветка: `new_2025`.

### Batch 1–9
- `commands/Programming` — `TOM-001–005`.
- `commands/Settings` — `TOM-006–011`.
- `commands/Custom Queue(s)` — `TOM-012–020`.
- `commands/Voice` — `TOM-021–033`.
- `commands/MiniGames` — `TOM-034–058`.
- `commands/Music` — `TOM-059–072`.
- `commands/School Commands` — `TOM-073–077`.
- `commands/Filter` — `TOM-078–092`.
- `commands/Owner` — `TOM-093–106`.

### Batch 10 — `commands/Setup` — ЗАВЕРШЁН
- `TOM-107–184` → `TOMATO_BATCH9*.md`.
- Recursive Setup перепроверен; redirects/дубли не размножены.

### Batch 11 — `commands/Economy` — ЗАВЕРШЁН
- `TOM-185–197` → `TOMATO_BATCH10.md`, `TOMATO_BATCH11.md`.
- Recursive Economy tree проверен; все 27 command files просмотрены.

### Batch 12 — `databases/` — ЗАВЕРШЁН
- `TOM-198–200` → `TOMATO_BATCH12.md`.
- Runtime storage/SQLite/WAL артефакты проверены и не считались отдельными механиками.

### Batch 13 — `events/` — ЗАВЕРШЁН
- `TOM-201–216` → `TOMATO_BATCH13.md`.
- `events/client` и `events/guild` закрыты.

### Batch 14–17 — `handlers/` — ЗАВЕРШЁН
- `TOM-217–242` → `TOMATO_BATCH14.md` … `TOMATO_BATCH17.md`.
- Root-level handlers и `playermanagers/`, `erela_events/` проверены рекурсивно.
- `handlers/` **ПОЛНОСТЬЮ ЗАВЕРШЁН**.

### Batch 18 — `botconfig/` + `social_log/` — ЗАВЕРШЁН
- `TOM-243–245`: Twitch Live Logger, live-role + temporary ping, автоматическое обновление Twitch OAuth.
- `TOM-246`: Twitter Feed с фильтрацией reply/retweet и дедупликацией.
- `TOM-247`: YouTube Feed с несколькими каналами и историей отправленных видео.
- TikTok Logger проверен, но в текущей ветке отключён; `twitterfeed2.js` закомментирован. Оба не добавлены как рабочие механики.
- Статические botconfig JSON не считаются самостоятельными механиками.
- `botconfig/` **ЗАВЕРШЁН**.
- `social_log/` **ЗАВЕРШЁН**.

### Batch 19 — `slashCommands/` — ЗАВЕРШЁН
- `TOM-248–254` → `TOMATO_BATCH19.md`.
- Рекурсивно проверены `Admin`, `Fun`, `Info`, `Music`, `NSFW` и root-level `chat.js`.
- Slash-команды, дублирующие уже исследованные системы, не размножались.
- Зафиксированы replay текущего трека, modstats, source-size diagnostics, расширенная invite statistics card, интерактивный FAQ, SoundCloud play+skip и общий слой image/meme generators.
- `Info/translate.js` исключён как нерабочий в текущем виде.
- `slashCommands/` **ЗАВЕРШЁН**.

### Batch 20 — финальный root-level контроль — ЗАВЕРШЁН
- `TOMATO_BATCH20.md`.
- Проверены `.github/`, `assets/`, `languages/`, `.eslintrc`, `.prettierrc`, `.gitignore`, `LICENSE`, `README.md`, `example.env`, `package.json`, `bun.lockb` и `index.js`.
- Новых самостоятельных механик не выявлено.
- Полный top-level Git Tree ветки `new_2025` закрыт.

`Tomato6966/Multipurpose-discord-bot` **ПОЛНОСТЬЮ ЗАВЕРШЁН**.

### Следующая точка
Все 7 источников из текущей очереди обработаны. Следующий этап — **глобальная обработка банка идей**: собрать идеи из всех `COR-*`/`TOM-*` и предыдущих файлов, найти пересечения, объединить дубликаты, сохранить уникальные UX/варианты и затем построить нормальный порядок реализации/RoadMap.

`bot/main.py` и другая реализация InsaneBot не изменялись.
