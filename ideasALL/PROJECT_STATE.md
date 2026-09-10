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
7. **Tomato6969/Multipurpose-discord-bot — СЛЕДУЮЩИЙ.**

## GAwesomeBot — COMPLETE

Ветка: `indev-4.0.2`. Полный обход закрыт: Commands, Configurations, Database, Internals, Modules, Temp, Web.

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

### Финализация CorwinDev
Проверены root-level `package.json`, `README.md`, `.env.example`, Docker/Replit/start scripts, `.github` workflow/config files, `src/index.js`, `src/bot.js`, `src/dev.js`, `src/assets/utils/*` и полный recursive tree.

Новые root/startup механики зафиксированы в Batch 12: проверка версии при запуске, Top.gg metrics/command publishing, автоматический respawn shard, reconnect/disconnect logging и единый webhook credential override через env.

`CorwinDev/Discord-Bot` **ПОЛНОСТЬЮ ЗАВЕРШЁН**.

## Следующий источник

**Tomato6969/Multipurpose-discord-bot** — можно начинать полный обход.

`bot/main.py` и другая реализация InsaneBot не изменяются.
