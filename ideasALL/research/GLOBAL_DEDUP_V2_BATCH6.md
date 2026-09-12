# GLOBAL DEDUP V2 — Batch 6

## Scope

Strict global re-audit of TitanBot service-layer mechanics against:
- previous canonical `GD-001–287`;
- `GLOBAL_DEDUP_V2_BATCH1–5`;
- thematic source files already audited.

Source: `codebymitch/TitanBot`.

## Main conclusion

`TITAN_SERVICES.md` contains overwhelmingly implementation/service-layer details of systems that already exist in the global catalog. Creating one system per `TSVC-*` would massively over-split the catalog and violate the rule that a system is a coherent user-facing/backend capability rather than an individual helper, validator or error type.

No new standalone user-facing system is created from TSVC-001–190.

All source IDs remain preserved in the source file and are mapped below by domain.

## 1. Cross-cutting service architecture

### TSVC-001–010
**Merge target:** global architecture / service layer / background reconciliation infrastructure.

These describe:
- separation of business logic from command/event UI;
- typed service-error boundary;
- contextual error information;
- safe suppression of expected background errors;
- structured negative results;
- reconciliation summaries;
- independent guild processing.

**Decision:** not standalone systems. Preserve as implementation architecture attached to the relevant domains and to the future common service layer.

## 2. Applications

### TSVC-011–026
**Merge target:** Titan Applications candidate identified in V2 Batch 3.

These are validation, persistence and review invariants for the existing Applications system:
- question/answer sanitization and length limits;
- required guild/user/role checks;
- one pending application per user;
- review state transition protection;
- approve/deny constraints;
- manager permissions;
- configuration validation;
- application retrieval and database error handling.

**Decision:** do not create additional systems. Attach to the Applications system and preserve as service-layer constraints.

## 3. Birthday

### TSVC-027–041
**Merge target:** existing Birthday system `GD-058`.

Preserve calendar correctness, leap-year handling, sorting/upcoming calculation, limits, missing-record behavior, birthday-role tracking, optional role behavior, and per-member/per-guild error isolation.

**Decision:** no new system.

## 4. Command access

### TSVC-042–053
**Merge target:** existing command-access/permission-control clusters from V2 Batch 1 and existing access-control ideas.

Important details to preserve:
- registry derived from actual commands;
- nested subcommand awareness;
- protected commands;
- parent/subcommand disable semantics;
- category-level toggles;
- reset behavior;
- normalized legacy config.

**Decision:** not a new user-facing system; implementation detail of centralized command access control.

## 5. Guild configuration

### TSVC-054–083
**Merge target:** `GD-071` per-server/scoped configuration + common configuration infrastructure.

Preserve:
- one canonical config service;
- defaults normalization;
- partial/deep patch semantics;
- array replacement rather than accidental merge;
- schema validation;
- protected keys;
- channel/role existence and type validation;
- role hierarchy validation;
- string/number bounds;
- legacy migration;
- old/new value reporting;
- conflict detection;
- bulk validation and result summaries;
- bounded configuration history;
- reset markers;
- human-readable config summaries and `Missing` state;
- centralized permission requirements.

**Decision:** these are configuration infrastructure/details, not dozens of independent systems.

## 6. Counting

### TSVC-084–096
**Merge target:** existing server counting system / counting cluster.

Preserve:
- state normalization;
- safe fallback to decimal;
- guild-specific storage;
- reset semantics where best streak survives;
- atomic state updates;
- Roman/Alphabet case-insensitive input;
- math expression/equality support;
- top-10 leaderboard;
- missing-member fallback;
- degraded read behavior.

**Decision:** no new standalone system.

## 7. Economy service

### TSVC-097–112
**Merge target:** existing economy systems `GD-028–053` and Economy V2 clusters.

Preserve:
- safe integer/non-negative balance validation;
- positive integer amounts and MAX_SAFE_INTEGER bound;
- transfer self-check and insufficient-funds check;
- rollback on partial persistence failure;
- explicit inconsistency logging if rollback fails;
- transaction logs with before/after/delta/source/reason;
- next-available information for daily/cooldowns;
- bank capacity checks;
- safe withdraw behavior;
- reusable cooldown checker;
- service API for external money changes.

**Decision:** no new economy systems.

## 8. Giveaway service

### TSVC-113–125
**Merge target:** existing `GD-054` Giveaway.

Preserve duration/prize/winner bounds, participant deduplication, automatic winner-count reduction, user+giveaway rate limiting, DB/Discord existence checks, per-giveaway failure isolation, persisted end state, embed/button update, public winner announcement and audit isolation.

**Decision:** no new system.

## 9. JoinToCreate service

### TSVC-126–142
**Merge target:** existing `GD-055` JTC.

Preserve all detailed sanitization and lifecycle behavior:
- Unicode NFKC normalization;
- control/invisible-character removal;
- unknown-placeholder rejection;
- forbidden-character checks;
- separate placeholder sanitization and limits;
- second sanitization pass after substitution;
- safe fallback names;
- bitrate validation;
- `0 = unlimited` user limit;
- one trigger channel constraint;
- per-trigger overrides;
- timestamps;
- cleanup of dependent state;
- safe false result on read failure;
- isolated logging failures.

**Decision:** no new system. These are important JTC implementation constraints and must not be lost during future consolidation.

## 10. Verification service

### TSVC-143–156
**Merge target:** existing Verification system / verification cluster.

Preserve:
- per guild:user cooldown;
- separate sliding-window attempt limit;
- independent attempt-window configuration;
- periodic bounded tracker cleanup;
- oldest-entry eviction;
- separate auto-verify role;
- account-age and server-size criteria;
- no-criteria mode;
- machine-readable rejection reasons;
- typed/internal errors with safe external result;
- optional DM notification;
- runtime role/channel/permission validation.

**Decision:** no new standalone system.

## 11. Panel health/reconciliation

### TSVC-161–169
**Merge target:** common persistent-panel/reconciliation infrastructure plus the relevant systems (tickets, verification, reaction roles, etc.).

Preserve:
- panel health checks;
- recovery of missing message IDs;
- reaction-role storage-key migration;
- reconciliation counters;
- manual repost/recovery for deleted panels;
- per-panel/per-guild isolation;
- level-role synchronization/reconciliation;
- cleanup of missing roles.

**Decision:** reusable infrastructure, not separate user-facing systems. Where a panel belongs to a domain, retain the behavior under that domain as well.

## 12. Cross-service resilience

### TSVC-170–190
**Merge target:** common architecture/quality/data-storage infrastructure.

Preserve the previously identified mechanics:
- continue/summary behavior for reconciliation jobs;
- machine-readable failure reasons;
- Discord entity existence checks;
- cache/API fallback;
- legacy storage normalization;
- audit isolation;
- bounded in-memory state;
- validation below command layer;
- reusable service APIs;
- level-role reconciliation and missing-role cleanup.

**Decision:** implementation/architecture details, not standalone systems.

## 13. Cross-check against Tickets and Economy Batch 5

`TITAN_SERVICES` confirms the Batch 5 conclusion rather than creating duplicate canonical systems:

- Ticket service details belong to the existing Ticket Platform; no new ticket system is created.
- Economy service details belong to the existing Economy domain; no duplicate balance/transfer/bank/cooldown systems are created.
- Service-layer validation is not counted as a separate system when it merely enforces an existing domain's rules.

## 14. New standalone systems in this batch

**0 confirmed.**

This is intentional. The purpose of this pass is to prevent implementation-level service mechanics from inflating the global system count.

## 15. Preservation rule

Do not delete `TITAN_SERVICES.md` or collapse its IDs into a short summary. The source file remains the evidence layer. Future canonical entries should reference these IDs where useful so that no validation, recovery, resilience, or failure-handling behavior is lost.

## Status

Titan service-layer pass: **audited / deduplicated**.

RoadMap remains postponed until the complete V2 all-files re-audit is finished.
