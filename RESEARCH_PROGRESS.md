# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения глубокого исследования в новом чате без потери позиции.

## Правила

- Источники исследуются строго по очереди.
- Внутри активного репозитория фиксируется каждая обработанная папка и файл в порядке фактического обхода.
- Переход к следующему источнику разрешён только после `ЗАВЕРШЁН` у текущего.
- `✅` означает реальный просмотр + сверку с банком идей.
- Дубликаты не добавляются; новые детали существующих систем сохраняются.
- После каждого существенного батча обновляются журнал и `PROJECT_STATE.md`.

## Источники

| № | Репозиторий | Статус | Журнал |
|---|---|---|---|
| 1 | `Cog-Creators/Red-DiscordBot` | ✅ ЗАВЕРШЁН | `research/red-discord-bot.md` |
| 2 | `python-discord/bot` | ✅ ЗАВЕРШЁН | `research/python-discord-bot.md` |
| 3 | `ItzSudhan/Discord-MusicBot` | ✅ ЗАВЕРШЁН | `research/discord-music-bot.md` |
| 4 | `codebymitch/TitanBot` | 🔵 АКТИВЕН | `research/titanbot.md` |
| 5 | `GAwesomeBot/bot` | ⏳ ОЖИДАЕТ | — |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | — |
| 7 | `Tomato6966/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | — |

## `ItzSudhan/Discord-MusicBot` — ЗАВЕРШЁН

Ветка: `v5`.

Recursive tree проверен полностью (`truncated=false`). Закрыты все исходные каталоги и root-файлы, включая `commands/`, `events/`, `lib/`, `util/`, `api/`, исходный `dashboard/`, `deploy/`, `docker/`, `.github/` и оставшиеся root/config/runtime files. `dashboard/out/` и `_next` классифицированы как build artifacts и не дублировались поверх исходников.

Идеи:
- `ideas/MUSIC.md` — MUSIC-001–042;
- `ideas/MUSIC_COMMANDS.md` — MUSIC-C001–055;
- `ideas/MUSIC_CONTEXT.md` — MUSIC-X001–007;
- `ideas/MUSIC_EVENTS.md` — MUSIC-E001–025;
- `ideas/MUSIC_STORAGE.md` — MUSIC-S001–018;
- `ideas/MUSIC_CORE.md` — MUSIC-K001–018;
- `ideas/MUSIC_WEB.md` — MUSIC-W001–031;
- `ideas/MUSIC_DEPLOY.md` — MUSIC-D001–026.

Финальная сверка выявила и добавила отдельные Docker/Lavalink варианты: сервисное разделение bot/Lavalink, `depends_on`, отдельная internal network, read-only config mounts, self-hosted Lavalink и параметры buffering/quality/metrics/request logging/rolling logs.

## Следующая точка

Начать `codebymitch/TitanBot` с его recursive tree. Сначала определить ветку/актуальный основной tree, затем идти строго по дереву, фиксируя каждый просмотренный файл и сравнивая находки с существующим банком идей. Создать `research/titanbot.md` и при необходимости новые тематические `ideas/`.

**`ItzSudhan/Discord-MusicBot` завершён. `codebymitch/TitanBot` — единственный следующий источник.**
