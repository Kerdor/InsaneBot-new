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
- `FILTERS-DEVELOPMENT.md` — ✅
- `filtering.py` — 🔎
- `_filter_context.py` — ✅
- `_filter_lists/*` — 🔎
- `_filters/antispam/*` — ✅
- `_filters/domain.py` — ✅
- `_filters/extension.py` — ✅
- `_filters/filter.py` — ✅
- `_filters/image_hash.py` — ✅
- `_filters/invite.py` — ✅
- `_filters/token.py` — ✅
- `_filters/unique/*` — ✅
- `_settings_types/actions/*` — ✅
- `_settings_types/settings_entry.py` — ✅
- `_settings_types/validations/*` — ✅
- `_settings.py` — ✅
- `_utils.py` — ✅
- `_image_hash.py` — ✅
- `_ui/filter.py` — ✅
- `_ui/filter_list.py` — ✅
- `_ui/search.py` — ✅
- `_ui/ui.py` — ✅
- `_ui/__init__.py` — trivial/empty
- `_settings_types/__init__.py` — trivial registry/import surface
- `__init__.py` — trivial/empty

## Последний батч: что извлечено

### Filtering UI
Добавлены `PDIS-FU009`–`PDIS-FU014`:
- type-aware редактор настроек: bool через True/False select, остальные типы через modal с конвертацией;
- специализированный редактор последовательностей со снятием/добавлением/полной заменой и подавлением дублей;
- интерактивный search query builder с выбором типа фильтра, критериями и template;
- пересоздание stateful view после изменения для предотвращения stale component/select state;
- привязка argument-completion controls к автору команды с ephemeral отказом посторонним;
- компактный structured embed renderer с placeholder для пустых значений, truncation, inline-эвристикой и скрытием внутренних полей.

## Идеи

Основные идеи предыдущих батчей: `ideas/PYTHON_DISCORD.md`.
Backend: `ideas/PYTHON_DISCORD_BACKEND.md`, `ideas/PYTHON_DISCORD_BACKEND_2.md`.
Filtering engine: `ideas/PYTHON_DISCORD_FILTERING_ENGINE.md`.
Filtering UI: `ideas/PYTHON_DISCORD_FILTERING_UI.md`.
Filtering specialized: `ideas/PYTHON_DISCORD_FILTERING_SPECIAL.md`.

## Статус

Filtering теперь фактически закрыт: просмотрены engine, lists, filters, anti-spam, unique/security, settings/actions/validations и UI. Следующая последовательная точка источника — `bot/exts/fun/`, затем остальные каталоги `bot/` по recursive tree.

**Источник не завершён. Другие репозитории не трогать.**
