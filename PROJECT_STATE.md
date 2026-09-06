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

Ветка: `v5`.

Recursive tree проверен полностью (`truncated=false`). Закрыты все исходные каталоги и root-файлы, включая `commands/`, `events/`, `lib/`, `util/`, `api/`, исходный `dashboard/`, `deploy/`, `docker/`, `.github/` и оставшиеся root/config/runtime files. `dashboard/out/` и `_next` классифицированы как build artifacts и не дублировались поверх исходников.

Пакеты идей:
- `ideas/MUSIC.md` — MUSIC-001–042;
- `ideas/MUSIC_COMMANDS.md` — MUSIC-C001–055;
- `ideas/MUSIC_CONTEXT.md` — MUSIC-X001–007;
- `ideas/MUSIC_EVENTS.md` — MUSIC-E001–025;
- `ideas/MUSIC_STORAGE.md` — MUSIC-S001–018;
- `ideas/MUSIC_CORE.md` — MUSIC-K001–018;
- `ideas/MUSIC_WEB.md` — MUSIC-W001–031;
- `ideas/MUSIC_DEPLOY.md` — MUSIC-D001–026.

Последняя сверка добавила Docker/Lavalink варианты: разделение bot/Lavalink на сервисы, `depends_on`, internal network, read-only config mounts, self-hosted Lavalink и отдельные параметры buffering/quality/metrics/request logging/rolling logs.

Журнал: `research/discord-music-bot.md` — статус `✅ ЗАВЕРШЁН`.

## `codebymitch/TitanBot` — АКТИВЕН

Следующая точка: начать с recursive tree репозитория `codebymitch/TitanBot`, определить актуальную ветку и полностью пройти дерево по порядку. Создать `research/titanbot.md`; идеи сразу сравнивать с существующим банком и распределять по тематическим файлам.

**Не переходить к GAwesomeBot и последующим источникам до полного завершения TitanBot.**
