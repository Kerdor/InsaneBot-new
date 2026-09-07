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

Проверены все 11 файлов PM и связанный `Commands/Private/giveaway.js`.

Зафиксировано **GAB-PM-001–GAB-PM-125** в `ideas/GAWESOME_COMMANDS_PM.md`.

### `Commands/Private/` — ЗАКРЫТ

Проверены все 4 файла:
- `giveaway.js`
- `index.js`
- `poll.js`
- `say.js`

Зафиксировано **GAB-PR-001–GAB-PR-049** в `ideas/GAWESOME_COMMANDS_PRIVATE.md`.

Ключевые блоки: private execution namespace; server resolution + membership gate; blocklist gate; channel resolution/type validation; lazy channel-state creation; remote say attribution и permission checks; poll end/revoke/re-vote; anonymous DM voting; pagination; callback validation; per-step timeouts; default options; giveaway state machine; secret prize; duration parser/fallback; maintainer bypass; nested state operations; initMsg correlation.

## Точная точка продолжения

**Следующий необработанный каталог: `Commands/Public/`.**

После `Public` продолжать `Shared`. Только после полного завершения `Commands/` переходить к `Configurations/`.

Другие репозитории не трогать до полного завершения GAwesomeBot.
