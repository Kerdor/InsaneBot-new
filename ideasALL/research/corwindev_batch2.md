# CorwinDev/Discord-Bot — Research Journal — Batch 2

Источник: `CorwinDev/Discord-Bot`, branch `main`.

## Проверено

Recursive Git Tree репозитория проверен полностью (`truncated=false`). В этом батче дополнительно просмотрены фактические файлы:

- `src/commands/birthdays/check.js`
- `src/commands/birthdays/delete.js`
- `src/commands/birthdays/list.js`
- `src/commands/birthdays/set.js`
- `src/commands/bot/info.js`
- `src/commands/guild/info.js`
- `src/commands/levels/createreward.js`
- `src/commands/levels/rank.js`
- `src/commands/levels/rewards.js`
- `src/commands/messages/createreward.js`
- `src/commands/notepad/add.js`
- `src/commands/stickymessages/stick.js`
- `src/commands/suggestions/send.js`
- `src/commands/thanks/thanks.js`
- `src/commands/invites/leaderboard.js`
- `src/commands/voice/rename.js`

## Выделенные идеи

- birthday profile: set/check/delete/list;
- overwrite существующей birthday-записи;
- server birthday board;
- валидация даты до сохранения;
- shard-wide bot diagnostics через broadcastEval;
- одновременное отображение global и current-shard statistics;
- runtime diagnostics: uptime, API latency, версии и memory;
- расширенная server info карточка с threads/stickers/boost/verification;
- role rewards за level и message thresholds;
- защита от повторного reward на одинаковый threshold;
- графическая rank card с XP/level/rank/progress;
- feature gate для levels;
- personal notepad с коротким числовым кодом;
- sticky message с хранением последнего message ID;
- suggestion channel + author embed + up/down reactions;
- thanks reputation с запретом self-thanks и повторной благодарности от одного автора;
- invite leaderboard;
- ownership/permission checks для временного voice;
- единая обработка пустых списков и отсутствующей конфигурации.

## Результат

Создан `ideasALL/ideas/CORWIN_BATCH2.md` с **COR-081–125**.

`bot/main.py` и реализация InsaneBot не изменялись.

## Следующая точка

Продолжить фактический обход оставшихся `src/commands`, затем перейти к `src/events`, `src/handlers`, `src/interactions`, `src/config`, `src/database`, `src/music`, `src/packages`.
