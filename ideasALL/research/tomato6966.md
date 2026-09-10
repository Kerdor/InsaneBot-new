# Research Journal — Tomato6966/Multipurpose-discord-bot

Источник: `Tomato6966/Multipurpose-discord-bot`
Ветка: `new_2025`

## Batch 1
### `commands/⌨️ Programming`
- Просмотрены `coliru.js`, `compile.js`, `github.js`, `httpstatus.js`, `npm.js`, `npmpkgsize.js`.
- `compile.js` и `coliru.js` — одна и та же механика, объединены.
- Зафиксированы `TOM-001–005` в `ideas/TOMATO_BATCH1.md`.

## Batch 2
### `commands/⚙️ Settings`
- Просмотрены все 20 файлов области Settings.
- Зафиксированы `TOM-006–011` в `ideas/TOMATO_BATCH2.md`.
- `prefix.js` сверён с `CORE-012`; money/AFK/music settings сверены с существующим банком.
- Закомментированные `toggledjonly.js` / `togglerequestonly.js` не учитывались.

## Batch 3
### `commands/⚜️ Custom Queue(s)`
- Обработан единственный `savedqueue.js` целиком.
- Зафиксированы `TOM-012–020` в `ideas/TOMATO_BATCH3.md`.

## Batch 4
### `commands/🎤 Voice`
- Обработан единственный `voice.js` целиком по всем веткам.
- Зафиксированы `TOM-021–033` в `ideas/TOMATO_BATCH3.md`.
- Найдены lock/unlock, stage/unstage, kick, invite, ban/unban, trust/untrust, user limit, bitrate и ownership transfer для временных Join-to-Create voice-каналов.

## Batch 5
### `commands/🎮 MiniGames`
- Проверена вся директория MiniGames.
- Зафиксированы `TOM-034–058` в `ideas/TOMATO_BATCH4.md`.
- Отключённые `.js.disabled` файлы не учитывались.
- `uno.js` и `poker-night.js` не учитывались как рабочие игровые механики.

## Batch 6 — текущий крупный проход
### `commands/🎶 Music`
- Проверена структура всей области и выполнен подробный проход по ключевым music-командам и их фактическому поведению.
- Зафиксированы `TOM-059–071` в `ideas/TOMATO_BATCH5.md`.
- Новые механики: добавление previous/similar треков, DM-grab текущего трека, playtop, перемещение пользователя к voice-каналу бота, большой каталог radio, поиск radio через RadioBrowser, reconnect сохранённого radio stream, восстановление очереди после shuffle, удаление дублей из очереди, единый queue status, преднастроенные Music Mix и Song of the Day.
- Проверены базовые play/search/playlist/skip/pause/resume/restart/seek/forward/rewind/volume/clearqueue/removetrack/stop и loop-варианты; отдельные дубли не создавались.
- `voteskip.js` и `removevoteskip.js` содержат полностью закомментированный код.
- `lyrics.js` и `searchplaylist.js` в текущей ветке намеренно не выполняют заявленную механику.
- В `move.js` обнаружен дефект: заявленные `from/to` фактически игнорируются, а последний трек переносится в начало; это отмечено в batch-файле как дефект, а не как полноценная позиционная механика.

## Точка продолжения
`commands/🎶 Music` **ЕЩЁ НЕ ЗАКРЫТА**. Нужно продолжить проверку оставшихся файлов этой области и только после полного прохода закрыть Music.

## Статус
Tomato6966/Multipurpose-discord-bot — **В РАБОТЕ**.
