# InsaneBot RoadMap

План реализации канонического банка `GD-001–307`.

## Правила

- RoadMap строится по зависимостям, а не по номеру `GD`.
- Один `GD` остаётся одной самостоятельной системой; варианты реализации входят в него.
- Сначала строятся фундаментальные сервисы, затем системы, которые от них зависят.
- `GD-001–027` относятся к историческому Batch 1, но исходный файл с названиями отсутствует в текущем tree. Их названия не восстанавливаются догадкой; этот блок нужно восстановить отдельно до финальной привязки.
- Сквозная нумерация пунктов сохраняет текущий порядок всех систем. Ни один существующий подпункт не удаляется.

## 1. Foundation / Core infrastructure

База, без которой остальные системы будут постоянно переделываться.

**1.** `GD-001–027` — **legacy historical block; placement pending source recovery**

**2.** `GD-041` — Economy API

**3.** `GD-071` — Per-server module configuration

**4.** `GD-135` — Moderation service layer

**5.** `GD-194` — Persistent scheduled event instances

**6.** `GD-197` — Recurring events

**7.** `GD-201` — Integration management/configuration

**8.** `GD-203` — Bot API for integrations

**9.** `GD-222` — Automated test CI

**10.** `GD-223` — Separate lint pipeline

**11.** `GD-224` — Code security scanning

**12.** `GD-225` — Reproducible dependency set

**13.** `GD-226` — Automated contribution metadata checks

**14.** `GD-228` — Staged release workflow

## 2. Discord data / server core

Основные сущности и операции Discord.

**15.** `GD-056` — Server counters

**16.** `GD-118` — Member/User validation

**17.** `GD-175` — Server counters extension

**18.** `GD-176` — User activity statistics

**19.** `GD-178` — Server growth statistics

**20.** `GD-180` — Channel activity statistics

**21.** `GD-183` — Personal/server stats cards

**22.** `GD-186` — Voice time statistics

**23.** `GD-258` — Server information card

**24.** `GD-286` — Nickname management

**25.** `GD-287` — Role inspection

## 3. Permissions / access / security foundation

До сложной модерации и web-control-plane.

**26.** `GD-302` — Access Control / Allowlist / Blocklist

**27.** `GD-116` — Hierarchical moderation checks

**28.** `GD-117` — Self/bot targeting protection

**29.** `GD-119` — Discord moderatability checks

**30.** `GD-128` — Required moderation reason

**31.** `GD-137` — Safe default reasons

**32.** `GD-142` — Destructive-action rate limits

**33.** `GD-273` — Discord identity for web authentication

**34.** `GD-274` — Route-level authorization boundaries

**35.** `GD-275` — Web authentication middleware

**36.** `GD-276` — XSS-safe Markdown pipeline

**37.** `GD-277` — Safe external URL fallback

## 4. Scheduler / background lifecycle

**38.** `GD-015` — Background task infrastructure from historical foundation

**39.** `GD-130` — Default tempban duration

**40.** `GD-134` — Timed mute/unmute

**41.** `GD-156` — Ticket follow-up notification

**42.** `GD-194` — Persistent scheduled event instances

**43.** `GD-197` — Recurring events

**44.** `GD-198` — QOTD/daily task events

**45.** `GD-199` — Temporary server events

**46.** `GD-285` — Named persistent server countdowns

**47.** `GD-289` — Scheduled Role with Manual Override

## 5. Moderation

**48.** `GD-120` — Warning system

**49.** `GD-121` — Warning points automation

**50.** `GD-122` — Configurable warn workflow

**51.** `GD-123` — Username/name history

**52.** `GD-124` — Safe rename

**53.** `GD-125` — Anti-repeat message protection

**54.** `GD-126` — Mention spam detection

**55.** `GD-127` — Reinvite after unban

**56.** `GD-129` — Ban message deletion policy

**57.** `GD-131` — Ban DM customization

**58.** `GD-132` — Mute implementation modes

**59.** `GD-133` — Channel-scoped mute

**60.** `GD-138` — Timeout presets

**61.** `GD-139` — UnTimeout validation

**62.** `GD-140` — Mass moderation with partial results

**63.** `GD-141` — Mass moderation input normalization

**64.** `GD-143` — Safe purge

**65.** `GD-144` — Bot-message cleanup

**66.** `GD-145` — Duplicate message cleanup

**67.** `GD-146` — Channel lock/unlock

**68.** `GD-147` — Staff DM

**69.** `GD-148` — Moderation send-message utility

## 6. Modlog / audit

**70.** `GD-060` — Moderation case history

**71.** `GD-136` — Moderation case records

**72.** `GD-216` — Sequential moderation case numbering

**73.** `GD-217` — Moderation case lookup

**74.** `GD-218` — Moderation case editing audit

**75.** `GD-219` — Human-readable case timestamps

**76.** `GD-220` — Configurable case rendering

**77.** `GD-221` — Typed moderation cases

**78.** `GD-179` — Moderation statistics

**79.** `GD-297` — Modlog Suppression Tokens

## 7. Advanced security / incident response

**80.** `GD-084` — Hierarchical content filter

**81.** `GD-085` — Nickname/display-name filtering

**82.** `GD-086` — Rate-based filter enforcement

**83.** `GD-087` — Exact/normalized filter matching

**84.** `GD-088` — Extended filter pipeline

**85.** `GD-089` — Filter enforcement + moderation case

**86.** `GD-090` — Automod immunity

**87.** `GD-091` — Compiled filter-pattern cache

**88.** `GD-092` — Large filter-rule management

**89.** `GD-296` — Emergency Server Lockdown

**90.** `GD-298` — Compromise-response Preset

## 8. Community / roles / social

**91.** `GD-057` — Self-service role panels

**92.** `GD-161` — Self-role toggle

**93.** `GD-162` — Self-role catalog

**94.** `GD-163` — Self-role administration

**95.** `GD-164` — Managed role editing

**96.** `GD-055` — Join-to-create voice channels

**97.** `GD-058` — Birthday system

**98.** `GD-059` — User notes

**99.** `GD-070` — Welcome / goodbye messages

**100.** `GD-169` — Family/social relations

**101.** `GD-170` — AFK status

**102.** `GD-171` — Social interaction

**103.** `GD-172` — Social relationships

**104.** `GD-173` — Social compatibility

**105.** `GD-174` — Social leaderboard

**106.** `GD-288` — Linked Accounts / Alternate Accounts

**107.** `GD-300` — Invite Tracking & Statistics

**108.** `GD-301` — Starboard

**109.** `GD-306` — Social Relations / Interactions

## 9. Utility / customization

**110.** `GD-065` — Custom commands

**111.** `GD-066` — Custom command aliases / shortcuts

**112.** `GD-067` — Keyword / trigger auto-responses

**113.** `GD-068` — Custom response placeholders

**114.** `GD-069` — Custom embeds

**115.** `GD-072` — Randomized custom command responses

**116.** `GD-237` — Dynamic permission-aware help menu

**117.** `GD-238` — Per-channel command cooldown

**118.** `GD-239` — Channel-wide quiet mode

**119.** `GD-240` — Persistent interactive counters

**120.** `GD-241` — Structured message archive export

**121.** `GD-242` — Filtered bulk message cleanup

**122.** `GD-243` — Emoji jumbo renderer

**123.** `GD-244` — Global custom emoji inspector

**124.** `GD-245` — URL redirect safety inspection

**125.** `GD-246` — Fuzzy category resolution

**126.** `GD-247` — Temporary private talk rooms

**127.** `GD-248` — Server to-do list

**128.** `GD-253` — Configurable server prefix

**129.** `GD-254` — RSS feed alias/catalog access

**130.** `GD-256` — Bitly shorten/expand utility

**131.** `GD-293` — Source Links for Commands / Cogs

**132.** `GD-294` — Moderation-only Echo / Embed Relay

**133.** `GD-303` — Global Broadcast

## 10. Tickets / reports / applications

**134.** `GD-149` — Ticket panel

**135.** `GD-150` — One active ticket per user

**136.** `GD-151` — Ticket claim/unclaim

**137.** `GD-152` — Ticket priority

**138.** `GD-153` — Ticket close states

**139.** `GD-154` — Ticket rename

**140.** `GD-155` — Ticket participants management

**141.** `GD-157` — Ticket transcript

**142.** `GD-158` — Custom ticket message

**143.** `GD-159` — Ticket limits

**144.** `GD-160` — Multiple ticket systems

**145.** `GD-188` — Built-in user reports

**146.** `GD-189` — Report server selection

**147.** `GD-190` — Report anti-spam windows

**148.** `GD-191` — Report attachments

**149.** `GD-192` — Report staff communication tunnel

**150.** `GD-193` — Sequential report numbering

**151.** `GD-299` — Applications / Staff Application Workflow

## 11. Progression / statistics

**152.** `GD-165` — Message XP progression

**153.** `GD-166` — Level role rewards

**154.** `GD-167` — Server leveling configuration

**155.** `GD-168` — Progression rank leaderboard

**156.** `GD-177` — Activity leaderboards

**157.** `GD-181` — Activity heatmap

**158.** `GD-182` — Period statistics

**159.** `GD-184` — Game statistics

**160.** `GD-185` — Invite statistics

**161.** `GD-187` — Statistics visualization

**162.** `GD-250` — Weekly guild statistics reset

**163.** `GD-251` — Command-usage statistics

**164.** `GD-252` — Rank-specific leaderboard

**165.** `GD-257` — User points leaderboard surface

**166.** `GD-307` — Statistics / Analytics

## 12. Economy

**167.** `GD-028` — Basic user balance

**168.** `GD-029` — Wallet/bank separation

**169.** `GD-030` — Economy shop/inventory

**170.** `GD-031` — Discord-role shop

**171.** `GD-032` — Periodic monetary rewards

**172.** `GD-033` — Role-based periodic reward

**173.** `GD-034` — Active work income

**174.** `GD-035` — Beg

**175.** `GD-036` — P2P currency transfer

**176.** `GD-037` — Administrative balance management

**177.** `GD-038` — Maximum balance limit

**178.** `GD-039` — Max-balance payout correction

**179.** `GD-040` — Economy leaderboard

**180.** `GD-042` — Paid actions integration

**181.** `GD-043` — Rewards from other systems

**182.** `GD-044` — Risky currency theft

**183.** `GD-045` — Crime / risk-reward

**184.** `GD-046` — Mine

**185.** `GD-047` — Fishing

**186.** `GD-048` — Hunt

**187.** `GD-049` — Gambling / slot machine

**188.** `GD-050` — Global vs server economy mode

**189.** `GD-051` — Currency name configuration

**190.** `GD-052` — Economy reset

**191.** `GD-053` — Inactive economy record cleanup

**192.** `GD-249` — Scaled points lottery

## 13. Games / Trivia / Fun

**193.** `GD-093` — Mini-game catalog

**194.** `GD-094` — Casino game section

**195.** `GD-095` — Independent mini-games

**196.** `GD-096` — Game rankings/statistics

**197.** `GD-097` — Daily game challenges

**198.** `GD-098` — Game economic rewards

**199.** `GD-099` — Mixed trivia pool

**200.** `GD-100` — Custom trivia sets

**201.** `GD-101` — Trivia-set configuration

**202.** `GD-102` — Trivia victory condition

**203.** `GD-103` — Trivia timers

**204.** `GD-104` — Bot participant in Trivia

**205.** `GD-105` — Trivia response UX

**206.** `GD-106` — Trivia answer matching

**207.** `GD-107` — Conditional Trivia reward

**208.** `GD-108` — Persistent Trivia statistics

**209.** `GD-109` — Channel-scoped concurrent Trivia

**210.** `GD-110` — Forced Trivia stop

**211.** `GD-111` — Async game-session lifecycle

**212.** `GD-112` — Fun command layer

**213.** `GD-113` — Random choice/response utilities

**214.** `GD-114` — Random media/fact fun

**215.** `GD-115` — Fun user/media transformations

**216.** `GD-259` — Per-answer visual variation

## 14. Music / external media

**217.** `GD-073` — Managed external media/audio node

**218.** `GD-074` — Automatic media-node runtime installation

**219.** `GD-075` — Managed-node configuration generation

**220.** `GD-076` — External-process environment preflight

**221.** `GD-077` — Runtime-check cache

**222.** `GD-078` — Managed-node resource control

**223.** `GD-079` — Readiness by stdout/logs

**224.** `GD-080` — External-process lifecycle manager

**225.** `GD-081` — Node plugin diagnostics

**226.** `GD-082` — Managed/unmanaged backend mode

**227.** `GD-083` — Reset managed backend settings

**228.** `GD-200` — External service integrations

**229.** `GD-205` — Multi-provider stream monitoring

**230.** `GD-206` — Multiple independent stream alerts

**231.** `GD-207` — Transition-based live alerts

**232.** `GD-208` — YouTube stream filtering

**233.** `GD-209` — Configurable stream mentions

**234.** `GD-210` — Stream watch action

**235.** `GD-211` — Stream API quota control

**236.** `GD-212` — Stream OAuth token refresh

**237.** `GD-213` — Shared stream credentials migration

**238.** `GD-214` — Missing-secret owner warning

**239.** `GD-215` — Resilient stream polling

## 15. Web / dashboard / advanced control plane

**240.** `GD-202` — Integration dashboard/web interface

**241.** `GD-260` — Web normalized DTO layer

**242.** `GD-261` — Privacy-aware public user profile

**243.** `GD-262` — Public server listing

**244.** `GD-263` — Web timestamps

**245.** `GD-264` — Versioned extension gallery

**246.** `GD-265` — Human-readable extension scopes

**247.** `GD-266` — Extension web administration

**248.** `GD-267` — Web dashboard control plane

**249.** `GD-268` — Web command configuration matrix

**250.** `GD-269` — Preserve untouched configuration fields

**251.** `GD-270` — Transactional dashboard save

**252.** `GD-271` — Dashboard destructive-action endpoint

**253.** `GD-272` — Dashboard statistics surface

**254.** `GD-278` — Controller/route/API separation

**255.** `GD-279` — Route-level feature namespaces

**256.** `GD-280` — Public content surface isolation

**257.** `GD-281` — Maintainer operational dashboard

**258.** `GD-282` — Web server lifecycle isolation

**259.** `GD-283` — Graceful missing remote entities

**260.** `GD-284` — Bulk mutual-guild resolution

**261.** `GD-292` — Persistent REPL / Eval Environment

**262.** `GD-290` — Multi-source Latency Healthcheck

**263.** `GD-291` — WebSocket Event-rate Diagnostics

**264.** `GD-295` — API Diff / Reconciliation Sync

**265.** `GD-304` — Installation Serverlock

**266.** `GD-305` — User Reports

## 16. Discord Activities / final large systems

**267.** `GD-093–111` — game architecture already prepared above

**268.** `GD-303` — Global Broadcast

**269.** `GD-304` — Installation Serverlock

**270.** `GD-307` — Statistics / Analytics

**271.** Discord Activities canonical system from CorwinDev source (`COR-303`, `COR-336–337`)

## Implementation principle

Внутри каждого этапа порядок сверху вниз — ориентир зависимостей. Если при реализации конкретной системы выясняется новая зависимость, RoadMap корректируется, но канонические IDs не перенумеровываются.

### Current milestone

**Milestone 0 — Foundation:** довести текущую структуру `main.py` / `bot/` / `cogs/`, configuration, extension lifecycle и базовую инфраструктуру до устойчивого состояния.

После этого переходить к storage/data layer, затем к permissions и moderation.
