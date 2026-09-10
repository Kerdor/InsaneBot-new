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
- `prefix.js` сверён с `CORE-012` и не дублирован.
- `addmoney.js` / `removemoney.js` сверены с `ECON-014–016` и не дублированы.
- `afk.js` сверён с `SOCIAL-004–007` и не дублирован.
- Музыкальные default/play-message настройки сверены с существующим `MUSIC` и не дублированы.
- `toggledjonly.js` и `togglerequestonly.js` содержат полностью закомментированный код и как рабочие механики не учитывались.

## Batch 3

### `commands/⚜️ Custom Queue(s)`
- Обработан единственный файл `savedqueue.js`.
- Просмотрен полный файл, включая все операции `create`, `addcurrenttrack`, `addcurrentqueue`, `removetrack`, `shuffle`, `removedupes`, `showall`, `createsave`, `delete`, `play`, `showdetails`.
- Зафиксированы `TOM-012–020` в `ideas/TOMATO_BATCH3.md`.
- Основная новая система — персональные именованные сохранённые музыкальные очереди с редактированием, просмотром и воспроизведением.

## Batch 4

### `commands/🎤 Voice`
- Обработан единственный файл `voice.js` целиком по всем веткам команд.
- Зафиксированы `TOM-021–033` в `ideas/TOMATO_BATCH3.md`.
- Найдены операции управления собственными временными Join-to-Create voice-каналами: lock/unlock, stage/unstage, kick, invite, ban/unban, trust/untrust, изменение user limit и bitrate, передача ownership.
- Для owner-check используется как сохранённый `owner_<guild>_<channel>`, так и наличие `MANAGE_CHANNELS` в overwrite пользователя.
- Перед изменением канала проверяются необходимые права бота; invite дополнительно требует `CREATE_INSTANT_INVITE`.

### Точка продолжения
Следующая область внутри `commands` — `🎮 MiniGames`.

## Статус
Tomato6966/Multipurpose-discord-bot — **В РАБОТЕ**.
