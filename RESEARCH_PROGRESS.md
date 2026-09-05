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
| 2 | `python-discord/bot` | 🔵 АКТИВЕН | `research/python-discord-bot.md` |
| 3 | `ItzSudhan/Discord-MusicBot` | ⏳ ОЖИДАЕТ | — |
| 4 | `codebymitch/TitanBot` | ⏳ ОЖИДАЕТ | — |
| 5 | `GAwesomeBot/bot` | ⏳ ОЖИДАЕТ | — |
| 6 | `CorwinDev/Discord-Bot` | ⏳ ОЖИДАЕТ | — |
| 7 | `Tomato6966/Multipurpose-discord-bot` | ⏳ ОЖИДАЕТ | — |

## Текущая точка — `python-discord/bot`

Полное recursive tree получено на tree SHA `0e4cd5cb46f2239eacccdded8cdf02ba89028ab9`.

Обработано по порядку:
1. `README.md` — ✅
2. дерево — ✅
3. `bot/bot.py` — ✅
4. `bot/constants.py` — ✅
5. `bot/converters.py` — ✅
6. `bot/decorators.py` — ✅
7. `bot/exts/info/subscribe.py` — ✅
8. `bot/exts/moderation/stream.py` — ✅
9. `bot/exts/moderation/silence.py` — ✅
10. `bot/exts/fun/duck_pond.py` — ✅
11. `bot/exts/info/resources.py` — ✅
12. `bot/exts/info/pypi.py` — ✅
13. `bot/exts/utils/ping.py` — ✅
14. `bot/exts/moderation/alts.py` — ✅
15. `bot/exts/moderation/modpings.py` — ✅
16. `bot/exts/info/help.py` — ✅
17. `bot/exts/utils/extensions.py` — ✅
18. `bot/exts/utils/bot.py` — ✅
19. `bot/exts/info/source.py` — ✅
20. `bot/exts/utils/internal.py` — ✅
21. `bot/exts/info/stats.py` — ✅
22+. Остальные `bot/exts/...`, `bot/resources/`, `bot/utils/`, `tests/`, root/.github/deployment — ⏳

## Последний батч

Добавлены `ideas/PYTHON_DISCORD_ADVANCED.md` и PDIS-A001–A012:
- alternate-account associations;
- scheduled role state with manual override;
- interactive help parent/subcommand navigation;
- fuzzy permission-aware help suggestions;
- custom help categories;
- wildcard extension batch management with rollback/locking;
- multi-source latency healthcheck;
- WebSocket event-rate diagnostics;
- persistent REPL eval with paste fallback;
- exact source-code links;
- normalized Discord event metrics;
- moderation-only echo/embed relay.

## Статус

**`python-discord/bot` НЕ ЗАВЕРШЁН.** Следующие репозитории не трогать. Продолжать строго с первой необработанной позиции recursive tree.
