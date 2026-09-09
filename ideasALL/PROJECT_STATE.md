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

### `Commands/Public/` — ЗАКРЫТ

Финальная сверка выполнена по recursive tree ветки `indev-4.0.2`. Каталог содержит **74 файла**, включая `_base.js`; все файлы сопоставлены с просмотренными материалами и банком идей.

Зафиксирован диапазон **GAB-PUB-001–GAB-PUB-672**. Пропусков в текущей нумерации не выявлено; историческое перекрытие `BATCH7` сохранено без удаления.

### `Commands/Shared/` — ЗАКРЫТ

Проверены все **4 файла**: `_base.js`, `debug.js`, `eval.js`, `reload.js`.
Зафиксировано **GAB-SH-001–GAB-SH-094**.

Разобраны общий контракт Shared-команд, shard/process/OS/master diagnostics, maintainer permission diagnostics, безопасный eval, secret censoring, async eval, большие результаты через gist, execution timing, hot-reload команд/events и wildcard reload.

### `Commands/` — ЗАКРЫТ

Все четыре подкаталога `Commands/PM/`, `Commands/Private/`, `Commands/Public/`, `Commands/Shared/` исследованы и закрыты.

### Точная точка продолжения

**Следующий шаг: начать `Configurations/` и пройти его полностью.**

После `Configurations/` → `Database/` → `Internals/` → `Modules/` → `Temp/` → `Web/`.

Другие репозитории не трогать до полного завершения GAwesomeBot.
