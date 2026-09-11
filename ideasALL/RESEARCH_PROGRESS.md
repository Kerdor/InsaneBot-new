# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения исследования без потери позиции.

## Этап 1 — сбор источников
Основные 7 источников исследованы, но при дополнительной сверке обнаружено, что `GAwesomeBot/Commands/Public/` в source-specific checkpoint был помечен как незакрытый. Поэтому его финальный проход не считаем закрытым до фактического завершения.

1. `Cog-Creators/Red-DiscordBot` — ✅
2. `python-discord/bot` — ✅
3. `ItzSudhan/Discord-MusicBot` — ✅
4. `codebymitch/TitanBot` — ✅
5. `GAwesomeBot/bot` — ⚠️ PM/Private закрыты; Public требует финального прохода
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

Основные объединения: DM profile wizard, personal server aliases, DM control-plane/relay, DM poll/giveaway workflows, dynamic permission-aware help, channel cooldown/quiet, persistent counters, structured message archive, filtered bulk cleanup, emoji tooling, URL redirect safety, temporary talk rooms, server to-do list, points lottery, weekly stats reset, command-usage stats, rank-specific leaderboards, RSS aliases, NSFW provider gates и Bitly utility.

Важно: Batch 6 не закрывает весь GAwesome Public. Дополнительные Public-файлы ещё должны пройти source-specific review и затем попасть в отдельный dedup pass.

## Следующая точка
Закончить `GAwesomeBot/Commands/Public/`, затем повторно сверить новые GAwesome mechanics с `GD-001–259`. RoadMap пока не строить.

`bot/main.py` и реализация InsaneBot не изменялись.
