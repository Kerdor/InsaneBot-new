# CorwinDev — Batch 9

Диапазон: **COR-342–COR-342**

## Database

### COR-342 — Кэширование запросов MongoDB в памяти с TTL и лимитом записей
Подключение Mongoose оборачивается `ts-cache-mongoose` с memory-cache: стандартный TTL — 60 секунд, максимальное количество записей — 5000. Это снижает количество повторных обращений к MongoDB для часто запрашиваемых данных.

## Примечание

Полностью просмотрены `src/database`: `connect.js` и все модели в `src/database/models`. Схемы моделей в основном являются хранилищем уже исследованных систем (AFK, profile, economy, levels, invites, giveaways, tickets, warnings, reaction roles, stats, custom commands, voice channels и т. д.) и новых уникальных пользовательских механик не добавляют. Отдельно зафиксирован архитектурный вариант кэширования запросов БД.
