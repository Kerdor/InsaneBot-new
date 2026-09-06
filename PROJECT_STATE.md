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

## `codebymitch/TitanBot` — АКТИВЕН

Recursive tree `main` проверен полностью (`truncated=false`). Закрыты Root/bootstrap, Birthday, Community, Core, Economy, Fun, Giveaway, JoinToCreate, Leveling, Logging, Moderation и Music.

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
- `ideas/MODERATION.md` — MOD-001–MOD-135;
- `ideas/TITAN_MUSIC.md` — TM-001–TM-154.

Music закрыт по command/service/handler/config paths: playback и queue controls, duplicate protection, requester metadata, loop/volume/seek, queue pagination, persistent Now Playing UI, auto-pause/resume, idle/24-7 lifecycle, Lavalink/Riffy setup, multi-node configuration, shard voice routing, lifecycle/error handling и shutdown.

Moderation закрыт по всем файлам `src/commands/Moderation/` и moderation services: centralized ModerationService, moderator/bot hierarchy validation, owner bypass, ban/kick/timeout/untimeout/unban, warnings, case IDs, mass ban/kick, purge, lock/unlock, staff DM, say, cases pagination и user notes.

### Точная точка продолжения

**Следующий раздел: `src/commands/Reaction_roles/`.**

После закрытия `Reaction_roles/` продолжать строго по порядку дерева `src/commands/`.

**Не переходить к GAwesomeBot до полного закрытия TitanBot.**
