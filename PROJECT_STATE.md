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

## Источники

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — ЗАВЕРШЁН.**
3. **ItzSudhan/Discord-MusicBot — ЗАВЕРШЁН.**
4. **codebymitch/TitanBot — АКТИВНО ИССЛЕДУЕТСЯ.**
5. GAwesomeBot/bot — ОЖИДАЕТ.
6. CorwinDev/Discord-Bot — ОЖИДАЕТ.
7. Tomato6966/Multipurpose-discord-bot — ОЖИДАЕТ.

## `ItzSudhan/Discord-MusicBot` — ЗАВЕРШЁН

Ветка: `v5`. Recursive tree проверен полностью (`truncated=false`), исходные каталоги закрыты и build artifacts отдельно классифицированы.

Пакеты идей:
- `ideas/MUSIC.md` — MUSIC-001–042;
- `ideas/MUSIC_COMMANDS.md` — MUSIC-C001–055;
- `ideas/MUSIC_CONTEXT.md` — MUSIC-X001–007;
- `ideas/MUSIC_EVENTS.md` — MUSIC-E001–025;
- `ideas/MUSIC_STORAGE.md` — MUSIC-S001–018;
- `ideas/MUSIC_CORE.md` — MUSIC-K001–018;
- `ideas/MUSIC_WEB.md` — MUSIC-W001–031;
- `ideas/MUSIC_DEPLOY.md` — MUSIC-D001–026.

## `codebymitch/TitanBot` — АКТИВЕН

Recursive tree `main` проверен полностью (`truncated=false`). На текущем этапе просмотрены Root/bootstrap, Birthday, Community, Core, Economy, Fun и Giveaway.

Пакеты TitanBot:
- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md`;
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065.

Fun закрыт на уровне просмотренных command/service файлов: counting game с 8 системами счёта, streak/leaderboard/reset/status, random duel, coin flip и dice notation.

Giveaway закрыт на уровне просмотренных command/service файлов: create/join/end/delete/reroll, автоматическое истечение, random unique winner selection, persistent lifecycle state, rate limit, fallback recovery и audit logging.

### Точная точка продолжения

**`src/commands/JoinToCreate/`**.

Уже начат `src/commands/JoinToCreate/jointocreate.js`; файл большой и был просмотрен частично. Следом полностью выжать его оставшуюся логику, затем `modules/config_setup.js`, `modules/setup.js`, `src/services/joinToCreateService.js`. После этого — `Leveling`.

**Не переходить к GAwesomeBot до полного закрытия TitanBot.**
