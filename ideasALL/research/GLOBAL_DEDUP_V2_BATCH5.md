# GLOBAL DEDUP V2 — Batch 5

## Scope

Строгая повторная дедупликация TitanBot по двум крупным источникам:

- `ideasALL/ideas/TITAN_TICKETS.md` — TT-001–170
- `ideasALL/ideas/TITAN_ECONOMY.md` — TITAN-E001–045

Сопоставление выполнено с:

- старым глобальным каталогом `GD-001–287`;
- `GLOBAL_DEDUP_V2_BATCH1–4`;
- тематическим `TICKETS.md`;
- ранее собранными Economy/Economy Advanced кластерами.

Принцип: не удалять исходные идеи и не превращать каждую техническую деталь в отдельную систему. Источник остаётся доказательством, а canonical-система содержит механику + варианты поведения + ограничения + recovery/UX детали.

---

# 1. TITAN Tickets

## 1.1. Основной вывод

`TT-001–170` почти полностью описывают уже существующую canonical ticket platform `GD-061–064` и расширяют её деталями. Новая ticket-система не создаётся.

Базовое объединение:

- `TT-001–035` → ticket panel/configuration/dashboard/recovery;
- `TT-036–070` → ticket creation, persistent state и permission context;
- `TT-071–094` → claim/unclaim, close, priority, pin;
- `TT-095–107` → delete/transcript;
- `TT-108–125` → ticket logging;
- `TT-126–138` → feedback/rating;
- `TT-139–155` → statistics и administration dashboard;
- `TT-156–170` → service/database/handler architecture и resilience.

Все эти детали сохраняются как свойства/механики ticket platform, а не как 170 отдельных систем.

## 1.2. Уже покрытые canonical-системы

### `GD-061` — Ticket Claim

`TT-047–049`, `TT-071–077` полностью подтверждают claim lifecycle:

- claimedBy / claimedAt;
- claim/unclaim;
- ограничения на unclaim;
- расширенные права staff;
- audit/log события.

Новых систем нет.

### `GD-062` — Ticket Priority

`TT-050`, `TT-084–091` подтверждают priority subsystem.

Сохраняются дополнительные варианты Titan:

- `none`, `low`, `medium`, `high`, `urgent`;
- label + emoji + color;
- audit изменения priority.

### `GD-063` — Ticket Limits

`TT-014–016`, `TT-052–056` расширяют существующий ticket limit:

- configurable max-open;
- default `3`;
- диапазон `1–10`;
- быстрый PostgreSQL count;
- fallback DB key scan;
- исключение служебных counter keys.

### `GD-064` — Ticket Transcripts

`TT-095–107` и `TT-098–104` расширяют transcript/delete workflow:

- configurable delete delay;
- предупреждение;
- transcript до удаления;
- отдельный destination channel;
- проверка прав назначения;
- transcript failure не блокирует delete;
- send failure не блокирует delete;
- обработка уже отсутствующего Discord channel;
- отдельный audit event.

Это не новый transcript system.

## 1.3. Ticket platform: объединение остальных механик

Все следующие TT-группы относятся к единой ticket platform:

- `TT-001–013` — panel, текст, button label, staff role, open/closed categories;
- `TT-017–035` — DM-on-close, dashboard, persistent config, initiator binding, collector timeout, panel health/repost/live update;
- `TT-036–046` — channel/ticket number/persistent ticket record/lifecycle timestamps;
- `TT-057–070` — permission context и permission validation;
- `TT-078–083` — close/archive/DM;
- `TT-092–094` — pin/unpin;
- `TT-108–125` — logging subsystem;
- `TT-126–138` — feedback/rating;
- `TT-139–155` — guild statistics и dashboard;
- `TT-156–170` — service/database/handler separation, typed errors, persistence/recovery.

Особенно важно: `TT-029–034` не превращать в отдельную "panel recovery system" внутри canonical ticket каталога. Это механика устойчивости ticket panel, хотя соответствующая reusable panel-health infrastructure уже отмечена в Batch 3 как отдельный архитектурный кандидат.

## 1.4. Реально новые / ранее не зафиксированные ticket-механики

### Candidate TICKET-A — Multiple Ticket Systems per Guild

Источник: `TICKET-014`.

CorwinDev допускает до 25 независимых ticket systems в одной конфигурации. Это отличается от обычной настройки одной ticket panel: разные системы могут иметь собственные категории/процессы.

Статус: **кандидат на отдельную механику ticket platform**, но не отдельная standalone-система.

Нужно сохранить как configurable multi-panel/multi-system capability.

### Candidate TICKET-B — Ticket Participant Management

Источник: `TICKET-009`.

`add/remove` пользователей внутри уже созданного ticket channel — самостоятельная ticket-механика, не покрываемая claim.

Статус: **новая механика ticket platform**, не новый standalone system.

### Candidate TICKET-C — Ticket Rename

Источник: `TICKET-008`.

Переименование существующего ticket channel/обращения.

Статус: **новая механика ticket platform**.

### Candidate TICKET-D — Ticket Notice / Follow-up

Источник: `TICKET-010`.

Staff может отправить creator напоминание с условием отсутствия ответа и последующего закрытия.

Это не обычный DM-on-close: событие происходит во время активного ticket lifecycle.

Статус: **новая ticket workflow механика**.

### Candidate TICKET-E — Instant Close / Instant Delete Paths

Источники: `TICKET-006`, `TICKET-007`.

CorwinDev имеет отдельные быстрые destructive/workflow paths.

Статус: **варианты ticket close/delete workflow**, не отдельные системы.

При объединении с Titan нельзя потерять различие между обычным lifecycle и bypass/instant operation.

## 1.5. Что НЕ надо объединять

- Ticket claim ≠ ticket participant management.
- Ticket close ≠ instant delete.
- Ticket delete ≠ transcript.
- Feedback ≠ ticket statistics.
- Ticket panel ≠ generic reaction-role/persistent panel.
- Ticket permission context ≠ глобальный command guard.
- Ticket logging ≠ общий modlog, хотя оба используют logging infrastructure.

## 1.6. Итог по Tickets

**Новых standalone canonical систем: 0.**

Есть **5 новых/уточняющих ticket-platform mechanics**:

1. multiple ticket systems per guild;
2. participant add/remove;
3. rename;
4. notice/follow-up;
5. instant close/delete paths.

Все остальные TT-ID нужно считать деталями существующей ticket platform и сохранить с source mapping.

---

# 2. TITAN Economy

## 2.1. Основной вывод

`TITAN-E001–045` не создают новых economy standalone systems. Это в основном более точные варианты уже существующих кластеров `GD-028–053` и Economy тематических файлов.

## 2.2. Сопоставление

### Balance / wallet / bank

`TITAN-E001–003`, `TITAN-E026–029` → существующие balance/wallet/bank clusters.

Сохраняются детали:

- wallet + bank + total;
- bank capacity;
- `deposit all`;
- clamp deposit по wallet/free capacity;
- bot-account exclusion;
- Bank Upgrade при заполнении.

Новой системы нет.

### Beg

`TITAN-E004–006` → `GD-035`.

Сохраняются:

- отдельный cooldown;
- configurable min/max reward;
- success/failure outcome;
- remaining time в человекочитаемом виде.

### Crime

`TITAN-E007–011` → `GD-045`.

Сохраняются:

- несколько crime types;
- individual risk/reward;
- failure → jail + wallet fine;
- fine bounded by wallet;
- `jailedUntil`.

### Fishing

`TITAN-E012–017` → `GD-047`.

Сохраняются:

- rarity tiers;
- random loot внутри rarity;
- fishing rod multiplier;
- action-specific cooldown;
- structured rate-limit error.

### Shop / inventory / upgrades / consumables / tools

`TITAN-E018–023` → `GD-030` + связанные economy item mechanics.

Сохраняются:

- quantity `1–10`;
- role item quantity=1;
- transaction rollback при ошибке Discord role assignment;
- item types `role`, `upgrade`, `consumable`, `tool`;
- persistent upgrades;
- quantity-based inventory items.

Это детали shop/inventory, не отдельные systems.

### Daily reward

`TITAN-E024–025` → `GD-032/033` и существующие reward mechanics.

Сохраняется premium-role percentage bonus.

### Work

`TITAN-E030–032` → `GD-034`.

Сохраняются:

- random profession;
- payout range;
- `extra_work` consumable для обхода cooldown;
- laptop multiplier.

### Mining

`TITAN-E033–034` → `GD-046`.

Сохраняются:

- tool multiplier tiers;
- flavor location.

### Transfer / payment

`TITAN-E035–038` → `GD-036`.

Сохраняются:

- parallel loading sender/receiver state;
- dedicated service method;
- recipient DM;
- self-transfer и bot-account restrictions.

### Robbery

`TITAN-E039–043` → `GD-044`.

Сохраняются:

- minimum victim wallet threshold;
- Personal Safe полностью блокирует robbery;
- cooldown всё равно сгорает;
- success → percentage transfer;
- failure → robber penalty;
- atomic persisted update для action result + cooldown.

### Result presentation / configurable cooldowns

`TITAN-E044–045` → общие economy UX/config mechanics.

- новый баланс показывается после операции;
- action-specific cooldowns configurable через `botConfig.economy.cooldowns.*` с fallback defaults.

Это cross-cutting economy behavior, а не новая система.

## 2.3. Важные сохранённые детали

Не терять при будущей консолидации Economy:

- transactional rollback для Discord role purchase;
- action-specific timestamps вместо единого cooldown;
- machine-readable rate-limit errors;
- persisted cooldown + action result в одной операции;
- Personal Safe как отдельный блокирующий фактор robbery;
- bounded penalties/rewards;
- premium/role/tool/consumable modifiers.

## 2.4. Итог по Economy

**Новых standalone canonical систем: 0.**

`TITAN-E001–045` полностью относятся к уже существующим economy systems и должны быть сохранены как дополнительные source variants/constraints/implementation details.

---

# 3. Повторная проверка против предыдущих V2 batch

## Уже подтверждённые совпадения

- Ticket platform → `GD-061–064` + broader ticket mechanics.
- Economy → `GD-028–053`.
- Ticket dashboard/persistent UI recovery → generic panel-health/recovery candidate из Titan Services/Reaction Roles.
- Typed errors/rate-limit errors → generic error architecture из Batch 1/3.
- Service separation → `TITAN_SERVICES.md` architecture, не отдельные user-facing systems.
- Guild-scoped configuration → `GD-071`.

## Не найдено оснований для merge с неродственными системами

- Tickets не объединяются с Applications: обе системы могут использовать forms/modals, но lifecycle и сущности различны.
- Tickets не объединяются с Reaction Roles: persistent panel здесь только UI-механизм.
- Economy не объединяется с generic cooldown system: action-specific cooldowns остаются reusable infrastructure + domain configuration.
- Ticket logging не объединяется полностью с modlog: разные события и domain semantics.

---

# 4. V2 Batch 5 result

### New standalone systems

**0**

### New domain mechanics/capabilities

- multi-ticket systems per guild;
- ticket participant add/remove;
- ticket rename;
- ticket notice/follow-up;
- instant close/delete paths.

### Large merged clusters

- `TT-001–170` → existing Ticket Platform + `GD-061–064` and related mechanics.
- `TITAN-E001–045` → existing Economy clusters `GD-028–053`.

### Preservation rule

Исходные `TITAN_TICKETS.md`, `TICKETS.md`, `TITAN_ECONOMY.md` не изменяются и не удаляются. Этот batch фиксирует только canonical mapping и результаты аудита.
