# TITAN CORE — Банк идей

Находки `codebymitch/TitanBot` (main).

- TITAN-K001 — При старте бот выполняет явную последовательность инициализации: БД → web server → commands → handlers → music → Discord login → slash registration.
- TITAN-K002 — При недоступности PostgreSQL бот может переключаться на in-memory storage и продолжать работу в degraded mode с явным предупреждением о неперсистентности.
- TITAN-K003 — `/health` и `/ready` разделяют liveness/health и readiness-проверку.
- TITAN-K004 — Readiness endpoint возвращает HTTP 503 и диагностические metrics, если Discord client ещё не Ready или БД degraded.
- TITAN-K005 — Health/ready API показывает uptime, guild count, command count, database mode/status и schema version.
- TITAN-K006 — Встроенный Express server имеет настраиваемый host/port и автоматически пробует следующие порты при `EADDRINUSE`.
- TITAN-K007 — Встроенный API имеет простой IP-based sliding-window rate limit без внешнего сервиса.
- TITAN-K008 — CORS поддерживает как wildcard, так и список разрешённых origins.
- TITAN-K009 — Graceful shutdown централизованно останавливает cron jobs, music players, web server, DB pool и Discord client.
- TITAN-K010 — Uncaught exceptions логируются как fatal task errors с последующим graceful shutdown.
- TITAN-K011 — Из unhandled rejections отдельно исключаются известные recoverable Discord interaction error codes.
- TITAN-K012 — Scheduler запускает независимые периодические задачи для birthdays, giveaways и server counters.
- TITAN-K013 — Scheduled maintenance может не только обновлять сущности, но и удалять orphaned records, ссылающиеся на уже удалённые Discord channels.
- TITAN-K014 — Command loader рекурсивно обходит категории, но намеренно исключает директории `modules/` из списка самостоятельных команд.
- TITAN-K015 — Загруженной команде автоматически добавляются metadata `category` и `filePath` из filesystem.
- TITAN-K016 — Duplicate primary command names подавляются через Set до помещения в Collection.
- TITAN-K017 — Перед регистрацией slash commands выполняется отдельная глубокая валидация длины names/descriptions/choices на уровнях command, option и subcommand.
- TITAN-K018 — При приближении к глобальному лимиту slash commands loader выдаёт предупреждение, а при превышении контролируемо обрезает payload до лимита.
- TITAN-K019 — Перед registration можно опционально очистить существующие global commands.
- TITAN-K020 — Команды можно hot-reload'ить через cache-busting ESM import с timestamp query parameter.
- TITAN-K021 — Birthday command оформлен как единая slash-команда с набором subcommands, а реализация каждой операции вынесена в отдельный module handler.
- TITAN-K022 — Birthday `/set` ограничивает month/day через Discord option min/max validation.
- TITAN-K023 — Birthday list/next проверяют существование Discord members и асинхронно удаляют stale birthday records для покинувших сервер пользователей.
- TITAN-K024 — Birthday subsystem имеет отдельную настройку канала объявлений с возможностью отключения через отсутствие channel.
- TITAN-K025 — Birthday `/next` вычисляет человекочитаемые relative states `Today`, `Tomorrow`, `In N days`.
