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
5. **GAwesomeBot/bot — АКТИВНО ИССЛЕДУЕТСЯ.**
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6969/Multipurpose-discord-bot — ОЖИДАЕТ.

## `GAwesomeBot/bot` — АКТИВЕН

Исследуется ветка `indev-4.0.2`. Фактический recursive tree проверен через Git Tree API; `truncated=false`.

Корневой порядок: `Commands/` → `Configurations/` → `Database/` → `Internals/` → `Modules/` → `Temp/` → `Web/`.

### `Commands/PM/` — ЗАКРЫТ

Проверены все 11 файлов PM и связанный `Commands/Private/giveaway.js` как исполнитель DM giveaway relay.

Зафиксировано **GAB-PM-001–GAB-PM-125** в `ideas/GAWESOME_COMMANDS_PM.md`.

Основные блоки: глобальный AFK; personal profile wizard; privacy/background/Bio; per-step timeout и quit; reminders; персональные server aliases; remote say/poll/giveaway; relay статусы none/multi/success; DM-контроль giveaway; secret prize; duration parser/default duration; membership/blocklist/permission checks; динамический PM help; dashboard redirect для deprecated config; OAuth invite.

### Точная точка продолжения

**Следующий необработанный каталог: `Commands/Private/`.**

После него: `Commands/Public/`, затем `Commands/Shared/`. Только после полного `Commands/` переходить к `Configurations/`.

Не переходить к CorwinDev/Discord-Bot или Tomato6969/Multipurpose-discord-bot до полного завершения GAwesomeBot.
