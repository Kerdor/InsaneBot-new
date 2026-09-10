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

## GAwesomeBot — ACTIVE

Ветка: `indev-4.0.2`. Recursive tree проверен через Git Tree API; `truncated=false`.

### Commands — ЗАКРЫТ

- PM: **GAB-PM-001–125**
- Private: **GAB-PR-001–049**
- Public: **GAB-PUB-001–672**, 74 файла включая `_base.js`; финальная сверка выполнена, пропусков не выявлено.
- Shared: **GAB-SH-001–094**, 4 файла.

### Configurations — ЗАКРЫТ

Проверены все 13 файлов каталога `Configurations/` по recursive tree и сопоставлены с банком идей.
Зафиксировано **GAB-CONF-001–086** в `ideasALL/ideas/GAWESOME_CONFIG.md`.

Разобраны command registry/metadata, aliases/categories/defaults, admin levels и named permissions, shard/web/database/runtime settings, logging levels, encryption/session secrets, global blocklists, maintainer roles, activity/status, event routing, modular event pipelines, rank thresholds, RSS streaming, status-message pools, tags, NSFW/profanity dictionary и trivia dataset.

### Точная точка продолжения

**Следующий шаг: начать `Database/` и пройти его полностью.**

После `Database/` → `Internals/` → `Modules/` → `Temp/` → `Web/`.

Другие репозитории не трогать до полного завершения GAwesomeBot.
