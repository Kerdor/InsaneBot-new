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
`GD-285–287`

### Batch 9 — Финальная сверка GAwesome Public — ✅
Все `GAB-PUB-001–109` повторно сверены с `GD-001–287`. Новых самостоятельных механик не обнаружено.

## Этап 2.5 — Global Dedup V2 — ✅

V2 выполнен в `GLOBAL_DEDUP_V2_BATCH1–13`.

Основные результаты:
- source-specific и thematic idea-файлы повторно сопоставлены между собой;
- infrastructure/helper/command-level findings не раздувают canonical system count;
- уникальные UX, constraints, recovery и lifecycle mechanics сохранены;
- Access Control, Global Broadcast, Installation Serverlock и другие V2 candidates сохранены;
- Reports / User Reports, Social Relations / Social Interactions и Statistics / Analytics подтверждены как отдельные candidates;
- `INDEX.md` и `README.md` проверены как административные файлы без новых mechanics.

### V2 Batch 13 — финальный проход — ✅
`ideasALL/research/GLOBAL_DEDUP_V2_BATCH13.md`

**Global Dedup V2 all-files audit завершён.**

## Этап 3 — Canonical Index — СЛЕДУЮЩИЙ ЭТАП

До RoadMap необходимо создать окончательный canonical index:

1. стабильные canonical IDs;
2. canonical names;
3. domain grouping;
4. source-ID mapping;
5. уникальные mechanics/UX/constraints/recovery;
6. границы между user-facing systems, subsystems и infrastructure;
7. финальная проверка на пропуски и дубли.

### Этап 4 — RoadMap

**Пока НЕ НАЧИНАЕМ.** RoadMap строится только после завершения canonical index.

`bot/main.py` и реализация InsaneBot не изменялись.
