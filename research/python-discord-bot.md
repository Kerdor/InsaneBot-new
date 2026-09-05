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
- Весь каталог — ✅

### `bot/exts/help_channels/`
- Весь каталог — ✅

### `bot/exts/info/`
- Весь runtime-каталог — ✅
- `doc/` включая batch parser/cache/doc item/HTML/inventory/Markdown/parsing — ✅
- Основные info-команды — ✅

### `bot/exts/moderation/`
- Все root-файлы moderation — ✅
- `watchchannels/__init__.py` — ✅ (пустой)
- `watchchannels/_watchchannel.py` — ✅
- `watchchannels/bigbrother.py` — ✅
- `infraction/__init__.py` — ✅ (пустой)
- `infraction/_scheduler.py` — ✅
- `infraction/_utils.py` — ✅
- `infraction/_views.py` — ✅
- `infraction/infractions.py` — ✅
- `infraction/management.py` — ✅
- `infraction/superstarify.py` — ✅

## Извлечённые идеи

### Moderation
`ideas/PYTHON_DISCORD_MODERATION_2.md` содержит `PDIS-M2-001`–`PDIS-M2-016`.

`ideas/PYTHON_DISCORD_MODERATION_3.md` содержит `PDIS-M3-001`–`PDIS-M3-015`.

`ideas/PYTHON_DISCORD_MODERATION_4.md` содержит `PDIS-M4-001`–`PDIS-M4-011`: комбинированный clean-ban, compromise-response preset, shadow infractions, contextual last/recent selector, resend DM, regex search, actor audit search, state markers, deterministic forced nickname и активный nickname enforcement.

`ideas/PYTHON_DISCORD_MODERATION_5.md` содержит `PDIS-M5-001`–`PDIS-M5-012`: отложенная агрегация watch-сообщений, двухуровневые очереди user/channel, контекстные headers, лимит сообщений на header, token/webhook leak protection, URL embed suppression, attachment fallback, stale-cache fallback, ручной fresh/cache режим, история watch-инцидентов, пометка ушедших участников и безопасный shutdown фоновой relay-задачи.

## Следующая точка

`bot/exts/moderation/` полностью закрыт. Следующий шаг — большой финальный проход оставшейся части `python-discord/bot` по recursive tree: root-файлы, остальные `bot/exts/*`, `.github`, deployment и прочие ещё не закрытые каталоги. Источник остаётся `python-discord/bot`; к `ItzSudhan/Discord-MusicBot` переходить только после полного закрытия этого tree.

**Другие источники не трогать.**
