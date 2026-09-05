# Research Log — `python-discord/bot`

Статус: 🔵 **АКТИВЕН**

Правило: этот репозиторий должен быть полностью обработан до перехода к следующему источнику.

## Порядок обхода

`✅` = реально просмотрено и сверено с банком; `⏳` = ещё не обработано; `➖` = просмотрено без новых переносимых механик.

## Фактический журнал

### Корень
- `README.md` — ✅
- Recursive tree — ✅
- Остальные root/.github/deployment files — ⏳

### `bot/`
- `bot/bot.py` — ✅
- `bot/constants.py` — ✅
- `bot/converters.py` — ✅
- `bot/decorators.py` — ✅
- `bot/exts/info/subscribe.py` — ✅
- `bot/exts/moderation/stream.py` — ✅
- `bot/exts/moderation/silence.py` — ✅
- `bot/exts/fun/duck_pond.py` — ✅
- `bot/exts/info/resources.py` — ✅
- `bot/exts/info/pypi.py` — ✅
- `bot/exts/utils/ping.py` — ✅
- `bot/exts/moderation/alts.py` — ✅
- `bot/exts/moderation/modpings.py` — ✅
- `bot/exts/info/help.py` — ✅
- `bot/exts/utils/extensions.py` — ✅
- `bot/exts/utils/bot.py` — ✅
- `bot/exts/info/source.py` — ✅
- `bot/exts/utils/internal.py` — ✅
- `bot/exts/info/stats.py` — ✅

### `bot/exts/backend/`
- `backend/__init__.py` — ✅
- `backend/branding/__init__.py` — ✅
- `backend/branding/_cog.py` — ✅
- `backend/branding/_repository.py` — ✅
- `backend/config_verifier.py` — ✅
- `backend/error_handler.py` — ✅
- `backend/logging.py` — ✅
- `backend/security.py` — ✅
- `backend/sync/__init__.py` — ✅
- `backend/sync/_cog.py` — ✅
- `backend/sync/_syncers.py` — ✅

### Additional inspected filtering surfaces (помечены отдельно, так как были просмотрены до входа в последовательный filtering pass)
- `filtering/_filter_lists/antispam.py` — 🔎 просмотрено
- `filtering/_filter_lists/domain.py` — 🔎 просмотрено
- `filtering/_filter_lists/extension.py` — 🔎 просмотрено
- `filtering/_filter_lists/image_hash.py` — 🔎 просмотрено
- `filtering/_filter_lists/invite.py` — 🔎 просмотрено
- `filtering/_filter_lists/token.py` — 🔎 просмотрено
- `filtering/_filter_lists/unique.py` — 🔎 просмотрено
- `filtering/_filter_lists/filter_list.py` — 🔎 просмотрено

### Следующая последовательная точка
`bot/exts/filtering/FILTERS-DEVELOPMENT.md` → затем продолжать `bot/exts/filtering/...` по recursive tree. Уже просмотренные filtering-файлы повторно не считать необработанными, но при прохождении их позиции сверить журнал с результатами первого просмотра.

## Найденные новые механики

Базовые идеи распределены по `ideas/PYTHON_DISCORD.md`; backend — `ideas/PYTHON_DISCORD_BACKEND.md` и `ideas/PYTHON_DISCORD_BACKEND_2.md`.

Дополнительно выявлены специализированные filtering mechanics, подготовленные к записи отдельным тематическим батчем:
- attachment extension allowlist с контекстными подсказками;
- perceptual image-hash filtering;
- invite normalization/anti-obfuscation + verified/partnered exceptions;
- spoiler-aware regex token filtering;
- per-filter validation/action overrides;
- event subscriptions для unique filters;
- suppression повторных deny triggers при message edit;
- delayed anti-spam deletion context и aggregated moderation alert;
- potential phishing signals;
- event-driven filter pipeline.

## Статус

**Источник не завершён.** Следующие репозитории не трогать.
