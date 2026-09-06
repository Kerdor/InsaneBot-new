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
- весь `util/`;
- весь исходный `api/`;
- исходный `dashboard/` — pages, components, utils;
- `.github/` recursive tree;
- root `Dockerfile`, `Procfile`, `app.json`, `.replit`.

Созданы/пополнены пакеты идей:
- `ideas/MUSIC.md` — MUSIC-001–042;
- `ideas/MUSIC_COMMANDS.md` — MUSIC-C001–055;
- `ideas/MUSIC_CONTEXT.md` — MUSIC-X001–007;
- `ideas/MUSIC_EVENTS.md` — MUSIC-E001–025;
- `ideas/MUSIC_STORAGE.md` — MUSIC-S001–018;
- `ideas/MUSIC_CORE.md` — MUSIC-K001–018;
- `ideas/MUSIC_WEB.md` — MUSIC-W001–031;
- `ideas/MUSIC_DEPLOY.md` — MUSIC-D001–009.

Из последнего батча особенно зафиксированы: Passport Discord OAuth и session auth, public/protected API split, динамическая загрузка route-файлов, dashboard runtime metrics, typed frontend API helpers, server selector/avatar UI, общий navbar/layout, login/logout redirects, server state model с queue/loop/playing, Docker/Alpine runtime, worker Procfile, Heroku deployment manifest и Replit runtime configuration.

Журнал: `research/discord-music-bot.md`.

## Следующая точка

Провести финальную сверку recursive tree `v5` с журналом: убедиться, что все оставшиеся root-файлы и каталоги действительно закрыты и не содержат новых исходных механик. Скомпилированный `dashboard/out/_next` не дублировать после анализа исходников; считать его build artifact.

Только после финальной сверки поставить `ItzSudhan/Discord-MusicBot` в статус **ЗАВЕРШЁН** и перейти к `codebymitch/TitanBot`.

**Другие источники до полного завершения MusicBot не трогать.**
