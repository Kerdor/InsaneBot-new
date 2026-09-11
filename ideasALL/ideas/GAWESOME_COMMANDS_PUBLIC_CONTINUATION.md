# GAwesomeBot — Commands/Public — continuation

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Этот файл продолжает source-specific проход по `Commands/Public/`. Проверенные здесь команды сверены с уже собранным global bank; новые глобальные механики здесь не создаются, если они уже канонизированы.

## Проверенные файлы — финальный проход

- `info.js` — server information card; уже **GD-258**.
- `invite.js` — выдача bot invite URL; самостоятельной новой механики нет.
- `joke.js` — внешний joke provider, progress message, length limit и error fallback; отдельной новой механики нет.
- `list.js` — server to-do list; уже **GD-248**.
- `lottery.js` — scaled points lottery; уже **GD-249**, включая multiplier, динамическую цену билета, лимит билетов и creator/admin/maintainer end control.
- `messages.js` — weekly message leaderboard, `me`, lookup участника, bot exclusion, top-8 и total count; stats/leaderboard канон.
- `translate.js` — source/target и автоопределение через `?`; translation integration.
- `twitter.js` — RSS-backed Twitter results, result count, progress и pagination; stream/integration канон.
- `wiki.js` — Wikipedia random/search, summary/full-content fallback, length protection и image fallback; отдельной системы нет.
- `wolfram.js` — progress reuse, pod aggregation, image fallback и no-result/error branches; **GAB-PUB-025–028**.
- `xkcd.js` — latest/by-number comic, timestamp и error fallback; отдельной новой системы нет.
- `unban.js` — ban lookup, confirmation, unban и ModLog; moderation workflow.
- `unmute.js` — permission/hierarchy checks, mute-state check, unmute и ModLog; moderation workflow.
- `year.js` — exact + humanized year countdown; **GAB-PUB-109**.
- `youtube.js` — video/playlist/channel search, result limit и pagination; provider-specific integration.
- `convert.js` — syntax normalization и typed backend errors; **GAB-PUB-098–099**.
- `time.js` — IANA timezone validation и self-service fallback; **GAB-PUB-104–105**.
- `weather.js` — API capability gate, sparse fields и provider icon; **GAB-PUB-106–108**.
- `cool.js` — channel command cooldown; **GAB-PUB-032–036 / GD-238**.
- `count.js` — persistent interactive counters; **GAB-PUB-041–047 / GD-240**.
- `countdown.js` — именованные server-local countdowns с human-duration parser, expiry timestamp, channel association, duplicate protection и paginated listing. Отдельная механика; требует global dedup.
- `disable.js` / `enable.js` — управление disabled/enabled commands через `ManageCommands`; underlying command availability/configuration уже покрывается существующим configuration/help каноном.
- `dog.js` / `dogfact.js` — random animal/fact pipeline; **GAB-PUB-089–093**.
- `games.js` — weekly game playtime leaderboard; stats/game leaderboard канон.
- `giveaway.js` — просмотр/вступление в active channel giveaway; giveaway канон.
- `kick.js` — kick с member search, hierarchy/permission checks, confirmation, DM notification и ModLog; moderation workflow.
- `modlog.js` — ModLog status, enable/disable, case deletion и channel selection; ModLog канон.
- `mute.js` — centralized action/hierarchy checks, duplicate prevention и ModLog; moderation канон.
- `nick.js` — self/admin nickname management, `.` reset, 32-character guard и hierarchy/permission checks. Отдельная механика; требует global dedup.
- `nuke.js` — filtered bulk cleanup; **GAB-PUB-057–061 / GD-242**.
- `numfact.js` — external number fact, random/default number, progress/error fallback; integration/fun канон.
- `ping.js` — measured send latency + websocket heartbeat + shard ID; runtime diagnostics канон.
- `poll.js` — active poll voting by number/name, duplicate-vote protection, paginated results; poll канон.
- `quiet.js` — channel/all-channel quiet, timed auto-return; **GAB-PUB-037–040 / GD-239**.
- `reddit.js` — subreddit normalization, state-specific errors, NSFW filtering, pagination and metadata; **GAB-PUB-013–019**.
- `remindme.js` — personal reminders and list view; existing reminder/event canon.
- `roleinfo.js` — role/server role inspection: paginated role lists, member-role aggregation, effective permissions, Administrator warning, role metadata and role search. Отдельная механика; требует global dedup.
- `roll.js` — one/two-bound random roll with reversed-bound normalization; **GAB-PUB-096–097**.
- `say.js` — bot relay with `@everyone` suppression; standalone system не образует.
- `streamers.js` — current live status of all server-tracked streamers with provider-specific presentation and pagination. Underlying monitoring is existing streams canon; live-status command surface требует global dedup review.
- `strike.js` / `strikes.js` — strike creation/history, ModLog linkage, moderator attribution, lazy member state and pagination; **GAB-PUB-067–073**.
- `urban.js` — Urban Dictionary random/search, pagination, metadata, tags and length protection; **GAB-PUB-020–024**.

## Source-specific Public status

Полный Git tree `Commands/Public/` на branch `indev-4.0.2` проверен; API tree возвращает `truncated=false`. Все файлы директории сопоставлены с существующими source-specific notes либо отмечены выше.

**Public source-specific pass завершён.**

Остались для global dedup только отличающиеся механики: `countdown.js`, `nick.js`, `roleinfo.js`, `streamers.js`.
