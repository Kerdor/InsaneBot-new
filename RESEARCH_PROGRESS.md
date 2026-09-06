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

Ветка: `v5`. Recursive tree проверен полностью (`truncated=false`). Закрыты все исходные каталоги и root-файлы, включая `commands/`, `events/`, `lib/`, `util/`, `api/`, исходный `dashboard/`, `deploy/`, `docker/`, `.github/` и оставшиеся root/config/runtime files. Build artifacts не считались самостоятельными источниками механик.

Идеи:
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

Последние пакеты:
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065;
- `ideas/TITAN_JOINTOCREATE.md` — TJ-001–TJ-080;
- `ideas/TITAN_LEVELING.md` — TL-001–TL-100;
- `ideas/TITAN_LOGGING.md` — TLOG-001–TLOG-100;
- `ideas/MODERATION.md` — MOD-001–MOD-135.

### `Logging` — ЗАКРЫТ

Просмотрены command/modules, logging service, logging UI, interaction handler и связанные event logging paths. Зафиксированы destination routing, global/category/event toggles, wildcard logic, ignore filters, permission/error handling, audit embed architecture, Before/After comparison, metadata/attachment support и member/role/message lifecycle logging.

### `Moderation` — ЗАКРЫТ

Просмотрены все файлы `src/commands/Moderation/` из recursive tree и moderation services. Зафиксированы централизованный ModerationService, hierarchy/permission checks, case IDs, warnings, mass actions, purge, lock/unlock, staff DM, say, cases UI, user notes, abuse protection и typed error handling. Пакет добавлен в `ideas/MODERATION.md` как MOD-044–MOD-135.

### Точная точка продолжения

**Следующий раздел: `src/commands/Music/`.**

Продолжать строго по порядку дерева `src/commands/`. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
