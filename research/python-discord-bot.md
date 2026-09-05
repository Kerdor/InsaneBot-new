# Research Log — `python-discord/bot`

Статус: 🔵 **АКТИВЕН**

`✅` = реально просмотрено и сверено с банком; `⏳` = ещё не обработано; `🔎` = предварительно просмотрено до последовательного прохода.

## Фактический журнал

### Корень
- `README.md` — ✅
- Recursive tree — ✅
- Остальные root/.github/deployment files — ⏳

### `bot/`
- Core: `bot.py`, `constants.py`, `converters.py`, `decorators.py` — ✅
- Utility/info/moderation/fun surfaces из предыдущих батчей — ✅

### `bot/exts/backend/`
- Весь каталог — ✅

### `bot/exts/filtering/`
- Весь каталог — ✅
- Engine, lists, filters, anti-spam, unique/security, settings/actions/validations и UI — просмотрены и сверены.

### `bot/exts/fun/`
- `__init__.py` — ✅ (пустой)
- `duck_pond.py` — ✅
- `off_topic_names.py` — ✅

### `bot/exts/help_channels/`
- `__init__.py` — ✅
- `_caches.py` — ✅
- `_channel.py` — ✅
- `_cog.py` — ✅
- `_stats.py` — ✅

### `bot/exts/info/`
- `codeblock/__init__.py` — ✅
- `codeblock/_cog.py` — ✅
- `codeblock/_instructions.py` — ✅
- `codeblock/_parsing.py` — ✅
- `doc/__init__.py` — ✅
- `doc/_cog.py` — ✅
- `doc/_batch_parser.py` — ✅
- `doc/_redis_cache.py` — ✅
- `doc/_doc_item.py` — ✅
- `doc/_html.py` — ✅
- `doc/_inventory_parser.py` — ✅
- `doc/_markdown.py` — ✅
- `doc/_parsing.py` — ✅
- `code_snippets.py` — ✅
- `information.py` — ✅
- `patreon.py` — ✅
- `pep.py` — ✅
- `python_news.py` — ✅
- `tags.py` — ✅
- `help.py`, `resources.py`, `pypi.py`, `stats.py`, `source.py`, `subscribe.py` — ✅ (ранее просмотрены)

### `bot/exts/moderation/`
- `alts.py` — ✅
- `clean.py` — ✅
- `defcon.py` — ✅
- `incidents.py` — 🔎 основная runtime-логика и event workflow просмотрены; при необходимости добрать остаток файла без повторного просмотра уже разобранной части
- `modpings.py` — ✅; в основном совпадает с уже зафиксированной scheduled role state механикой, новых дублей не добавлено
- `stream.py` — ✅
- Остальные root moderation files — ⏳
- `infraction/` — ⏳

## Извлечённые идеи

### Info
Основной файл `ideas/PYTHON_DISCORD_INFO.md` содержит `PDIS-I001`–`PDIS-I026`: автоматический codeblock review, edit-aware подсказки, Python/REPL detection, multi-source code snippets, безопасную выдачу кода, Intersphinx inventories, conflict resolution, lazy batch parsing, priority queue, stale inventory detection, Redis cache, inventory refresh/retry, diff refresh, PEP cache/autocomplete, Patreon monthly supporters, Python News aggregation и News Channel publishing.

Дополнительный файл `ideas/PYTHON_DISCORD_INFO_2.md` содержит `PDIS-I2-001`–`PDIS-I2-011`: raw Discord API inspector, human/JSON diagnostic output, paste fallback, mixed rule-number/keyword lookup, staff alerts на rule requests, per-tag frontmatter metadata, per-channel tag cooldown, hierarchical tag groups, permission-aware fuzzy suggestions, tier-up support events и динамически подключаемые documentation sources.

### Moderation
Дополнительный файл `ideas/PYTHON_DISCORD_MODERATION_2.md` содержит `PDIS-M2-001`–`PDIS-M2-016`: DEFCON account-age gate, automatic expiry/reminders, emergency server lockdown, reaction-based incident states, startup incident catch-up, archive-before-delete safety, deleted-message recovery through modlog, Discord message-link previews, composable clean filters, hybrid 14-day bulk/individual deletion, cancellable cleaning, audit logs и persisted temporary streaming permissions с upgrade/revoke/list behavior.

`modpings.py` дополнительно проверен на scheduled pingable-role behavior; отдельные идеи не дублировались, потому что ключевая схема уже была зафиксирована ранее как `PDIS-A002`.

## Следующая точка

Продолжать **только `python-discord/bot`**. Текущая активная область — `bot/exts/moderation/`: добрать остальные root-файлы и затем весь `infraction/`, постоянно сверяя идеи с существующим банком и не создавая дубликаты.

После полного завершения `python-discord/bot` только тогда переходить к `ItzSudhan/Discord-MusicBot`.

**Другие источники не трогать.**
