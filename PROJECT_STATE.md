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

- Продолжен глубокий обход Red-DiscordBot без перехода к следующему источнику.
- Расширен `ideas/COG_MANAGEMENT.md`: pin/unpin модулей, отдельная проверка обновлений, управляемый reload после update, обновление до конкретной revision, диагностика неоднозначного короткого SHA, metadata репозитория, install messages, install agreement и переустановка зависимостей.
- Добавлен `ideas/DATA_STORAGE.md`: изолированное хранилище модулей, разделение core/cog данных, read-only bundled assets, несколько bot instances, temporary instance, storage backend abstraction, bootstrap config, schema migrations и migration locks.
- Добавлен `ideas/AUDIO_INFRA.md`: managed audio/media node, автоматическая загрузка runtime, генерация конфигурации, проверки Java/архитектуры, memory limits, readiness по логам, lifecycle monitoring, plugin detection и managed/unmanaged режим.
- Обновлён `ideas/INDEX.md` для новых категорий.
- Ранее добавлены уникальные Red-механики custom commands/aliases, warning points, warning thresholds/reasons, name history, reports/communication tunnels, selfroles, role editing, global announcements/serverlock, scoped configuration, advanced permissions, advanced trivia, advanced streams и mute subsystem.

## Следующий этап внутри Red

Финальный добивающий проход: оставшиеся `userinfo`, `modlog/events`, API keys/RPC, audio commands, core command surface, оставшиеся cogs, tests/docs/deployment и changelog. **К следующему репозиторию пока не переходим.** После этого отдельным шагом закроем Red как источник и только затем начнём `python-discord/bot`.
