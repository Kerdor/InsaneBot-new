# Research Log — `python-discord/bot`

Статус: 🔵 **АКТИВЕН**

Правило: этот репозиторий должен быть полностью обработан до перехода к следующему источнику.

## Порядок обхода

Формат статуса:
- `⏳` — ещё не обработано
- `🔄` — сейчас исследуется
- `✅` — полностью просмотрено, идеи сверены с `ideas/`, новые механики распределены
- `➖` — просмотрено, новых переносимых механик не найдено

## Фактический порядок обработки

### Корень
1. `README.md` — ✅
2. Дерево репозитория — ✅
3. Остальные root-файлы — ⏳

### `bot/`
4. `bot/bot.py` — ✅
5. `bot/constants.py` — ✅
6. `bot/converters.py` — ✅
7. `bot/decorators.py` — ✅
8. `bot/exts/info/subscribe.py` — ✅
9. `bot/exts/moderation/stream.py` — ✅
10. `bot/exts/moderation/silence.py` — ✅
11. `bot/exts/fun/duck_pond.py` — ✅
12. `bot/exts/info/resources.py` — ✅
13. `bot/exts/info/pypi.py` — ✅
14. `bot/exts/utils/ping.py` — ✅
15. `bot/exts/moderation/alts.py` — ✅
16. `bot/exts/moderation/modpings.py` — ✅
17. `bot/exts/info/help.py` — ✅
18. `bot/exts/utils/extensions.py` — ✅
19. `bot/exts/utils/bot.py` — ✅
20. `bot/exts/info/source.py` — ✅
21. `bot/exts/utils/internal.py` — ✅
22. `bot/exts/info/stats.py` — ✅

### `bot/exts/backend/`
23. `bot/exts/backend/__init__.py` — ⏳
24. `bot/exts/backend/branding/__init__.py` — ✅
25. `bot/exts/backend/branding/_cog.py` — ✅
   - External event branding daemon, persistent Redis state, event/asset discovery, event cache, asset hash tracking, automatic event entry, scheduled asset rotation, upload timeout and debug mocking.
26. `bot/exts/backend/branding/_repository.py` — ✅
   - Typed remote GitHub objects, metadata parsing, fallback/year-agnostic event dates, validation, 5-attempt exponential retry for GitHub 5xx responses and cached-by-caller API responsibility.
27. `bot/exts/backend/config_verifier.py` — ✅
   - Startup validation of configured Discord channel IDs with aggregated warnings for missing resources.
28. `bot/exts/backend/error_handler.py` — ✅
   - Error-specific routing, command/tag/shorthand fallback, interactive help button, fuzzy suggestion fallback, API status classification and structured Sentry context.
29. `bot/exts/backend/logging.py` — ⏳
30. `bot/exts/backend/security.py` — ✅
   - Global command guards against bot users and DM command execution.
31. `bot/exts/backend/sync/__init__.py` — ⏳
32. `bot/exts/backend/sync/_cog.py` — ✅
   - Startup guild chunk readiness loop with manual fallback, delayed background sync, event-driven user/role synchronization and manual role/user sync commands.
33. `bot/exts/backend/sync/_syncers.py` — ✅
   - Generic diff-based reconciliation, hashable normalized records, cache-integrity fetch fallback, paginated API traversal and fixed-size bulk writes.

### Следующая точка
Продолжить с `bot/exts/backend/__init__.py`, затем строго по оставшемуся recursive tree. Уже просмотренные out-of-order extension files остаются отмеченными `✅`; дальнейшие новые позиции фиксируются в фактическом порядке обхода.

## Найденные новые механики

Базовые механики записаны в `ideas/PYTHON_DISCORD.md`, дополнительные backend-механики — в `ideas/PYTHON_DISCORD_BACKEND.md`.

К текущему батчу добавлены:
- persistent event-branding daemon;
- external repository event discovery and validation;
- fair asset rotation by usage iterations + compound hashes;
- startup Discord-resource config verification;
- global bot-user/DM command guards;
- error-specific interactive Help and structured diagnostics;
- diff/reconciliation API synchronization with pagination and chunked writes.

## Дубликаты

Общие pagination, timestamps, selfroles/button roles, базовые permissions, moderation hierarchy, scheduling, state recovery, logging/error handling и integrations не размножаются; фиксируются только новые детали, UX, ограничения или архитектурные варианты.

## Примечание

Источник **не завершён**. Следующие репозитории не трогать до полного обхода `python-discord/bot`.
