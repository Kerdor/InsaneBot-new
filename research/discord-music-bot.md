# Research Journal — ItzSudhan/Discord-MusicBot

Источник: `ItzSudhan/Discord-MusicBot`
Ветка: `v5`
Статус: 🔵 АКТИВЕН

## Правило обхода

Идём от корня по recursive tree, затем закрываем каталоги и файлы по порядку. Ничего из следующих источников не исследуется до полного завершения этого репозитория.

## Просмотрено в текущем батче

- `README.md` — ✅
- recursive tree v5 — ✅
- `config.js` — ✅
- `index.js` — ✅
- `package.json` — ✅
- `lib/DiscordMusicBot.js` — ✅ (основной lifecycle/Manager/event pipeline; файл ещё требует дочитывания)
- `lib/SlashCommand.js` — ✅
- `lib/EpicPlayer.js` — ✅
- `util/loadCommands.js` — ✅
- `util/Controller.js` — ✅
- `events/interactionCreate.js` — ✅
- `commands/slash/autoleave.js` — ✅
- `commands/slash/autopause.js` — ✅
- `commands/slash/autoqueue.js` — ✅
- `commands/slash/clean.js` — ✅
- `commands/slash/clear.js` — ✅
- `commands/slash/filters.js` — ✅
- `commands/slash/guildleave.js` — ✅
- `commands/slash/help.js` — ✅
- `commands/slash/loop.js` — ✅
- `commands/slash/loopq.js` — ✅
- `commands/slash/queue.js` — ✅

## Найдено и сверено

Добавлен первый пакет `ideas/MUSIC.md`: `MUSIC-001`–`MUSIC-042`.

Ключевые группы находок:
- per-player audio settings;
- auto pause / auto leave / 24/7 / auto queue;
- reconnect/disconnect lifecycle и retry policy;
- track error/stuck recovery UX;
- now-playing controller;
- защита от повторного удаления старых control messages;
- voice-channel authorization для кнопок;
- replay/next/loop state machine;
- динамический loader slash/context commands;
- paginated help + build hash;
- multi-provider autocomplete;
- selective bot-message cleanup;
- centralized audio configuration;
- debug/Replit recovery;
- runtime counters.

## Точная точка продолжения

Следующий батч продолжает `commands/slash/` с первой ещё не просмотренной команды после уже закрытых:
`247.js`, `invite.js`, `lyrics.js`, `move.js`, `nowplaying.js`, `pause.js`, `ping.js`, `play.js`, `previous.js`, `reload.js`, `remove.js`, `replay.js`, `resume.js`, `save.js`, `search.js`, `seek.js`, `shuffle.js`, `skip.js`, `skipto.js`, `stats.js`, `stop.js`, `summon.js`, `volume.js`.

После полного закрытия `commands/slash/` перейти к `commands/context/`, затем `events/`, `util/`, `api/`, `dashboard/`, `deploy/`, `docker/`, `.github/` и остальным root-файлам recursive tree.

**Репозиторий НЕ завершён.**
