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

Recursive Git Tree проверен. Основные области: `src/commands`, `src/config`, `src/database`, `src/events`, `src/handlers`, `src/interactions`, `src/music`, `src/packages`.

### Первый батч

Закрыты для текущего батча:
- `commands/automod`
- `commands/autosetup`
- `commands/casino`
- `commands/custom-commands`
- `commands/economy`
- `commands/family`
- `commands/games`
- `handlers/security/antiad.js`
- `handlers/security/antispam.js`
- `handlers/security/blacklist.js`
- ключевая transcript/ticket-инфраструктура `handlers/functions/ticket.js`

Каталог: `ideasALL/ideas/CORWIN_BATCH1.md` — **COR-001–080**.
Журнал: `ideasALL/research/corwindev.md`.

### Важные находки первого батча
- autosetup создаёт инфраструктуру нескольких систем и сохраняет созданные сущности;
- automod поддерживает channel whitelist и bypass для модераторов;
- security проверяет edited messages;
- antispam использует локальное временное состояние с отдельными окнами;
- economy содержит предметы с состоянием/прочностью и role shop;
- casino использует живое редактирование одного сообщения;
- family хранит relationship graph и запрещает брак с родственниками;
- custom commands регистрируются как реальные guild slash commands и имеют Normal/Embed/DM response modes;
- ticket transcript строится как HTML с sanitization, reply references и мультимедиа.

### Точная точка продолжения
**Продолжить CorwinDev/Discord-Bot с оставшихся `src/commands`, затем `src/events`, `src/handlers`, `src/interactions`, `src/config`, `src/database`, `src/music`, `src/packages` и прочих файлов.**

Только после полного закрытия CorwinDev перейти к Tomato6969.

`bot/main.py` и другая реализация InsaneBot не изменяются.
