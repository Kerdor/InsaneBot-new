# GLOBAL DEDUP V2 — Batch 3

Дата: 2026-09-12

## Scope

Строгий повторный аудит TitanBot-материалов против:
- предыдущего canonicalization `GD-001–287`;
- `GLOBAL_DEDUP_V2_BATCH1`;
- `GLOBAL_DEDUP_V2_BATCH2`;
- других тематических файлов `ideasALL/ideas`.

В этом batch проверены прежде всего:
- `TITAN_CORE.md`
- `TITAN_CONFIG.md`
- `TITAN_APPLICATIONS.md`
- `TITAN_JOINTOCREATE.md`
- `TITAN_GIVEAWAY.md`
- `TITAN_REACTION_ROLES.md` (включая доступную часть большого файла)

Правило: source IDs не удаляются; объединение означает только привязку механики к общей системе/кластеру. Уникальные ограничения, recovery, UX и архитектурные варианты сохраняются.

---

## 1. Titan Core / lifecycle

### TITAN-K001
Явная startup-последовательность DB → web → commands → handlers → music → Discord login → slash registration.

**Решение:** не отдельная пользовательская система. Это вариант **startup orchestration**. Связать с существующими startup/dependency-preflight материалами из V2 Batch 1 (`PDIS-B001`, `PDIS-CU034/035`) и старым `ARCH-012/015`, но сохранить порядок Titan как source-specific lifecycle policy.

### TITAN-K002
Fallback PostgreSQL → in-memory degraded mode.

**Решение:** новый кандидат в общий **storage degradation / graceful degradation** кластер. Не сливать с обычным DB backend abstraction (`DATA-006`): здесь важен runtime fallback с явным non-persistent mode.

### TITAN-K003–K005
`/health` и `/ready`, readiness 503, metrics: uptime/guild count/command count/DB mode/schema.

**Решение:** объединить в общий **health/readiness/diagnostics** кластер с `PDIS-A007` (multi-source latency healthcheck), `PDIS-A011` (normalized event metrics) и runtime diagnostics. Не объединять music-specific stats с generic healthcheck: music может быть отдельным provider внутри общей health model.

### TITAN-K006–K008
Configurable web host/port, automatic port fallback, IP sliding-window rate limit, CORS modes.

**Решение:** web control-plane infrastructure. Port fallback и CORS — детали deployment/web subsystem, не отдельные user-facing systems. IP rate limit — отдельный reusable API security policy.

### TITAN-K009–K011
Central graceful shutdown; fatal uncaught exception shutdown; ignore known recoverable Discord interaction errors.

**Решение:** объединить с **centralized error + lifecycle shutdown**. Связать с `PDIS-B006/007` и `ARCH-025`; recoverable Discord errors сохранить как специальную policy.

### TITAN-K012–K013
Independent schedulers for birthdays/giveaways/counters; orphan-record cleanup.

**Решение:** общая **scheduler/maintenance infrastructure**, но не объединять сами birthday/giveaway/counter systems. Orphan cleanup — reusable maintenance/reconciliation mechanic.

### TITAN-K014–K020
Recursive command loader, filesystem metadata, duplicate suppression, deep command validation, slash limit warning/truncation, global command cleanup, ESM cache-busting hot reload.

**Решение:** объединить с **cog/command lifecycle** (`CORE-005/006/007/009/010/011`, `COG-001–024`, `PDIS-A006`).

Важно сохранить отдельные детали:
- recursive discovery;
- metadata category/filePath;
- duplicate command-name suppression;
- Discord slash payload validation;
- limit-aware registration;
- cache-busting reload.

Это не один «load cog» механический пункт, а lifecycle subsystem с несколькими фазами.

### TITAN-K021–K025
Birthday slash command/subcommands, option bounds, stale-member cleanup, optional announcement channel, relative `Today/Tomorrow/In N days`.

**Решение:** объединить с существующим **birthday system** (`GD-058`, `COMM-007`, `EVENT-008–012`). Не создавать отдельную систему. Сохранить Titan-specific option validation, stale-record cleanup и relative-state UX как variants/details.

---

## 2. Titan Config / configuration architecture

### TITAN-G001–G019
Server configuration dashboard, select-based setting navigation, setup wizard in DM, ephemeral notice, closed-DM recovery instructions, one active wizard per user, per-question parser/validator, skip/cancel, immediate persistence, live dashboard refresh, 3-minute timeout, mention/raw-ID input, explicit `none`, prefix validation, cross-links to other configuration surfaces, inactivity timeout, resolved mentions, centralized theme summary.

**Решение:** это не набор отдельных systems. Объединить в общий **configuration dashboard + interactive setup wizard** кластер с:
- `GD-071` scoped server configuration;
- `PDIS-A002` scheduled role/manual override только как пример configurable workflow, не как часть dashboard;
- `PDIS-B001` startup/config reconciliation;
- общими persistent interactive UI паттернами (`PDIS-018`, `PDIS-A003–005` help UI — только UX pattern).

Сохранить как отдельные механики:
- DM-based wizard;
- immediate write after each validated answer;
- skip vs cancel semantics;
- closed-DM recovery;
- single-session lock;
- explicit nullable `none`;
- dashboard refresh;
- inactivity timeout.

### TITAN-G020–G038
Presence object, multiple activities, owners from env, global cooldown, slash registration flag, test guild config, maintenance mode, prefix+slash coexistence, env aliases, env-based IDs, environment flags, centralized runtime paths/config object, config freeze.

**Решение:** **runtime configuration architecture**, не пользовательские systems. Merge with `CONFIG-002/003`, `DATA-007`, `ARCH-006`, `QUALITY_AND_RELEASE` material where applicable. `maintenance mode` additionally belongs to permission/availability policy and must remain explicit.

### TITAN-G039–G047
Central semantic embed palette, feature-domain colors, priority color maps, centralized footer/author/thumbnail defaults.

**Решение:** общий **presentation/theme system**. Не размазывать по каждой feature. `ticket priority colors + emoji + labels` остаются ticket-specific configuration variant.

### TITAN-G048–G055
Application questions/config, default questions, status colors, cooldown, retention, manager roles.

**Решение:** объединить с Titan Application system, не с generic configuration. Retention policy и role manager policy сохранить как application lifecycle details.

### TITAN-G056–G086
Currency config, starting balance, bank capacity/upgrades, payout ranges, cooldown maps, rob probability/jail, shop categories/items/rarity/emojis, quantity/refund/restock/sales, dynamic pricing, premium role pricing, bulk discounts, max quantity/level, durability, declarative effects.

**Решение:** почти целиком уже покрыто **economy/shop cluster** из V2 Batch 2 (`ECON-*`, `GD-028–053`). Не создавать новые systems только из-за config granularity.

Сохранить как details:
- bank capacity vs upgrades;
- independent payout ranges;
- risk probability/jail duration;
- item category model;
- refund window/fee;
- restock/sales scheduling;
- premium-role pricing;
- bulk discount;
- maxQuantity/maxLevel;
- durability/null durability;
- declarative item effects;
- consumable uses.

### TITAN-G087–G093
Ticket defaults, giveaway limits, hosting policies, birthday role/channel/timezone.

**Решение:** feature-specific configuration attached to **ticket/giveaway/birthday systems**, not standalone systems.

### TITAN-G094–G107
Verification panel/config, criteria modes, account-age/server-size thresholds, DM notification, attempt cooldown/window, bounded in-memory maps and cleanup.

**Решение:** общий **verification/anti-abuse lifecycle** cluster. Account-age threshold connects conceptually to `PDIS-M2-001/002`, but verification is not the same as DEFCON moderation. Preserve the distinction.

---

## 3. Titan Applications

### TITAN-A001–A003
Autocomplete application selection, modal answers, application → role mapping, per-role questions with global defaults.

**Решение:** один **role application system**. Do not merge into generic ticket/forms. Modal + role-targeted application is a distinct workflow.

### TITAN-A004–A007
One pending application per user, Application ID, status lookup/list (last 10), status text + emoji.

**Решение:** same application lifecycle. These are state/UX mechanics, not separate systems.

### TITAN-A008–A013
Staff review embed, Approve/Deny buttons, reason modal, reviewer-bound collector, role assignment on approval, DM result, persistent log message edited after review.

**Решение:** one application review workflow. Keep reviewer binding, timeout/max-one, DM failure tolerance, and edit-in-place log as implementation/recovery details.

### TITAN-A014–A020
Staff filtering by status/role/user, manager permission checks, interactive setup, auto-enable, duplicate role prevention, dashboard handoff, configurable log/manager/questions/retention.

**Решение:** same application management/config system.

### TITAN-A021–A025
Persistent answers/metadata, explicit disabled error, dynamic customId carrying role ID, runtime validation of role/config, setup modal timeout/filter.

**Решение:** same system. Dynamic customId/context restoration and runtime revalidation should be preserved as interaction-safety details.

**Cross-source note:** this is a potentially important **new canonical candidate** if no prior source contains a true staff application workflow. Do not collapse it into tickets merely because both have forms and staff review.

---

## 4. Titan Join-to-Create

### TJ-001–TJ-006
Voice trigger creates temporary channel, moves user, guild-scoped config, one trigger per guild, optional category/root-level mode.

**Решение:** merge into existing **GD-055 Join-to-Create**. Preserve one-trigger-per-guild and category/root-level variants.

### TJ-007–TJ-023
Template-based names, username/display name/tag/guild/source-channel placeholders, aliases, Unicode normalization, invisible/control character removal, dangerous-character blocking, unknown-placeholder rejection, length limits, value truncation, final sanitization, whitespace compression, fallback name.

**Решение:** same JTC system, but this is a substantial **safe-name generation subsystem**. Do not reduce it to “custom channel name”. Preserve all sanitization/normalization constraints as JTC-specific UX/security details.

### TJ-024–TJ-030
User limit, unlimited `0`, 0–99 validation, bitrate, 8–384 range, runtime clamp, default 64.

**Решение:** JTC channel creation configuration.

### TJ-031–TJ-044
Per-trigger options, dashboard/buttons/select/modal, initiator-bound controls, permission recheck, timeout, destructive confirmation, config cleanup, stale-trigger cleanup, duplicate setup prevention.

**Решение:** JTC configuration dashboard + lifecycle. Reuse general interactive dashboard patterns but retain JTC-specific rules.

### TJ-045–TJ-064
Voice-state join/leave/move handling, bot ignore, old-channel cleanup, empty-channel delete, ownership, ownership transfer/rename/persistence, re-entry to existing room, race/state checks, creation cooldown, cooldown cleanup/cap, permission preflight, cooldown reset on failure, DM errors.

**Решение:** core JTC lifecycle. This is not duplicate content just because similar cooldown/cleanup helpers exist elsewhere; the semantics are JTC-specific.

### TJ-065–TJ-080
Persistent temporary registration, DB-first cleanup, missing-record handling, read-only helpers, audit logging, enabled state, createdAt, setup summary, multiple UI configuration methods, migration/fallback config, DB safety, per-field validation, permission overwrites/category inheritance.

**Решение:** same JTC platform. Preserve DB-first cleanup, audit non-fatality, migration behavior, and permission overwrite policy.

---

## 5. Titan Giveaway

### TG-001–TG-018
Duration parser/limits, winner limits, prize validation, guild-only, deferred response, state fields/message IDs/host/entries/end flags.

**Решение:** merge into existing **GD-054 Giveaway** / `COMM-001–003 + EVENT-001–007`. These are implementation details and validation rules of the same giveaway system.

### TG-019–TG-031
Active/ended embeds, relative timestamp, Join/End/Reroll/View Winners buttons, unique entries, random selection, participant shortage handling, per-user/per-giveaway interaction cooldown.

**Решение:** same giveaway system. Keep state-specific UI and interaction rate limit as details.

### TG-032–TG-046
Message-first persistence, partial failure tolerance, expiry scheduler, per-giveaway error isolation, restart recovery via IDs, orphan skipping, automatic winner selection, winner announcement, empty-winner message, winner announcement ID, manual-end audit.

**Решение:** same giveaway system + **generic scheduler/recovery patterns**. Do not merge the giveaway state machine into generic scheduler; scheduler is infrastructure, giveaway is domain logic.

### TG-047–TG-065
Delete by message ID with fallbacks, DB verification, ended-only reroll, participant sufficiency, reroll audit, edit-in-place messages, fallbacks for missing Discord objects, audit events, contextual error objects.

**Решение:** same giveaway system. Error context joins centralized error architecture (`PDIS-B006/007`), but giveaway-specific fields remain domain metadata.

---

## 6. Titan Reaction Roles

### TRR-001–TRR-018
Dedicated management command/dashboard, Administrator access, target channel/title/description, initial 5-role options, ManageRoles/SendMessages preflight, panel count limit, duplicate/hierarchy/dangerous/managed/everyone role checks, partial-validity handling.

**Решение:** merge into existing **self-service role panel** cluster (`GD-057`, `ROLE-001`, `PDIS-001/002`). Important distinction: Titan provides a **configuration/admin panel around the self-service role system**, while PDIS provides persistent role-panel recovery. These are complementary, not duplicate.

### TRR-019–TRR-034
Embed panel, String Select Menu, zero-selection remove semantics, dynamic max values, emoji/options limits, safe truncation, persistent metadata, rollback orphan message, audit logging.

**Решение:** same self-service role panel. Preserve rollback and metadata/audit mechanics.

### TRR-035–TRR-047
Dashboard discovery/autocomplete, cache-only autocomplete, ephemeral dashboard, panel status, live message link, inactivity timeout.

**Решение:** merge with **persistent interactive UI + panel status/recovery** (`PDIS-018` and PDIS self-service role cluster). `panel status` is reusable infrastructure and may later be shared with ticket/verification panels.

### TRR-048–TRR-082
Add/remove roles, runtime 25-role limit, live rebuild, deleted-role filtering, last-role auto-delete, explicit delete confirmation, independent DB cleanup, audit.

**Решение:** same self-service role panel lifecycle. Keep initial-setup 5 vs runtime 25 as a source-specific distinction.

### TRR-083–TRR-110
Edit panel text, ownership-bound modal, timeouts, missing-message state, repost/recovery, message-ID migration, limited channel scan, panel status states.

**Решение:** strong reusable **persistent panel recovery/repost** subsystem. Merge conceptually with `PDIS-002` and `PDIS-018`, but retain source-specific recovery algorithm: bot-author + customId identification, scan window 50, canonical message-ID migration.

### TRR-111–TRR-129
Generic panel-status helper, guild-only interaction, stale metadata handling, repeated permission/hierarchy/danger checks at execution time, per-role skipped/added/removed result, partial failure isolation.

**Решение:** split logically:
- generic panel-status/recovery → reusable UI infrastructure;
- self-service role execution → GD-057/ROLE-001 cluster;
- per-role partial failure result → reusable batch-action result pattern.

Do not create separate systems for each validation.

---

## 7. Cross-check against V2 Batch 1–2

No evidence in this pass that requires deleting an existing useful canonical/source idea.

Important confirmed merges:
- Titan JTC → existing JTC cluster (`GD-055`).
- Titan Giveaway → existing giveaway cluster (`GD-054`).
- Titan Birthday → existing birthday cluster (`GD-058`).
- Titan Economy/Shop → existing economy/shop clusters (`GD-028–053`, `ECON-*`).
- Titan Reaction Roles → existing self-service role panel cluster (`GD-057`, `ROLE-001`, `PDIS-001/002`).
- Titan Ticket config → existing ticket platform (`GD-061–064` + `TICKET-*`).
- Titan configuration dashboard → scoped configuration architecture (`GD-071`) plus reusable interactive UI patterns.
- Titan command loader → cog/command lifecycle cluster (`CORE-*`, `COG-*`, `PDIS-A006`).

Potential genuinely new canonical candidates from this Titan pass:
1. **Role application workflow** — user application → modal → staff review → approve/deny → role assignment → retention/audit.
2. **Storage degraded-mode fallback** — persistent DB unavailable → bounded in-memory runtime mode with explicit degraded state.
3. **Reusable panel status/recovery service** — persisted panel metadata + live Discord message discovery/repost/message-ID migration.
4. **Health/readiness endpoint model** — generic liveness/readiness separation with dependency state and machine-readable metrics.

These are candidates, not final GD IDs. They require cross-source confirmation before final canonicalization.

---

## 8. Safety / no-loss rule for later merge

When converting these findings into final canonical systems:
- keep every Titan source ID as provenance;
- do not flatten JTC sanitization/race/ownership details into a generic temporary-channel bullet;
- do not flatten giveaway recovery/reroll/delete fallbacks into a generic giveaway bullet;
- do not flatten reaction-role recovery/repost into ordinary role assignment;
- do not merge applications into tickets solely because both use forms/modals;
- do not treat configuration fields as separate systems when they only configure an existing domain;
- do not delete source-specific files.
