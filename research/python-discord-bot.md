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
- `codeblock/__init__.py` — ✅ (структура)
- `codeblock/_cog.py` — ✅
- `codeblock/_instructions.py` — ✅
- `codeblock/_parsing.py` — ✅
- `doc/__init__.py` — ✅ (структура)
- `doc/_cog.py` — ✅
- `doc/_batch_parser.py` — ✅
- `doc/_redis_cache.py` — ✅
- `code_snippets.py` — ✅
- `information.py` — 🔎 основной runtime-код просмотрен, полный файл ещё требует добора после лимита вывода
- `patreon.py` — ✅
- `pep.py` — ✅
- `python_news.py` — ✅
- `tags.py` — ✅
- `doc/_doc_item.py`, `_html.py`, `_inventory_parser.py`, `_markdown.py`, `_parsing.py` — ⏳ (структура известна, содержимое ещё нужно добрать)

## Последний батч: что извлечено

### Info: Code Block
Добавлен `ideas/PYTHON_DISCORD_INFO.md`, `PDIS-I001`–`PDIS-I020`:
- автоматический ревьюер Markdown code blocks;
- повторная проверка и редактирование/удаление подсказки после edit;
- уверенное определение Python/REPL перед обучающей подсказкой;
- распознавание IPython/REPL prompt-последовательностей;
- антиобход через визуально похожие tick-символы;
- fallback длинного snippet в bot-commands;
- GitHub/Gist/GitLab/Bitbucket/paste snippet extraction;
- защита Markdown injection в коде и безопасное определение language;
- Intersphinx documentation inventories;
- разрешение конфликтов одинаковых doc symbols;
- lazy batch parsing всей HTML-страницы;
- приоритет пользовательского запроса в parse queue;
- stale inventory detector с ограничением предупреждений;
- недельный page-oriented Redis cache;
- безопасный refresh inventory с retry/reschedule;
- diff добавленных/удалённых inventories;
- PEP cache refresh + fuzzy autocomplete;
- месячная Patreon-supporter публикация по tier;
- агрегатор Python News из RSS/mailing lists с persistent seen state;
- News Channel publish после webhook pipeline.

## Что просмотрено, но пока требует более глубокого добора

`information.py` был получен только частично из-за ограничения вывода инструмента. Основная логика server/user/role information уже просмотрена, но необходимо получить оставшуюся часть файла, чтобы не пропустить команды и мелкие UX-механики.

`doc/` также требует добора `_doc_item.py`, `_html.py`, `_inventory_parser.py`, `_markdown.py`, `_parsing.py`; текущий батч фиксирует только основные runtime-поверхности `_cog.py`, `_batch_parser.py`, `_redis_cache.py` и каталог.

## Статус

`bot/exts/fun/` и `bot/exts/help_channels/` закрыты. `bot/exts/info/` **ещё НЕ закрыт**: текущий батч дал 20 уникальных info-идей, но нужно последовательно дочитать остаток `doc/` и полный `information.py`, после чего продолжить по recursive tree.

**Источник не завершён. Другие репозитории не трогать.**
