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

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — АКТИВНО ИССЛЕДУЕТСЯ.**
4. codebymitch/TitanBot — ОЖИДАЕТ.
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `ItzSudhan/Discord-MusicBot` — АКТИВЕН

Ветка: `v5`.

Закрыты:
- root README/tree/config/index/package;
- все `commands/slash/`;
- `commands/context/play.js`;
- все 6 файлов `events/`;
- `lib/DiscordMusicBot.js`, `lib/SlashCommand.js`, `lib/EpicPlayer.js`;
- `util/Controller.js`, `util/db.js`, `util/getChannel.js`, `util/getConfig.js`, `util/getLavalink.js`, `util/guildDb.js`, `util/loadCommands.js`.

Созданы/пополнены пакеты идей:
- `ideas/MUSIC.md` — MUSIC-001–042;
- `ideas/MUSIC_COMMANDS.md` — MUSIC-C001–055;
- `ideas/MUSIC_CONTEXT.md` — MUSIC-X001–007;
- `ideas/MUSIC_EVENTS.md` — MUSIC-E001–025;
- `ideas/MUSIC_STORAGE.md` — MUSIC-S001–018;
- `ideas/MUSIC_CORE.md` — MUSIC-K001–018.

Из последних находок особенно зафиксированы: context-menu play по target message, выбор результата поиска через Select Menu с TTL, lyrics candidate/source/tips UX, Stage Channel recovery, составной seek, DM save, короткая/длинная queue с циклической pagination, TTL+idle collectors, dual latency ping, hot reload require cache, voice-state automation с различением JOIN/LEAVE/MOVE, server mute pause/resume, delayed auto-leave с повторной проверкой, lazy per-guild JSON DB, queued persistence, DB registry и player/controller factories.

Журнал: `research/discord-music-bot.md`.

## Следующая точка

Продолжить строго по recursive tree `v5` с `util/` после уже просмотренных файлов. Затем закрыть `api/`, `dashboard/`, `deploy/`, `docker/`, `.github/` и остальные root-файлы.

**Другие источники до полного завершения MusicBot не трогать.**
