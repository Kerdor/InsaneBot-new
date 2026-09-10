# RESEARCH PROGRESS

Этот файл — контрольная точка для продолжения глубокого исследования без потери позиции.

## Правила

- Источники исследуются строго по очереди.
- Внутри активного репозитория фиксируется каждая обработанная папка и файл.
- Переход к следующему источнику разрешён только после `ЗАВЕРШЁН` у текущего.
- `✅` означает реальный просмотр + сверку с банком идей.
- Дубликаты не добавляются; новые детали существующих систем сохраняются.
- На текущем этапе bot implementation не изменяется; исследуются только ideas/research/checkpoints.

## Источники

| № | Репозиторий | Статус | Журнал |
|---|---|---|---|
| 1 | `Cog-Creators/Red-DiscordBot` | ✅ ЗАВЕРШЁН | `research/red-discord-bot.md` |
| 2 | `python-discord/bot` | ✅ ЗАВЕРШЁН | `research/python-discord-bot.md` |
| 3 | `ItzSudhan/Discord-MusicBot` | ✅ ЗАВЕРШЁН | `research/discord-music-bot.md` |
| 4 | `codebymitch/TitanBot` | ✅ ЗАВЕРШЁН | `research/titanbot.md` |
| 5 | `GAwesomeBot/bot` | ✅ ЗАВЕРШЁН | `research/gawesomebot.md` |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | `—` |
| 7 | `Tomato6969/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | `—` |

## GAwesomeBot/bot — ЗАВЕРШЁН

Ветка: `indev-4.0.2`.

### Закрытые области
- Commands: PM **GAB-PM-001–125**, Private **GAB-PR-001–049**, Public **GAB-PUB-001–672**, Shared **GAB-SH-001–094**.
- Configurations: **GAB-CONF-001–086**.
- Database: **GAB-DB-001–096**.
- Internals: **GAB-INT-001–123**.
- Modules: **GAB-MOD-001–080**.
- Temp: служебный каталог, дополнительных механик нет.
- Web: **GAB-WEB-001–060**, файл `ideasALL/ideas/GAWESOME_WEB.md`.

### Web — основные группы
Web DTO/parsers; публичные профили пользователей и серверов; mutual servers; extension gallery/versioning/scopes; Discord authentication; membership/permission gates; dashboard control plane; per-channel command configuration; API/route separation; XSS-safe Markdown; blog/wiki/activity/donation surfaces; maintainer/debug panels; operational statistics; graceful missing entities; web lifecycle isolation.

## Точная точка продолжения

**Следующий источник: `CorwinDev/Discord-Bot`.**

`bot/main.py` и другая реализация InsaneBot не изменяются.
