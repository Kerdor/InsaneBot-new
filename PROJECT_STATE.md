# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **максимально глубокий сбор и каталогизация идей/механик из сторонних Discord-ботов.**

## Правила этапа

- Источники исследуются строго по очереди: один репозиторий полностью обследуется до перехода к следующему.
- Собираем максимально всё, без предварительной фильтрации.
- Перед добавлением сверяем найденное с банком идей и не создаём идентичные дубликаты.
- Если система уже есть, добавляем только новые UX, поведение, настройки, ограничения или архитектурные варианты.
- Проверяем исходный код, структуру, команды, handlers, конфиги, утилиты, API, deployment, тесты и документацию.
- Обычные и очевидные команды тоже фиксируем.
- Идеи сразу распределяются по тематическим `ideas/`; новые тематические файлы разрешены.

## Правило восстановления после смены чата

- `RESEARCH_PROGRESS.md` — общий порядок источников и текущая точка.
- `research/<source>.md` — последовательный журнал каждой папки/файла.
- `✅` означает реальный просмотр + сверку с банком идей.
- После каждого существенного батча обновляются журнал и `PROJECT_STATE.md`.

## Источники и порядок

1. **Cog-Creators/Red-DiscordBot — ЗАВЕРШЁН.**
2. **python-discord/bot — АКТИВЕН.**
3. ItzSudhan/Discord-MusicBot — ждать завершения.
4. codebymitch/TitanBot — ждать завершения.
5. GAwesomeBot/bot — ждать завершения.
6. CorwinDev/Discord-Bot — ждать завершения.
7. Tomato6966/Multipurpose-discord-bot — ждать завершения.

## Текущий прогресс `python-discord/bot`

Полное recursive tree получено на tree SHA `0e4cd5cb46f2239eacccdded8cdf02ba89028ab9`.

Последний завершённый батч включает:
- `README.md`;
- `bot/bot.py`;
- `bot/constants.py`;
- `bot/converters.py`;
- `bot/decorators.py`;
- `bot/exts/info/subscribe.py`;
- `bot/exts/moderation/stream.py`;
- `bot/exts/moderation/silence.py`;
- `bot/exts/fun/duck_pond.py`;
- `bot/exts/info/resources.py`;
- `bot/exts/info/pypi.py`;
- `bot/exts/utils/ping.py`;
- `bot/exts/moderation/alts.py`;
- `bot/exts/moderation/modpings.py`;
- `bot/exts/info/help.py`;
- `bot/exts/utils/extensions.py`;
- `bot/exts/utils/bot.py`;
- `bot/exts/info/source.py`;
- `bot/exts/utils/internal.py`;
- `bot/exts/info/stats.py`.

Добавлен `ideas/PYTHON_DISCORD_ADVANCED.md` с новым батчем механик PDIS-A001–A012. Существующие общие идеи намеренно не размножались.

**Следующая точка:** продолжить остальные файлы `bot/exts/...` строго по recursive tree. После них — `bot/resources/`, `bot/utils/`, `tests/`, root/.github/deployment surfaces.

**Источник не завершён. Следующие репозитории не трогать.**
