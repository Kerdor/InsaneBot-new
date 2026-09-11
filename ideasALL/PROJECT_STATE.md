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

Зафиксированы канонические кластеры `GD-028–072`: базовая экономика, кошелёк/банк, магазин и инвентарь, периодические награды, PayDay, P2P, административные операции, лимиты баланса, лидерборды, Economy API, rob/crime, fishing/hunt/mine, gambling, глобальный/серверный режим, economy reset/prune, giveaways, JTC, counters, role panels, birthdays, user notes, moderation cases, ticket workflow/priority/limits/transcripts, custom commands, aliases, triggers, placeholders, embeds, welcome/goodbye и per-server configuration.

### Следующая точка
Продолжить глобальную дедупликацию следующего крупного тематического блока. Batch 1–2 повторно не пересобирать без новых исходных данных.

`bot/main.py` и другая реализация InsaneBot не изменялись.
