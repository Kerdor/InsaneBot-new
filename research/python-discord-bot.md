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

## Последний батч: что извлечено

### Fun
Добавлены `PDIS-FUN001`–`PDIS-FUN012` в `ideas/PYTHON_DISCORD_FUN.md`:
- threshold-triggered reaction relay с unique-user counting;
- restricted reaction promotion;
- idempotent relay marker + lock;
- manual bypass;
- attachment-preserving webhook relay с graceful degradation;
- восстановление completion marker;
- scheduled random channel-name rotation;
- active/deactivated content pool;
- fuzzy similarity guard + force-add;
- normalized fuzzy search;
- rate-limit-aware deferred operation;
- exhaustion handling конечного random pool.

### Help channels
Добавлены `PDIS-HF001`–`PDIS-HF013` в `ideas/PYTHON_DISCORD_HELP_CHANNELS.md`:
- watchdog + per-post inactivity scheduler/rescheduler;
- разные причины закрытия и аналитика по ним;
- интеграция с native Forum/Thread lifecycle;
- автоматическая opener-инструкция;
- pin starter message;
- claimant-only close + staff override с silent failure;
- отдельное переименование help post;
- уведомление при уходе владельца;
- answered/unanswered analytics через Redis marker;
- open-count gauge + session timing;
- fallback при удалённом starter message;
- participant-aware ping при закрытии из-за inactivity;
- graceful closure при ошибке отправки уведомления.

## Идеи

Основные идеи предыдущих батчей: `ideas/PYTHON_DISCORD.md`.
Backend: `ideas/PYTHON_DISCORD_BACKEND.md`, `ideas/PYTHON_DISCORD_BACKEND_2.md`.
Filtering engine: `ideas/PYTHON_DISCORD_FILTERING_ENGINE.md`.
Filtering UI: `ideas/PYTHON_DISCORD_FILTERING_UI.md`.
Filtering specialized: `ideas/PYTHON_DISCORD_FILTERING_SPECIAL.md`.
Fun: `ideas/PYTHON_DISCORD_FUN.md`.
Help channels: `ideas/PYTHON_DISCORD_HELP_CHANNELS.md`.

## Статус

`bot/exts/fun/` и `bot/exts/help_channels/` теперь закрыты. Следующая последовательная точка источника — `bot/exts/info/`, начиная с ещё не закрытых файлов/подкаталогов; ранее просмотренные info-файлы повторно не считать новыми без дополнительного материала.

**Источник не завершён. Другие репозитории не трогать.**
