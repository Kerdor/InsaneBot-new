# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **глобальная дедупликация и каталогизация собранных идей после завершения всех источников.**

## Правила

- Все 7 источников уже полностью исследованы; к ним не возвращаемся без необходимости.
- Исходные `COR-*`/`TOM-*` и тематические файлы сохраняются как трассировка.
- Одинаковые системы объединяются в канонические кластеры.
- При различиях сохраняются уникальные UX, поведение, настройки, ограничения и архитектурные варианты.
- Командные интерфейсы не считаются отдельными системами, если underlying mechanic уже есть.
- После глобальной дедупликации строится порядок реализации/RoadMap.
- На текущем этапе bot implementation не изменяется.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — ЗАВЕРШЁН.**
5. **GAwesomeBot/bot — ЗАВЕРШЁН.**
6. **CorwinDev/Discord-Bot — ЗАВЕРШЁН.**
7. **Tomato6966/Multipurpose-discord-bot — ЗАВЕРШЁН.**

## Global Dedup

### Batch 1 — Core / Architecture / Storage / Access — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH1.md`

Обработаны:
- `CORE_FRAMEWORK.md`
- `COG_MANAGEMENT.md`
- `ARCHITECTURE.md`
- `CONFIGURATION.md`
- `DATA_STORAGE.md`
- `ACCESS_CONTROL.md`

Зафиксированы канонические кластеры `GD-001–027`: модульная архитектура, lifecycle модулей, источники расширений, безопасность установки, диагностика, hot reload, версии расширений, permission/ACL, scoped configuration, reusable UI, background tasks, persistent state, storage isolation, multi-instance, migration locking, backup/restore, scaling/deployment, localization/timezone, error/audit layers, broadcast/serverlock, runtime info и core RPC.

### Следующая точка
Продолжить глобальную дедупликацию следующих тематических областей, не пересобирая уже закрытый Batch 1 без появления новых исходных данных.

`bot/main.py` и другая реализация InsaneBot не изменялись.
