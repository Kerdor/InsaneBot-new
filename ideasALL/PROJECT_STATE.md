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

Исследуется ветка `indev-4.0.2`. Фактический recursive tree проверен через Git tree API; `truncated=false`.

Корневой порядок: `Commands/` → `Configurations/` → `Database/` → `Internals/` → `Modules/` → `Temp/` → `Web/`.

### `Commands/PM/` — ЗАКРЫТ

Зафиксировано **GAB-PM-001–GAB-PM-125**.

### `Commands/Private/` — ЗАКРЫТ

Зафиксировано **GAB-PR-001–GAB-PR-049**.

### `Commands/Public/` — ФИНАЛЬНАЯ СВЕРКА

Все файлы Public из recursive tree фактически просмотрены. Последний новый batch: `ideas/GAWESOME_COMMANDS_PUBLIC_BATCH8.md`, **GAB-PUB-591–GAB-PUB-672**.

Проверены и сопоставлены с банком: moderation, tags, counters, help, archive, Imgur, RSS, Safebooru/NSFW, strikes, roles, media/search, weather, conversion и остальные Public-команды.

### Точная точка продолжения

**Финально сверить весь `Commands/Public/` по recursive tree против GAB-PUB-001–672. Если пропусков нет — закрыть Public и перейти к `Commands/Shared/`.**

После Public → Shared → только после полного Commands → Configurations.

Не переходить к CorwinDev/Discord-Bot или Tomato6969/Multipurpose-discord-bot до полного завершения GAwesomeBot.
