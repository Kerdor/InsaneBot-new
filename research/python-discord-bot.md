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
- `_filters/antispam/__init__.py` — ✅
- `_filters/antispam/attachments.py` — ✅
- `_filters/antispam/burst.py` — ✅
- `_filters/antispam/chars.py` — ✅
- `_filters/antispam/duplicates.py` — ✅
- `_filters/antispam/emoji.py` — ✅
- `_filters/antispam/links.py` — ✅
- `_filters/antispam/mentions.py` — ✅
- `_filters/antispam/newlines.py` — ✅
- `_filters/antispam/role_mentions.py` — ✅
- `_filters/domain.py` — ✅
- `_filters/extension.py` — ✅
- `_filters/filter.py` — ✅
- `_filters/image_hash.py` — ✅
- `_filters/invite.py` — ✅
- `_filters/token.py` — ✅
- `_filters/unique/__init__.py` — ✅
- `_filters/unique/discord_token.py` — ✅
- `_filters/unique/everyone.py` — ✅
- `_filters/unique/webhook.py` — ✅
- `_settings_types/actions/infraction_and_notification.py` — ✅
- `_settings_types/actions/remove_context.py` — ✅
- `_settings_types/actions/ping.py` — ✅
- `_settings_types/actions/send_alert.py` — ✅
- `_settings_types/settings_entry.py` — ✅
- `_settings_types/validations/bypass_roles.py` — ✅
- `_settings_types/validations/channel_scope.py` — ✅
- `_settings_types/validations/filter_dm.py` — ✅
- `_settings.py` — ✅
- `_utils.py` — ✅
- Remaining filtering files/directories — ⏳

## Последний батч: что извлечено

### Anti-spam
Добавлен `PDIS-FS009`: отдельные измерения спама — burst, duplicate messages, character volume, attachment volume, emoji volume, link volume, user mentions, role mentions, total/consecutive newlines — с независимыми окнами/порогами и объяснимым measured quantity.

### Filtering context/settings
Подтверждён расширяемый FilterContext для входных данных и side effects. Settings framework поддерживает typed entries, наследование defaults, точечные overrides, объединение actions и безопасное игнорирование неизвестных настроек с предупреждением.

### Новые специализированные идеи
Добавлены `PDIS-FS010` — normalization layer против invisible/Zalgo/URL-encoding/backslash/newline bypasses; `PDIS-FS011` — безопасное перехватывание Discord token/webhook leaks с валидацией, цензурированием и предотвращением повторного логирования; `PDIS-FS012` — semantic filter events независимые от gateway events.

`discord_token` использует структурную проверку потенциального токена, определение bot/user по decoded ID, redaction HMAC и подавление обычного deletion log. Webhook filter не только обнаруживает секретный URL, но и отзывает webhook через API.

## Идеи

Основные идеи предыдущих батчей: `ideas/PYTHON_DISCORD.md`.
Backend: `ideas/PYTHON_DISCORD_BACKEND.md`, `ideas/PYTHON_DISCORD_BACKEND_2.md`.
Filtering engine: `ideas/PYTHON_DISCORD_FILTERING_ENGINE.md`.
Filtering UI: `ideas/PYTHON_DISCORD_FILTERING_UI.md`.
Filtering specialized: `ideas/PYTHON_DISCORD_FILTERING_SPECIAL.md`.

## Статус

**Источник не завершён.** Следующая последовательная точка — оставшиеся файлы/подкаталоги `bot/exts/filtering/`, затем следующий каталог `bot/exts/fun/`. Следующие репозитории не трогать.
