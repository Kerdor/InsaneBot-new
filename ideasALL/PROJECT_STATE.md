# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **глобальная дедупликация и каталогизация собранных идей завершены; следующий этап — построение RoadMap.**

## Правила

- Исходные `COR-*`/`TOM-*` и тематические файлы сохраняются как трассировка.
- Одинаковые системы объединяются в канонические кластеры.
- При различиях сохраняются уникальные UX, поведение, настройки, ограничения и архитектурные варианты.
- Командные интерфейсы не считаются отдельными системами, если underlying mechanic уже есть.
- После глобальной дедупликации строится порядок реализации/RoadMap.
- На этапе исследования bot implementation не изменяется.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — ЗАВЕРШЁН.**
5. **GAwesomeBot/bot — ЗАВЕРШЁН.** PM, Private и полный `Commands/Public/` закрыты source-specific проходом.
6. **CorwinDev/Discord-Bot — ЗАВЕРШЁН.**
7. **Tomato6966/Multipurpose-discord-bot — ЗАВЕРШЁН.**

## Global Dedup

### Batch 1 — Core / Architecture / Storage / Access — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH1.md`

Зафиксированы канонические кластеры `GD-001–027`.

### Batch 2 — Economy / Community / Customization — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH2.md`

Зафиксированы канонические кластеры `GD-028–072`.

### Batch 3 — Audio / Filtering / Games / Trivia / Fun — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH3.md`

Зафиксированы канонические кластеры `GD-073–115`.

### Batch 4 — Moderation / Tickets — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH4.md`

Зафиксированы канонические кластеры `GD-116–160`.

### Batch 5 — Roles / Progression / Social / Stats / Reports / Events / Integrations / Streams / Modlog / Quality — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH5.md`

Зафиксированы канонические кластеры `GD-161–229`.

### Batch 6 — GAwesome PM / Private / подтверждённые Public mechanics — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH6.md`

Зафиксированы канонические кластеры `GD-230–259`.

### Batch 7 — GAwesome Web — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH7.md`

Зафиксированы канонические кластеры `GD-260–284`.

### Batch 8 — GAwesome Public final dedup — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH8.md`

Зафиксированы новые канонические кластеры `GD-285–287`: named persistent server countdowns, self/admin nickname management, role inspection with effective permissions.

### Batch 9 — Финальная сверка GAwesome Public — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH9.md`

Все `GAB-PUB-001–109` повторно сверены с `GD-001–287`. Новых самостоятельных механик не обнаружено; `GD-288+` искусственно не создавались.

## Следующая точка
**Глобальная дедупликация завершена на `GD-287`. Следующий этап — построение RoadMap реализации на основе полного канонического банка.**

`bot/main.py` и другая реализация InsaneBot не изменялись.
