# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения исследования без потери позиции.

## Этап 1 — сбор источников
Все 7 основных источников исследованы и source-specific checkpoints закрыты.

1. `Cog-Creators/Red-DiscordBot` — ✅
2. `python-discord/bot` — ✅
3. `ItzSudhan/Discord-MusicBot` — ✅
4. `codebymitch/TitanBot` — ✅
5. `GAwesomeBot/bot` — ✅ PM, Private и полный `Commands/Public/` закрыты
6. `CorwinDev/Discord-Bot` — ✅
7. `Tomato6966/Multipurpose-discord-bot` — ✅

## Этап 2 — глобальная дедупликация
Цель: собрать пересечения между всеми источниками, объединить идентичные механики, сохранить уникальные варианты и только после этого строить RoadMap.

### Batch 1 — Core / Architecture / Storage / Access — ✅
`GD-001–027`

### Batch 2 — Economy / Community / Customization — ✅
`GD-028–072`

### Batch 3 — Audio / Filtering / Games / Trivia / Fun — ✅
`GD-073–115`

### Batch 4 — Moderation / Tickets — ✅
`GD-116–160`

### Batch 5 — Roles / Progression / Social / Stats / Reports / Events / Integrations / Streams / Modlog / Quality — ✅
`GD-161–229`

### Batch 6 — GAwesome PM / Private / подтверждённые Public mechanics — ✅
`GD-230–259`

### Batch 7 — GAwesome Web — ✅
`GD-260–284`

### Batch 8 — GAwesome Public final dedup — ✅
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH8.md`
Результат: `GD-285–287`.

Новые механики:
- `GD-285` — named persistent server countdowns.
- `GD-286` — self/admin nickname management.
- `GD-287` — role inspection with effective permissions.

Остальные финальные Public-команды сверены с уже существующими кластерами; новых GD для них не создавалось.

## Следующая точка
Продолжить глобальную дедупликацию с `GD-288`. RoadMap пока не строить.

`bot/main.py` и реализация InsaneBot не изменялись.
