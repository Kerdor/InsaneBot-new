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
6. **CorwinDev/Discord-Bot — АКТИВНО ИССЛЕДУЕТСЯ.**
7. Tomato6969/Multipurpose-discord-bot — ОЖИДАЕТ.

## GAwesomeBot — COMPLETE

Ветка: `indev-4.0.2`. Полный обход закрыт: Commands, Configurations, Database, Internals, Modules, Temp, Web.

## CorwinDev/Discord-Bot — ACTIVE

Ветка: `main`.

Recursive Git Tree проверен полностью. Основные области: `src/commands`, `src/config`, `src/database`, `src/events`, `src/handlers`, `src/interactions`, `src/music`, `src/packages`.

### Batch 1

Каталог: `ideasALL/ideas/CORWIN_BATCH1.md` — **COR-001–080**.

### Batch 2

Каталог: `ideasALL/ideas/CORWIN_BATCH2.md` — **COR-081–125**.

### Batch 3

Каталог: `ideasALL/ideas/CORWIN_BATCH3.md` — **COR-126–201**.

`src/commands` подтверждённо закрыт.

### Batch 4

Каталог: `ideasALL/ideas/CORWIN_BATCH4.md` — **COR-202–248**.

### Batch 5

Каталог: `ideasALL/ideas/CORWIN_BATCH5.md` — **COR-249–293**.

`src/events` подтверждённо закрыт.

### Batch 6

Каталог: `ideasALL/ideas/CORWIN_BATCH6.md` — **COR-294–314**.

### Batch 7

Каталог: `ideasALL/ideas/CORWIN_BATCH7.md` — **COR-315–332**.

### Batch 8

Каталог: `ideasALL/ideas/CORWIN_BATCH8.md` — **COR-333–341**.

Продолжен полный обход `src/interactions`: общая slash-command архитектура, Discord Activities, интерактивный Embed builder и User Context Menu.

### Точная точка продолжения

`src/events` **ЗАКРЫТ**.
`src/handlers` **ЗАКРЫТ**.
`src/interactions` **НЕ ЗАКРЫТ** — Batch 8 обработал `Command` и `ContextMenu`, требуется финальная сверка полного дерева перед закрытием.

После полного закрытия `interactions`: `src/config` → `src/database` → `src/music` → `src/packages` → прочие файлы.

Только после полного закрытия CorwinDev перейти к Tomato6969.

`bot/main.py` и другая реализация InsaneBot не изменяются.
