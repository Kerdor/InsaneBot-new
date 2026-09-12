# Global Dedup V2 — Batch 11

Дата: 2026-09-12

## Цель

Очередной проход по файлам, которые не были явно зафиксированы в V2 Batch 1–10. Проверка выполняется относительно уже существующего `GD-001–287` и всех решений `GLOBAL_DEDUP_V2_BATCH1–10`.

Правило: не создавать отдельную систему для отдельной команды/механики, если она является частью уже существующего домена. Все source IDs и детали сохраняются в исходных файлах.

## Проверенные файлы

- `GAWESOME_COMMANDS_PM.md`
- `GAWESOME_COMMANDS_PRIVATE.md`
- `GAWESOME_COMMANDS_SHARED.md`
- `GAWESOME_CONFIG.md`
- `GENERAL_UX.md`
- `HELP_UX.md`
- `PERMISSIONS.md`
- `PROGRESSION.md`
- `REPORTS.md`
- `SOCIAL.md`
- `STATS.md`
- `UTILITY.md`
- `MUSIC_CONTEXT.md`
- `MUSIC_DEPLOY.md`
- `MUSIC_EVENTS.md`
- `MUSIC_STORAGE.md`
- `MUSIC_WEB.md`

---

## 1. GAwesomeBot PM / Private / Shared / Config

### `GAWESOME_COMMANDS_PM.md`

**Итог: 0 новых standalone-систем.**

Основные блоки уже представлены в старой канонизации GAwesome PM/Private (`GD-230–259`) и в V2-кластерах:

- AFK → существующий AFK/social user-status кластер.
- Personal profile setup → существующий профиль/user-customization кластер; интерактивный DM wizard, privacy, background URL, Bio, timeout и atomic application изменений сохраняются как детали.
- Personal reminders → не смешивать с server countdown (`GD-285`): это персональные reminders. В исходном GAwesome PM это уже часть старого PM-кластера; не создавать второй дубль.
- Personal server aliases → часть пользовательского server-resolution/remote-DM механизма; сохраняются alias overwrite, ambiguity handling, stale guild handling и personal scope.
- Remote server commands from DM → один private/remote relay механизм; `say`, `poll`, `giveaway` — разные операции поверх одного relay, не три системы.
- DM giveaway control → механики существующего Giveaway (`GD-054`), а не отдельный giveaway system.
- PM help → Help/command-discovery слой; не отдельная система.

Особенно сохраняются: per-step timeout, progress-message edit вместо DM-spam, membership gate, server alias resolution, target-channel resolution, permission checks, maintainer bypass, secret giveaway semantics и DM confirmation flows.

### `GAWESOME_COMMANDS_PRIVATE.md`

**Итог: 0 новых standalone-систем.**

- `GAB-PR-001–007` → общий remote/private relay + server/channel resolution + authorization preconditions.
- `GAB-PR-008–012` → remote `say` как механика relay.
- `GAB-PR-013–026` → Poll, включая revoke/re-vote, anonymous DM voting, pagination и validation.
- `GAB-PR-027–040` → Giveaway (`GD-054`) и command-specific authorization details.
- `GAB-PR-041–048` → общий async/progress/correlation/error/state-update infrastructure.

Не объединять Poll и Giveaway в один user-facing system: они остаются отдельными системами внутри общего remote relay infrastructure.

### `GAWESOME_COMMANDS_SHARED.md`

**Итог: 0 новых standalone-систем.**

- Debug diagnostics → существующий health/diagnostics/observability domain; сохраняются process/client/master/OS/DB/version sections, IPC, fallback и комбинируемые flags.
- Eval → существующий developer REPL/eval tooling; сохраняются safe/unsafe режимы, secret censoring, structured inspect, execution timing и gist fallback.
- Reload → существующий Cog/Extension Management (`COG-*`, `PDIS-A006`), с дополнительными namespace/event/module reload details.
- Shared namespace/command contract → framework architecture, не standalone user system.

### `GAWESOME_CONFIG.md`

**Итог: 0 новых standalone-систем.**

Command registry, metadata, help categories, global runtime config, maintainer levels, event routing, static dictionaries, rank/trivia/filter content и encryption configuration относятся к существующим configuration/framework/permission/observability доменам.

Важно сохранить:
- executable command metadata;
- named permission capabilities;
- глобальные user/guild/activity blocklists;
- declarative event routing с несколькими handlers;
- внешние static content dictionaries;
- отдельные encryption password/IV и предупреждение о последствиях их изменения.

---

## 2. General UX / Help / Permissions

### `GENERAL_UX.md`

**Итог: 0 новых standalone-систем.**

Stopwatch — отдельная мелкая personal utility mechanic, но не требует отдельного домена в текущем дедупе. Flip/social interactions относятся к Fun/Social. Humanized numbers, detailed mode, relative timestamps и server-info enrichment — UX/details существующих information systems.

### `HELP_UX.md`

**Итог: 0 новых standalone-систем.**

Весь файл — один Help / Command Discovery domain. `HELP-001–015` объединяются с существующим help/navigation/discovery кластером. Сохраняются заменяемый formatter, HelpSettings, разные navigation adapters, permission-aware filtering, hidden/unavailable commands, nested signatures, alias truncation, pagination, DM checkmark, timeout/delete delay и различение unknown command/subcommand.

### `PERMISSIONS.md`

**Итог: не отдельная система; объединить с Access Control.**

`PERM-001–010` расширяют ранее выделенный **Access Control / Allowlist / Blocklist** домен из Batch 8.

Сохраняются как его mechanics:
- command/cog allow/deny rules;
- user/role/channel/object scope;
- глобальные и server ACL;
- deterministic precedence;
- default allow/deny/clear;
- permission simulation/diagnostics;
- YAML export/import;
- replace vs partial patch;
- owner lockout protection;
- правила для ещё не загруженных cog/command.

Это не отдельный `Command Permissions` system: хранение и применение access policies логически относятся к единому Access Control domain, а глобальные guards остаются инфраструктурным механизмом проверки.

---

## 3. Progression / Reports / Social / Stats / Utility

### `PROGRESSION.md`

**Итог: 0 новых standalone-систем.**

`PROG-001–005` → существующий Leveling / XP / progression domain. XP, levels, level roles, guild configuration и leaderboard остаются mechanics одного домена.

### `REPORTS.md`

**Итог: NEW standalone candidate — Reports / User Reports.**

Не объединять с Tickets: report не требует ticket channel и имеет собственный lifecycle/numbering.

Состав системы:
- report submission from guild или DM;
- server selection через DM;
- multi-window anti-spam;
- attachments;
- persistent sequential report numbering per guild;
- staff ↔ author DM communication tunnel;
- tunnel close/reopen state and attachment relay.

Связь с Tickets допустима на уровне общего обращений/communication infrastructure, но user-facing lifecycle и storage модели различаются.

### `SOCIAL.md`

**Итог: NEW standalone candidate — Social Relations / Social Interactions.**

Объединить `SOCIAL-001–003` (family/kinship) и `SOCIAL-008–015` (friendship, romance, compatibility, requests, relationship list, social rankings) в один Social Relations domain.

`SOCIAL-004–007` (AFK) не дублировать: это существующий AFK user-status cluster.

Сохраняются отдельные mechanics family/kinship, friendship, relationship types, requests accept/deny, compatibility score и leaderboards.

### `STATS.md`

**Итог: NEW standalone candidate — Statistics / Analytics.**

Не смешивать с `GD-056` Counters: counters — отдельная real-time presentation mechanic, а Statistics/Analytics хранит/агрегирует исторические показатели.

Состав candidate:
- text/voice activity;
- activity leaderboards;
- XP/economy/moderation/game/invite statistics;
- member growth;
- channel statistics;
- hourly heatmaps;
- period-based reports;
- personal/server statistics;
- visualization/charts.

`STAT-001–005` counters остаются в существующем Counters domain; `STAT-006–025` относятся к Statistics/Analytics.

### `UTILITY.md`

**Итог: 0 новых standalone-систем.**

- `UTIL-001–002` → существующие pagination/time utility infrastructure.
- `UTIL-003–004` → FAQ/help/resource information mechanics.
- `UTIL-005` → information utility.
- `UTIL-006–007` → существующий server backup/restore + scheduler infrastructure; не создавать отдельный backup system только из-за auto-backup.
- `UTIL-008` → Reaction Roles (`GD-057` + ROLE-001 cluster).
- `UTIL-009–010` → existing keyword/custom-response + placeholder mechanics.

---

## 4. Music remaining thematic files

### `MUSIC_CONTEXT.md`

**Итог: 0 новых standalone-систем.**

`MUSIC-X001–007` → существующий Music interactive/player command domain. Context Menu Play — дополнительный command adapter над тем же audio pipeline, не отдельный Music system.

### `MUSIC_DEPLOY.md`

**Итог: 0 новых standalone-систем.**

Docker/Heroku/Replit/Compose/Lavalink/Prometheus/logging details — deployment/audio infrastructure. Сохраняются self-hosted Lavalink, separate bot/node services, internal network, read-only config mounts, buffer/quality/stuck-track settings и metrics/logging controls.

### `MUSIC_EVENTS.md`

**Итог: 0 новых standalone-систем.**

JOIN/LEAVE/MOVE normalization, autoPause, autoLeave, 24/7, server mute recovery и voice payload handling относятся к существующему Music player lifecycle. Mention-help и message-delete synchronization относятся к общему bot UX/event infrastructure.

### `MUSIC_STORAGE.md`

**Итог: 0 новых standalone-систем.**

Named JSON DB registry, write/delete queues, guild lazy DB, config fallback, Lavalink selection и voice channel resolver — storage/runtime infrastructure. Не превращать music storage implementation в отдельный user-facing system.

### `MUSIC_WEB.md`

**Итог: 0 новых standalone-систем.**

Express/Next dashboard, Discord OAuth, sessions, public data API, protected dashboard API, server list, stats cards и typed frontend helpers → существующий Dashboard/Web Control Plane + Integration/API domain.

---

## Batch 11 — результат

### Новые standalone candidates

1. **Reports / User Reports** — `REPORT-001–007`.
2. **Social Relations / Social Interactions** — `SOCIAL-001–003`, `SOCIAL-008–015`.
3. **Statistics / Analytics** — `STAT-006–025`.

### Объединено с существующими доменами

- `PERM-001–010` → Access Control.
- `SOCIAL-004–007` → AFK.
- `STAT-001–005` → Counters.
- GAwesome PM/Private → existing PM/Private/remote relay + existing Giveaway/Poll/Profile/AFK/reminder clusters.
- GAwesome Shared → diagnostics/eval/cog management/framework.
- Music thematic files → existing Music/Audio/Deployment/Web/Storage domains.
- Progression → existing Leveling/XP domain.
- Utility → existing utility/infrastructure and existing user-facing systems.

### Защита от потери деталей

Исходные файлы не изменялись и не удалялись. Source IDs сохранены. В объединённых доменах не схлопывались UX-варианты, timeout/recovery semantics, permission boundaries, storage behavior, scheduler behavior, fallback paths и архитектурные варианты.

### RoadMap

**Не открывать.** После Batch 11 требуется продолжить V2-аудит оставшихся idea-файлов, прежде чем считать глобальный дедуп завершённым.
