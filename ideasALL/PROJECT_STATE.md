# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **повторная глобальная дедупликация V2 всех idea-файлов. RoadMap временно отложен до завершения V2.**

Причина: после более строгой повторной проверки обнаружились дополнительные случаи, где source-specific системы являются расширениями уже существующих кластеров, а также несколько самостоятельных механик, которые нельзя терять. Первоначальный `GD-001–287` теперь считается предыдущим уровнем канонизации, а не окончательным результатом.

## Правила

- Исходные `COR-*`/`TOM-*`, source-specific и тематические файлы **не удаляются**.
- Одинаковые системы объединяются в канонические кластеры.
- При различиях сохраняются уникальные UX, поведение, настройки, ограничения, recovery и архитектурные варианты.
- Командные интерфейсы не считаются отдельными системами, если underlying mechanic уже есть.
- Если объединение сомнительно, запись сохраняется отдельно до подтверждения.
- Никакая полезная деталь не удаляется только ради уменьшения количества IDs.
- После V2 формируется окончательный канонический индекс, и только затем строится RoadMap.
- На этапе исследования bot implementation не изменяется.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — ЗАВЕРШЁН.**
5. **GAwesomeBot/bot — ЗАВЕРШЁН.** PM, Private и полный `Commands/Public/` закрыты source-specific проходом.
6. **CorwinDev/Discord-Bot — ЗАВЕРШЁН.**
7. **Tomato6966/Multipurpose-discord-bot — ЗАВЕРШЁН.**

## Previous Global Dedup

Первоначальная дедупликация была выполнена в Batch 1–9 и довела канонический банк до `GD-287`.

- `GLOBAL_DEDUP_BATCH1.md` → `GD-001–027`
- `GLOBAL_DEDUP_BATCH2.md` → `GD-028–072`
- `GLOBAL_DEDUP_BATCH3.md` → `GD-073–115`
- `GLOBAL_DEDUP_BATCH4.md` → `GD-116–160`
- `GLOBAL_DEDUP_BATCH5.md` → `GD-161–229`
- `GLOBAL_DEDUP_BATCH6.md` → `GD-230–259`
- `GLOBAL_DEDUP_BATCH7.md` → `GD-260–284`
- `GLOBAL_DEDUP_BATCH8.md` → `GD-285–287`
- `GLOBAL_DEDUP_BATCH9.md` → финальная сверка GAwesome Public без новых GD

## Global Dedup V2

### Batch 1 — Python Discord повторная сверка — В ПРОЦЕССЕ
`ideasALL/research/GLOBAL_DEDUP_V2_BATCH1.md`

Проверены дополнительные Python Discord role/access/UI, Advanced, Backend, Core Utils и Moderation 2–3 материалы.

Обнаружены важные объединения и дополнительные кандидаты, включая:
- persistent self-role UI recovery;
- temporary permission-role lifecycle;
- channel silence/restore;
- context-aware command whitelist/redirect;
- linked/alternate accounts with context;
- scheduled role with manual override;
- multi-source latency diagnostics;
- WebSocket event-rate diagnostics;
- persistent REPL eval;
- source-code links;
- API diff/reconciliation sync;
- emergency server lockdown;
- incident reaction state machine;
- advanced bulk-clean;
- modlog suppression tokens;
- resource locking;
- bounded message cache.

### Следующий этап V2
Повторно проверить оставшиеся тематические/source-specific файлы и сопоставить их **между собой**, а не только с предыдущими `GD`.

После завершения всех V2 passes:
1. объединить подтверждённые кластеры;
2. сохранить все source IDs и уникальные детали;
3. проверить, что ни одна исходная механика не потеряна;
4. только после этого считать global dedup окончательным;
5. затем строить RoadMap.

`bot/main.py` и другая реализация InsaneBot не изменялись.
