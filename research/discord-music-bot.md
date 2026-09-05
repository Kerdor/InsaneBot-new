# Research Journal — ItzSudhan/Discord-MusicBot

Источник: `ItzSudhan/Discord-MusicBot`
Ветка: `v5`
Статус: 🔵 АКТИВЕН

## Правило обхода

Идём от корня по recursive tree, затем закрываем каталоги и файлы по порядку. Ничего из следующих источников не исследуется до полного завершения этого репозитория.

## Закрыто в текущем батче

- `commands/slash/247.js` — ✅
- `commands/slash/invite.js` — ✅
- `commands/slash/lyrics.js` — ✅
- `commands/slash/move.js` — ✅
- `commands/slash/nowplaying.js` — ✅
- `commands/slash/pause.js` — ✅
- `commands/slash/ping.js` — ✅
- `commands/slash/play.js` — ✅
- `commands/slash/previous.js` — ✅
- `commands/slash/reload.js` — ✅
- `commands/slash/remove.js` — ✅
- `commands/slash/replay.js` — ✅
- `commands/slash/resume.js` — ✅
- `commands/slash/save.js` — ✅
- `commands/slash/search.js` — ✅
- `commands/slash/seek.js` — ✅
- `commands/slash/shuffle.js` — ✅
- `commands/slash/skip.js` — ✅
- `commands/slash/skipto.js` — ✅
- `commands/slash/stats.js` — ✅
- `commands/slash/stop.js` — ✅
- `commands/slash/summon.js` — ✅
- `commands/slash/volume.js` — ✅

## Найдено и сверено

Создан дополнительный пакет `ideas/MUSIC_COMMANDS.md`: `MUSIC-C001`–`MUSIC-C055`.

Ключевые новые группы:
- интерактивный search Select Menu с выбором конкретного результата и timeout;
- раздельный UX для track/search result/playlist;
- playlist statistics;
- Stage Channel suppression/request-to-speak recovery;
- составной человекочитаемый seek;
- volume read-only режим;
- сохранение трека в DM;
- компактный и расширенный режимы queue;
- циклическая pagination;
- TTL + idle timeout для collectors;
- user-bound interaction buttons;
- remove/move/skipto queue operations;
- фильтры через единый preset enum и Reset;
- dual latency ping;
- объединённые Lavalink/system stats;
- hot reload command cache;
- lyrics search по текущему треку с очисткой шумовых суффиксов;
- lyrics candidate selection, source/tips UI, restricted-content UX и truncation;
- replay через seek(0);
- persistent voice semantics stop/247;
- summon с переносом существующего player;
- точечные ошибки для отсутствующего player.

## Предыдущие результаты

Первый пакет `ideas/MUSIC.md`: `MUSIC-001`–`MUSIC-042`.

## Точная точка продолжения

Каталог `commands/slash/` закрыт по всем командам из recursive tree. Следующая точка — `commands/context/play.js`.

После `commands/context/` продолжить строго по recursive tree: `events/`, `util/`, `api/`, `dashboard/`, `deploy/`, `docker/`, `.github/` и остальные root-файлы.

**Репозиторий НЕ завершён.**
