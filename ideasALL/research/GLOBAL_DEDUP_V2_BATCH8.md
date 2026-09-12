# GLOBAL DEDUP V2 — Batch 8

## Scope

Строгая сверка оставшихся тематических/архитектурных файлов против `GD-001–287` и `GLOBAL_DEDUP_V2_BATCH1–7`.

Проверены:
- `ACCESS_CONTROL.md`;
- `ARCHITECTURE.md`;
- `CORE_FRAMEWORK.md`;
- `CONFIGURATION.md`;
- `DATA_STORAGE.md`;
- `AUDIO_INFRA.md`;
- `QUALITY_AND_RELEASE.md`.

Правило: не удалять полезные исходные идеи. Одинаковые системы объединять, а уникальные UX/ограничения/recovery/архитектурные детали сохранять.

---

## 1. ACCESS_CONTROL — Allowlist / Blocklist

### ACCESS-001–008
Глобальный/локальный allowlist и blocklist пользователей/ролей, массовое управление, работа по ID и полная очистка списка образуют **единый Access Control / ACL system**.

Это не то же самое, что существующие global command guards (`PDIS-B005`) или permission requirements: guards определяют правила выполнения, а ACL хранит управляемые списки субъектов доступа.

**Решение: NEW standalone candidate — Access Control / Allowlist / Blocklist.**

Сохранить:
- global + guild scope;
- user + role entries;
- allowlist + blocklist semantics;
- bulk add/remove;
- ID-only management;
- clear/reset;
- owner bypass;
- диагностику источника отказа;
- безопасное восстановление доступа при self-lockout.

### ACCESS-009–011
Объединяются с тем же ACL system, а не создают отдельные systems.

---

## 2. ARCHITECTURE — global broadcast / serverlock

### ARCH-001–030
Базовые пункты — модульность, cogs, handlers, commands, DB layer, scoped config, permissions, pagination, scheduler, restart recovery, dashboard/API, sharding, localization, embeds, errors, audit/logging, tests и CI.

**Решение:** архитектурные принципы/инфраструктура. Не создавать отдельные standalone systems из каждого пункта. Они уже сверены с соответствующими V2-кластерами.

### ARCH-031 + ARCH-032 — Global Broadcast

Owner запускает одно объявление по всем guild через отдельный исполнитель; второй broadcast одновременно запрещён; есть cancel; для guild можно задать отдельный destination channel и fallback.

Это уже не просто reusable announcement infrastructure: есть самостоятельный owner-driven workflow массовой рассылки с собственным lifecycle.

**Решение: NEW standalone candidate — Global Broadcast.**

Сохранить:
- отдельный worker/process;
- concurrency lock;
- cancel;
- per-guild destination;
- fallback/clear channel config.

### ARCH-033 — Serverlock

Режим ограничения инсталляции: bot остаётся только на заранее разрешённых guild и автоматически покидает неизвестные.

Это не обычный command ACL: контролируется сама принадлежность bot instance к guild.

**Решение: NEW standalone candidate — Installation Serverlock.**

---

## 3. CORE_FRAMEWORK

`CORE-001–022` повторно сверены с V2 Batch 1–7.

### CORE-001–011
Multi-source module paths, temporary paths, third-party install directory, path validation, module discovery, load/unload/reload, batch result, traceback storage, command conflict checks, reload import handling и cache invalidation.

**Решение:** существующий cog/extension lifecycle cluster (`CORE/COG`, `PDIS-A006`, Titan command loader). Не создавать новые systems.

### CORE-012–018
Prefixes, invite visibility, dangerous-operation confirmation, owner protection, separate bot/user permissions, command-tree override states и hooks.

**Решение:** configuration + permission/access architecture. `CORE-015`/owner bypass также сохраняется как общий safety rule и ACL detail, но не отдельная system.

### CORE-019–022
Runtime info, update check, instance age и core RPC.

**Решение:** runtime/developer tooling. Не standalone user systems.

---

## 4. CONFIGURATION

### CONFIG-001–003
Embed configuration inheritance, scoped configuration и explicit reset override полностью совпадают по смыслу с `GD-071`/Titan configuration architecture/`TSVC-054–083`.

**Решение:** объединить в общий scoped configuration system.

Сохранить:
- global/guild/channel/user/command scopes;
- fallback hierarchy;
- command-specific overrides;
- explicit clear/reset вместо forced True/False;
- итоговый effective-value view.

Не создавать отдельную систему embed configuration.

---

## 5. DATA_STORAGE

### DATA-001–012
Изоляция data directories, core/module storage, read-only bundled data, multiple instances, temporary instances, storage backend abstraction, bootstrap config, immutable storage details, schema version/migration lock и module-derived storage paths.

**Решение:** общая data/storage architecture.

Особенно сохранить как infrastructure details:
- schema migrations;
- migration locking;
- temporary/degraded instances;
- per-module isolation;
- backend abstraction.

`DATA-006` не поглощает Titan K002: backend abstraction и runtime degraded fallback — разные capabilities внутри storage architecture.

Новых standalone user-facing systems нет.

---

## 6. AUDIO_INFRA

### AUDIO-001–012
Managed media-node, automatic runtime download, generated node config, environment preflight, cached runtime checks, memory bounds, readiness via logs, child-process lifecycle, plugin diagnostics, managed/unmanaged mode, reset и duplicate-start/shutdown protection.

**Решение:** merge в существующий Music/Audio runtime lifecycle (`MUSIC-010–015`, `MUSIC-K011/K018`, Corwin music lifecycle) как managed-node/backend capability.

Это важная **audio runtime subsystem**, но не отдельная пользовательская standalone system: node обслуживает существующий music/audio domain.

Не терять managed/unmanaged режим и process lifecycle/recovery.

---

## 7. QUALITY_AND_RELEASE

### QUALITY-001–009
CI tests, lint, CodeQL, dependency reproducibility, contribution metadata checks, translation automation, staged release, security configs и git-blame ignore.

**Решение:** единый quality/release engineering layer.

Не создавать пользовательские systems. `QUALITY-003` и `QUALITY-008` относятся к security tooling, а не к runtime bot security features.

---

## 8. Cross-check с предыдущими V2 batch

### Access Control
`ACCESS-001–011` не дублируют полностью `PDIS-B005`: global guards остаются механизмом проверки, ACL — самостоятельным управляемым списком доступа. Также не поглощать owner bypass в один безликий permission helper: он должен остаться как policy detail.

### Global Broadcast
`ARCH-031/032` не являются просто scheduler/announcement configuration: массовая рассылка имеет собственный workflow, lock и cancellation.

### Serverlock
`ARCH-033` не является обычным guild command permission: это installation-level admission policy.

### Configuration
`CONFIG-001–003` подтверждают `GD-071` и `TSVC-054–083`, без нового canonical system.

### Audio
`AUDIO-*` расширяют существующий Music/Audio runtime, но не создают отдельный music-adjacent user system.

### Storage / Quality
Остаются инфраструктурными слоями.

---

## Итог Batch 8

### Новые standalone candidates

**3:**
1. **Access Control / Allowlist / Blocklist** — `ACCESS-001–011`.
2. **Global Broadcast** — `ARCH-031–032`.
3. **Installation Serverlock** — `ARCH-033`.

### Объединено без новых standalone systems

- `CORE-001–022` → cog/command lifecycle + permissions/config/runtime tooling;
- `CONFIG-001–003` → scoped configuration (`GD-071` / `TSVC-054–083`);
- `DATA-001–012` → storage architecture;
- `AUDIO-001–012` → Music/Audio runtime lifecycle;
- `QUALITY-001–009` → CI/release engineering.

### Preservation

Исходные тематические файлы не изменяются и не удаляются. Все source IDs сохраняются как evidence layer. RoadMap по-прежнему **не начинать**, пока V2 all-files audit не завершён.
