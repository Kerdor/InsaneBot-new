# Research Journal — Tomato6966/Multipurpose-discord-bot

Источник: `Tomato6966/Multipurpose-discord-bot`
Ветка: `new_2025`

## Batch 1–9
- `commands/⌨️ Programming`: `TOM-001–005`.
- `commands/⚙️ Settings`: `TOM-006–011`.
- `commands/⚜️ Custom Queue(s)`: `TOM-012–020`.
- `commands/🎤 Voice`: `TOM-021–033`.
- `commands/🎮 MiniGames`: `TOM-034–058`.
- `commands/🎶 Music`: `TOM-059–072`.
- `commands/🏫 School Commands`: `TOM-073–077`.
- `commands/👀 Filter`: `TOM-078–092`.
- `commands/👑 Owner`: `TOM-093–106`.

## Batch 10 — Setup
- `TOM-107–116`: category toggles, Number Counter, daily facts, Anti-New-Account, Anti-Spam, Anti-Link, boost DM/log, Ghost Ping Detector, Epic Games Verification.
- `TOM-117–145`: AI-Chat, anti-* protections, backups, Auto-Delete/Embed/Meme/NSFW, Anti-Warn toggle, Anti-Nuke, Application, Auto-Support, Custom Commands, Embed customization.
- `TOM-146–171`: language, admin command log, Member Counter, Menu Apply/Ticket, music request panel, Valid-Code, Joinlist, JTC, mute settings, level-up reply, Roster, Report Log, Ticket, Suggestions, TikTok/Twitter/Twitch.
- `TOM-172–184`: Welcome/Leave and Warn systems.
- Recursive Setup закрыт; дубли/redirect не размножены.

## Batch 11 — `commands/💸 Economy`
### Batch 1: `TOM-185–196`
- Recursive Economy tree проверен; все 27 command files просмотрены.
- `TOM-185–187`: общий Black Market multiplier, покупаемый boost 2–5x на 5 дней и отдельные cooldown tiers.
- `TOM-188–191`: bulk buy/sell, 10% sell fee, valuation inventory и leaderboard по `balance + bank + inventory value` с pagination/личным rank.
- `TOM-192–194`: Coinflip 1.5x, Dice 4x и Slots 9x/2x payout variants.
- `TOM-195–196`: Crime с повышенной наградой + Black Market и Rob с минимальным balance цели 500.
- Проверены все 27 Economy-файлов; дубли не размножены.
- `ecohelp.js` зафиксирован как `TOM-197`.

### Состояние
`commands/💸 Economy` **ЗАВЕРШЁН**.

## Batch 12 — `databases/` + database loader
- Дерево `databases/` проверено; содержащиеся там артефакты — Enmap/SQLite runtime-хранилища и placeholder-файлы, а не самостоятельные команды.
- `handlers/loaddb.js` просмотрен полностью.
- `TOM-198`: разделение Enmap-баз по доменам и отдельным каталогам.
- `TOM-199`: архитектурный паттерн numbered slots для до 100 независимых конфигураций одного типа.
- `TOM-200`: инициализация обязательной структуры данных через `ensure`/default records.
- SQLite/WAL-файлы не добавлены как отдельные идеи: это бинарные данные состояния, а не механики.

### Состояние
`databases/` **ЗАВЕРШЁН**.

## Batch 13 — `events/`
- Проверены обе функциональные ветки: `events/client` и `events/guild`.
- `events/client`: `debug`, `disconnect`, `error`, `rateLimit`, `ready`, `reconnecting`, `shardDisconnect`, `shardError`, `shardReady`, `shardReconnecting`, `shardResume`, `warn`.
- `events/guild`: `interactionCreate`, `message`, `messageCreate`, `threadCreate`.
- `TOM-201–216` → `ideasALL/ideas/TOMATO_BATCH13.md`.
- Новые варианты: автоочистка невалидных bot-channel IDs, запрет обычных команд в music-request channel, preflight Bot Permissions, auto-join threads, единый command gateway, synthetic Message adapter для slash, music self-healing/preconditions, dynamic status placeholders/rotation, startup diagnostics, lazy databasing, partial object fetch, временные error replies и отдельный shard lifecycle logging.
- Базовые lifecycle events, пустые handlers и уже существующие cooldown/permission механики отдельно не размножены.

### Состояние
`events/` **ЗАВЕРШЁН**.

## Batch 14 — `handlers/` — первая крупная часть
- После `events/` начат последовательный проход `handlers/`.
- Проверены функциональные handlers, включая `aichat.js`, `anti_nuke.js`, `antiselfbot.js`, `apply.js`, `blacklist.js`, `epicgamesverification.js`, `extraevents.js`, `functions.js`, `joinvc.js`, `keyword.js`, `logger.js`, `validcode.js` и связанные runtime handlers.
- `TOM-217–227` → `ideasALL/ideas/TOMATO_BATCH14.md`.
- Новые/дополнительные механики: role while in voice, обновляемые VC join/leave messages, Anti-Self-Bot detection/action thresholds, DM-based application questionnaire safeguards, Epic Games verification flow details, keyword/custom-command trigger debounce, snipe cache, auto-crosspost, persistent bot server-deaf, owner operational guild join/leave DM и guild chunk/raid diagnostics.
- `anti_nuke`, blacklist, anti-link/caps/mention, backup, auto-* и другие handlers сверены с уже собранными Setup-системами и не размножены.
- `functions.js` признан преимущественно helper-библиотекой; отдельные уже существующие механики не добавлялись повторно.

## Batch 15 — `handlers/playermanagers/` + `handlers/erela_events/`
- `playermanagers/` проверен: `playlist.js`, `playtop.js`, `request.js`, `search.js`, `similar.js`, `skiptrack.js`, `song.js`.
- `erela_events/` проверен по дереву: `client_events.js`, `creation.js`, `events.js`, `musicsystem.js`, `node_events.js`; крупные playback lifecycle и music panel участки просмотрены.
- `TOM-228–230` → `ideasALL/ideas/TOMATO_BATCH15.md`.
- `TOM-228`: timed messages по дням/часам/минутам через cron.
- `TOM-229`: единая интерактивная Music Control Panel с кнопками playback/seek/loop/autoplay/shuffle и динамическим состоянием.
- `TOM-230`: единый music voice preflight с проверками CONNECT, SPEAK и переполнения voice channel до маршрутизации конкретного player manager.
- Уже собранные playlist/search/similar/skiptrack/playtop и отдельные music controls не размножены; сохранены только новые UX/архитектурные варианты.

### Состояние
`handlers/` **НЕ ЗАКРЫТ**.

### Точка продолжения
Продолжить с оставшимися root-level functional handlers из `handlers/`, которые ещё не были полностью закрыты, и отдельно сверить ticket/welcome/leave/ranking/reactionrole/roster/suggest и прочие оставшиеся крупные handlers. После полного recursive прохода закрыть `handlers/`.

## Статус
Tomato6966/Multipurpose-discord-bot — **В РАБОТЕ**.
