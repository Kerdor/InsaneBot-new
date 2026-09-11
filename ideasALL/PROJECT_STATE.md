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

Зафиксированы канонические кластеры `GD-001–027`.

### Batch 2 — Economy / Community / Customization — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH2.md`

Обработаны:
- `ECONOMY.md`
- `ECONOMY_ADVANCED.md`
- `COMMUNITY.md`
- `CUSTOMIZATION.md`

Зафиксированы канонические кластеры `GD-028–072`.

### Batch 3 — Audio / Filtering / Games / Trivia / Fun — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH3.md`

Обработаны:
- `AUDIO_INFRA.md`
- `FILTERING.md`
- `GAMES.md`
- `GAMES_TRIVIA_ADVANCED.md`
- `FUN.md`

Зафиксированы канонические кластеры `GD-073–115`.

### Batch 4 — Moderation / Tickets — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH4.md`

Обработаны:
- `MODERATION.md`
- `TICKETS.md`

Зафиксированы канонические кластеры `GD-116–160`: moderation hierarchy/safety, warnings, warning points, bans/tempbans, mute/timeout, moderation cases, mass moderation, purge, lock/unlock, staff DM и ticket panel/workflow/claim/priority/limits/transcripts/multiple systems.

### Batch 5 — Roles / Progression / Social / Stats / Reports / Events / Integrations / Streams / Modlog / Quality — ЗАВЕРШЁН
`ideasALL/research/GLOBAL_DEDUP_BATCH5.md`

Обработаны:
- `ROLES.md`
- `PROGRESSION.md`
- `SOCIAL.md`
- `STATS.md`
- `REPORTS.md`
- `EVENTS.md`
- `INTEGRATIONS.md`
- `INTEGRATIONS_STREAMS_ADVANCED.md`
- `MODLOG.md`
- `QUALITY_AND_RELEASE.md`

Зафиксированы канонические кластеры `GD-161–229`: selfroles/managed roles, XP/levels, social/AFK/relations, activity statistics, reports, persistent/recurring events, external integrations and credentials, multi-provider stream monitoring, moderation case lookup/editing/rendering и CI/security/release automation.

### Следующая точка
Продолжить глобальную дедупликацию следующего крупного тематического блока. Batch 1–5 повторно не пересобирать без новых исходных данных.

`bot/main.py` и другая реализация InsaneBot не изменялись.
