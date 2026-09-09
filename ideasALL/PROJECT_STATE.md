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

Зафиксировано **GAB-PM-001–GAB-PM-125**.

### `Commands/Private/` — ЗАКРЫТ

Зафиксировано **GAB-PR-001–GAB-PR-049**.

### `Commands/Public/` — В РАБОТЕ

Public уже имеет основной банк и четыре предыдущих батча. Последний созданный батч — `ideas/GAWESOME_COMMANDS_PUBLIC_BATCH5.md`, **GAB-PUB-386–GAB-PUB-452**.

В батче 5 дополнительно подтверждены детали `_base.js`, moderation confirmation/DM/ModLog flows, weekly server statistics, streamer watchlist, tags, temporary rooms, trivia, timezone/translation и URL/media edge cases.

Public **НЕ ЗАКРЫТ**: необходимо продолжить полный просмотр оставшихся файлов и только после этого сделать финальную сверку всего каталога.

### Точная точка продолжения

Продолжать **`Commands/Public/`**. Следующая работа — пройти оставшиеся Public-файлы, сверить каждую новую механику с GAB-PUB-001–452 и не переходить в `Shared` до фактического закрытия Public.

После `Public` → `Commands/Shared/`. Только после полного `Commands/` → `Configurations/`.

Не переходить к CorwinDev/Discord-Bot или Tomato6969/Multipurpose-discord-bot до полного завершения GAwesomeBot.
