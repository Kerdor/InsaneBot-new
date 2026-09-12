# GLOBAL DEDUP V2 — BATCH 2

Повторная сверка тематических банков и второй слой source-specific материалов.

## 1. Moderation 4–5

### PDIS-M4-001 → Advanced moderation / Clean Ban
Комбинированный ban + cleanup не является отдельной системой ban. Это workflow, объединяющий существующие moderation actions.

**Решение:** объединить с ban/cleanup infrastructure; сохранить возможность прикрепить cleanup log к уже созданной infraction без второй записи.

### PDIS-M4-002 — Compromise-response preset
**NEW candidate.** Это готовый incident-response preset для скомпрометированного аккаунта: наказание + объяснение + security instructions + appeal path.

### PDIS-M4-003 → Infraction lifecycle
Shadow/hidden infractions должны быть вариантом обычной infraction с `notify_user=false`, а не отдельной системой.

### PDIS-M4-004–008 → Infraction management
`last/recent`, regex search, actor search, sorting и compact state markers — детали одного infraction-management интерфейса.

**Решение:** объединить в infraction history/search UX, не теряя ни одну возможность.

### PDIS-M4-009–011 → Nickname enforcement
Deterministic forced nickname + active enforcement + повторное применение после rejoin + отдельные user/modlog reasons — один specialized moderation workflow.

**Решение:** объединить как `Nickname Enforcement Infraction`; не смешивать с обычным nickname edit.

### PDIS-M5-001–004 → Watch relay aggregation
Delayed batching + user/channel queue + context header + configurable messages-per-header — одна watch relay pipeline.

### PDIS-M5-005–007 → Secure message relay
Secret-token redaction, URL embed suppression и attachment fallback — общая relay safety layer.

**Решение:** объединить с message relay infrastructure, но сохранить каждую защиту как отдельную policy.

### PDIS-M5-008–011 → Watch cache/history
Cache stale fallback, explicit fresh/cache mode, previous watch incidents и departed-user history — один watch management cluster.

### PDIS-M5-012 → Generic unload-safe background queue
Это не только watch feature: cancellation при unload + shutdown contract относится к background worker infrastructure.

**Решение:** перенести в reusable task lifecycle, не создавать watch-specific system.

---

## 2. Roles / Community / Customization

### ROLE-001 + CUST-009–012 + COMM-006 → Self-service role systems
Все относятся к одному role self-service domain, но интерфейсы отличаются:
- command toggle;
- reaction roles;
- button roles;
- select-menu roles;
- multi-role panel.

**Решение:** один canonical self-service roles cluster с разными UI adapters. Persistent UI recovery из V2 Batch 1 сохраняется как отдельная деталь.

### ROLE-002–004 → Selfrole configuration
List, mass setup, hierarchy checks и auto-clean invalid IDs — один selfrole administration cluster.

### ROLE-005–006 → Role editing
Color/name editing — самостоятельные role administration actions. Не смешивать с selfroles.

### COMM-001–003 + EVENT-001–007
Giveaway, multiple winners, conditions, persistence/recovery, reroll — одна giveaway system.

### COMM-004 → Join-to-create voice
Уже есть GD-055. Объединить source trace, не создавать новый cluster.

### COMM-005 → Server counters
Уже есть GD-056. Сохранить динамическое обновление и типы counters.

### COMM-007 + EVENT-008–012
Birthday system, date storage, user timezone, automated greeting и channel setting — одна birthday system.

### COMM-008 → User notes
Уже GD-059. Не смешивать с infraction history.

### COMM-009 → Moderation case management
Уже GD-060/modlog family. Не создавать отдельный cluster только из-за названия Case.

### COMM-010–013 → Tickets
Claim, priority, limits, transcripts уже GD-061–064 и TICKET-003/004/013/011. Объединить source variants.

### CUST-001–005, CUST-019–025, CUST-026–032
Custom commands и aliases — один customization domain, но **не одна механика**.

Объединить:
- CUST-001/065 → custom commands;
- CUST-002/067 → keyword/trigger responses;
- CUST-003 → regex triggers;
- CUST-004/068 → placeholders;
- CUST-005/069 → custom embeds;
- CUST-006/007/070 → welcome/goodbye;
- CUST-026/027/066 → aliases / saved command invocations;
- CUST-029/072 → randomized custom responses;
- CUST-028 → fuzzy custom-command search;
- CUST-030 → raw source view;
- CUST-031 → custom-command metadata;
- CUST-032 → per-command cooldown.

**Важно:** alias и custom command не объединять в одну сущность — они разные underlying mechanics.

### CUST-008 + server auto-role variants
Auto-role после join отличается от self-service role. Не объединять.

### CUST-013–015 + GD-071
Channel/module/permission configuration и per-server module enable/disable — часть server configuration scope.

### CUST-016–018
Economy/XP/ticket server settings — scoped configuration variants, а не отдельные системы.

---

## 3. Events / Integrations

### EVENT-013–020
Scheduled announcements, reminders, recurring events, todo/reminder tasks, QOTD, daily tasks, temporary events и background tasks имеют общую scheduling infrastructure, но являются разными user-facing systems.

**Решение:** не сливать их в одну «Events» механику. Общий scheduler — инфраструктурная зависимость.

### INT-001–030
INT-001–018 — разные внешние интеграции; не объединять только потому, что используют API.

INT-019–020 → webhook subscriptions + HMAC validation: один webhook security/inbound integration family.

INT-021–023 → dashboard/OAuth/API: web control-plane cluster.

INT-024 + GD-071 → per-server integration toggles/scoped config.

INT-025–030 → credential registry/lifecycle. Это одна infrastructure family с отдельными capabilities:
- separate credential storage;
- shared token registry;
- stable keys;
- cross-module reuse;
- update events;
- add/remove/clear.

---

## 4. Tickets

TICKET-001–014 — одна ticket platform, но не одна механика.

Объединения:
- TICKET-001 → ticket panel;
- TICKET-002 + TICKET-013 → ticket creation limits (один-per-user и global/per-system limits — разные ограничения внутри одной системы);
- TICKET-003 → claim/unclaim;
- TICKET-004 → priority;
- TICKET-005/006/007 → close/instant-close/instant-delete как разные close paths;
- TICKET-008 → rename;
- TICKET-009 → participants;
- TICKET-010 → user notice/follow-up;
- TICKET-011 + GD-064 → transcript;
- TICKET-012 → configurable ticket UI message;
- TICKET-014 + CUST-020 → multiple independent ticket systems.

**Решение:** сохраняем отдельные mechanics внутри ticket platform, не дробим их на сотни IDs.

---

## 5. Music second-pass observations

### MUSIC-001–009 + MUSIC-K007–010
AutoPause/AutoLeave/24/7/AutoQueue/inactivity disconnect и lifecycle safety — одна player lifecycle system с отдельными policies.

### MUSIC-010–015 + MUSIC-K011/K018
Audio-node lifecycle + player movement/recovery — audio runtime lifecycle.

### MUSIC-016–026 + MUSIC-C003/C014–018/C025/C050–052
Now Playing/controller/queue interactive UI — один interactive player control surface.

Сохраняем:
- state-dependent button styles;
- loop state visualization;
- user-only control;
- collector TTL + idle timeout;
- short vs long queue UX;
- player movement checks;
- 24/7 stop semantics.

### MUSIC-C019–023/C047–048
Queue remove/move/skipto/previous/replay — отдельные queue/player actions, не дублировать только по названию command.

### MUSIC-C026–027
Filter presets + reset — filtering system, связанный с player.

### MUSIC-C028–031 + PDIS-A007
Latency/stats surfaces похожи, но MUSIC stats специфичны audio backend; не поглощать generic healthcheck.

### MUSIC-C032–035 + MUSIC-K013–014
Admin authorization + command loader/reloader — command/runtime management, не music-only mechanic.

### MUSIC-C037–043
Lyrics search/selection/source/tips/truncation/privacy — одна lyrics integration workflow.

### MUSIC-C044–046
Search metadata/no-results/seek bounds — details соответствующих search/seek actions.

---

## 6. Экономика

ECON-001/028 → basic balance.
ECON-002/003 → shop + inventory.
ECON-004/032 → periodic rewards/cooldowns.
ECON-005/034 → work.
ECON-006/035 → beg.
ECON-007/036/017 → P2P transfer.
ECON-008/044 → rob.
ECON-009/045 → crime.
ECON-010/046 → mine.
ECON-011/047 → fishing.
ECON-012/049 → gambling/slot.
ECON-013/051 → currency naming.
ECON-014/037 → admin balance management.
ECON-015/016 → deposit/withdraw.
ECON-018/052 → economy reset.
ECON-019/053 → prune inactive records.
ECON-020/040 → economy leaderboard.
ECON-021/038 → max balance.
ECON-022/041 → Economy API.
ECON-023/042 → paid actions.
ECON-024/043 → rewards from game systems.

**Решение:** это не новые дубли — source variants должны быть объединены в existing GD clusters, при этом уникальные wallet/bank, fees, cooldown tiers, bulk operations и advanced economy variants сохраняются отдельно как детали/подсистемы.

---

## Важный вывод Batch 2

После сверки тематических файлов видно, что многие apparent duplicates на самом деле являются **одной платформой с несколькими самостоятельными действиями**. Их нельзя просто схлопнуть в одну запись до потери функциональности.

Правильная структура:

`Platform/System → mechanics/actions → source variants → UX/constraints/recovery`

а не:

`каждая команда = отдельная система`.

Следующий pass должен продолжить по remaining large source-specific files (Titan/GAwesome/Tomato/Corwin) и искать cross-source совпадения уже с V2-кластерами.
