# Research Journal — ItzSudhan/Discord-MusicBot

Источник: `ItzSudhan/Discord-MusicBot`
Ветка: `v5`
Статус: 🔵 АКТИВЕН

## Правило обхода

Идём от корня по recursive tree, затем закрываем каталоги и файлы по порядку. Ничего из следующих источников не исследуется до полного завершения этого репозитория.

## Закрыто

- `commands/slash/` — все команды из recursive tree;
- `commands/context/play.js`;
- все 6 файлов `events/`;
- `lib/DiscordMusicBot.js`;
- `lib/SlashCommand.js`, `lib/EpicPlayer.js`;
- весь `util/`;
- весь исходный `api/`;
- исходный `dashboard/` — pages, components, utils;
- `.github/` — recursive tree и issue/support automation files;
- root `Dockerfile`, `Procfile`, `app.json`, `.replit`.

## Найдено и сверено

Созданы/пополнены пакеты:
- `ideas/MUSIC_COMMANDS.md` — `MUSIC-C001`–`MUSIC-C055`;
- `ideas/MUSIC_CONTEXT.md` — `MUSIC-X001`–`MUSIC-X007`;
- `ideas/MUSIC_EVENTS.md` — `MUSIC-E001`–`MUSIC-E025`;
- `ideas/MUSIC_STORAGE.md` — `MUSIC-S001`–`MUSIC-S018`;
- `ideas/MUSIC_CORE.md` — `MUSIC-K001`–`MUSIC-K018`;
- `ideas/MUSIC_WEB.md` — `MUSIC-W001`–`MUSIC-W031`;
- `ideas/MUSIC_DEPLOY.md` — `MUSIC-D001`–`MUSIC-D009`.

В web-батче зафиксированы Discord OAuth через Passport, session-based auth middleware, автоматическая регистрация API route-файлов, разделение public/protected API, динамический invite URL, dashboard runtime metrics, typed frontend API helpers, stat cards, server selector/avatar UI, общий navbar/layout, login/logout redirects и заготовленная server state model с queue/loop/playing.

В deployment-батче зафиксированы Docker/Alpine runtime, подготовка через package scripts, worker Procfile, Heroku one-click manifest с environment metadata, Replit run configuration и переиспользование единого entrypoint.

## Следующая точка

`util/`, `api/`, исходный `dashboard/`, `.github/` и deployment-файлы закрыты. Перед завершением репозитория проверить оставшиеся root-файлы/каталоги по recursive tree, особенно файлы, которые ещё не были отдельно просмотрены; затем сверить весь source tree с журналом и только после этого поставить `ЗАВЕРШЁН`.

Скомпилированный `dashboard/out/_next` не считать отдельным источником механик после анализа исходного TypeScript; при финальной сверке учитывать его как build artifact.

**Репозиторий НЕ завершён. Следующие источники не трогать.**
