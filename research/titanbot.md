# Research Journal — codebymitch/TitanBot

Источник: `codebymitch/TitanBot`
Ветка: `main`
Статус: 🔵 АКТИВЕН

## Стартовая сверка

Репозиторий публичный, актуальная default branch — `main`. Recursive tree корня закрыт: есть `src/`, `scripts/`, `lavalink/`, `.github/workflows/` и deployment/config files.

## Уже просмотрено

- root recursive tree;
- `README.md`;
- `src/app.js`;
- `src/handlers/loaders/commandLoader.js`;
- `src/commands/Birthday/birthday.js`;
- `src/commands/Birthday/modules/birthday_set.js`;
- `src/commands/Birthday/modules/birthday_list.js`;
- `src/commands/Birthday/modules/next_birthdays.js`.

## Первые направления находок

- startup orchestration: database → web server → commands → handlers → music → Discord login → global registration;
- degraded in-memory DB fallback с явным предупреждением о потере данных после restart;
- `/health` и `/ready` с различными semantics, metrics и HTTP 503 при неготовности;
- встроенный Express API с CORS и простым IP-based rate limiter;
- автоматический перебор следующего порта при `EADDRINUSE`;
- graceful shutdown cron/music/web/database/Discord client;
- централизованный обработчик uncaught exception/unhandled rejection с классификацией recoverable Discord errors;
- cron-задачи для birthdays, giveaways и server counters;
- scheduled cleanup orphaned server counters;
- рекурсивный command loader с категорией из директории, filePath metadata и пропуском `modules/`;
- защита от duplicate primary command names;
- pre-registration validation Discord command names/descriptions/options/choices;
- предупреждение около лимита глобальных команд и controlled truncation сверх лимита;
- опциональное удаление существующих global commands перед registration;
- hot reload command через cache-busting import query;
- birthday subsystem: set/info/list/remove/next/setchannel, валидация month/day и очистка stale users при выводе списка.

## Следующая точка

Продолжить строго по дереву `src/commands/`: сначала завершить `Birthday`, затем `Community`, `Core`, `Economy` и далее по порядку дерева. После каждой существенной пачки обновлять журнал и `PROJECT_STATE.md`. Build/dependency artifacts не считать самостоятельными источниками механик без содержательной логики.
