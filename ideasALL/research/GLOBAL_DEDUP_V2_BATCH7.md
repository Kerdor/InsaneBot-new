# GLOBAL DEDUP V2 — Batch 7

## Scope

Повторная строгая сверка CorwinDev Batch 6–12 против `GD-001–287` и `GLOBAL_DEDUP_V2_BATCH1–6`.

Цель: не удалять исходные идеи, а объединять только действительно совпадающие системы/механики и сохранять уникальные детали как варианты внутри канонической системы.

Источники:
- `CORWIN_BATCH6.md` — COR-294–314
- `CORWIN_BATCH7.md` — COR-315–332
- `CORWIN_BATCH8.md` — COR-333–341
- `CORWIN_BATCH9.md` — COR-342
- `CORWIN_BATCH10.md` — COR-343–346
- `CORWIN_BATCH11.md` — COR-347–354
- `CORWIN_BATCH12.md` — COR-355–359

---

## 1. COR-294–314 — handlers/functions/security

### Полностью объединяется с существующими системами/инфраструктурой

- **COR-294** — централизованная permission-проверка → существующий global permission/access-control слой.
- **COR-295** — перевод permission bitfield в названия → деталь permission/error presentation.
- **COR-296** — поиск канала по mention/ID/name → общий Discord resource resolver.
- **COR-297** — защита текста от mentions → существующий mention-sanitization/AllowedMentions security слой.
- **COR-298** — beta subcommand через guild config → конфигурация + command routing, не отдельная система.
- **COR-299** — проверка temporary voice channel через БД → JTC/temporary voice infrastructure.
- **COR-300–302** — paginated leaderboard + author-bound controls + timeout → общая interactive pagination, с сохранением ownership/timeout деталей.
- **COR-304–307** — генераторы buttons/select menus → reusable Discord UI component infrastructure.
- **COR-308, COR-312, COR-313** — embed template, guild color, description limit → centralized embed/message presentation.
- **COR-309–311** — error/success/interaction response helpers → centralized response/error infrastructure.
- **COR-314** — anti-link/anti-invite на message edit → существующая anti-abuse/link protection система; важно сохранить поддержку edited messages.

### Отдельные кандидаты/механики, которые нельзя потерять

- **COR-303** — генерация Discord Activity invite через `target_application_id` → механика Discord Activities.

---

## 2. COR-315–319 — music

Все относятся к уже существующей Music/Audio системе, но детали сохраняются:

- **COR-315** — player controls через message buttons → существующая interactive music player UI.
- **COR-316** — восстановление radio после restart → radio persistence/recovery.
- **COR-317** — auto-restart radio stream после Idle/error → radio resilience.
- **COR-318** — auto-unsuppress в Stage Channel → voice connection lifecycle.
- **COR-319** — soundboard queue с последовательным проигрыванием → soundboard queue.

Дополнительно сверено с предыдущими music batches: это не новые standalone-системы.

---

## 3. COR-320–327 — games / XP

- **COR-320** — math expressions в counting → existing Counting system; сверить/объединить с Titan `TSVC-093`.
- **COR-321** — запрет двух последовательных ходов → existing Counting rule.
- **COR-322–325** — guess-number/guess-word/word-snake → existing Games/Fun domain, сохраняются как отдельные игровые механики.
- **COR-326–327** — XP helpers + leaderboard position → existing XP/Level/Leaderboard system.

---

## 4. COR-328–331 — Help / Links UI

- **COR-328** — category select help panel → existing Help/Discovery system.
- **COR-329** — button pagination + author restriction + timeout → existing reusable pagination + Help UI.
- **COR-330** — единая navigation panel внешних ссылок → Help/Links panel.
- **COR-331** — external link buttons → тот же Links/Help UI слой.

Не создавать отдельную систему на каждую страницу/кнопку.

---

## 5. COR-332–341 — loaders, interactions, Activities, Embed builder, moderation context menu

- **COR-332** — dynamic event loader → existing event/cog loader architecture; не новый пользовательский system.
- **COR-333** — subcommand dispatcher → command architecture.
- **COR-334** — встроенный category help → Help/Discovery.
- **COR-335** — deferReply перед длительной обработкой → interaction lifecycle.
- **COR-336** — запуск Discord Activities через slash command → объединить с COR-303 как **Discord Activities**; COR-337 сохраняется как voice precondition.
- **COR-337** — проверка voice channel перед Activity invite → Activity validation.
- **COR-338–340** — interactive Embed builder → существующая Custom Embed/Embed Builder система, сохраняя select-menu editing, temporary collector и temporary webhook delivery.
- **COR-341** — User Context Menu moderation flow → существующая Moderation/Warnings система; Modal/select-menu flow сохранить.

---

## 6. COR-342 — database cache

- **COR-342** — MongoDB query cache с TTL и max entries → **общая data/storage performance infrastructure**.

Это не пользовательская система. Сохранить как архитектурный вариант кэширования storage layer.

---

## 7. COR-343–346 — music lifecycle

Объединить с Music Player lifecycle:

- **COR-343** — destroy player при disconnect.
- **COR-344** — auto-leave после окончания queue.
- **COR-345** — стабилизация player после voice move через ping-based delay.
- **COR-346** — Now Playing Embed с track metadata и expected end timestamp.

Это детали существующей Music system, не новые standalone-системы.

---

## 8. COR-347–353 — Giveaway

Объединяются с существующей **Giveaway system (`GD-054`)** и предыдущими Titan/Corwin giveaway findings.

Сохранить как дополнительные механики:

- **COR-347** — bonus entries: maximum или cumulative bonuses.
- **COR-348** — исключение победителей по Discord permissions.
- **COR-349** — custom member filter callback.
- **COR-350** — разрешение/запрет bot accounts, per-giveaway или global default.
- **COR-351** — TTL хранения завершённых giveaway и невозможность reroll после удаления.
- **COR-352** — forced periodic message update.
- **COR-353** — сравнение Embed перед update + override через forceUpdateEvery.

Не создавать новые giveaway-системы для этих механик.

---

## 9. COR-354 — Weather

- **COR-354** — язык и единицы измерения в weather lookup → существующая Weather/External API utility.

Новый standalone ID не нужен, если Weather уже присутствует в общем каталоге; сохранить как параметр/вариант API.

---

## 10. COR-355–359 — startup / infrastructure

- **COR-355** — проверка новой версии через GitHub release → startup/update notification infrastructure.
- **COR-356** — публикация guild/shard/command metrics в Top.gg → существующая Top.gg integration + stats publishing.
- **COR-357** — автоматический respawn умершего shard → sharding resilience.
- **COR-358** — shard reconnect/disconnect webhook logging → centralized logging/monitoring.
- **COR-359** — единый override webhook credentials через `.env` → webhook configuration/credential management.

Это инфраструктурные механики, не standalone пользовательские системы.

---

## 11. Cross-check: важные объединения

### Counting
`COR-320` подтверждает и расширяет `TSVC-093`: math counting должен поддерживать expression и `left=right` вариант.

### Discord Activities
`COR-303 + COR-336 + COR-337` объединяются в одну Discord Activities систему с разными входами/проверками.

### Giveaway
`COR-347–353` добавляются к уже объединённому `GD-054` и Titan Giveaway механикам. Особенно не терять bonus entries, permission/custom filters, bot participation и cleanup TTL.

### Music
`COR-315–319 + COR-343–346` — детали одного Music/Audio domain, а не отдельные системы.

### Interactive UI
`COR-300–302`, `COR-329`, а также существующие pagination findings → общий reusable pagination/interaction ownership/timeout слой.

### Storage
`COR-342` не превращать в отдельную пользовательскую систему; это storage optimization.

---

## Итог Batch 7

- Новых подтверждённых standalone-систем: **0**.
- Найдены и объединены многочисленные дубли существующих систем.
- Новые/важные механики сохранены как детали существующих систем: Discord Activities, Counting math, Giveaway bonus/filter/cleanup, Music lifecycle, Weather parameters, storage cache и shard resilience.
- Исходные `COR-*` файлы **не удаляются**.
- Ничего полезного из исходных находок не исключается.
