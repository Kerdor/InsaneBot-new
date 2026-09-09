# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения глубокого исследования в новом чате без потери позиции.

## Правила

- Источники исследуются строго по очереди.
- Внутри активного репозитория фиксируется каждая обработанная папка и файл в порядке фактического обхода.
- Переход к следующему источнику разрешён только после `ЗАВЕРШЁН` у текущего.
- `✅` означает реальный просмотр + сверку с банком идей.
- Дубликаты не добавляются; новые детали существующих систем сохраняются.
- После каждого существенного батча обновляются журнал и `PROJECT_STATE.md`.
- На текущем этапе bot implementation не изменяется; исследуются только ideas/research/checkpoints.

## Источники

| № | Репозиторий | Статус | Журнал |
|---|---|---|---|
| 1 | `Cog-Creators/Red-DiscordBot` | ✅ ЗАВЕРШЁН | `research/red-discord-bot.md` |
| 2 | `python-discord/bot` | ✅ ЗАВЕРШЁН | `research/python-discord-bot.md` |
| 3 | `ItzSudhan/Discord-MusicBot` | ✅ ЗАВЕРШЁН | `research/discord-music-bot.md` |
| 4 | `codebymitch/TitanBot` | ✅ ЗАВЕРШЁН | `research/titanbot.md` |
| 5 | `GAwesomeBot/bot` | 🔵 АКТИВЕН | `research/gawesomebot.md` |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | — |
| 7 | `Tomato6969/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | — |

## `GAwesomeBot/bot` — АКТИВЕН

Ветка: `indev-4.0.2`. Фактический recursive tree проверен через Git Tree API; `truncated=false`.

Корневой порядок: `Commands/` → `Configurations/` → `Database/` → `Internals/` → `Modules/` → `Temp/` → `Web/`.

### `Commands/PM/` — ЗАКРЫТ

**GAB-PM-001–GAB-PM-125**.

### `Commands/Private/` — ЗАКРЫТ

**GAB-PR-001–GAB-PR-049**.

### `Commands/Public/` — 🔵 В РАБОТЕ

Idea bank Public расширен до **GAB-PUB-590**. Последние записи находятся в `ideas/GAWESOME_COMMANDS_PUBLIC_BATCH6.md`.

Дополнительно просмотрены/перепроверены command base, cooldown, giveaway, moderation, points, streamers, tags, anime, App Store, GIF/animals, counting, archive, conversion и redirect-chain flows.

### Точная точка продолжения

**Продолжать `Commands/Public/`: пройти ещё не закрытые Public-файлы, затем выполнить финальную сверку всего каталога с GAB-PUB-001–590.**

Не переходить в `Commands/Shared/`, пока Public не будет реально закрыт. После Public → Shared → только после полного Commands → Configurations.

Другие репозитории не трогать до полного завершения GAwesomeBot.
