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
| 6 | `CorwinDev/Discord-Bot` | 🔵 АКТИВЕН | `research/corwindev.md` |
| 7 | `Tomato6969/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | `—` |

## CorwinDev/Discord-Bot — ACTIVE

Repository: `CorwinDev/Discord-Bot`, branch `main`.

### Начальный обход
Recursive Git Tree проверен. Репозиторий содержит крупные области `src/commands`, `src/config`, `src/database`, `src/events`, `src/handlers`, `src/interactions`, `src/music`, `src/packages`.

### Закрытые в текущем батче
- `src/commands/automod`
- `src/commands/autosetup`
- `src/commands/casino`
- `src/commands/custom-commands`
- `src/commands/economy`
- `src/commands/family`
- `src/commands/games`
- `src/handlers/security/antiad.js`
- `src/handlers/security/antispam.js`
- `src/handlers/security/blacklist.js`
- `src/handlers/functions/ticket.js` — просмотр ключевой transcript/ticket инфраструктуры

### Каталог
`ideasALL/ideas/CORWIN_BATCH1.md` — **COR-001–080**.

### Точная точка продолжения
Продолжить CorwinDev с оставшихся областей `src/commands`, затем `src/events`, `src/handlers`, `src/interactions`, `src/config`, `src/database`, `src/music`, `src/packages` и прочих файлов.

**Не переходить к Tomato6969 до полного закрытия CorwinDev.**

`bot/main.py` и другая реализация InsaneBot не изменяются.
