# ARCHITECTURE — Банк идей

Архитектурные и эксплуатационные идеи из крупных ботов.

- ARCH-001 — модульная архитектура по функциям.
- ARCH-002 — cog/plugin-style modules.
- ARCH-003 — отдельные handlers для событий.
- ARCH-004 — отдельные command modules.
- ARCH-005 — единый слой базы данных.
- ARCH-006 — guild-scoped настройки.
- ARCH-007 — user-scoped данные.
- ARCH-008 — права/permissions как отдельный слой.
- ARCH-009 — reusable pagination.
- ARCH-010 — единый formatter Discord timestamps.
- ARCH-011 — отдельные converters для аргументов команд.
- ARCH-012 — background scheduled tasks.
- ARCH-013 — восстановление состояния после рестарта.
- ARCH-014 — backup/restore базы.
- ARCH-015 — autosetup сервера.
- ARCH-016 — dashboard/web UI.
- ARCH-017 — API слой.
- ARCH-018 — Docker deployment.
- ARCH-019 — sharding для больших инсталляций.
- ARCH-020 — clustering для масштабирования.
- ARCH-021 — localization/language layer.
- ARCH-022 — timezone-aware функции.
- ARCH-023 — reusable embed/message builders.
- ARCH-024 — reusable component/pagination system.
- ARCH-025 — централизованная обработка ошибок.
- ARCH-026 — отдельный audit/logging слой.
- ARCH-027 — автоматическое создание дефолтных записей БД.
- ARCH-028 — отдельные базы/таблицы для разных модулей.
- ARCH-029 — тесты для модулей.
- ARCH-030 — CodeQL/dependency automation.

## Cog-Creators/Red-DiscordBot

### ARCH-031 — Глобальный broadcast через отдельный announcer-процесс
- Источник: Cog-Creators/Red-DiscordBot
- Owner может запустить одно объявление сразу по всем серверам.
- Рассылка выполняется отдельным процессом/исполнителем, а не блокирует обычную командную обработку.
- Одновременный второй broadcast запрещён.
- Предусмотрена отдельная отмена текущей рассылки.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО

### ARCH-032 — Серверный канал для глобального broadcast
- Источник: Cog-Creators/Red-DiscordBot
- Каждый сервер может отдельно указать канал, в который бот будет отправлять глобальные объявления.
- Настройку можно очистить и вернуть fallback-поведение.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО

### ARCH-033 — Serverlock для контроля инсталляции
- Источник: Cog-Creators/Red-DiscordBot
- Владелец может включить режим, в котором бот остаётся только на заранее известных серверах.
- При присоединении к неизвестному серверу бот автоматически покидает его.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО
