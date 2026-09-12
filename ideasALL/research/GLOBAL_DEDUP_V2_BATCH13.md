# Global Dedup V2 — Batch 13

Дата: 2026-09-12

## Scope

Финальный проход по оставшимся служебным файлами банка идей:

- `ideasALL/ideas/INDEX.md`
- `ideasALL/ideas/README.md`

Дополнительно выполнена финальная сверка новых V2-кандидатов из Batch 11 с уже проведёнными source-specific и thematic passes.

Правило сохраняется: служебный индекс/README не считаются источниками новых mechanics сами по себе; command names, категории и навигационные записи не превращаются в standalone systems.

## 1. INDEX.md

**Итог: 0 новых standalone-систем.**

`INDEX.md` содержит только навигационный перечень документов и их тематические разделы. Новых механик, source IDs или поведенческих деталей, отсутствующих в соответствующих idea-файлах, здесь нет.

Отдельно подтверждено:

- `STATS.md` — источник Statistics/Analytics candidate из Batch 11;
- `ACCESS_CONTROL.md` — Access Control candidate из Batch 8;
- `CORE_FRAMEWORK.md`, `DATA_STORAGE.md`, `AUDIO_INFRA.md`, `QUALITY_AND_RELEASE.md` уже закрыты предыдущими V2 passes.

## 2. README.md

**Итог: 0 новых standalone-систем.**

README описывает назначение банка, структуру документов, список источников и статусы идей. Поведенческих механик или дополнительных source-specific findings, которых нет в idea-файлах, не содержит.

## 3. Финальная cross-check новых кандидатов Batch 11

### Reports / User Reports

Остаётся самостоятельной системой.

Не объединять с Tickets: report имеет собственную сущность, последовательную нумерацию, author/staff communication tunnel и lifecycle без обязательного ticket channel.

Не объединять с User Notes или ModLog: это разные storage/lifecycle semantics.

### Social Relations / Social Interactions

Остаётся самостоятельным social domain.

Family/kinship, friendship, romance/compatibility, relationship requests/list/rankings образуют один coherent Social Relations domain. AFK из `SOCIAL.md` остаётся отдельным существующим user-status domain и в этот кандидат не входит.

Не объединять Social Relations с generic reactions, Fun interactions или AFK только из-за пересечения UI/interaction surface.

### Statistics / Analytics

Остаётся самостоятельным analytics domain.

Важно сохранить границу:

- counters — оперативная presentation mechanic;
- Statistics/Analytics — исторические/агрегированные показатели, периоды, activity data, leaderboards, heatmaps и reports.

Server statistics/counter providers из Corwin не создают вторую систему: они остаются source variants/providers внутри соответствующего counters/statistics boundary.

## 4. Final V2 audit result

Все idea-файлы, содержащие содержательные mechanics, покрыты V2 passes:

- Python Discord / Advanced / Backend / Core Utils / Deployment / Filtering / Fun / Help / Info / Moderation / Recruitment / Testing / Utils;
- Titan Core / Config / Applications / JoinToCreate / Giveaway / Reaction Roles / Leveling / Logging / Music / Search / ServerStats / Services / Tickets / Tools / Utility / Utils и связанные файлы;
- Corwin batches 1–12;
- Tomato batches 1–20 и parts;
- GAwesome PM / Private / Public / Shared / Config / Database / Internals / Modules / Web;
- thematic/domain files;
- remaining administrative `INDEX.md` и `README.md`.

Служебные файлы не добавляют новых systems.

## 5. Result

**Batch 13: 0 новых standalone-систем.**

**Global Dedup V2 audit завершён.**

Итоговые подтверждённые V2 candidates, которые должны попасть в следующий canonical index:

1. Reports / User Reports.
2. Social Relations / Social Interactions.
3. Statistics / Analytics.

Ранее подтверждённые candidates из предыдущих V2 passes также сохраняются: V2 не отменяет ни один source ID или canonical cluster без отдельного решения.

## Next step

Следующий этап — не RoadMap.

Сначала нужно собрать **окончательный canonical index**: стабильные canonical IDs, названия систем, source-ID mapping, domain grouping и preservation of unique mechanics.

Только после этого можно переходить к построению RoadMap реализации.

Исходные idea/source файлы не изменялись и не удалялись.
