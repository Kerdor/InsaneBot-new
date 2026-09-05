# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **максимально глубокий сбор и каталогизация идей/механик из сторонних Discord-ботов.**

## Правила

- Источники исследуются строго по очереди и не переключаются до полного завершения текущего.
- Собираем максимально всё, включая очевидные, маленькие и потенциально бесполезные механики.
- Перед добавлением сверяем банк идей; идентичные дубликаты не размножаем.
- Для существующей системы сохраняем только новые UX, поведение, настройки, ограничения или архитектурные варианты.
- Идеи сразу распределяются по тематическим `ideas/`; новые тематические файлы разрешены.
- Работа ведётся большими батчами, но с фиксацией точной точки продолжения.

## Восстановление после смены чата

- `RESEARCH_PROGRESS.md` — глобальная контрольная точка.
- `research/<source>.md` — последовательный журнал источника.
- `✅` означает реальный просмотр и сверку.
- После каждого существенного батча обновляются журнал и `PROJECT_STATE.md`.

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — АКТИВЕН.**
3. ItzSudhan/Discord-MusicBot — ОЖИДАЕТ.
4. codebymitch/TitanBot — ОЖИДАЕТ.
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `python-discord/bot` — текущая точка

Полное recursive tree получено на tree SHA `0e4cd5cb46f2239eacccdded8cdf02ba89028ab9`.

Полностью обработаны `bot/exts/backend/`, `bot/exts/filtering/`, `bot/exts/fun/`, `bot/exts/help_channels/` и `bot/exts/info/`.

`bot/exts/moderation/` теперь полностью закрыт: все root-файлы, `infraction/` и `watchchannels/` просмотрены.

Дополнительные moderation-пакеты:
- `PYTHON_DISCORD_MODERATION_2.md` — `PDIS-M2-001`–`PDIS-M2-016`;
- `PYTHON_DISCORD_MODERATION_3.md` — `PDIS-M3-001`–`PDIS-M3-015`;
- `PYTHON_DISCORD_MODERATION_4.md` — `PDIS-M4-001`–`PDIS-M4-011`;
- `PYTHON_DISCORD_MODERATION_5.md` — `PDIS-M5-001`–`PDIS-M5-012`.

## Следующая точка

Продолжать **только `python-discord/bot`**. Следующий этап — большой финальный проход recursive tree по ещё не закрытым каталогам/файлам за пределами уже обработанных `backend`, `filtering`, `fun`, `help_channels`, `info`, `moderation`. После каждого крупного участка обновлять research/state.

`ItzSudhan/Discord-MusicBot` не трогать до полного закрытия `python-discord/bot`.

**Другие источники не трогать.**
