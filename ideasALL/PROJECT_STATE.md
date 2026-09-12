# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **Global Dedup V2 завершён. Следующий этап — построение окончательного canonical index. RoadMap пока не начинаем.**

Причина V2: после первоначального `GD-001–287` повторная cross-source проверка обнаружила дополнительные случаи, где source-specific системы являются расширениями уже существующих кластеров, а также несколько самостоятельных механик, которые нельзя терять.

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

V2 завершён в Batch 1–13.

### Batch 1 — Python Discord повторная сверка
Проверены дополнительные Python Discord role/access/UI, Advanced, Backend, Core Utils и Moderation 2–3 материалы. Выделены дополнительные reusable subsystems и кандидаты, включая linked accounts, scheduled roles, diagnostics, persistent REPL, source links, API reconciliation, emergency lockdown, resource locking и bounded message cache.

### Batch 2 — тематические банки + Python Discord moderation/roles/community/customization/music/economy
Подтверждены границы между платформами и отдельными mechanics; source variants объединены без потери поведения.

### Batch 3 — Titan Core/Config/Applications/JTC/Giveaway/Reaction Roles
Проверены Titan lifecycle/config/application/JTC/giveaway/reaction-role материалы. Новые кандидаты и важные domain mechanics сохранены.

### Batch 4 — Corwin Batch 4–5
Проверены guild lifecycle, audit/logging, invite tracking, starboard, server statistics, verification и temporary voice/JTC.

### Batch 5 — Titan Tickets/Economy
Подтверждены Ticket Platform и Economy clusters; добавлены важные ticket-platform mechanics: multi-ticket systems per guild, participants, rename, notice/follow-up, instant close/delete paths.

### Batch 6 — Titan Services
Service-layer mechanics привязаны к существующим domain systems и infrastructure; новых standalone systems нет.

### Batch 7 — Corwin Batch 6–12
Повторно проверены handlers/security, music, games, XP, help, Activities, embed builder, giveaway, weather и startup infrastructure. Новых standalone systems нет.

### Batch 8 — оставшиеся thematic/architecture files
Проверены Access Control, Architecture, Core Framework, Configuration, Data Storage, Audio Infra и Quality/Release. Подтверждены candidates:
- Access Control / Allowlist / Blocklist;
- Global Broadcast;
- Installation Serverlock.

### Batch 9 — Cog Management
`COG-001–024` объединены в единый Cog / Extension Management lifecycle.

### Batch 10 — second pass Community/Events/Filtering/Games/Economy/Customization/Moderation/command catalog
Новых standalone systems не найдено; подтверждены важные distinction rules.

### Batch 11 — оставшиеся thematic/GAwesome/Music files
Проверены PM, Private, Shared, Config, General UX, Help UX, Permissions, Progression, Reports, Social, Stats, Utility и Music thematic files.

Новые candidates:
1. **Reports / User Reports** — `REPORT-001–007`.
2. **Social Relations / Social Interactions** — `SOCIAL-001–003`, `SOCIAL-008–015`.
3. **Statistics / Analytics** — `STAT-006–025`.

`PERM-001–010` объединены с Access Control; counters из `STAT-001–005` остались отдельным counters domain.

### Batch 12 — GAwesome infrastructure
Проверены `GAWESOME_DATABASE.md`, `GAWESOME_INTERNALS.md`, `GAWESOME_MODULES.md`, `GAWESOME_WEB.md`. Новых standalone systems нет.

### Batch 13 — final administrative files + candidate cross-check
Проверены `INDEX.md` и `README.md`; новых mechanics нет. Дополнительно подтверждено, что Reports, Social Relations и Statistics/Analytics не поглощаются Tickets, AFK/Counters или generic interaction infrastructure.

**Batch 13 завершает V2 all-files audit.**

## Next step: canonical index

До RoadMap необходимо:
1. собрать окончательный список canonical systems;
2. назначить стабильные canonical IDs;
3. сгруппировать systems по domains;
4. привязать source IDs к canonical entries;
5. сохранить уникальные mechanics/UX/constraints/recovery;
6. отдельно отметить infrastructure/subsystems и границы между ними;
7. проверить canonical index на пропуски и дубли.

Только после этого открывать RoadMap реализации.

`bot/main.py` и другая реализация InsaneBot не изменялись.
