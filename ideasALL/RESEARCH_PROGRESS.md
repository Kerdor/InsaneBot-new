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
| 6 | `CorwinDev/Discord-Bot` | 🔵 АКТИВЕН | `research/corwindev.md` + `research/corwindev_batch2.md` |
| 7 | `Tomato6969/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | `—` |

## CorwinDev/Discord-Bot — ACTIVE

Repository: `CorwinDev/Discord-Bot`, branch `main`.

Recursive Git Tree проверен полностью (`truncated=false`). Основные области: `src/commands`, `src/config`, `src/database`, `src/events`, `src/handlers`, `src/interactions`, `src/music`, `src/packages`.

### Уже обработано
- Batch 1: `automod`, `autosetup`, `casino`, `custom-commands`, `economy`, `family`, `games`, security handlers и ключевая ticket/transcript инфраструктура.
- `CORWIN_BATCH1.md` — **COR-001–080**.
- Batch 2: birthdays, bot info, guild info, levels, message rewards, notepad, sticky messages, suggestions, thanks, invites и voice.
- `CORWIN_BATCH2.md` — **COR-081–125**.
- Batch 3: фактическое продолжение по `fun`, `games`, `giveaway`, `guild`, `moderation`, `profile`, `reactionroles`, `tickets`, `tools`, `search`, `images` и `music`.
- `CORWIN_BATCH3.md` — **COR-126–201**.

### Точная точка продолжения
Продолжить **фактический полный обход оставшихся `src/commands`**. Batch 3 добавил большой набор найденных механик, но `src/commands` ещё не считается закрытым. После полного закрытия commands перейти к `src/events`, затем `src/handlers`, `src/interactions`, `src/config`, `src/database`, `src/music`, `src/packages` и прочим файлам.

**Не переходить к Tomato6969 до полного закрытия CorwinDev.**

`bot/main.py` и другая реализация InsaneBot не изменяются.
