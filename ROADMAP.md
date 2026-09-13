# InsaneBot RoadMap

План реализации канонического банка `GD-001–307`.

## Правила

- RoadMap строится по зависимостям, а не по номеру `GD`.
- Один `GD` остаётся одной самостоятельной системой; варианты реализации входят в него.
- Сначала строятся фундаментальные сервисы, затем системы, которые от них зависят.
- `GD-001–027` относятся к историческому Batch 1, но исходный файл с названиями отсутствует в текущем tree. Их названия не восстанавливаются догадкой; этот блок нужно восстановить отдельно до финальной привязки.

## 1. Foundation / Core infrastructure

База, без которой остальные системы будут постоянно переделываться.

**1.1** `GD-001–027` — **legacy historical block; placement pending source recovery**
**1.2** `GD-041` — Economy API
**1.3** `GD-071` — Per-server module configuration
**1.4** `GD-135` — Moderation service layer
**1.5** `GD-194` — Persistent scheduled event instances
**1.6** `GD-197` — Recurring events
**1.7** `GD-201` — Integration management/configuration
**1.8** `GD-203` — Bot API for integrations
**1.9** `GD-222` — Automated test CI
**1.10** `GD-223` — Separate lint pipeline
**1.11** `GD-224` — Code security scanning
**1.12** `GD-225` — Reproducible dependency set
**1.13** `GD-226` — Automated contribution metadata checks
**1.14** `GD-228` — Staged release workflow

## 2. Discord data / server core

Основные сущности и операции Discord.

**2.1** `GD-056` — Server counters
**2.2** `GD-118` — Member/User validation
**2.3** `GD-175` — Server counters extension
**2.4** `GD-176` — User activity statistics
**2.5** `GD-178` — Server growth statistics
**2.6** `GD-180` — Channel activity statistics
**2.7** `GD-183` — Personal/server stats cards
**2.8** `GD-186` — Voice time statistics
**2.9** `GD-258` — Server information card
**2.10** `GD-286` — Nickname management
**2.11** `GD-287` — Role inspection

## 3. Permissions / access / security foundation

До сложной модерации и web-control-plane.

**3.1** `GD-302` — Access Control / Allowlist / Blocklist
**3.2** `GD-116` — Hierarchical moderation checks
**3.3** `GD-117` — Self/bot targeting protection
**3.4** `GD-119` — Discord moderatability checks
**3.5** `GD-128` — Required moderation reason
**3.6** `GD-137` — Safe default reasons
**3.7** `GD-142` — Destructive-action rate limits
**3.8** `GD-273` — Discord identity for web authentication
**3.9** `GD-274` — Route-level authorization boundaries
**3.10** `GD-275` — Web authentication middleware
**3.11** `GD-276` — XSS-safe Markdown pipeline
**3.12** `GD-277` — Safe external URL fallback

## 4. Scheduler / background lifecycle

**4.1** `GD-015` — Background task infrastructure from historical foundation
**4.2** `GD-130` — Default tempban duration
**4.3** `GD-134` — Timed mute/unmute
**4.4** `GD-156` — Ticket follow-up notification
**4.5** `GD-194` — Persistent scheduled event instances
**4.6** `GD-197` — Recurring events
**4.7** `GD-198` — QOTD/daily task events
**4.8** `GD-199` — Temporary server events
**4.9** `GD-285` — Named persistent server countdowns
**4.10** `GD-289` — Scheduled Role with Manual Override

## 5. Moderation

**5.1** `GD-120` — Warning system
**5.2** `GD-121` — Warning points automation
**5.3** `GD-122` — Configurable warn workflow
**5.4** `GD-123` — Username/name history
**5.5** `GD-124` — Safe rename
**5.6** `GD-125` — Anti-repeat message protection
**5.7** `GD-126` — Mention spam detection
**5.8** `GD-127` — Reinvite after unban
**5.9** `GD-129` — Ban message deletion policy
**5.10** `GD-131` — Ban DM customization
**5.11** `GD-132` — Mute implementation modes
**5.12** `GD-133` — Channel-scoped mute
**5.13** `GD-138` — Timeout presets
**5.14** `GD-139` — UnTimeout validation
**5.15** `GD-140` — Mass moderation with partial results
**5.16** `GD-141` — Mass moderation input normalization
**5.17** `GD-143` — Safe purge
**5.18** `GD-144` — Bot-message cleanup
**5.19** `GD-145` — Duplicate message cleanup
**5.20** `GD-146` — Channel lock/unlock
**5.21** `GD-147` — Staff DM
**5.22** `GD-148` — Moderation send-message utility

## 6. Modlog / audit

**6.1** `GD-060` — Moderation case history
**6.2** `GD-136` — Moderation case records
**6.3** `GD-216` — Sequential moderation case numbering
**6.4** `GD-217` — Moderation case lookup
**6.5** `GD-218` — Moderation case editing audit
**6.6** `GD-219` — Human-readable case timestamps
**6.7** `GD-220` — Configurable case rendering
**6.8** `GD-221` — Typed moderation cases
**6.9** `GD-179` — Moderation statistics
**6.10** `GD-297` — Modlog Suppression Tokens

## 7. Advanced security / incident response

**7.1** `GD-084` — Hierarchical content filter
**7.2** `GD-085` — Nickname/display-name filtering
**7.3** `GD-086` — Rate-based filter enforcement
**7.4** `GD-087` — Exact/normalized filter matching
**7.5** `GD-088` — Extended filter pipeline
**7.6** `GD-089` — Filter enforcement + moderation case
**7.7** `GD-090` — Automod immunity
**7.8** `GD-091` — Compiled filter-pattern cache
**7.9** `GD-092` — Large filter-rule management
**7.10** `GD-296` — Emergency Server Lockdown
**7.11** `GD-298` — Compromise-response Preset

## 8. Community / roles / social

**8.1** `GD-057` — Self-service role panels
**8.2** `GD-161` — Self-role toggle
**8.3** `GD-162` — Self-role catalog
**8.4** `GD-163` — Self-role administration
**8.5** `GD-164` — Managed role editing
**8.6** `GD-055` — Join-to-create voice channels
**8.7** `GD-058` — Birthday system
**8.8** `GD-059` — User notes
**8.9** `GD-070` — Welcome / goodbye messages
**8.10** `GD-169` — Family/social relations
**8.11** `GD-170` — AFK status
**8.12** `GD-171` — Social interaction
**8.13** `GD-172` — Social relationships
**8.14** `GD-173` — Social compatibility
**8.15** `GD-174` — Social leaderboard
**8.16** `GD-288` — Linked Accounts / Alternate Accounts
**8.17** `GD-300` — Invite Tracking & Statistics
**8.18** `GD-301` — Starboard
**8.19** `GD-306` — Social Relations / Interactions

## 9. Utility / customization

**9.1** `GD-065` — Custom commands
**9.2** `GD-066` — Custom command aliases / shortcuts
**9.3** `GD-067` — Keyword / trigger auto-responses
**9.4** `GD-068` — Custom response placeholders
**9.5** `GD-069` — Custom embeds
**9.6** `GD-072` — Randomized custom command responses
**9.7** `GD-237` — Dynamic permission-aware help menu
**9.8** `GD-238` — Per-channel command cooldown
**9.9** `GD-239` — Channel-wide quiet mode
**9.10** `GD-240` — Persistent interactive counters
**9.11** `GD-241` — Structured message archive export
**9.12** `GD-242` — Filtered bulk message cleanup
**9.13** `GD-243` — Emoji jumbo renderer
**9.14** `GD-244` — Global custom emoji inspector
**9.15** `GD-245` — URL redirect safety inspection
**9.16** `GD-246` — Fuzzy category resolution
**9.17** `GD-247` — Temporary private talk rooms
**9.18** `GD-248` — Server to-do list
**9.19** `GD-253` — Configurable server prefix
**9.20** `GD-254` — RSS feed alias/catalog access
**9.21** `GD-256` — Bitly shorten/expand utility
**9.22** `GD-293` — Source Links for Commands / Cogs
**9.23** `GD-294` — Moderation-only Echo / Embed Relay
**9.24** `GD-303` — Global Broadcast

## 10. Tickets / reports / applications

**10.1** `GD-149` — Ticket panel
**10.2** `GD-150` — One active ticket per user
**10.3** `GD-151` — Ticket claim/unclaim
**10.4** `GD-152` — Ticket priority
**10.5** `GD-153` — Ticket close states
**10.6** `GD-154` — Ticket rename
**10.7** `GD-155` — Ticket participants management
**10.8** `GD-157` — Ticket transcript
**10.9** `GD-158` — Custom ticket message
**10.10** `GD-159` — Ticket limits
**10.11** `GD-160` — Multiple ticket systems
**10.12** `GD-188` — Built-in user reports
**10.13** `GD-189` — Report server selection
**10.14** `GD-190` — Report anti-spam windows
**10.15** `GD-191` — Report attachments
**10.16** `GD-192` — Report staff communication tunnel
**10.17** `GD-193` — Sequential report numbering
**10.18** `GD-299` — Applications / Staff Application Workflow

## 11. Progression / statistics

**11.1** `GD-165` — Message XP progression
**11.2** `GD-166` — Level role rewards
**11.3** `GD-167` — Server leveling configuration
**11.4** `GD-168` — Progression rank leaderboard
**11.5** `GD-177` — Activity leaderboards
**11.6** `GD-181` — Activity heatmap
**11.7** `GD-182` — Period statistics
**11.8** `GD-184` — Game statistics
**11.9** `GD-185` — Invite statistics
**11.10** `GD-187` — Statistics visualization
**11.11** `GD-250` — Weekly guild statistics reset
**11.12** `GD-251` — Command-usage statistics
**11.13** `GD-252` — Rank-specific leaderboard
**11.14** `GD-257` — User points leaderboard surface
**11.15** `GD-307` — Statistics / Analytics

## 12. Economy

**12.1** `GD-028` — Basic user balance
**12.2** `GD-029` — Wallet/bank separation
**12.3** `GD-030` — Economy shop/inventory
**12.4** `GD-031` — Discord-role shop
**12.5** `GD-032` — Periodic monetary rewards
**12.6** `GD-033` — Role-based periodic reward
**12.7** `GD-034` — Active work income
**12.8** `GD-035` — Beg
**12.9** `GD-036` — P2P currency transfer
**12.10** `GD-037` — Administrative balance management
**12.11** `GD-038` — Maximum balance limit
**12.12** `GD-039` — Max-balance payout correction
**12.13** `GD-040` — Economy leaderboard
**12.14** `GD-042` — Paid actions integration
**12.15** `GD-043` — Rewards from other systems
**12.16** `GD-044` — Risky currency theft
**12.17** `GD-045` — Crime / risk-reward
**12.18** `GD-046` — Mine
**12.19** `GD-047` — Fishing
**12.20** `GD-048` — Hunt
**12.21** `GD-049` — Gambling / slot machine
**12.22** `GD-050` — Global vs server economy mode
**12.23** `GD-051` — Currency name configuration
**12.24** `GD-052` — Economy reset
**12.25** `GD-053` — Inactive economy record cleanup
**12.26** `GD-249` — Scaled points lottery

## 13. Games / Trivia / Fun

**13.1** `GD-093` — Mini-game catalog
**13.2** `GD-094` — Casino game section
**13.3** `GD-095` — Independent mini-games
**13.4** `GD-096` — Game rankings/statistics
**13.5** `GD-097` — Daily game challenges
**13.6** `GD-098` — Game economic rewards
**13.7** `GD-099` — Mixed trivia pool
**13.8** `GD-100` — Custom trivia sets
**13.9** `GD-101` — Trivia-set configuration
**13.10** `GD-102` — Trivia victory condition
**13.11** `GD-103` — Trivia timers
**13.12** `GD-104` — Bot participant in Trivia
**13.13** `GD-105` — Trivia response UX
**13.14** `GD-106` — Trivia answer matching
**13.15** `GD-107` — Conditional Trivia reward
**13.16** `GD-108` — Persistent Trivia statistics
**13.17** `GD-109` — Channel-scoped concurrent Trivia
**13.18** `GD-110` — Forced Trivia stop
**13.19** `GD-111` — Async game-session lifecycle
**13.20** `GD-112` — Fun command layer
**13.21** `GD-113` — Random choice/response utilities
**13.22** `GD-114` — Random media/fact fun
**13.23** `GD-115` — Fun user/media transformations
**13.24** `GD-259` — Per-answer visual variation

## 14. Music / external media

**14.1** `GD-073` — Managed external media/audio node
**14.2** `GD-074` — Automatic media-node runtime installation
**14.3** `GD-075` — Managed-node configuration generation
**14.4** `GD-076` — External-process environment preflight
**14.5** `GD-077` — Runtime-check cache
**14.6** `GD-078` — Managed-node resource control
**14.7** `GD-079` — Readiness by stdout/logs
**14.8** `GD-080` — External-process lifecycle manager
**14.9** `GD-081` — Node plugin diagnostics
**14.10** `GD-082` — Managed/unmanaged backend mode
**14.11** `GD-083` — Reset managed backend settings
**14.12** `GD-200` — External service integrations
**14.13** `GD-205` — Multi-provider stream monitoring
**14.14** `GD-206` — Multiple independent stream alerts
**14.15** `GD-207` — Transition-based live alerts
**14.16** `GD-208` — YouTube stream filtering
**14.17** `GD-209` — Configurable stream mentions
**14.18** `GD-210` — Stream watch action
**14.19** `GD-211` — Stream API quota control
**14.20** `GD-212` — Stream OAuth token refresh
**14.21** `GD-213` — Shared stream credentials migration
**14.22** `GD-214` — Missing-secret owner warning
**14.23** `GD-215` — Resilient stream polling

## 15. Web / dashboard / advanced control plane

**15.1** `GD-202` — Integration dashboard/web interface
**15.2** `GD-260` — Web normalized DTO layer
**15.3** `GD-261` — Privacy-aware public user profile
**15.4** `GD-262` — Public server listing
**15.5** `GD-263` — Web timestamps
**15.6** `GD-264` — Versioned extension gallery
**15.7** `GD-265` — Human-readable extension scopes
**15.8** `GD-266` — Extension web administration
**15.9** `GD-267` — Web dashboard control plane
**15.10** `GD-268` — Web command configuration matrix
**15.11** `GD-269` — Preserve untouched configuration fields
**15.12** `GD-270` — Transactional dashboard save
**15.13** `GD-271` — Dashboard destructive-action endpoint
**15.14** `GD-272` — Dashboard statistics surface
**15.15** `GD-278` — Controller/route/API separation
**15.16** `GD-279` — Route-level feature namespaces
**15.17** `GD-280` — Public content surface isolation
**15.18** `GD-281` — Maintainer operational dashboard
**15.19** `GD-282` — Web server lifecycle isolation
**15.20** `GD-283` — Graceful missing remote entities
**15.21** `GD-284` — Bulk mutual-guild resolution
**15.22** `GD-292` — Persistent REPL / Eval Environment
**15.23** `GD-290` — Multi-source Latency Healthcheck
**15.24** `GD-291` — WebSocket Event-rate Diagnostics
**15.25** `GD-295` — API Diff / Reconciliation Sync
**15.26** `GD-304` — Installation Serverlock
**15.27** `GD-305` — User Reports

## 16. Discord Activities / final large systems

**16.1** `GD-093–111` — game architecture already prepared above
**16.2** `GD-303` — Global Broadcast
**16.3** `GD-304` — Installation Serverlock
**16.4** `GD-307` — Statistics / Analytics
**16.5** Discord Activities canonical system from CorwinDev source (`COR-303`, `COR-336–337`)

## Implementation principle

Внутри каждого этапа порядок сверху вниз — ориентир зависимостей. Если при реализации конкретной системы выясняется новая зависимость, RoadMap корректируется, но канонические IDs не перенумеровываются.

### Current milestone

**Milestone 0 — Foundation:** довести текущую структуру `main.py` / `bot/` / `cogs/`, configuration, extension lifecycle и базовую инфраструктуру до устойчивого состояния.

После этого переходить к storage/data layer, затем к permissions и moderation.
