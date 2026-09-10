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
| 5 | `GAwesomeBot/bot` | 🔵 АКТИВЕН | `research/gawesomebot.md` |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | `—` |
| 7 | `Tomato6969/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | `—` |

## GAwesomeBot/bot — АКТИВЕН

Ветка: `indev-4.0.2`. Фактический recursive tree проверен через Git tree API; `truncated=false`.

### Commands — ЗАКРЫТ
- PM: **GAB-PM-001–125**
- Private: **GAB-PR-001–049**
- Public: **GAB-PUB-001–672**
- Shared: **GAB-SH-001–094**

### Configurations — ЗАКРЫТ
Проверены все **13 файлов**. **GAB-CONF-001–086**.

### Database — ЗАКРЫТ
Проверены все **19 файлов**: 6 верхнего уровня + 13 схем. **GAB-DB-001–096**.

### Internals — ЗАКРЫТ
Полный каталог закрыт: core, Errors, Events, Extendables, Extensions/API, IPC, Logger, Sharding, Worker и связанные handlers/components. **GAB-INT-001–123**.

### Modules — ЗАКРЫТ
Проверены все фактические файлы `Modules/` и вложенных `Emoji/`, `MessageUtils/ReactionMenus/`, `Timeouts/`, `Utils/`. Зафиксировано **GAB-MOD-001–080** в `ideasALL/ideas/GAWESOME_MODULES.md`.

Ключевые находки: conversion/cache и shard coordination; emoji/media normalization и GIF composition; entity resolvers; API wrappers; RSS incremental streaming; reusable paginated/reaction menus; duration/reminder parsing; long-duration timers; ModLog CRUD/case linkage; voice→text access control; onboarding; polls/trivia; activity/streamer state; safe text/regex/URL helpers; MOTD scheduler; temporary storage; encryption; Central updater; extension sandbox.

### Точная точка продолжения

**Следующий каталог: `GAwesomeBot/bot → Temp/`. После него — `Web/`.**

Другие репозитории не трогать до полного завершения GAwesomeBot.

`bot/main.py` и другая реализация InsaneBot не изменяются.
