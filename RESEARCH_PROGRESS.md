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

### Просмотрено

1. `README.md` — ✅
2. recursive tree — ✅
3. `config.js` — ✅
4. `index.js` — ✅
5. `package.json` — ✅
6. `lib/DiscordMusicBot.js` — ✅ частично; основной lifecycle/event pipeline просмотрен, файл требует дочитывания
7. `lib/SlashCommand.js` — ✅
8. `lib/EpicPlayer.js` — ✅
9. `util/loadCommands.js` — ✅
10. `util/Controller.js` — ✅
11. `events/interactionCreate.js` — ✅
12. `commands/slash/autoleave.js` — ✅
13. `commands/slash/autopause.js` — ✅
14. `commands/slash/autoqueue.js` — ✅
15. `commands/slash/clean.js` — ✅
16. `commands/slash/clear.js` — ✅
17. `commands/slash/filters.js` — ✅
18. `commands/slash/guildleave.js` — ✅
19. `commands/slash/help.js` — ✅
20. `commands/slash/loop.js` — ✅
21. `commands/slash/loopq.js` — ✅
22. `commands/slash/queue.js` — ✅

### Последний батч

Добавлены `ideas/MUSIC.md` и `MUSIC-001`–`MUSIC-042`.

### Следующая точка

Продолжать `commands/slash/` с:
`247.js`, `invite.js`, `lyrics.js`, `move.js`, `nowplaying.js`, `pause.js`, `ping.js`, `play.js`, `previous.js`, `reload.js`, `remove.js`, `replay.js`, `resume.js`, `save.js`, `search.js`, `seek.js`, `shuffle.js`, `skip.js`, `skipto.js`, `stats.js`, `stop.js`, `summon.js`, `volume.js`.

После закрытия slash-команд: `commands/context/`, затем `events/`, `util/`, `api/`, `dashboard/`, `deploy/`, `docker/`, `.github/` и root-файлы.

**`ItzSudhan/Discord-MusicBot` НЕ ЗАВЕРШЁН.**
