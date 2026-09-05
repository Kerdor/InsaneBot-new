# PYTHON-DISCORD — Deployment / Bootstrap mechanics

Уникальные deployment и startup-паттерны из `python-discord/bot`. Общий Docker/CI уже есть в банке; здесь только дополнительные конкретные механики.

## PDIS-D001 — Bootstrap-синхронизация Discord → env-конфиг
- Отдельный bootstrap процесс получает фактическое состояние guild через Discord API и генерирует `.env.server`.
- В конфиг попадают реальные IDs каналов, категорий, ролей, webhooks и emojis.

## PDIS-D002 — Bootstrap работает идемпотентно
- Перед созданием ресурса система сначала ищет существующий ресурс по configured ID/name/channel/application owner.
- Повторный запуск не создаёт дубликаты.
- Возвращается `changes_made`, чтобы различать no-op и реально изменившийся setup.

## PDIS-D003 — Приоритет собственного webhook приложения
- Если несколько webhooks совпадают по каналу/имени, предпочтение получает webhook, созданный самим приложением.
- Только затем используется подходящий внешний webhook как fallback.

## PDIS-D004 — Webhook reuse по сохранённому ID
- Сначала проверяется конкретный configured webhook ID.
- Если он существует и имеет token, его конфигурация сохраняется вместо создания нового webhook.

## PDIS-D005 — Автоматическое создание отсутствующих webhooks
- Если нужный webhook не найден, bootstrap создаёт его в требуемом канале и записывает новый ID в конфигурацию.
- Таким образом setup можно восстановить после ручного удаления ресурса.

## PDIS-D006 — Emoji bootstrap с clone fallback
- Если нужный custom emoji отсутствует, bootstrap скачивает исходный emoji asset с CDN, кодирует его и создаёт emoji в guild.
- Если asset не найден, операция не маскируется как успешная.

## PDIS-D007 — Нормализация Discord names → config keys
- Названия ролей/каналов преобразуются в стабильные config keys: lowercase, spaces → `_`, hyphens → `_`.
- Специальные последовательности каналов можно преобразовать в индексированные logical names.

## PDIS-D008 — Автоматическое различение каналов и категорий
- Bootstrap одним API проходом строит две отдельные mapping-структуры: text/other channels и categories.
- Config model выбирает ресурс из соответствующего namespace.

## PDIS-D009 — Missing-resource fallback с предупреждением
- Отсутствующий channel/role/category не обязательно ломает весь bootstrap: записывается warning, после чего применяется default config.
- Это позволяет частично восстановить сервер без ручного пересоздания всего набора ресурсов.

## PDIS-D010 — Startup проверка membership перед mutation
- Перед изменением guild bootstrap сначала проверяет, является ли bot участником требуемого сервера.
- 403/404 трактуются как понятное отсутствие membership; прочие HTTP ошибки пробрасываются.

## PDIS-D011 — Автоматический Community upgrade
- Bootstrap может обнаружить, что guild не имеет Community feature, и выполнить controlled upgrade с указанием rules и announcements channels.
- Повторный запуск не меняет уже Community guild.

## PDIS-D012 — Application intent flags self-healing
- Bootstrap читает текущие application flags, вычисляет `current | minimum_required` и PATCH'ит только недостающие flags.
- Уже включённые flags не перезаписываются.

## PDIS-D013 — Различение изменения конфигурации и изменения runtime-ресурсов
- Создание webhook/emoji может менять Discord state, но итоговый config считается источником истины.
- Bootstrap отслеживает отдельно изменения generated config и использует итоговый env как reconciliation result.

## PDIS-D014 — Atomic-ish generated env rewrite with change detection
- Сгенерированный env сначала сравнивается с предыдущим содержимым.
- Файл обновляется целиком и `before != after` позволяет точно определить, был ли config изменён.

## PDIS-D015 — Commented sections в generated configuration
- Автогенерируемый env группируется по категориям с комментариями (`categories`, `channels`, `roles`, `webhooks`, `emojis`), чтобы человек мог быстро инспектировать результат.

## PDIS-D016 — Fatal diagnostics вместо продолжения с битой конфигурацией
- Отсутствующий обязательный environment variable останавливает bootstrap с конкретным сообщением о том, что добавить.
- Неизвестные ключи в критических config dictionaries также приводят к понятному fatal exit.

## PDIS-D017 — Разные exit semantics для startup failure
- Неверная конфигурация, недоступный Redis и недоступный site API имеют разные диагностические сообщения, хотя процесс завершается единообразно.

## PDIS-D018 — Docker build dependency layer отдельно от source layer
- Dependencies устанавливаются до копирования исходников.
- Изменение кода не инвалидирует дорогой dependency layer, что ускоряет rebuild.

## PDIS-D019 — Frozen lockfile в production build
- Production image устанавливает зависимости строго из lockfile без пересчёта dependency resolution.
- CI/build падает, если lockfile не соответствует project configuration.

## PDIS-D020 — BuildKit cache для dependency installation
- uv cache монтируется как build cache, ускоряя повторные builds без включения cache в image.

## PDIS-D021 — Runtime image отделён от builder image
- Сборка dependency environment выполняется в builder stage, а runtime image получает готовое окружение без build tooling.

## PDIS-D022 — Git SHA как runtime diagnostic identity
- Commit SHA передаётся в image через build arg и сохраняется в environment variable.
- Sentry/diagnostics могут однозначно связать runtime exception с исходным commit.

## PDIS-D023 — Read-only source mount для локальной разработки
- В compose source code монтируется в контейнер read-only, сохраняя код доступным для разработки без возможности случайной записи контейнером.

## PDIS-D024 — Health-gated startup dependencies
- Compose ждёт healthcheck PostgreSQL перед запуском зависимого service.
- Остальные сервисы запускаются с `depends_on`, формируя явный dependency graph.

## PDIS-D025 — Container restart policies по типу сервиса
- Критические долгоживущие сервисы используют `unless-stopped`, а условно отключаемый/ошибочный сервис — `on-failure`.

## PDIS-D026 — Ограничение Docker log files
- JSON logs каждого контейнера имеют `max-size` и `max-file`, чтобы runtime logs не заполняли диск бесконечно.

## PDIS-D027 — Localhost-only exposure development services
- Redis, HTTP API и sandbox service публикуются только на `127.0.0.1`, а не на все сетевые интерфейсы хоста.

## PDIS-D028 — Isolated privileged sandbox service
- Code execution sandbox выделен в отдельный контейнер с отдельным endpoint.
- Основной bot container не выполняет untrusted code непосредственно внутри себя.

## PDIS-D029 — CI concurrency cancellation
- Для одной workflow/ref разрешён один актуальный run.
- Новый push автоматически отменяет устаревший run, экономя CI ресурсы.

## PDIS-D030 — Reusable workflow stages
- Lint/test, build/deploy и Sentry release оформлены отдельными reusable workflows.
- Основной pipeline связывает их зависимостями вместо дублирования YAML.

## PDIS-D031 — SHA-tagged container releases
- Каждый main commit получает короткий immutable SHA tag дополнительно к `latest`.
- Deployment использует SHA tag, а не mutable `latest`.

## PDIS-D032 — Deploy only after successful build/test
- Kubernetes deployment зависит от успешного lint/test и build jobs.
- Broken commit физически не доходит до production deployment stage.

## PDIS-D033 — Production environment gate
- Production deployment запускается только для main branch и выполняется через отдельный GitHub environment.
- Это отделяет обычные PR builds от production mutation.

## PDIS-D034 — Sentry release после deployment
- Sentry release создаётся отдельной стадией после успешного deploy.
- Runtime errors связываются с production release metadata.

## PDIS-D035 — Dependency updates группируются по экосистеме
- Dependabot/аналогичный updater отдельно отслеживает Python/uv dependencies и GitHub Actions.
- Updates Actions можно автоматически объединять в одну группу.

## PDIS-D036 — Автоматический lock refresh при изменении dependency manifest
- Pre-commit hook запускает `uv lock`, если изменены `pyproject.toml`, `uv.lock` или `uv.toml`.
- Это уменьшает шанс закоммитить рассинхронизированный manifest/lockfile.

## PDIS-D037 — Pre-commit как локальная копия CI quality gates
- YAML/TOML validation, EOF/trailing-whitespace и Ruff запускаются локально тем же инструментом, который используется до merge.
- Исправления Ruff могут автоматически применяться, но изменённый код обязан пройти повторную проверку.

## PDIS-D038 — CI dependency resolution на lowest supported versions
- Отдельный режим dependency resolver может проверять проект на минимально разрешённых версиях, а не только на latest lock.
- Это ловит случайные зависимости от новых API.
