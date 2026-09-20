# InsaneBot RoadMap

План реализации канонического банка `GD-001–307`.

## Правила

- RoadMap строится по зависимостям, а не по номеру `GD`.
- Один `GD` остаётся одной самостоятельной системой; варианты реализации входят в него.
- Сначала строятся фундаментальные сервисы, затем системы, которые от них зависят.
- `GD-001–027` относятся к историческому Batch 1. Исходный файл с точными названиями отсутствует, поэтому 1:1 восстановление canonical IDs не выполняется. Только уникальные требования, которые не дублируют существующие пункты, добавляются в соответствующие категории как `B1-*` requirements.
- Сквозная нумерация пунктов сохраняет текущий порядок всех систем. Ни один существующий подпункт не удаляется.

## 1. Foundation / Core infrastructure

База, без которой остальные системы будут постоянно переделываться.

**1.** ~~`GD-001–027`~~ — **~~legacy historical block; audited — unique Batch 1 requirements redistributed below; original 1:1 GD mapping remains unavailable~~ **DONE — Batch 1 systems audited and redistributed into the roadmap.****

**2.** `B1-CORE` — **Runtime information / diagnostics** — единый слой информации о состоянии и окружении бота для диагностики.

**3.** `B1-CORE` — **Multi-instance lifecycle** — управление жизненным циклом нескольких экземпляров бота/воркеров.

**4.** `B1-CORE` — **Core RPC** — внутреннее взаимодействие между экземплярами/процессами бота.

**5.** `B1-CORE` — **Localization / timezone infrastructure** — единые локаль, язык и часовой пояс для серверов/пользователей.

**6.** `GD-041` — Economy API

**7.** `GD-071` — Per-server module configuration

**8.** `GD-135` — Moderation service layer

**9.** `GD-194` — Persistent scheduled event instances

**10.** `GD-197` — Recurring events

**11.** `GD-201` — Integration management/configuration

**12.** `GD-203` — Bot API for integrations

**13.** `GD-222` — Automated test CI

**14.** `GD-223` — Separate lint pipeline

**15.** `GD-224` — Code security scanning

**16.** `GD-225` — Reproducible dependency set

**17.** `GD-226` — Automated contribution metadata checks

**18.** `GD-228` — Staged release workflow

## 2. Discord data / server core

Основные сущности и операции Discord.

**19.** `B1-STORAGE` — **Backup / restore** — резервное копирование и восстановление persistent data.

**20.** `GD-056` — Server counters

**21.** `GD-118` — Member/User validation

**22.** `GD-175` — Server counters extension

**23.** `GD-176` — User activity statistics

**24.** `GD-178` — Server growth statistics

**25.** `GD-180` — Channel activity statistics

**26.** `GD-183` — Personal/server stats cards

**27.** `GD-186` — Voice time statistics

**28.** `GD-258` — Server information card

**29.** `GD-286` — Nickname management

**30.** `GD-287` — Role inspection

## 3. Permissions / access / security foundation

До сложной модерации и web-control-plane.

**31.** `GD-302` — Access Control / Allowlist / Blocklist

**32.** `GD-116` — Hierarchical moderation checks

**33.** `GD-117` — Self/bot targeting protection

**34.** `GD-119` — Discord moderatability checks

**35.** `GD-128` — Required moderation reason

**36.** `GD-137` — Safe default reasons

**37.** `GD-142` — Destructive-action rate limits

**38.** `GD-273` — Discord identity for web authentication

**39.** `GD-274` — Route-level authorization boundaries

**40.** `GD-275` — Web authentication middleware

**41.** `GD-276` — XSS-safe Markdown pipeline

**42.** `GD-277` — Safe external URL fallback

## 4. Scheduler / background lifecycle

**43.** `GD-015` — Background task infrastructure from historical foundation

**44.** `GD-130` — Default tempban duration

**45.** `GD-134` — Timed mute/unmute

**46.** `GD-156` — Ticket follow-up notification

**47.** `GD-194` — Persistent scheduled event instances

**48.** `GD-197` — Recurring events

**49.** `GD-198` — QOTD/daily task events

**50.** `GD-199` — Temporary server events

**51.** `GD-285` — Named persistent server countdowns

**52.** `GD-289` — Scheduled Role with Manual Override

## 5. Moderation

**53.** `GD-120` — Warning system

**54.** `GD-121` — Warning points automation

**55.** `GD-122` — Configurable warn workflow

**56.** `GD-123` — Username/name history

**57.** `GD-124` — Safe rename

**58.** `GD-125` — Anti-repeat message protection

**59.** `GD-126` — Mention spam detection

**60.** `GD-127` — Reinvite after unban

**61.** `GD-129` — Ban message deletion policy

**62.** `GD-131` — Ban DM customization

**63.** `GD-132` — Mute implementation modes

**64.** `GD-133` — Channel-scoped mute

**65.** `GD-138` — Timeout presets

**66.** `GD-139` — UnTimeout validation

**67.** `GD-140` — Mass moderation with partial results

**68.** `GD-141` — Mass moderation input normalization

**69.** `GD-143` — Safe purge

**70.** `GD-144` — Bot-message cleanup

**71.** `GD-145` — Duplicate message cleanup

**72.** `GD-146` — Channel lock/unlock

**73.** `GD-147` — Staff DM

**74.** `GD-148` — Moderation send-message utility

## 6. Modlog / audit

**75.** `GD-060` — Moderation case history

**76.** `GD-136` — Moderation case records

**77.** `GD-216` — Sequential moderation case numbering

**78.** `GD-217` — Moderation case lookup

**79.** `GD-218` — Moderation case editing audit

**80.** `GD-219` — Human-readable case timestamps

**81.** `GD-220` — Configurable case rendering

**82.** `GD-221` — Typed moderation cases

**83.** `GD-179` — Moderation statistics

**84.** `GD-297` — Modlog Suppression Tokens

## 7. Advanced security / incident response

**85.** `GD-084` — Hierarchical content filter

**86.** `GD-085` — Nickname/display-name filtering

**87.** `GD-086` — Rate-based filter enforcement

**88.** `GD-087` — Exact/normalized filter matching

**89.** `GD-088` — Extended filter pipeline

**90.** `GD-089` — Filter enforcement + moderation case

**91.** `GD-090` — Automod immunity

**92.** `GD-091` — Compiled filter-pattern cache

**93.** `GD-092` — Large filter-rule management

**94.** `GD-296` — Emergency Server Lockdown

**95.** `GD-298` — Compromise-response Preset

## 8. Community / roles / social

**96.** `GD-057` — Self-service role panels

**97.** `GD-161` — Self-role toggle

**98.** `GD-162` — Self-role catalog

**99.** `GD-163` — Self-role administration

**100.** `GD-164` — Managed role editing

**101.** `GD-055` — Join-to-create voice channels

**102.** `GD-058` — Birthday system

**103.** `GD-059` — User notes

**104.** `GD-070` — Welcome / goodbye messages

**105.** `GD-169` — Family/social relations

**106.** `GD-170` — AFK status

**107.** `GD-171` — Social interaction

**108.** `GD-172` — Social relationships

**109.** `GD-173` — Social compatibility

**110.** `GD-174` — Social leaderboard

**111.** `GD-288` — Linked Accounts / Alternate Accounts

**112.** `GD-300` — Invite Tracking & Statistics

**113.** `GD-301` — Starboard

**114.** `GD-306` — Social Relations / Interactions

## 9. Utility / customization

**115.** `GD-065` — Custom commands

**116.** `GD-066` — Custom command aliases / shortcuts

**117.** `GD-067` — Keyword / trigger auto-responses

**118.** `GD-068` — Custom response placeholders

**119.** `GD-069` — Custom embeds

**120.** `GD-072` — Randomized custom command responses

**121.** `GD-237` — Dynamic permission-aware help menu

**122.** `GD-238` — Per-channel command cooldown

**123.** `GD-239` — Channel-wide quiet mode

**124.** `GD-240` — Persistent interactive counters

**125.** `GD-241` — Structured message archive export

**126.** `GD-242` — Filtered bulk message cleanup

**127.** `GD-243` — Emoji jumbo renderer

**128.** `GD-244` — Global custom emoji inspector

**129.** `GD-245` — URL redirect safety inspection

**130.** `GD-246` — Fuzzy category resolution

**131.** `GD-247` — Temporary private talk rooms

**132.** `GD-248` — Server to-do list

**133.** `GD-253` — Configurable server prefix

**134.** `GD-254` — RSS feed alias/catalog access

**135.** `GD-256` — Bitly shorten/expand utility

**136.** `GD-293` — Source Links for Commands / Cogs

**137.** `GD-294` — Moderation-only Echo / Embed Relay

**138.** `GD-303` — Global Broadcast

## 10. Tickets / reports / applications

**139.** `GD-149` — Ticket panel

**140.** `GD-150` — One active ticket per user

**141.** `GD-151` — Ticket claim/unclaim

**142.** `GD-152` — Ticket priority

**143.** `GD-153` — Ticket close states

**144.** `GD-154` — Ticket rename

**145.** `GD-155` — Ticket participants management

**146.** `GD-157` — Ticket transcript

**147.** `GD-158` — Custom ticket message

**148.** `GD-159` — Ticket limits

**149.** `GD-160` — Multiple ticket systems

**150.** `GD-188` — Built-in user reports

**151.** `GD-189` — Report server selection

**152.** `GD-190` — Report anti-spam windows

**153.** `GD-191` — Report attachments

**154.** `GD-192` — Report staff communication tunnel

**155.** `GD-193` — Sequential report numbering

**156.** `GD-299` — Applications / Staff Application Workflow

## 11. Progression / statistics

**157.** `GD-165` — Message XP progression

**158.** `GD-166` — Level role rewards

**159.** `GD-167` — Server leveling configuration

**160.** `GD-168` — Progression rank leaderboard

**161.** `GD-177` — Activity leaderboards

**162.** `GD-181` — Activity heatmap

**163.** `GD-182` — Period statistics

**164.** `GD-184` — Game statistics

**165.** `GD-185` — Invite statistics

**166.** `GD-187` — Statistics visualization

**167.** `GD-250` — Weekly guild statistics reset

**168.** `GD-251` — Command-usage statistics

**169.** `GD-252` — Rank-specific leaderboard

**170.** `GD-257` — User points leaderboard surface

**171.** `GD-307` — Statistics / Analytics

## 12. Economy

**172.** `GD-028` — Basic user balance

**173.** `GD-029` — Wallet/bank separation

**174.** `GD-030` — Economy shop/inventory

**175.** `GD-031` — Discord-role shop

**176.** `GD-032` — Periodic monetary rewards

**177.** `GD-033` — Role-based periodic reward

**178.** `GD-034` — Active work income

**179.** `GD-035` — Beg

**180.** `GD-036` — P2P currency transfer

**181.** `GD-037` — Administrative balance management

**182.** `GD-038` — Maximum balance limit

**183.** `GD-039` — Max-balance payout correction

**184.** `GD-040` — Economy leaderboard

**185.** `GD-042` — Paid actions integration

**186.** `GD-043` — Rewards from other systems

**187.** `GD-044` — Risky currency theft

**188.** `GD-045` — Crime / risk-reward

**189.** `GD-046` — Mine

**190.** `GD-047` — Fishing

**191.** `GD-048` — Hunt

**192.** `GD-049` — Gambling / slot machine

**193.** `GD-050` — Global vs server economy mode

**194.** `GD-051` — Currency name configuration

**195.** `GD-052` — Economy reset

**196.** `GD-053` — Inactive economy record cleanup

**197.** `GD-249` — Scaled points lottery

## 13. Games / Trivia / Fun

**198.** `GD-093` — Mini-game catalog

**199.** `GD-094` — Casino game section

**200.** `GD-095` — Independent mini-games

**201.** `GD-096` — Game rankings/statistics

**202.** `GD-097` — Daily game challenges

**203.** `GD-098` — Game economic rewards

**204.** `GD-099` — Mixed trivia pool

**205.** `GD-100` — Custom trivia sets

**206.** `GD-101` — Trivia-set configuration

**207.** `GD-102` — Trivia victory condition

**208.** `GD-103` — Trivia timers

**209.** `GD-104` — Bot participant in Trivia

**210.** `GD-105` — Trivia response UX

**211.** `GD-106` — Trivia answer matching

**212.** `GD-107` — Conditional Trivia reward

**213.** `GD-108` — Persistent Trivia statistics

**214.** `GD-109` — Channel-scoped concurrent Trivia

**215.** `GD-110` — Forced Trivia stop

**216.** `GD-111` — Async game-session lifecycle

**217.** `GD-112` — Fun command layer

**218.** `GD-113` — Random choice/response utilities

**219.** `GD-114` — Random media/fact fun

**220.** `GD-115` — Fun user/media transformations

**221.** `GD-259` — Per-answer visual variation

## 14. Music / external media

**222.** `GD-073` — Managed external media/audio node

**223.** `GD-074` — Automatic media-node runtime installation

**224.** `GD-075` — Managed-node configuration generation

**225.** `GD-076` — External-process environment preflight

**226.** `GD-077` — Runtime-check cache

**227.** `GD-078` — Managed-node resource control

**228.** `GD-079` — Readiness by stdout/logs

**229.** `GD-080` — External-process lifecycle manager

**230.** `GD-081` — Node plugin diagnostics

**231.** `GD-082` — Managed/unmanaged backend mode

**232.** `GD-083` — Reset managed backend settings

**233.** `GD-200` — External service integrations

**234.** `GD-205` — Multi-provider stream monitoring

**235.** `GD-206` — Multiple independent stream alerts

**236.** `GD-207` — Transition-based live alerts

**237.** `GD-208` — YouTube stream filtering

**238.** `GD-209` — Configurable stream mentions

**239.** `GD-210` — Stream watch action

**240.** `GD-211` — Stream API quota control

**241.** `GD-212` — Stream OAuth token refresh

**242.** `GD-213` — Shared stream credentials migration

**243.** `GD-214` — Missing-secret owner warning

**244.** `GD-215` — Resilient stream polling

## 15. Web / dashboard / advanced control plane

**245.** `GD-202` — Integration dashboard/web interface

**246.** `GD-260` — Web normalized DTO layer

**247.** `GD-261` — Privacy-aware public user profile

**248.** `GD-262` — Public server listing

**249.** `GD-263` — Web timestamps

**250.** `GD-264` — Versioned extension gallery

**251.** `GD-265` — Human-readable extension scopes

**252.** `GD-266` — Extension web administration

**253.** `GD-267` — Web dashboard control plane

**254.** `GD-268` — Web command configuration matrix

**255.** `GD-269` — Preserve untouched configuration fields

**256.** `GD-270` — Transactional dashboard save

**257.** `GD-271` — Dashboard destructive-action endpoint

**258.** `GD-272` — Dashboard statistics surface

**259.** `GD-278` — Controller/route/API separation

**260.** `GD-279` — Route-level feature namespaces

**261.** `GD-280` — Public content surface isolation

**262.** `GD-281` — Maintainer operational dashboard

**263.** `GD-282` — Web server lifecycle isolation

**264.** `GD-283` — Graceful missing remote entities

**265.** `GD-284` — Bulk mutual-guild resolution

**266.** `GD-292` — Persistent REPL / Eval Environment

**267.** `GD-290` — Multi-source Latency Healthcheck

**268.** `GD-291` — WebSocket Event-rate Diagnostics

**269.** `GD-295` — API Diff / Reconciliation Sync

**270.** `GD-304` — Installation Serverlock

**271.** `GD-305` — User Reports

## 16. Discord Activities / final large systems

**272.** `GD-093–111` — game architecture already prepared above

**273.** `GD-303` — Global Broadcast

**274.** `GD-304` — Installation Serverlock

**275.** `GD-307` — Statistics / Analytics

**276.** Discord Activities canonical system from CorwinDev source (`COR-303`, `COR-336–337`)

## Implementation principle

Внутри каждого этапа порядок сверху вниз — ориентир зависимостей. Если при реализации конкретной системы выясняется новая зависимость, RoadMap корректируется, но канонические IDs не перенумеровываются.

### Current milestone

**Milestone 0 — Foundation: [~] IN PROGRESS**

Довести текущую структуру `main.py` / `bot/` / `cogs/`, configuration, extension lifecycle и базовую инфраструктуру до устойчивого состояния.

Уже сделано в рамках Milestone 0:
- базовая структура `main.py` / `bot/` / `cogs/`;
- переход на `commands.InteractionBot()`;
- загрузчик extensions/cogs;
- базовая конфигурация через `.env`;
- SQLAlchemy + Alembic foundation;
- базовая модель `User`;
- отдельный logging layer с уровнями и цветным выводом;
- обработка ошибок загрузки extensions через logging;
- базовый `cog manager` с load/unload/reload.

После завершения Milestone 0 переходить к storage/data layer, затем к permissions и moderation.
