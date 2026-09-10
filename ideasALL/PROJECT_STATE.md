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
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6969/Multipurpose-discord-bot — ОЖИДАЕТ.

## GAwesomeBot — COMPLETE

Ветка: `indev-4.0.2`. Recursive tree проверен через Git Tree API.

### Commands — ЗАКРЫТ
- PM: **GAB-PM-001–125**
- Private: **GAB-PR-001–049**
- Public: **GAB-PUB-001–672**
- Shared: **GAB-SH-001–094**

### Configurations — ЗАКРЫТ
Проверены все **13 файлов**. **GAB-CONF-001–086**.

### Database — ЗАКРЫТ
Проверены все **19 файлов**: 6 верхнего уровня + 13 схем. **GAB-DB-001–096**.

### Internals — ЗАКРЫТ
Полный каталог закрыт. **GAB-INT-001–123**.

### Modules — ЗАКРЫТ
Проверены все фактические файлы `Modules/` и вложенных `Emoji/`, `MessageUtils/ReactionMenus/`, `Timeouts/`, `Utils/`. **GAB-MOD-001–080**.

### Temp — ЗАКРЫТ
`Temp/` — служебный каталог без дополнительных рабочих механик, требующих отдельного idea-каталога.

### Web — ЗАКРЫТ
Проверены web server, controllers, dashboard controllers, routes, middleware, helpers/parsers и связанные web-поверхности.

Зафиксировано **GAB-WEB-001–060** в `ideasALL/ideas/GAWESOME_WEB.md`.

Ключевые направления: web DTO/parsers; публичные user/server profiles; mutual servers; extension gallery/versioning/scopes; Discord authentication; membership/permission gates; dashboard control plane; per-channel command configuration; API/route separation; XSS-safe Markdown; blog/wiki/activity/donation surfaces; maintainer/debug panels; operational statistics; graceful missing entities; web lifecycle isolation.

## Точная точка продолжения

**GAwesomeBot полностью завершён. Следующий источник: `CorwinDev/Discord-Bot`.**

`bot/main.py` и другая реализация InsaneBot не изменяются.
