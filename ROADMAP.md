# InsaneBot RoadMap

План реализации канонического банка `GD-001–307`.

## Правила

- RoadMap строится по зависимостям, а не по номеру `GD`.
- Один `GD` остаётся одной самостоятельной системой; варианты реализации входят в него.
- Сначала строятся фундаментальные сервисы, затем системы, которые от них зависят.
- `GD-001–027` относятся к историческому Batch 1, но исходный файл с названиями отсутствует в текущем tree. Их названия не восстанавливаются догадкой; этот блок нужно восстановить отдельно до финальной привязки.

## 1. Foundation / Core infrastructure

База, без которой остальные системы будут постоянно переделываться.

- `GD-001–027` — **legacy historical block; placement pending source recovery**
- `GD-041` — Economy API
- `GD-071` — Per-server module configuration
- `GD-135` — Moderation service layer
- `GD-194` — Persistent scheduled event instances
- `GD-197` — Recurring events
- `GD-201` — Integration management/configuration
- `GD-203` — Bot API for integrations
- `GD-222` — Automated test CI
- `GD-223` — Separate lint pipeline
- `GD-224` — Code security scanning
- `GD-225` — Reproducible dependency set
- `GD-226` — Automated contribution metadata checks
- `GD-228` — Staged release workflow

## 2. Discord data / server core

Основные сущности и операции Discord.

- `GD-056` — Server counters
- `GD-118` — Member/User validation
- `GD-175` — Server counters extension
- `GD-176` — User activity statistics
- `GD-178` — Server growth statistics
- `GD-180` — Channel activity statistics
- `GD-183` — Personal/server stats cards
- `GD-186` — Voice time statistics
- `GD-258` — Server information card
- `GD-286` — Nickname management
- `GD-287` — Role inspection

## 3. Permissions / access / security foundation

До сложной модерации и web-control-plane.

- `GD-302` — Access Control / Allowlist / Blocklist
- `GD-116` — Hierarchical moderation checks
- `GD-117` — Self/bot targeting protection
- `GD-119` — Discord moderatability checks
- `GD-128` — Required moderation reason
- `GD-137` — Safe default reasons
- `GD-142` — Destructive-action rate limits
- `GD-273` — Discord identity for web authentication
- `GD-274` — Route-level authorization boundaries
- `GD-275` — Web authentication middleware
- `GD-276` — XSS-safe Markdown pipeline
- `GD-277` — Safe external URL fallback

## 4. Scheduler / background lifecycle

- `GD-015` — Background task infrastructure from historical foundation
- `GD-130` — Default tempban duration
- `GD-134` — Timed mute/unmute
- `GD-156` — Ticket follow-up notification
- `GD-194` — Persistent scheduled event instances
- `GD-197` — Recurring events
- `GD-198` — QOTD/daily task events
- `GD-199` — Temporary server events
- `GD-285` — Named persistent server countdowns
- `GD-289` — Scheduled Role with Manual Override

## 5. Moderation

- `GD-120` — Warning system
- `GD-121` — Warning points automation
- `GD-122` — Configurable warn workflow
- `GD-123` — Username/name history
- `GD-124` — Safe rename
- `GD-125` — Anti-repeat message protection
- `GD-126` — Mention spam detection
- `GD-127` — Reinvite after unban
- `GD-129` — Ban message deletion policy
- `GD-131` — Ban DM customization
- `GD-132` — Mute implementation modes
- `GD-133` — Channel-scoped mute
- `GD-138` — Timeout presets
- `GD-139` — UnTimeout validation
- `GD-140` — Mass moderation with partial results
- `GD-141` — Mass moderation input normalization
- `GD-143` — Safe purge
- `GD-144` — Bot-message cleanup
- `GD-145` — Duplicate message cleanup
- `GD-146` — Channel lock/unlock
- `GD-147` — Staff DM
- `GD-148` — Moderation send-message utility

## 6. Modlog / audit

- `GD-060` — Moderation case history
- `GD-136` — Moderation case records
- `GD-216` — Sequential moderation case numbering
- `GD-217` — Moderation case lookup
- `GD-218` — Moderation case editing audit
- `GD-219` — Human-readable case timestamps
- `GD-220` — Configurable case rendering
- `GD-221` — Typed moderation cases
- `GD-179` — Moderation statistics
- `GD-297` — Modlog Suppression Tokens

## 7. Advanced security / incident response

- `GD-084` — Hierarchical content filter
- `GD-085` — Nickname/display-name filtering
- `GD-086` — Rate-based filter enforcement
- `GD-087` — Exact/normalized filter matching
- `GD-088` — Extended filter pipeline
- `GD-089` — Filter enforcement + moderation case
- `GD-090` — Automod immunity
- `GD-091` — Compiled filter-pattern cache
- `GD-092` — Large filter-rule management
- `GD-296` — Emergency Server Lockdown
- `GD-298` — Compromise-response Preset

## 8. Community / roles / social

- `GD-057` — Self-service role panels
- `GD-161` — Self-role toggle
- `GD-162` — Self-role catalog
- `GD-163` — Self-role administration
- `GD-164` — Managed role editing
- `GD-055` — Join-to-create voice channels
- `GD-058` — Birthday system
- `GD-059` — User notes
- `GD-070` — Welcome / goodbye messages
- `GD-169` — Family/social relations
- `GD-170` — AFK status
- `GD-171` — Social interaction
- `GD-172` — Social relationships
- `GD-173` — Social compatibility
- `GD-174` — Social leaderboard
- `GD-288` — Linked Accounts / Alternate Accounts
- `GD-300` — Invite Tracking & Statistics
- `GD-301` — Starboard
- `GD-306` — Social Relations / Interactions

## 9. Utility / customization

- `GD-065` — Custom commands
- `GD-066` — Custom command aliases / shortcuts
- `GD-067` — Keyword / trigger auto-responses
- `GD-068` — Custom response placeholders
- `GD-069` — Custom embeds
- `GD-072` — Randomized custom command responses
- `GD-237` — Dynamic permission-aware help menu
- `GD-238` — Per-channel command cooldown
- `GD-239` — Channel-wide quiet mode
- `GD-240` — Persistent interactive counters
- `GD-241` — Structured message archive export
- `GD-242` — Filtered bulk message cleanup
- `GD-243` — Emoji jumbo renderer
- `GD-244` — Global custom emoji inspector
- `GD-245` — URL redirect safety inspection
- `GD-246` — Fuzzy category resolution
- `GD-247` — Temporary private talk rooms
- `GD-248` — Server to-do list
- `GD-253` — Configurable server prefix
- `GD-254` — RSS feed alias/catalog access
- `GD-256` — Bitly shorten/expand utility
- `GD-293` — Source Links for Commands / Cogs
- `GD-294` — Moderation-only Echo / Embed Relay
- `GD-303` — Global Broadcast

## 10. Tickets / reports / applications

- `GD-149` — Ticket panel
- `GD-150` — One active ticket per user
- `GD-151` — Ticket claim/unclaim
- `GD-152` — Ticket priority
- `GD-153` — Ticket close states
- `GD-154` — Ticket rename
- `GD-155` — Ticket participants management
- `GD-157` — Ticket transcript
- `GD-158` — Custom ticket message
- `GD-159` — Ticket limits
- `GD-160` — Multiple ticket systems
- `GD-188` — Built-in user reports
- `GD-189` — Report server selection
- `GD-190` — Report anti-spam windows
- `GD-191` — Report attachments
- `GD-192` — Report staff communication tunnel
- `GD-193` — Sequential report numbering
- `GD-299` — Applications / Staff Application Workflow

## 11. Progression / statistics

- `GD-165` — Message XP progression
- `GD-166` — Level role rewards
- `GD-167` — Server leveling configuration
- `GD-168` — Progression rank leaderboard
- `GD-177` — Activity leaderboards
- `GD-181` — Activity heatmap
- `GD-182` — Period statistics
- `GD-184` — Game statistics
- `GD-185` — Invite statistics
- `GD-187` — Statistics visualization
- `GD-250` — Weekly guild statistics reset
- `GD-251` — Command-usage statistics
- `GD-252` — Rank-specific leaderboard
- `GD-257` — User points leaderboard surface
- `GD-307` — Statistics / Analytics

## 12. Economy

- `GD-028` — Basic user balance
- `GD-029` — Wallet/bank separation
- `GD-030` — Economy shop/inventory
- `GD-031` — Discord-role shop
- `GD-032` — Periodic monetary rewards
- `GD-033` — Role-based periodic reward
- `GD-034` — Active work income
- `GD-035` — Beg
- `GD-036` — P2P currency transfer
- `GD-037` — Administrative balance management
- `GD-038` — Maximum balance limit
- `GD-039` — Max-balance payout correction
- `GD-040` — Economy leaderboard
- `GD-042` — Paid actions integration
- `GD-043` — Rewards from other systems
- `GD-044` — Risky currency theft
- `GD-045` — Crime / risk-reward
- `GD-046` — Mine
- `GD-047` — Fishing
- `GD-048` — Hunt
- `GD-049` — Gambling / slot machine
- `GD-050` — Global vs server economy mode
- `GD-051` — Currency name configuration
- `GD-052` — Economy reset
- `GD-053` — Inactive economy record cleanup
- `GD-249` — Scaled points lottery

## 13. Games / Trivia / Fun

- `GD-093` — Mini-game catalog
- `GD-094` — Casino game section
- `GD-095` — Independent mini-games
- `GD-096` — Game rankings/statistics
- `GD-097` — Daily game challenges
- `GD-098` — Game economic rewards
- `GD-099` — Mixed trivia pool
- `GD-100` — Custom trivia sets
- `GD-101` — Trivia-set configuration
- `GD-102` — Trivia victory condition
- `GD-103` — Trivia timers
- `GD-104` — Bot participant in Trivia
- `GD-105` — Trivia response UX
- `GD-106` — Trivia answer matching
- `GD-107` — Conditional Trivia reward
- `GD-108` — Persistent Trivia statistics
- `GD-109` — Channel-scoped concurrent Trivia
- `GD-110` — Forced Trivia stop
- `GD-111` — Async game-session lifecycle
- `GD-112` — Fun command layer
- `GD-113` — Random choice/response utilities
- `GD-114` — Random media/fact fun
- `GD-115` — Fun user/media transformations
- `GD-259` — Per-answer visual variation

## 14. Music / external media

- `GD-073` — Managed external media/audio node
- `GD-074` — Automatic media-node runtime installation
- `GD-075` — Managed-node configuration generation
- `GD-076` — External-process environment preflight
- `GD-077` — Runtime-check cache
- `GD-078` — Managed-node resource control
- `GD-079` — Readiness by stdout/logs
- `GD-080` — External-process lifecycle manager
- `GD-081` — Node plugin diagnostics
- `GD-082` — Managed/unmanaged backend mode
- `GD-083` — Reset managed backend settings
- `GD-200` — External service integrations
- `GD-205` — Multi-provider stream monitoring
- `GD-206` — Multiple independent stream alerts
- `GD-207` — Transition-based live alerts
- `GD-208` — YouTube stream filtering
- `GD-209` — Configurable stream mentions
- `GD-210` — Stream watch action
- `GD-211` — Stream API quota control
- `GD-212` — Stream OAuth token refresh
- `GD-213` — Shared stream credentials migration
- `GD-214` — Missing-secret owner warning
- `GD-215` — Resilient stream polling

## 15. Web / dashboard / advanced control plane

- `GD-202` — Integration dashboard/web interface
- `GD-260` — Web normalized DTO layer
- `GD-261` — Privacy-aware public user profile
- `GD-262` — Public server listing
- `GD-263` — Web timestamps
- `GD-264` — Versioned extension gallery
- `GD-265` — Human-readable extension scopes
- `GD-266` — Extension web administration
- `GD-267` — Web dashboard control plane
- `GD-268` — Web command configuration matrix
- `GD-269` — Preserve untouched configuration fields
- `GD-270` — Transactional dashboard save
- `GD-271` — Dashboard destructive-action endpoint
- `GD-272` — Dashboard statistics surface
- `GD-278` — Controller/route/API separation
- `GD-279` — Route-level feature namespaces
- `GD-280` — Public content surface isolation
- `GD-281` — Maintainer operational dashboard
- `GD-282` — Web server lifecycle isolation
- `GD-283` — Graceful missing remote entities
- `GD-284` — Bulk mutual-guild resolution
- `GD-292` — Persistent REPL / Eval Environment
- `GD-290` — Multi-source Latency Healthcheck
- `GD-291` — WebSocket Event-rate Diagnostics
- `GD-295` — API Diff / Reconciliation Sync
- `GD-304` — Installation Serverlock
- `GD-305` — User Reports

## 16. Discord Activities / final large systems

- `GD-093–111` — game architecture already prepared above
- `GD-303` — Global Broadcast
- `GD-304` — Installation Serverlock
- `GD-307` — Statistics / Analytics
- Discord Activities canonical system from CorwinDev source (`COR-303`, `COR-336–337`)

## Implementation principle

Внутри каждого этапа порядок сверху вниз — ориентир зависимостей. Если при реализации конкретной системы выясняется новая зависимость, RoadMap корректируется, но канонические IDs не перенумеровываются.

### Current milestone

**Milestone 0 — Foundation:** довести текущую структуру `main.py` / `bot/` / `cogs/`, configuration, extension lifecycle и базовую инфраструктуру до устойчивого состояния.

После этого переходить к storage/data layer, затем к permissions и moderation.
