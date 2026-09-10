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
- Public: **GAB-PUB-001–672**, 74 файла включая `_base.js`.
- Shared: **GAB-SH-001–094**.

### Configurations — ЗАКРЫТ
Проверены все **13 файлов**. Зафиксировано **GAB-CONF-001–086**.

### Database — ЗАКРЫТ
Проверены все **19 файлов**: 6 верхнего уровня + 13 схем. Зафиксировано **GAB-DB-001–096**.

### Internals — 🔵 В ПРОЦЕССЕ
Проверены core-направления `Boot`, `Client`, `Constants`, `Errors`, event framework, `Extendables`, `Extensions`, `IPC`, `Logger`, `ShardUtil`, `Sharder`, `Worker`, README и доступные Extension API-компоненты.

Зафиксировано **GAB-INT-001–123** в `ideasALL/ideas/GAWESOME_INTERNALS.md`.

Обработаны staged boot lifecycle, Safe Mode, runtime timers, hot reload, entity resolvers, violation pipeline, coded errors, event requirements/prerequisites, event registry, extendables, shard-aware IPC, shard respawn, structured logging/Sentry, plugin sandbox/scopes/storage, validated Embed builder, worker isolation, entity cleanup и audit/status pipelines.

### Точная точка продолжения

**Продолжить полный обход оставшихся фактических файлов `Internals/Events/` и остальных элементов `Internals/`, затем только после проверки всех файлов поставить `Internals` в ЗАВЕРШЁН.**

После полного `Internals/` → `Modules/` → `Temp/` → `Web/`.

Другие репозитории не трогать до полного завершения GAwesomeBot.

`bot/main.py` и другая реализация InsaneBot не изменяются.
