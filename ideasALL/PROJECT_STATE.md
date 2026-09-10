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

Recursive Git Tree проверен полностью (`truncated=false`). Основные области: `src/commands`, `src/config`, `src/database`, `src/events`, `src/handlers`, `src/interactions`, `src/music`, `src/packages`.

### Batch 1

Каталог: `ideasALL/ideas/CORWIN_BATCH1.md` — **COR-001–080**.

Обработаны: `commands/automod`, `commands/autosetup`, `commands/casino`, `commands/custom-commands`, `commands/economy`, `commands/family`, `commands/games`, security handlers и ключевая ticket/transcript инфраструктура.

### Batch 2

Каталог: `ideasALL/ideas/CORWIN_BATCH2.md` — **COR-081–125**.

Дополнительно фактически просмотрены отдельные файлы birthdays, bot info, guild info, levels, message rewards, notepad, sticky messages, suggestions, thanks, invites и voice.

Журнал продолжения: `ideasALL/research/corwindev_batch2.md`.

### Точная точка продолжения

**Не считать `src/commands` закрытым. Продолжить его полный фактический обход с оставшихся команд/категорий. Затем: `src/events` → `src/handlers` → `src/interactions` → `src/config` → `src/database` → `src/music` → `src/packages` → прочие файлы.**

Только после полного закрытия CorwinDev перейти к Tomato6969.

`bot/main.py` и другая реализация InsaneBot не изменяются.
