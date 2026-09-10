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

Recursive Git Tree проверен полностью. Основные области: `src/commands`, `src/config`, `src/database`, `src/events`, `src/handlers`, `src/interactions`, `src/music`, `src/packages`.

### Уже обработано
- Batch 1: `COR-001–080`.
- Batch 2: `COR-081–125`.
- Batch 3: `COR-126–201`.
- `src/commands` подтверждённо закрыт.
- Batch 4: `src/events` — `channel`, `client`, `emoji`, `event`, `giveaway`, `guild`, `message/messageCreate.js`, `role`; **COR-202–248**.
- Batch 5: оставшиеся ветки `invite`, `message`, `stats`, `sticker`, `thread`, `voice`, `warn`; **COR-249–293**.
- Batch 6: начат `src/handlers`; обработаны `functions` (выбранные файлы), `components` и `security`; **COR-294–314**.

### Точная точка продолжения
`src/events` **ЗАКРЫТ**.

`src/handlers` **НЕ ЗАКРЫТ**. Продолжить `audio`, `games`, `helppanel`, `linkspanel`, `loaders`, остальные фактически присутствующие файлы `functions` и детальную сверку `security`.

После полного закрытия `handlers`: `src/interactions` → `src/config` → `src/database` → `src/music` → `src/packages` → прочие файлы.

**Не переходить к Tomato6969 до полного закрытия CorwinDev.**

`bot/main.py` и другая реализация InsaneBot не изменяются.
