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
| 3 | `ItzSudhan/Discord-MusicBot` | 🔵 АКТИВЕН | `research/discord-music-bot.md` |
| 4 | `codebymitch/TitanBot` | ⏳ ОЖИДАЕТ | — |
| 5 | `GAwesomeBot/bot` | ⏳ ОЖИДАЕТ | — |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | — |
| 7 | `Tomato6966/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | — |

## `ItzSudhan/Discord-MusicBot` — АКТИВЕН

Ветка: `v5`.

### Закрыто

- root README/tree/config/index/package;
- `commands/slash/` — все команды из recursive tree;
- `commands/context/play.js`;
- `events/interactionCreate.js`;
- `events/messageCreate.js`;
- `events/messageDelete.js`;
- `events/raw.js`;
- `events/ready.js`;
- `events/voiceStateUpdate.js`;
- `lib/DiscordMusicBot.js` — дочитан полностью;
- `lib/SlashCommand.js`, `lib/EpicPlayer.js`;
- `util/loadCommands.js`, `util/Controller.js`, `util/db.js`, `util/getChannel.js`, `util/getConfig.js`, `util/getLavalink.js`, `util/guildDb.js`.

### Идеи

- `ideas/MUSIC.md` — MUSIC-001–042;
- `ideas/MUSIC_COMMANDS.md` — MUSIC-C001–055;
- `ideas/MUSIC_CONTEXT.md` — MUSIC-X001–007;
- `ideas/MUSIC_EVENTS.md` — MUSIC-E001–025;
- `ideas/MUSIC_STORAGE.md` — MUSIC-S001–018;
- `ideas/MUSIC_CORE.md` — MUSIC-K001–018.

### Последний батч

Закрыты context/event/core/storage-части, добавлены дополнительные варианты UX, voice-state automation, delayed leave/recheck, server mute handling, lazy per-guild JSON DB, queued persistence, command/player factories и controller state rendering.

## Следующая точка

Продолжить `util/` с первой ещё не закрытой позицией recursive tree после уже просмотренных файлов, затем `api/`, `dashboard/`, `deploy/`, `docker/`, `.github/` и остальные root-файлы.

**`ItzSudhan/Discord-MusicBot` НЕ ЗАВЕРШЁН. Следующие источники не трогать.**
