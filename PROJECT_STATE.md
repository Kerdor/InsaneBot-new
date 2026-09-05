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

## Восстановление после смены чата

- `RESEARCH_PROGRESS.md` — глобальная контрольная точка.
- `research/<source>.md` — последовательный журнал источника.
- `✅` означает реальный просмотр и сверку.
- После каждого существенного батча обновляются журнал и `PROJECT_STATE.md`.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — АКТИВНО ИССЛЕДУЕТСЯ.**
4. codebymitch/TitanBot — ОЖИДАЕТ.
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `python-discord/bot` — ЗАВЕРШЁН

Полностью закрыт recursive tree.

## `ItzSudhan/Discord-MusicBot` — АКТИВЕН

Ветка: `v5`.

Первый глубокий батч закрыт по корню/ядру и части `commands/slash/`.

Проверены:
- `README.md` и recursive tree;
- `config.js`, `index.js`, `package.json`;
- `lib/DiscordMusicBot.js` — основной lifecycle/event pipeline, файл ещё требует дочитывания;
- `lib/SlashCommand.js`;
- `lib/EpicPlayer.js`;
- `util/loadCommands.js`;
- `util/Controller.js`;
- `events/interactionCreate.js`;
- `commands/slash/autoleave.js`;
- `commands/slash/autopause.js`;
- `commands/slash/autoqueue.js`;
- `commands/slash/clean.js`;
- `commands/slash/clear.js`;
- `commands/slash/filters.js`;
- `commands/slash/guildleave.js`;
- `commands/slash/help.js`;
- `commands/slash/loop.js`;
- `commands/slash/loopq.js`;
- `commands/slash/queue.js`.

Добавлен `ideas/MUSIC.md` с `MUSIC-001`–`MUSIC-042`.

Журнал: `research/discord-music-bot.md`.

## Следующая точка

Продолжить **`commands/slash/`** с первой необработанной команды:
`247.js`, затем `invite.js`, `lyrics.js`, `move.js`, `nowplaying.js`, `pause.js`, `ping.js`, `play.js`, `previous.js`, `reload.js`, `remove.js`, `replay.js`, `resume.js`, `save.js`, `search.js`, `seek.js`, `shuffle.js`, `skip.js`, `skipto.js`, `stats.js`, `stop.js`, `summon.js`, `volume.js`.

После полного закрытия slash-команд перейти к `commands/context/`, затем `events/`, `util/`, `api/`, `dashboard/`, `deploy/`, `docker/`, `.github/` и root-файлам.

**Другие источники до полного завершения MusicBot не трогать.**
