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

Основной банк и пять батчей Public. Последний: `ideas/GAWESOME_COMMANDS_PUBLIC_BATCH5.md`, **GAB-PUB-386–GAB-PUB-452**.

В последнем продолжении полностью просмотрены/перепроверены `_base.js`, `cool.js`, `giveaway.js`, `kick.js`, `modlog.js`, `mute.js`, `points.js`, `room.js`, `shorten.js`, `stats.js`, `streamers.js`, `tag.js`, `time.js`, `translate.js`, `trivia.js`, `twitter.js`, `unban.js`, `unmute.js`, `wiki.js`, `weather.js`, `wolfram.js`, `xkcd.js`, `youtube.js`, `year.js`.

### Точная точка продолжения

**Продолжать `Commands/Public/`: пройти оставшиеся Public-файлы, затем выполнить финальную сверку всего Public с банком.**

Не переходить в `Commands/Shared/`, пока Public не будет реально закрыт. После Public → Shared → только после полного Commands → Configurations.

Другие репозитории не трогать до полного завершения GAwesomeBot.
