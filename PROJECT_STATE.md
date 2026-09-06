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

Ветка: `v5`. Recursive tree `truncated=false`, исходные каталоги закрыты и build artifacts отдельно классифицированы.

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

Recursive tree `main` проверен полностью (`truncated=false`). Обработаны Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging и Moderation.

Пакеты TitanBot:
- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md`;
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065;
- `ideas/TITAN_JOINTOCREATE.md` — TJ-001–TJ-080;
- `ideas/TITAN_LEVELING.md` — TL-001–TL-100;
- `ideas/TITAN_LOGGING.md` — TLOG-001–TLOG-100;
- `ideas/MODERATION.md` — MOD-001–MOD-135.

JoinToCreate закрыт по просмотренным command/service/event paths: temporary voice channels, ownership transfer, auto-delete, configurable naming, bitrate/user limits, interactive dashboard, stale-state cleanup, cooldowns и permission/error handling.

Leveling закрыт по просмотренным command/service/event paths: XP range/cooldown/multiplier, ignored channels/roles/users, mutex-protected XP updates, level progression до 1000, rank/leaderboard, role rewards, announcements, admin level controls и interactive dashboard.

Logging закрыт по command/modules/service/UI/handler и связанным event logging paths: отдельные Audit/Applications/Reports destinations, global/category/event toggles, wildcard category controls, user/channel ignore filters, permission checks, fallback/legacy channel resolution, unified audit embed builder, Before/After comparison, metadata/attachments, lifecycle logging участников/ролей/сообщений и resilient error handling.

Moderation закрыт по всем файлам `src/commands/Moderation/` и moderation services: centralized ModerationService, moderator/bot hierarchy validation, owner bypass, ban/kick/timeout/untimeout/unban, warnings, case IDs, mass ban/kick, purge, lock/unlock, staff DM, say, cases pagination и user notes. В `ideas/MODERATION.md` добавлен большой TitanBot-пакет MOD-044–MOD-135.

### Точная точка продолжения

**Следующий раздел: `src/commands/Music/`.**

После определения и закрытия `Music/` продолжать строго по порядку дерева `src/commands/`.

**Не переходить к GAwesomeBot до полного закрытия TitanBot.**
