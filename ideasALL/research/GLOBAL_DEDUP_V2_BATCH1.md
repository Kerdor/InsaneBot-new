# GLOBAL DEDUP V2 — BATCH 1

## Цель

Это повторная, более строгая сверка банка идей после первоначального `GD-001–287`.

Главный принцип: **ничего полезного не удалять**. Исходные source-specific документы остаются на месте. При объединении переносится не только название системы, но и все отличающиеся варианты поведения, ограничения, UX, recovery и архитектурные детали.

## Правила V2

1. Точное совпадение → один канонический кластер.
2. Одинаковая базовая механика с разным UX → один кластер + оба UX-варианта как детали.
3. Общая инфраструктура не поглощает самостоятельную пользовательскую механику.
4. Временная версия системы не считается отдельной системой, если отличается только expiry/recovery; это вариант основной системы.
5. Но workflow перехода состояния, которого нет у основной системы, сохраняется как отдельная деталь.
6. Интеграционные варианты не удаляются: они привязываются к базовой системе.
7. Source IDs не удаляются — они остаются трассировкой происхождения.
8. Если есть сомнение, **не объединять**, пока сходство не доказано.

---

## Pass 1 — Python Discord: role/access/UI

### PDIS-001 → Self-service roles + persistent UI recovery
Базовая механика уже входит в `GD-057` (self-service role panels).

Не терять следующие детали:
- постоянное сообщение-панель;
- persistent view после рестарта;
- поиск существующего сообщения по `message_id`/содержимому;
- автоматическое пересоздание панели при отсутствии сообщения;
- временная персональная ephemeral-панель с timeout;
- состояние кнопки Add/Remove для конкретного пользователя;
- запрет чужого управления панелью.

**Решение:** объединить в `GD-057` как расширенный вариант persistent/self-service role UI. Отдельным GD не делать.

### PDIS-002 → GD-057
Полностью входит в self-service role panels. UX-детали сохранить.

### PDIS-003 + PDIS-004 + PDIS-005 → Temporary permission-role lifecycle
Базовая выдача роли существует в role/permission механиках, но сочетание `temporary → scheduled revoke → persistent recovery → temporary→permanent upgrade → expiry-sorted list` является отдельным reusable workflow.

**Решение:** сохранить как отдельный кластер временных разрешений/ролей, связанный с ролями и scheduler. Не растворять в обычной выдаче роли.

### PDIS-006 → Streaming permission revoke
Повторяется с `PDIS-M2-015`.

**Решение:** объединить оба source ID в один вариант streaming-permission revoke: отзыв права должен уметь завершать уже активный stream.

### PDIS-007 + PDIS-008 + PDIS-009 + PDIS-010 → Channel silence/unsilence
Базовая channel permission blocking относится к moderation/channel controls, но сохранение исходных overwrites, единый text+voice workflow, permanent-silence notifier и per-resource lock — дополнительные детали одной системы.

**Решение:** один кластер `Channel Silence` с вариантами:
- text/voice;
- temporary/permanent;
- exact overwrite restore;
- fallback restore;
- periodic staff reminders;
- lock against concurrent operations.

### PDIS-011 + PDIS-012 → Command context/redirect controls
Whitelist/blacklist по channel/category/role и redirect в правильный канал — одна система context-aware command routing.

**Решение:** объединить; сохранить background execution, paste fallback и override-роли как детали.

### PDIS-013 → Reusable target-role hierarchy check
Это не отдельная пользовательская система, а reusable safety primitive для moderation/role actions.

**Решение:** привязать к общей permission/target validation инфраструктуре, не создавать отдельный GD.

### PDIS-014 + PDIS-015 + PDIS-016 → Validators/converters
URL availability check, Snowflake timestamp validation и duration parser — разные utility primitives.

**Решение:** не объединять между собой. Они похожи только архитектурно (validators/converters), но решают разные задачи.

### PDIS-017 → Resource topic deep-link
Уникальная utility-механика. Сохранить отдельно.

### PDIS-018 → Persistent public + ephemeral private UI
Пересекается с `PDIS-001/002`, но является более общим UI pattern.

**Решение:** сохранить как общий UX-паттерн внутри role-panel/interactive UI кластера, не отдельная система.

---

## Pass 2 — Python Discord Advanced

### PDIS-A001 — Linked accounts with context
**NEW candidate.**
Связанные аккаунты с author/time/context, редактированием, удалением и историей raw IDs не покрываются обычными user notes или moderation history.

**Решение:** сохранить отдельной системой `Linked Accounts / Alternate Accounts`.

### PDIS-A002 — Scheduled role with temporary manual override
**NEW candidate.**
Ежедневное расписание включения/выключения роли + временный ручной override + restore schedule + timezone + Redis recovery.

**Решение:** отдельная scheduled-role workflow система; не смешивать с обычными roles.

### PDIS-A003 — Interactive help parent/subcommand navigation
Связано с `HELP-003/HELP-009` и существующим Help UX, но добавляет navigation state без нового сообщения и возврат к parent.

**Решение:** объединить в Help UX как navigation workflow; не отдельная система.

### PDIS-A004 — Fuzzy command discovery with permission-aware suggestions
Связано с `HELP-004` и `HELP-005`, но расширяет поиск на aliases/groups/cogs/categories.

**Решение:** объединить в Help/command discovery; сохранить расширенный candidate search.

### PDIS-A005 — User-defined help categories
Уникальный способ группировать команды нескольких cogs в одну help category.

**Решение:** сохранить как отдельную деталь Help UX, не отдельный GD.

### PDIS-A006 — Mass extension management with wildcard + rollback
Связано с `CORE-006/007` и `COG-007/008`, но rollback к предыдущему рабочему состоянию — важная дополнительная гарантия.

**Решение:** объединить в cog lifecycle cluster; сохранить wildcard semantics, progress report, global operation lock и rollback.

### PDIS-A007 — Multi-source latency healthcheck
**NEW candidate.**
Одна диагностика объединяет command processing latency, external API health и Discord API latency с независимыми failure states.

**Решение:** сохранить отдельной diagnostic system.

### PDIS-A008 — WebSocket event-rate diagnostics
**NEW candidate.**
Счётчики событий, rate и top event types.

**Решение:** отдельная runtime diagnostics detail/system.

### PDIS-A009 — Persistent REPL eval environment + paste fallback
**NEW candidate.**
Сохраняемость окружения между eval-вызовами + reset + paste fallback — отдельный owner/developer tool.

**Решение:** сохранить отдельно; не смешивать с обычной error diagnostics.

### PDIS-A010 — Source links for commands/cogs
**NEW candidate.**
Получение точной GitHub-ссылки на реализацию объекта/диапазон строк.

**Решение:** сохранить как developer utility.

### PDIS-A011 — Normalized Discord event metrics
Связано со статистикой, но это инфраструктурные gauges/counters для event pipeline.

**Решение:** привязать к stats/observability; не отдельный пользовательский GD.

### PDIS-A012 — Moderation-only echo/embed relay
**NEW candidate.**
Минимальный staff relay-инструмент, который не равен полноценной announcement-системе.

**Решение:** сохранить отдельно.

---

## Pass 3 — Python Discord Backend

### PDIS-B001 — Startup reconciliation of configured Discord resources
Связано с configuration bootstrap и startup diagnostics.

**Решение:** объединить с configuration validation/startup health. Сохранить конкретный diff отсутствующих channel/role/category IDs.

### PDIS-B002 + PDIS-B003 — Repository-managed event assets + fair asset rotation
Event metadata discovery и rotation assets имеют общий event-branding контекст, но rotation — отдельный stateful механизм.

**Решение:** один event-branding cluster с двумя независимыми частями; не удалять ни одну.

### PDIS-B004 — API sync via diff/reconciliation
**NEW candidate.**
Структурированный `created/updated/deleted` diff, batching, pagination, cache completeness fallback и ручной sync.

**Решение:** отдельный synchronization subsystem.

### PDIS-B005 — Global command guards
Пересекается с permissions, но это именно core-level guard до локальных checks.

**Решение:** объединить в permission architecture как global guard layer.

### PDIS-B006 — Error response with interactive Help
Связано с Help UX + centralized errors.

**Решение:** объединить, сохранив кнопку contextual help и разные input/API error counters.

### PDIS-B007 — Structured unexpected-error context
Связано с centralized error handling/logging, но конкретный контекст (message jump link, command, IDs, raw message) должен сохраниться.

**Решение:** объединить в error/observability cluster.

---

## Pass 4 — Python Discord Core Utils

### PDIS-CU001–005 — Resource locking
Все пять записей описывают одну общую locking infrastructure:
- resource-scoped lock;
- isolated namespaces;
- fail-fast vs wait;
- structured busy error;
- dynamic keys;
- active-holder counting/wait-all.

**Решение:** объединить в один reusable `Resource Locking` subsystem. Не терять режимы и semantics.

### PDIS-CU006–010 — Bounded message cache
Одна система ring buffer + O(1) ID lookup + metadata + indexing/slices + update-if-cached.

**Решение:** объединить в один message cache subsystem.

### PDIS-CU011–013 — Context whitelist/redirect/silent checks
Пересекается с PDIS-011/012.

**Решение:** объединить в один context-aware command access/redirect cluster; сохранить silent mode и auto-whitelist redirect behavior.

### PDIS-CU014 — Role bypass over cooldown
Связано с cooldown infrastructure, но это универсальный policy modifier.

**Решение:** сохранить как cooldown policy detail, не отдельную систему.

### PDIS-CU015–016 — Reaction access/deletion workflow
Одна reaction-control infrastructure с ACL, auto-removal чужих реакций, expiry и safe handling already-deleted messages.

**Решение:** объединить.

### PDIS-CU017–018 — Attachment relay
Одна relay-система с split, size fallback и partial-failure handling.

**Решение:** объединить.

### PDIS-CU019 — Unique reaction voters
Отдельная статистическая utility. Не смешивать с reaction control.

### PDIS-CU020 — Webhook username sanitization
Небольшая, но самостоятельная безопасность relay pipeline. Сохранить как webhook/relay detail.

### PDIS-CU021–022 — Standardized log API
Одна log presentation infrastructure с event timestamp, embed fields, critical mentions и content limits.

**Решение:** объединить в logging presentation layer.

### PDIS-CU023 — Deleted-message archive
Связано с message archive/audit; сохраняется как конкретная архивная система с API/web-view link.

### PDIS-CU024–025 — Reply-aware response
Одна response helper: сохраняет reply context, но безопасно отказывается от reply для self-reference/invalid reference.

**Решение:** объединить.

### PDIS-CU026–031 — Time/duration/expiry presentation
Это один family of temporal formatting primitives, но не одна пользовательская система.

**Решение:** объединить в shared time/expiry utility family, сохранив отдельные capabilities:
- Discord timestamp formats;
- humanized duration;
- expiration states;
- timestamp + remaining duration;
- relative→absolute conversion.

### PDIS-CU032–033 — Restricted interactive pagination
Пересекается с reusable pagination, но user/role restriction и auto-delete — детали общего paginator.

**Решение:** объединить в pagination subsystem.

### PDIS-CU034–035 — Startup dependency preflight
HTTP/Redis/API dependency initialization + class-specific fatal messages.

**Решение:** объединить в startup preflight/health subsystem.

### PDIS-CU036 — Development StatsD fallback
Уникальный deployment/observability detail. Сохранить.

### PDIS-CU037 — Minimal production intents
Уникальная production optimization/security detail. Сохранить.

### PDIS-CU038 — Global AllowedMentions policy
Уникальная global safety policy. Сохранить в permissions/safety layer.

### PDIS-CU039 — Semantic configuration exceptions
Пересекается с centralized error handling; сохранить типизированные exception classes как detail.

### PDIS-CU040 — Decorator globals for annotation resolution
Уникальная Python-specific framework detail. Сохранить отдельно в architecture/developer tooling.

---

## Pass 5 — Python Discord moderation

### PDIS-M2-001 + PDIS-M2-002 — DEFCON account-age threshold lifecycle
Одна аварийная система с temporary threshold, expiry, scheduler, persistent state и staff reminders.

**Решение:** объединить в один `Emergency Account-Age Gate`.

### PDIS-M2-003 — Emergency server lockdown
**NEW candidate.**
Массовое временное ограничение @everyone по text/thread/reaction/voice permissions.

**Решение:** сохранить отдельно; не смешивать с обычным channel silence.

### PDIS-M2-004–006 — Incident reaction state machine + archival safety
Одна incident workflow: reaction states, role ACL, startup catch-up, archive-before-delete, lock и confirmation of deletion.

**Решение:** объединить.

### PDIS-M2-007–008 — Deleted-message recovery + privacy-aware Discord-link previews
Связанные, но разные capabilities.

**Решение:** объединить в incident/message audit tooling, сохранив privacy check и deleted-state presentation.

### PDIS-M2-009–012 — Advanced clean workflow
Одна система bulk cleanup с composable filters, 14-day API split, cancellation, single-flight execution и audit archive.

**Решение:** объединить в advanced clean system.

### PDIS-M2-013–016 — Streaming permissions lifecycle
Повторяют PDIS-003/004/006 и объединяются с ними в reusable temporary permission + streaming-specific revoke behavior.

---

## Pass 6 — Python Discord moderation 3

### PDIS-M3-001 — Modlog suppression tokens
**NEW candidate.**
One-shot suppression of expected gateway audit events to prevent duplicate logs.

### PDIS-M3-002 — Permission-aware modlog blacklist
Связано с access control и modlog.

**Решение:** сохранить как modlog visibility policy.

### PDIS-M3-003 — Role diff in member audit
Часть member audit/modlog; объединить, не удаляя отдельные Role added/removed semantics.

### PDIS-M3-004 — Reply context in deleted-message audit
Объединить с deleted-message archive/audit, сохранив reference states.

### PDIS-M3-005 — Detailed voice-state audit
Часть modlog member/voice audit; сохранить granular diff semantics.

### PDIS-M3-006–008 — Infraction lifecycle/history/pardon
Одна infraction lifecycle system с active/inactive state, edit history, separate pardon reason/DM policy.

**Решение:** объединить.

### PDIS-M3-009–011 — Moderation-message tidy-up + scheduler resync + lazy callable
Tidy-up и scheduler recovery относятся к moderation lifecycle; callable coroutine creation — generic async scheduling implementation detail.

**Решение:** не смешивать всё в одну пользовательскую систему; сохранить implementation details внутри scheduler/error infrastructure.

### PDIS-M3-012–014 — Reason/audit/appeal presentation
Одна infraction notification policy с отдельными human/audit reasons, type-specific appeal destinations и context-sensitive staff confirmation.

**Решение:** объединить как notification/presentation layer инфракций.

### PDIS-M3-015 — Timeout cap normalization
Деталь Discord timeout validation. Не отдельная система; сохранить в moderation duration handling.

---

## Итог этой повторной проверки

Эта V2-проверка уже показывает, что первоначальный `GD-001–287` **нельзя считать окончательно очищенным от дублей и пропущенных вариантов**.

Особенно важные кандидаты, которые нужно обязательно сохранить в следующем каноническом банке:
- linked/alternate accounts with context;
- scheduled role with manual override;
- multi-source healthcheck;
- websocket event-rate diagnostics;
- persistent REPL eval;
- source-code links;
- API diff/reconciliation sync;
- emergency server lockdown;
- incident reaction state machine;
- advanced bulk-clean;
- modlog suppression tokens;
- temporary permission-role lifecycle;
- channel silence/restore;
- bounded message cache;
- reusable resource locking.

**Исходные файлы не удалять.** Следующий V2 pass должен сверить остальные тематические и source-specific файлы с этим набором и между собой, после чего обновить канонические кластеры и только затем переходить к RoadMap.
