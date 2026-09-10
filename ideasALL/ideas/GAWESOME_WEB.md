# GAwesomeBot — Web

> Идеи из `Web/`. Фиксируем архитектуру, UX и механики, а не копируем реализацию.

## Server / user presentation

### GAB-WEB-001 — Единый parser server data
- Собирает имя, ID, icon, owner, member count, message activity, age, prefix и публичные listing-поля в один DTO.

### GAB-WEB-002 — Публичный server listing как отдельный feature flag
- Сервер может иметь описание/категорию/invite, но полностью скрывать listing.

### GAB-WEB-003 — Absolute + relative dates
- Для web UI полезно хранить точную дату и человекочитаемое `from now` одновременно.

### GAB-WEB-004 — User profile privacy gate
- Приватные поля профиля не сериализуются в публичный DTO, пока пользователь не разрешил публичность.

### GAB-WEB-005 — Mutual server directory
- Профиль пользователя показывает только серверы, общие с ботом, с сортировкой по имени.

### GAB-WEB-006 — Profile status normalization
- Discord presence переводится в единый UI status + UI class.

### GAB-WEB-007 — Profile metadata aggregation
- Возраст аккаунта, last seen, points, AFK, past names, roles статуса и contributor/maintainer flags доступны web UI как готовые поля.

## Extension gallery

### GAB-WEB-008 — Extension version selector
- Страница расширения может отображать published version либо явно выбранную версию.

### GAB-WEB-009 — Type-specific extension metadata
- Для command/keyword/timer/event показываются разные поля, но общий DTO остаётся единым.

### GAB-WEB-010 — Extension lifecycle status
- Gallery хранит featured/state/accepted/level/points/last updated и scopes.

### GAB-WEB-011 — Scope visualization
- Разрешения расширения превращаются из внутренних scope ID в человекочитаемые названия.

### GAB-WEB-012 — Relative + raw extension update time
- UI получает обе формы timestamp.

### GAB-WEB-013 — Extension owner fallback
- Если владелец расширения недоступен, web-страница получает безопасный `invalid-user`, а не падает.

### GAB-WEB-014 — Extension builder/version workflow
- Web-панель позволяет работать с черновиком, версиями, публикацией, принятием и состоянием расширения как отдельными стадиями.

## Dashboard

### GAB-WEB-015 — Dashboard как control plane
- Настройки Discord-сервера доступны через web вместо необходимости выполнять длинные серии команд.

### GAB-WEB-016 — Command configuration UI
- Для каждой команды можно менять enabled state, admin level и список отключённых каналов.

### GAB-WEB-017 — Channel-level command switches
- Команда может быть включена глобально, но запрещена в отдельных text channels.

### GAB-WEB-018 — Bulk command configuration
- Dashboard работает с группой настроек за один submit, а не требует отдельного запроса на каждое поле.

### GAB-WEB-019 — Preserve untouched settings
- При сохранении изменяются только поля, представленные текущей формой.

### GAB-WEB-020 — Administration dashboard sections
- Административные настройки разделяются по смыслу, чтобы большая конфигурация не превращалась в одну форму.

### GAB-WEB-021 — Feature-specific dashboard pages
- Commands, statistics, administration и other settings имеют отдельные controller/page boundaries.

### GAB-WEB-022 — Dashboard deletion flow
- Удаление серверных данных выделяется в отдельный endpoint/controller, а не смешивается с обычным сохранением.

### GAB-WEB-023 — Dashboard stats view
- Статистика сервера доступна отдельно от configuration UI.

### GAB-WEB-024 — Web configuration uses same server state as bot
- Dashboard изменяет persistent guild configuration, поэтому bot и web используют один источник истины.

## Authentication / authorization

### GAB-WEB-025 — Discord-based web authentication
- Web identity привязывается к Discord user, а не создаётся отдельным аккаунтом.

### GAB-WEB-026 — Server membership as authorization boundary
- Наличие пользователя на сервере проверяется до доступа к его dashboard.

### GAB-WEB-027 — Permission-aware dashboard
- Доступ к отдельным административным операциям определяется Discord permissions/role hierarchy.

### GAB-WEB-028 — Maintainer-only web area
- Внутренние страницы отделены от обычного guild dashboard и требуют отдельного privileged статуса.

### GAB-WEB-029 — Auth middleware before controller
- Проверка identity/authorization вынесена в middleware, а controller занимается бизнес-операцией.

### GAB-WEB-030 — Separate debug authorization
- Debug routes не должны автоматически наследовать обычный dashboard access.

## API / routing

### GAB-WEB-031 — Controller/route separation
- Route отвечает за mapping URL → controller, controller — за операцию.

### GAB-WEB-032 — Base Route abstraction
- Общие параметры и поведение web routes выносятся в базовый класс.

### GAB-WEB-033 — Dedicated API routes
- JSON/API endpoints отделены от HTML dashboard routes.

### GAB-WEB-034 — Shared parsers for API and pages
- Сложные Discord/DB objects сначала превращаются в безопасные web DTO, после чего их используют разные представления.

### GAB-WEB-035 — Central web helpers
- Повторяющиеся URL, redirect, rendering и formatting operations держатся в helper layer.

### GAB-WEB-036 — Error boundary at web layer
- Ошибки controller не должны превращать внутренний stack trace в пользовательскую страницу.

## Security / rendering

### GAB-WEB-037 — XSS filtering before Markdown rendering
- Пользовательский текст проходит sanitization до преобразования Markdown в HTML.

### GAB-WEB-038 — Safe Markdown flavor
- Web Markdown parser включает только необходимые GitHub-like возможности.

### GAB-WEB-039 — Sanitized profile fields
- Custom profile fields проходят тот же защитный pipeline, что и остальной пользовательский текст.

### GAB-WEB-040 — Safe invite fallback
- Если публичный invite отсутствует, UI получает безопасный fallback вместо пустого/ломаного URL.

### GAB-WEB-041 — Web DTO вместо raw Discord objects
- Controller не отдаёт шаблонам целые внутренние Discord/DB objects.

## Public content

### GAB-WEB-042 — Blog category presentation
- Категория blog entry преобразуется в отдельный UI presentation class.

### GAB-WEB-043 — Blog author fallback
- Недоступный автор не ломает страницу публикации.

### GAB-WEB-044 — Blog publication timestamps
- Публикация показывает raw и relative timestamp.

### GAB-WEB-045 — Activity page as separate public surface
- Discord activity/служебная статистика может иметь отдельный web controller, не смешанный с dashboard.

### GAB-WEB-046 — Wiki as independent content surface
- Wiki-контент имеет отдельный controller/route слой и может развиваться независимо от dashboard.

### GAB-WEB-047 — Donation page isolation
- Сервисные страницы вроде donation не должны зависеть от guild dashboard state.

## Maintainer / operations

### GAB-WEB-048 — Maintainer dashboard
- Внутренняя web-панель для обслуживания бота отделена от пользовательского dashboard.

### GAB-WEB-049 — Operational stats surface
- Shard/bot statistics доступны web maintainer-интерфейсу отдельно от обычной серверной статистики.

### GAB-WEB-050 — Debug web surface
- Диагностические операции вынесены в собственный route/controller namespace.

### GAB-WEB-051 — Extension administration from web
- Gallery/extension lifecycle можно администрировать через web UI без ручного редактирования DB.

### GAB-WEB-052 — Web as privileged bot control plane
- Maintainer dashboard может быть интерфейсом для операций, которые слишком опасны или громоздки для Discord-команд.

## Architecture

### GAB-WEB-053 — Web DTO layer
- Отдельные `serverData`, `userData`, `extensionData`, `blogData` показывают шаблон: raw state → normalized presentation DTO → view.

### GAB-WEB-054 — Graceful missing Discord entities
- Любой web parser должен иметь fallback для удалённых пользователей/guilds.

### GAB-WEB-055 — Lazy remote entity resolution
- Parser запрашивает Discord data только тогда, когда оно нужно конкретной странице.

### GAB-WEB-056 — Mutual data resolved in bulk
- Для профилей лучше один bulk lookup mutual guilds, чем последовательный запрос каждой guild.

### GAB-WEB-057 — Server configuration form as transaction
- Набор изменений dashboard лучше применять как одну логическую операцию после валидации формы.

### GAB-WEB-058 — Read/write separation in dashboard
- Отдельно формируется текущее состояние для страницы и отдельно обрабатывается submitted state.

### GAB-WEB-059 — Route-level feature boundaries
- `dashboard`, `debug`, `maintainer`, `api` и public routes должны иметь отдельные security/behavior boundaries.

### GAB-WEB-060 — Web server lifecycle isolation
- Запуск и остановка web server не должны быть тесно связаны с конкретным controller.
