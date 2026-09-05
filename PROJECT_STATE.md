# PROJECT STATE

## Текущее состояние

Проект: новый InsaneBot с нуля.

Текущий этап: **максимально глубокий сбор и каталогизация идей/механик из сторонних Discord-ботов.**

## Правила этапа

- Источники исследуются **строго по очереди**: сначала один репозиторий доводится до максимально полного обследования, только после этого переходим к следующему.
- Сейчас активен **только первый источник: `Cog-Creators/Red-DiscordBot`**. Остальные источники временно не исследуются.
- Собираем максимально всё, без предварительной фильтрации.
- Перед добавлением сверяем найденную механику с уже существующим банком идей и **не создаём дубликаты идентичных систем**.
- Если существующая система уже записана, новые детали добавляются только когда они дают новый UX, поведение, настройку, ограничение или архитектурный вариант.
- Проверяем не только README/MD-документацию, но и исходный код, структуру директорий, команды, event handlers, конфиги, утилиты, API, dashboard/web, deployment, тесты и прочие файлы.
- Обычные команды тоже фиксируем отдельно; очевидность функции не является причиной её пропуска.
- Маленькие, странные, неиспользуемые и потенциально бесполезные механики тоже сохраняем.
- Все найденные варианты одной механики сохраняем, если они отличаются поведением, настройками, UX или архитектурой.
- Источники используются как идеи и механики для самостоятельной реализации; исходный код и защищённые ассеты не копируются.
- Идеи не складываются в один временный файл: после сверки они сразу раскладываются по тематическим системам. Если существующей категории недостаточно, создаётся новый файл.

## Источники и порядок

1. **Cog-Creators/Red-DiscordBot — АКТИВЕН, исследуем до дыр.**
2. python-discord/bot — ждать полного завершения Red-DiscordBot.
3. ItzSudhan/Discord-MusicBot — ждать полного завершения Red-DiscordBot.
4. codebymitch/TitanBot — ждать полного завершения Red-DiscordBot.
5. GAwesomeBot/bot — ждать полного завершения Red-DiscordBot.
6. CorwinDev/Discord-Bot — ждать полного завершения Red-DiscordBot.
7. Tomato6966/Multipurpose-discord-bot — ждать полного завершения Red-DiscordBot.

## Последние существенные действия

- Зафиксирован новый порядок исследования: **один источник целиком → следующий источник**.
- Активным источником назначен `Cog-Creators/Red-DiscordBot`.
- Для Red-DiscordBot продолжается обход реального дерева репозитория: core framework, cogs, команды, event handlers, конфиги, утилиты, API, deployment, тесты и документация.
- Выполнена сверка новых находок с существующим банком идей: уже покрытые economy/fun/ticket/social/stats и другие идентичные системы не дублируются.
- Ранее добавлены уникальные Red-механики custom commands/aliases, warning points, warning thresholds/reasons, name history, reports/communication tunnels, selfroles, role editing, global announcements/serverlock, scoped configuration, advanced permissions, advanced trivia, advanced streams и mute subsystem.
- Добавлен `ideas/CORE_FRAMEWORK.md`: многоуровневые/временные cog paths, install path, безопасное добавление путей, dynamic module discovery, batch load/unload/reload, подробные статусы загрузки, сохранение последнего traceback, конфликт command/alias, import cache/reload, global/server prefixes, invite visibility, confirmation UX и permission-state mechanics.
- Добавлен `ideas/HELP_UX.md`: заменяемый help formatter, единый HelpSettings, reactions/buttons/select navigation, фильтрация только доступных команд, прямой показ недоступной команды, custom tagline `[p]`, полные signatures, компактное отображение aliases, пагинация subcommands, embed/code-block режимы, delete/reaction timeout и разные ошибки unknown command/subcommand.
- Добавлен `ideas/FILTERING.md`: server/channel filters, thread inheritance, name/nickname filtering, безопасный fallback nickname, autoban по count/timeframe, per-user reset counters, word-boundary/case-insensitive matching, проверка poll/attachment/forward/embed/component text, modlog cases, edited messages, automod immunity, regex cache, DM выдача списка и bulk add/remove фраз.
- Индекс обновлён новыми категориями `CORE_FRAMEWORK.md`, `HELP_UX.md`, `FILTERING.md`.
- Red **не считается завершённым**. Следующий проход продолжает downloader, admin, modlog/events, userinfo, data/config/i18n, API keys/RPC, audio и оставшиеся cogs/tests/docs/deployment.
