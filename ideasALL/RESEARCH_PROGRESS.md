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

Полные source-specific checkpoints находятся в `research/` и `ideas/`.

## Этап 2 — глобальная дедупликация
Цель: собрать пересечения между всеми источниками, объединить идентичные механики, сохранить уникальные варианты и только после этого строить RoadMap.

### Batch 1 — Core / Architecture / Storage / Access — ✅ ЗАВЕРШЁН
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH1.md`
Результат: `GD-001–027`.

### Batch 2 — Economy / Community / Customization — ✅ ЗАВЕРШЁН
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH2.md`
Результат: `GD-028–072`.

### Batch 3 — Audio / Filtering / Games / Trivia / Fun — ✅ ЗАВЕРШЁН
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH3.md`
Результат: `GD-073–115`.

### Batch 4 — Moderation / Tickets — ✅ ЗАВЕРШЁН
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH4.md`
Результат: `GD-116–160`.

### Batch 5 — Roles / Progression / Social / Stats / Reports / Events / Integrations / Streams / Modlog / Quality — ✅ ЗАВЕРШЁН
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH5.md`
Результат: `GD-161–229`.

### Batch 6 — GAwesome PM / Private / подтверждённые Public mechanics — ✅ ЗАВЕРШЁН
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH6.md`
Результат: `GD-230–259`.

### Batch 7 — GAwesome Web — ✅ ЗАВЕРШЁН
Файл: `ideasALL/research/GLOBAL_DEDUP_BATCH7.md`
Результат: `GD-260–284`.

Основные объединения: web DTO/presentation layer, privacy-aware profiles, public server listings, extension gallery/versioning, dashboard control plane, bulk/transactional/partial configuration, Discord web authentication, route-level authorization, XSS-safe Markdown, controller/API separation, isolated public/maintainer surfaces и web server lifecycle.

## Следующая точка
Начать **Global Dedup Batch 8**: повторно сверить оставшиеся GAwesome Public mechanics с `GD-001–284` и зафиксировать только действительно новые канонические кластеры, начиная с `GD-285`. RoadMap пока не строить.

`bot/main.py` и реализация InsaneBot не изменялись.
