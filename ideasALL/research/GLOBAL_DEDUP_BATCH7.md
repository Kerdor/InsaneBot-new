# GLOBAL DEDUP — BATCH 7

Тематические области: GAwesomeBot Web.

Правило: web-механики объединяются с уже существующими общими архитектурными кластерами, если это тот же underlying mechanic. Сохраняются отличительные web UX, security boundaries, DTO-подход и lifecycle.

## Web presentation / data

### GD-260 — Web normalized DTO layer
Источники: GAB-WEB-001–007, 053–056.
Канон: web получает нормализованные DTO для server/user/extension/blog вместо raw Discord/DB objects; поддерживаются graceful fallback, lazy remote resolution и bulk lookup там, где это уменьшает число запросов.

### GD-261 — Privacy-aware public user profile
Источник: GAB-WEB-004–007.
Канон: публичный профиль сериализует только разрешённые поля; дополнительно может показывать mutual servers, normalized presence, account age, last seen, points, AFK, past names и безопасные contributor/maintainer flags.

### GD-262 — Public server listing feature flag
Источник: GAB-WEB-002.
Канон: guild может отдельно разрешить публичный listing с описанием/категорией/invite, не делая сервер автоматически публичным.

### GD-263 — Raw + relative web timestamps
Источники: GAB-WEB-003, 012, 044.
Канон: web DTO предоставляет точное время и человекочитаемое relative-время одновременно.

## Extension gallery

### GD-264 — Versioned extension gallery
Источники: GAB-WEB-008–014.
Канон: extension имеет версии и lifecycle stages (draft/published/accepted/state), а gallery показывает тип, scopes, featured, points, owner, update time и другие type-specific metadata.

### GD-265 — Human-readable extension scopes
Источник: GAB-WEB-011.
Канон: внутренние permission/scope IDs расширения отображаются пользователю через человекочитаемые названия.

### GD-266 — Extension web administration
Источники: GAB-WEB-014, 051.
Канон: web UI позволяет создавать/редактировать draft, управлять версиями, публикацией и acceptance/state без ручного редактирования storage.

## Dashboard / configuration

### GD-267 — Web dashboard as configuration control plane
Источники: GAB-WEB-015–024.
Канон: dashboard изменяет тот же persistent guild state, что использует bot; configuration разделена на тематические страницы и feature sections.

### GD-268 — Web command configuration matrix
Источники: GAB-WEB-016–020.
Канон: для команды через web можно управлять enabled state, admin level и disabled channels; bulk submit изменяет несколько настроек за одну логическую операцию.

### GD-269 — Preserve untouched configuration fields
Источник: GAB-WEB-019.
Канон: partial form update меняет только поля, представленные текущей формой, сохраняя остальные значения.

### GD-270 — Transactional dashboard save
Источник: GAB-WEB-057.
Канон: submitted configuration валидируется и применяется как одна логическая операция; чтение текущего state и обработка submitted state разделены.

### GD-271 — Explicit dashboard destructive-action endpoint
Источник: GAB-WEB-022.
Канон: удаление server data выделено в отдельный destructive flow/controller, а не смешивается с обычным save.

### GD-272 — Dedicated dashboard statistics surface
Источник: GAB-WEB-023.
Канон: server statistics имеют отдельную web surface, не смешанную с configuration forms.

## Authentication / security

### GD-273 — Discord identity for web authentication
Источники: GAB-WEB-025–030.
Канон: web authentication использует Discord identity; membership и Discord permissions/role hierarchy проверяются перед доступом к guild dashboard, а maintainer/debug доступы отделены.

### GD-274 — Route-level authorization boundaries
Источники: GAB-WEB-028–030, 059.
Канон: dashboard, API, public, maintainer и debug routes имеют независимые security/behavior boundaries; debug не наследует обычный dashboard access автоматически.

### GD-275 — Web authentication middleware
Источник: GAB-WEB-029.
Канон: identity/authorization проверяется middleware до controller, оставляя controller бизнес-операциям.

### GD-276 — XSS-safe Markdown pipeline
Источники: GAB-WEB-037–039.
Канон: пользовательский текст sanitizes до Markdown→HTML; используется ограниченный Markdown flavor, а profile/custom fields проходят тот же pipeline.

### GD-277 — Safe external URL fallback
Источник: GAB-WEB-040.
Канон: отсутствие/некорректность публичного invite или другого внешнего URL не приводит к сломанной ссылке; UI получает безопасный fallback.

## Routing / web architecture

### GD-278 — Controller/route/API separation
Источники: GAB-WEB-031–036.
Канон: route отвечает за URL mapping, controller за операцию; HTML и JSON API endpoints разделены, общие parsers/helpers переиспользуются, web layer имеет собственную error boundary.

### GD-279 — Route-level feature namespaces
Источники: GAB-WEB-021, 045–047, 059.
Канон: dashboard, public content, API, debug и maintainer surfaces имеют отдельные controller/route namespaces и могут развиваться независимо.

### GD-280 — Public content surface isolation
Источники: GAB-WEB-042–047.
Канон: blog/wiki/activity/donation — независимые web surfaces с собственными presentation/controller boundaries; отсутствующие authors/entities получают fallback.

## Maintainer / operations

### GD-281 — Maintainer operational dashboard
Источники: GAB-WEB-048–052.
Канон: privileged web panel для shard/bot statistics, extension administration и опасных/громоздких maintenance operations отделена от обычного guild dashboard.

### GD-282 — Web server lifecycle isolation
Источник: GAB-WEB-060.
Канон: запуск/остановка web server не привязаны к lifecycle конкретного controller.

### GD-283 — Graceful missing remote entities
Источник: GAB-WEB-054.
Канон: удалённые/недоступные Discord users/guilds не должны ломать web page; parser возвращает безопасный placeholder state.

### GD-284 — Bulk mutual-guild resolution
Источник: GAB-WEB-056.
Канон: mutual guild data для профиля запрашивается bulk-операцией вместо последовательного fetch каждой guild.

## Cross-theme notes

- GD-260 не заменяет общий data/storage слой: это presentation boundary между bot state и web views.
- GD-267–270 расширяют GD-013 scoped configuration и GD-022 dashboard/API, но сохраняют web-specific bulk save, partial update и transaction semantics.
- GD-273–276 используют общий ACL/error/security подход, но web authentication, route isolation и XSS pipeline остаются отдельными web concerns.
- GD-281 является web-версией privileged control plane и не дублирует Discord owner commands буквально.
