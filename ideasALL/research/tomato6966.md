# Research Journal — Tomato6966/Multipurpose-discord-bot

Источник: `Tomato6966/Multipurpose-discord-bot`
Ветка: `new_2025`

## Batch 1
### `commands/⌨️ Programming`
- Просмотрены `coliru.js`, `compile.js`, `github.js`, `httpstatus.js`, `npm.js`, `npmpkgsize.js`.
- `compile.js` и `coliru.js` — одна и та же механика, объединены.
- Зафиксированы `TOM-001–005`.

## Batch 2
### `commands/⚙️ Settings`
- Просмотрены все 20 файлов.
- Зафиксированы `TOM-006–011`.
- `prefix.js` сверён с `CORE-012`; money/AFK/music settings сверены с существующим банком.

## Batch 3
### `commands/⚜️ Custom Queue(s)` + `commands/🎤 Voice`
- `savedqueue.js` обработан целиком: `TOM-012–020`.
- `voice.js` обработан целиком: `TOM-021–033`.

## Batch 5
### `commands/🎮 MiniGames`
- Вся директория проверена: `TOM-034–058`.
- `.js.disabled`, `uno.js` и unsupported `poker-night.js` не учитывались как рабочие механики.

## Batch 6
### `commands/🎶 Music`
- Вся директория проверена: `TOM-059–072`.
- Проверены remaining/base controls, нерабочие и закомментированные варианты; `move.js` содержит дефект и не считается полноценной positional move механикой.

## Batch 7
### `commands/🏫 School Commands`
- Все 5 файлов проверены: `TOM-073–077`.

## Batch 8
### `commands/👀 Filter`
- Вся область проверена: `TOM-078–092`.
- EQ reset duplicate не размножен; speed/rate оставлены отдельно от pitch.

## Batch 9
### `commands/👑 Owner`
- Все 19 файлов проверены: `TOM-093–106`.
- Отключённые/нерабочие stop/reload варианты не считались рабочими командами; PM2 restart отмечен как небезопасный без owner-check.

## Batch 10 — `commands/💪 Setup`
### Часть 1: `TOM-107–116`
- Проверена первая часть Setup: category toggles, Number Counter, daily facts, Anti-New-Account, Anti-Spam, Anti-Link, boost DM/log, Ghost Ping Detector и Epic Games Verification.

### Часть 2: `TOM-117–145`
- Проверены AI-Chat, Anti-Caps, Anti-Discord Links, Anti-Mention, backups, Auto-Delete, Auto-Embed, Auto-Meme, Auto-NSFW, Auto-Warn batch toggle, Anti-Nuke.
- Затем Application, Auto-Support, Custom Commands и Embed settings.
- Зафиксированы `TOM-117–145`.
- Redirect и повторные blacklist/anti-* setup-файлы отдельно не размножались.

### Часть 3: `TOM-146–171`
- Продолжен последовательный просмотр Setup крупными блоками.
- `TOM-146`: интерактивная смена языка с reset/status.
- `TOM-147`: отдельный Admin Command Log.
- `TOM-148–149`: до 25 Member Counter систем и большой набор placeholders для серверной статистики.
- `TOM-150`: Menu Apply до 100 конфигураций и до 25 options.
- `TOM-151–152`: Menu Ticket до 100 конфигураций, до 25 options, access/closed category и per-system Claim messages.
- `TOM-153`: постоянная Music Request панель.
- `TOM-154`: Valid-Code toggle.
- `TOM-155`: Joinlist с шестью условиями и четырьмя действиями.
- `TOM-156`: до 100 JTC конфигураций с отдельными trigger VC и шаблонами имени.
- `TOM-157–158`: mute style timeout/role, отдельная mute-role и составное default mute time с максимумом 1 Week.
- `TOM-159`: level-up reply/channel вариант.
- `TOM-160–161`: до 100 Server Roster систем и настройка style/inline/show-all-roles.
- `TOM-162`: Report Log channel.
- `TOM-163–164`: основной Ticket Setup до 100 systems и отдельная closed-ticket category.
- `TOM-165–166`: Suggestion System с кастомными status texts и upvote/downvote emoji.
- `TOM-167–168`: TikTok logger до 3 sources и кастомные notification templates с placeholders.
- `TOM-169–170`: Twitter logger, retweet toggle и Manual Setup fallback для username/ID.
- `TOM-171`: Twitch logger до 10 sources, связка с Discord user, custom message, publication channel, live role, ghost-ping role и multi-remove.
- `setup-boost.js`, `setup-logger.js`, `setup-radio.js`, `setup-admin.js` проверены как дубли/варианты уже собранных систем.
- `setup-serverstats.js` — redirect на `setup-membercount`.
- `setup-reactionrole.js` сверён с существующей Reaction Roles системой и новых самостоятельных требований не добавил.
- `setup-rank.js` сверён с `TITAN_LEVELING`; сохранён только reply-vs-channel вариант.

### Состояние
`commands/💪 Setup` **НЕ ЗАВЕРШЁН**.

## Точка продолжения
Продолжать Setup после social block: сначала определить и обработать оставшиеся файлы `setup-*` по recursive tree, затем закрыть Setup полностью. Economy не начинать до этого.

## Статус
Tomato6966/Multipurpose-discord-bot — **В РАБОТЕ**.
