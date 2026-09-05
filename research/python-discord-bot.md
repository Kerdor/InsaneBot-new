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
- `filtering.py` — 🔎
- `_filter_context.py` — ✅
  - Единый контекст фильтрации хранит входные данные, результаты, matches, filter_info, related messages/channels, дополнительные actions, uploaded attachments и отдельные potential-phish signals.
- `_filter_lists/antispam.py` — 🔎
- `_filter_lists/domain.py` — 🔎
- `_filter_lists/extension.py` — 🔎
- `_filter_lists/filter_list.py` — 🔎
- `_filter_lists/image_hash.py` — 🔎
- `_filter_lists/invite.py` — 🔎
- `_filter_lists/token.py` — 🔎
- `_filter_lists/unique.py` — 🔎
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
- `_settings_types/actions/infraction_and_notification.py` — ✅
- `_settings_types/actions/remove_context.py` — ✅
- `_settings_types/actions/ping.py` — ✅
- `_settings_types/actions/send_alert.py` — ✅
- `_settings_types/settings_entry.py` — ✅
- `_settings_types/validations/bypass_roles.py` — ✅
- `_settings_types/validations/channel_scope.py` — ✅
- `_settings_types/validations/filter_dm.py` — ✅
- Remaining filtering files/directories — ⏳

## Последний батч: что извлечено

### Anti-spam
Добавлен `PDIS-FS009` в `ideas/PYTHON_DISCORD_FILTERING_SPECIAL.md`: отдельные измерения спама — burst, duplicate messages, character volume, attachment volume, emoji volume, link volume, user mentions, role mentions, total/consecutive newlines — с независимыми окнами/порогами и объяснимым measured quantity. Для mentions учитывается Discord-resolved список, с исключением bot/self/replied author; emoji не считаются внутри fenced code blocks.

### Filtering context
Контекст фильтрации выступает как расширяемый контейнер не только для входа, но и для side effects: связанные сообщения/каналы, отложенные actions, загруженные вложения, DM/alert content, action descriptions, matches, potential-phish signals и флаг удаления.

### Action/validation framework
Обнаружены дополнительные варианты, которые нужно учитывать при дальнейшем сравнении: действие может быть идемпотентно объединено через `union`; `RemoveContext` объединяется через OR; ping-настройки объединяются через set union; отправка alert объединяется через OR. `InfractionAndNotification` объединяет уведомление с наказанием, выбирает более строгое наказание/длительность и использует fallback-канал для модерации при невалидном channel ID. Duration принимает как секунды, так и человекочитаемые строки и сериализуется в секунды.

Validation surfaces поддерживают bypass по ролям, сложный channel/category allow+deny scope и отдельное разрешение фильтрации DM.

## Идеи

Основные идеи предыдущих батчей: `ideas/PYTHON_DISCORD.md`.
Backend: `ideas/PYTHON_DISCORD_BACKEND.md`, `ideas/PYTHON_DISCORD_BACKEND_2.md`.
Filtering engine: `ideas/PYTHON_DISCORD_FILTERING_ENGINE.md`.
Filtering UI: `ideas/PYTHON_DISCORD_FILTERING_UI.md`.
Filtering specialized: `ideas/PYTHON_DISCORD_FILTERING_SPECIAL.md`.

## Статус

**Источник не завершён.** Следующая последовательная точка — оставшиеся файлы `bot/exts/filtering/`, затем следующий каталог `bot/exts/fun/`. Следующие репозитории не трогать.
