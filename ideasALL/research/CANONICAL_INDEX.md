# Canonical Index

Единый индекс канонических систем InsaneBot.

## Статус

- Initial Global Dedup: `GD-001–287`.
- Global Dedup V2: завершён, Batch 1–13.
- Канонический индекс: **готов**.
- RoadMap можно строить после этого файла.
- Source-specific файлы не заменяются и не удаляются: они остаются evidence layer.

## Правила

- Один `GD` = одна самостоятельная система/механика, а не одна команда.
- UX, recovery, ограничения и варианты реализации сохраняются внутри системы.
- Source IDs не удаляются.
- Инфраструктурные детали не превращаются в отдельные системы без самостоятельной ценности.
- Новые canonical IDs добавляются только при наличии source evidence.

## Existing canonical bank

Первоначальный банк `GD-001–287` сохраняется без перенумерации.

| Диапазон | Источник канонизации |
|---|---|
| GD-001–027 | Historical Batch 1; исходный файл отсутствует в текущем tree, поэтому названия не восстанавливаются догадкой |
| GD-028–072 | `GLOBAL_DEDUP_BATCH2.md` |
| GD-073–115 | `GLOBAL_DEDUP_BATCH3.md` |
| GD-116–160 | `GLOBAL_DEDUP_BATCH4.md` |
| GD-161–229 | `GLOBAL_DEDUP_BATCH5.md` |
| GD-230–259 | `GLOBAL_DEDUP_BATCH6.md` |
| GD-260–284 | `GLOBAL_DEDUP_BATCH7.md` |
| GD-285–287 | `GLOBAL_DEDUP_BATCH8.md` |
| Final cross-check | `GLOBAL_DEDUP_BATCH9.md` |

## V2 additions

V2 добавил **20** новых самостоятельных систем. IDs `GD-288–307` являются стабильными.

| ID | Canonical system | Основные источники |
|---|---|---|
| GD-288 | Linked Accounts / Alternate Accounts | PDIS-A001 |
| GD-289 | Scheduled Role with Manual Override | PDIS-A002 |
| GD-290 | Multi-source Latency Healthcheck | PDIS-A007 |
| GD-291 | WebSocket Event-rate Diagnostics | PDIS-A008 |
| GD-292 | Persistent REPL / Eval Environment | PDIS-A009 |
| GD-293 | Source Links for Commands / Cogs | PDIS-A010 |
| GD-294 | Moderation-only Echo / Embed Relay | PDIS-A012 |
| GD-295 | API Diff / Reconciliation Sync | PDIS-B004 |
| GD-296 | Emergency Server Lockdown | PDIS-M2-003 |
| GD-297 | Modlog Suppression Tokens | PDIS-M3-001 |
| GD-298 | Compromise-response Preset | PDIS-M4-002 |
| GD-299 | Applications / Staff Application Workflow | TITAN-A001–A025, TSVC-011–026 |
| GD-300 | Invite Tracking & Statistics | COR-229–230, COR-249–255 |
| GD-301 | Starboard | COR-260–268 |
| GD-302 | Access Control / Allowlist / Blocklist | ACCESS-001–011 |
| GD-303 | Global Broadcast | ARCH-031–032 |
| GD-304 | Installation Serverlock | ARCH-033 |
| GD-305 | User Reports | REPORT-001–007 |
| GD-306 | Social Relations / Interactions | SOCIAL-001–003, SOCIAL-008–015 |
| GD-307 | Statistics / Analytics | STAT-006–025 |

## Important V2 merges / boundaries

- Temporary permission-role lifecycle, channel silence/restore, bounded message cache и resource locking остаются важными reusable subsystems, но не получают отдельные IDs здесь, если они являются infrastructure/workflow слоями существующих систем.
- Discord Activities (`COR-303`, `COR-336–337`) — одна Activity system, без дублирования по source.
- Storage degradation/graceful degradation — infrastructure capability, а не отдельная пользовательская система.
- Applications не объединяются с Tickets: lifecycle и сущность разные.
- Invite Tracking не объединяется с обычными server counters.
- Starboard не объединяется с reaction roles или message audit.
- Reports не объединяются с Tickets/User Notes.
- Social Relations не объединяются с AFK.
- Statistics/Analytics не объединяются с Counters.
- Access Control / ACL не объединяется с command guards: ACL хранит управляемые списки доступа, guards контролируют выполнение.
- Installation Serverlock не является обычным command permission: он контролирует допустимые guild для bot instance.

## V2 audit coverage

`GLOBAL_DEDUP_V2_BATCH1–13` завершили повторную cross-source проверку Python Discord, Titan, CorwinDev, Tomato, GAwesome и thematic/architecture files.

Batch 1–11 выявили и проверили новые standalone-системы; Batch 12–13 не добавили новых систем и подтвердили итоговый набор.

**Итог:** `GD-001–307` — текущий канонический банк после Global Dedup V2.

## Next step

**Следующий этап — RoadMap реализации.**

Новые canonical IDs без новой source evidence больше не добавлять.