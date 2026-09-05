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
- `__init__.py` — ✅
- `branding/__init__.py` — ✅
- `branding/_cog.py` — ✅
- `branding/_repository.py` — ✅
- `config_verifier.py` — ✅
- `error_handler.py` — ✅
- `logging.py` — ✅
- `security.py` — ✅
- `sync/__init__.py` — ✅
- `sync/_cog.py` — ✅
- `sync/_syncers.py` — ✅

### `bot/exts/filtering/`
- `FILTERS-DEVELOPMENT.md` — ✅
  - Internal semantic filtering events, filter-list/filter inheritance model, typed settings groups and staged bot/site schema evolution.
- `filtering.py` — 🔎
  - Main dispatcher, attachment/snapshot content extraction, message/edit/thread/nickname/Snekbox processing, persistent deletion recovery, filter management commands and image-hash utility inspected.
- `_filter_lists/antispam.py` — 🔎
- `_filter_lists/domain.py` — 🔎
- `_filter_lists/extension.py` — 🔎
- `_filter_lists/filter_list.py` — 🔎
- `_filter_lists/image_hash.py` — 🔎
- `_filter_lists/invite.py` — 🔎
- `_filter_lists/token.py` — 🔎
- `_filter_lists/unique.py` — 🔎
- Remaining filtering files/directories — ⏳

### Следующая последовательная точка
Продолжить `bot/exts/filtering/` по recursive tree с оставшихся файлов/директорий. Предварительно просмотренные filtering surfaces повторно не терять: при прохождении их места использовать уже полученные результаты и добирать только недостающие детали.

## Идеи

Основные идеи предыдущих батчей: `ideas/PYTHON_DISCORD.md`.
Backend: `ideas/PYTHON_DISCORD_BACKEND.md`, `ideas/PYTHON_DISCORD_BACKEND_2.md`.
Filtering engine: `ideas/PYTHON_DISCORD_FILTERING_ENGINE.md`.
Filtering UI: `ideas/PYTHON_DISCORD_FILTERING_UI.md`.
Filtering specialized: `ideas/PYTHON_DISCORD_FILTERING_SPECIAL.md`.

Добавлены специализированные механики: attachment extension allowlist guidance, perceptual image hashes, invite anti-obfuscation/trusted-server handling, spoiler-aware regex tokens, per-filter overrides, unique-event subscriptions, edit-trigger suppression, delayed anti-spam aggregation and potential-phishing signals.

## Статус

**Источник не завершён.** Следующие репозитории не трогать.
