# GLOBAL DEDUP V2 — Batch 9

## Scope

Строгая сверка `COG_MANAGEMENT.md` против `GD-001–287` и `GLOBAL_DEDUP_V2_BATCH1–8`.

Правило: не удалять полезные исходные идеи. Если механика относится к уже существующему домену — объединять её туда, сохраняя все уникальные ограничения, UX, recovery и архитектурные варианты.

Источник:
- `COG_MANAGEMENT.md` — `COG-001–024`

---

## 1. COG-001–014 — источники, discovery и безопасное управление расширениями

### Объединение с существующим cog/extension lifecycle

`COG-001–006` уже совпадают с ранее найденным кластером управления расширениями:

- несколько источников расширений и порядок приоритета;
- временные и постоянные источники;
- отдельное хранилище сторонних модулей;
- просмотр путей и их приоритета;
- безопасная проверка package/data/core paths;
- динамический поиск доступных модулей.

Они объединяются с `CORE-001–011`, `COG-*` findings из предыдущих source-specific файлов и `PDIS-A006` (mass extension management / rollback).

`COG-007–012` также являются частью того же lifecycle:

- batch load/unload/reload;
- подробный batch report;
- сохранение последнего traceback;
- обнаружение конфликтов команд/alias;
- корректный hot reload импортов;
- `importlib` cache invalidation.

`COG-013–014` — дополнительные safety/configuration details того же extension manager:

- временное или persistent добавление пути;
- исключение невалидных Python package names.

**Решение:** новых standalone systems здесь не создавать. Всё входит в общий **Cog / Extension Management** platform/admin system.

Сохранить все перечисленные варианты, не сводя их только к простому `load/unload/reload`.

---

## 2. COG-015–020 — pin/update lifecycle

Эти пункты расширяют тот же Extension Management platform, а не создают отдельную систему:

- `COG-015` — pin установленного модуля на commit/revision;
- `COG-016` — массовый pin/unpin;
- `COG-017` — проверка обновлений без установки;
- `COG-018` — update с явным поведением reload после обновления;
- `COG-019` — update до конкретной revision;
- `COG-020` — диагностика неоднозначной короткой revision.

Это единый lifecycle расширения: **source → install → inspect → update → pin/unpin → reload**.

Не объединять эти механики с обычным bot update checker (`CORE-019`, `COR-355`): там обновляется сам бот/релиз, здесь управляются сторонние расширения.

---

## 3. COG-021–024 — repository/install lifecycle

`COG-021–024` остаются деталями Extension Management:

- `COG-021` — metadata repository source: URL, branch, authors, description;
- `COG-022` — install message стороннего модуля с substitutions;
- `COG-023` — explicit agreement/confirmation перед установкой стороннего source;
- `COG-024` — переустановка dependencies всех установленных extensions.

`COG-023` дополнительно согласуется с существующими dangerous-operation confirmations, но не заменяется ими: для external module installation сохраняется отдельный policy/UX step.

`COG-024` сохраняется как maintenance capability Extension Management, а не превращается в отдельную dependency-management system.

---

## 4. Cross-check с предыдущими V2 batches

### PDIS-A006 / CORE / Titan loader

`COG-001–024` существенно расширяют уже существующий extension/cog management cluster. Особенно важно не потерять внешние sources, priority, temporary paths, safe path validation, batch operations, traceback diagnostics, command conflict detection и cache invalidation.

### Bot update vs extension update

Не объединять `COG-015–020` с bot self-update/update-check infrastructure. Они имеют другой объект управления и другой lifecycle.

### Permissions / confirmation

`COG-023` использует общий механизм confirmation/safety, но сохраняется как installation-specific policy detail.

---

## Итог Batch 9

### Новых standalone systems

**0.**

`COG-001–024` полностью относятся к единому **Cog / Extension Management** platform/admin domain, уже представленному предыдущими V2 findings.

### Что обязательно сохранить

- multiple extension sources + priority;
- temporary/persistent sources;
- isolated third-party storage;
- path inspection and safe-path validation;
- dynamic discovery;
- batch operations + detailed report;
- traceback retention;
- command conflict detection;
- hot reload + import cache invalidation;
- package-name validation;
- revision pinning and bulk pin/unpin;
- update check without installation;
- controlled reload behavior after update;
- update to exact revision;
- ambiguous short-SHA diagnostics;
- repository metadata;
- third-party install messages;
- explicit installation agreement;
- dependency reinstall maintenance operation.

Исходный `COG_MANAGEMENT.md` не изменяется и не удаляется.
RoadMap по-прежнему не начинать до завершения V2 all-files audit.
