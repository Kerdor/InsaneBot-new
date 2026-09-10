# GAwesomeBot — Internals

> Механики и архитектурные идеи из `GAwesomeBot/bot/Internals/`.
> Это идеи для собственной архитектуры InsaneBot, а не копирование реализации.

## Boot / Lifecycle

### GAB-INT-001 — Разделение pre-boot и boot stack
- Источник: `Internals/Boot.js`
- Категория: Lifecycle
- Описание: запуск разделён на предварительный стек и основной стек и выполняется последовательно.
- Наш вариант: отдельные стадии startup с явными границами.

### GAB-INT-002 — Разные bootstrap-функции master/shard
- Источник: `Boot.js`
- Категория: Sharding
- Описание: master и shard-процессы имеют разные pre-boot/boot stacks.
- Наш вариант: процессная роль должна определять набор инициализируемых подсистем.

### GAB-INT-003 — CLI boot hooks
- Источник: `Boot.js`
- Категория: Developer tools
- Описание: аргументы запуска превращаются в вызываемые boot-функции через registry.
- Наш вариант: registry startup-команд для миграций, safe mode, диагностики и т. п.

### GAB-INT-004 — Alias для CLI boot-команд
- Источник: `Boot.js`
- Категория: UX
- Описание: длинные имена boot-функций имеют короткие алиасы.
- Наш вариант: удобные сокращения для dev/maintenance запуска.

### GAB-INT-005 — Safe Mode
- Источник: `Boot.js`
- Категория: Надёжность
- Описание: специальный режим запускает только минимальные internals и БД, не поднимая обычный web/runtime слой.
- Наш вариант: аварийный режим для восстановления конфигурации и диагностики.

### GAB-INT-006 — Режим запуска без обработки сообщений
- Источник: `Boot.js`
- Категория: Диагностика
- Описание: отдельный startup flag отключает MESSAGE_CREATE на shard.
- Наш вариант: режим «бот онлайн, но команды выключены» для обслуживания.

### GAB-INT-007 — Runtime promotion host → sudo maintainer
- Источник: `Boot.js`
- Категория: Безопасность
- Описание: startup-параметр может назначить host-пользователя привилегированным и сохранить это в конфиге.
- Наш вариант: отдельный аварийный bootstrap-owner механизм.

### GAB-INT-008 — Атомарная запись конфигурации при bootstrap-изменении
- Источник: `Boot.js`
- Категория: Надёжность
- Описание: изменение startup-конфига записывается атомарно.
- Наш вариант: не оставлять частично записанные конфиги после сбоя.

## Client / Runtime

### GAB-INT-009 — Единый расширенный Client как runtime facade
- Источник: `Client.js`
- Категория: Архитектура
- Описание: вокруг Discord client собран единый facade для команд, IPC, workers, conversion, extendables и lifecycle.
- Наш вариант: один контролируемый runtime facade вместо доступа подсистем к случайным глобалам.

### GAB-INT-010 — Отдельное состояние readiness
- Источник: `Client.js`
- Категория: Lifecycle
- Описание: client хранит собственный флаг готовности, независимый от базового Discord-класса.
- Наш вариант: явные состояния `starting/ready/stopping`.

### GAB-INT-011 — Process role / shard identity в Client
- Источник: `Client.js`
- Категория: Sharding
- Описание: client знает свой shard ID и может использовать его во всех сервисах.
- Наш вариант: единый runtime context с process/shard identity.

### GAB-INT-012 — Централизованное управление пользовательскими timeout
- Источник: `Client.js`
- Категория: Lifecycle
- Описание: timeout/interval регистрируются внутри Client и автоматически отменяются при destroy.
- Наш вариант: timer registry, очищаемый при остановке бота.

### GAB-INT-013 — Именованные таймеры
- Источник: `Client.js`
- Категория: Диагностика
- Описание: timer получает логический key, по которому его можно классифицировать.
- Наш вариант: key для отладки и контроля фоновых задач.

### GAB-INT-014 — Sweep разных типов сообщений с разными TTL
- Источник: `Client.js`
- Категория: Производительность
- Описание: обычные сообщения и командные сообщения имеют разные сроки жизни в cache.
- Наш вариант: отдельные retention policy для дорогих/полезных объектов.

### GAB-INT-015 — Не чистить cache при unlimited TTL
- Источник: `Client.js`
- Категория: Производительность
- Описание: специальное значение lifetime полностью отключает sweep.
- Наш вариант: явный unlimited режим вместо неочевидного поведения.

### GAB-INT-016 — Подсчёт результата cache sweep
- Источник: `Client.js`
- Категория: Диагностика
- Описание: sweep возвращает/логирует количество удалённых объектов и каналов.
- Наш вариант: maintenance-метрики для cache cleanup.

### GAB-INT-017 — Локальный prefix с поддержкой mention
- Источник: `Client.js`
- Категория: Команды
- Описание: prefix может быть обычной строкой или специальным режимом упоминания бота.
- Наш вариант: единый prefix resolver с mention-mode.

### GAB-INT-018 — Ожидание PM-сообщения с фильтром и timeout
- Источник: `Client.js`
- Категория: UX
- Описание: интерактивные DM-сценарии используют отдельный await-механизм с фильтром и сроком жизни.
- Наш вариант: reusable conversation/session waiter.

### GAB-INT-019 — Один активный PM waiter на channel+user
- Источник: `Client.js`
- Категория: Надёжность
- Описание: новый waiter заменяет старый для той же пары channel/user, предварительно отменяя старый timeout.
- Наш вариант: предотвращать конфликтующие интерактивные сессии.

### GAB-INT-020 — IPC-проксирование PM waiter между shard
- Источник: `Client.js`
- Категория: Sharding
- Описание: master хранит waiter, а shard обращается к нему через IPC.
- Наш вариант: централизованные операции, требующие единой точки состояния.

### GAB-INT-021 — Универсальные reload API для command modules
- Источник: `Client.js`
- Категория: Developer tools
- Описание: PM/Public/Shared команды можно перезагрузить отдельно или все сразу без перезапуска процесса.
- Наш вариант: hot-reload модулей для разработки.

### GAB-INT-022 — Нормализация command aliases перед reload/get
- Источник: `Client.js`
- Категория: Архитектура
- Описание: получение и reload команды сначала разрешает canonical command name из alias.
- Наш вариант: alias resolver как единый слой.

### GAB-INT-023 — Централизованный permission matrix для shared-команд
- Источник: `Client.js`
- Категория: Безопасность
- Описание: eval/admin/shutdown имеют отдельные уровни доступа: host, maintainer, sudo maintainer.
- Наш вариант: декларативные уровни привилегий для developer/admin tools.

### GAB-INT-024 — Единый member/channel/role resolver
- Источник: `Client.js`
- Категория: UX
- Описание: сущности можно искать по ID, mention, username, nickname, name и другим формам.
- Наш вариант: reusable entity resolution service.

### GAB-INT-025 — Разделение client capability и hierarchy при moderation
- Источник: `Client.js`
- Категория: Модерация
- Описание: проверка действия возвращает отдельно возможность бота выполнить действие и положение инициатора относительно цели.
- Наш вариант: не смешивать bot permissions и moderator hierarchy в одной проверке.

### GAB-INT-026 — Централизованный violation pipeline
- Источник: `Client.js`
- Категория: Модерация
- Описание: нарушение проходит общий pipeline: штраф/strike → роль → действие → уведомление пользователя → уведомление админов → ModLog.
- Наш вариант: единый violation service с различными action strategies.

### GAB-INT-027 — Fallback block при невозможности наказания
- Источник: `Client.js`
- Категория: Модерация
- Описание: если mute/kick/ban не удалось выполнить, бот может заблокировать пользователя от использования самого бота и сообщить администраторам.
- Наш вариант: безопасный fallback action для автоматической модерации.

### GAB-INT-028 — Изоляция ошибок DM от основной модерации
- Источник: `Client.js`
- Категория: Надёжность
- Описание: невозможность отправить DM не отменяет основное действие.
- Наш вариант: notification side-effects никогда не должны ломать core action.

### GAB-INT-029 — Уведомление всех bot-admins через общий resolver
- Источник: `Client.js`
- Категория: Модерация
- Описание: пользователи с достаточным bot-admin level получают DM о важных событиях.
- Наш вариант: централизованный admin notification service.

### GAB-INT-030 — Точечный channel mute через permission overwrite
- Источник: `Client.js`
- Категория: Модерация
- Описание: mute может действовать только в конкретном канале, не затрагивая сервер целиком.
- Наш вариант: channel-scoped punishment.

### GAB-INT-031 — Безопасный unmute с сохранением чужих overwrites
- Источник: `Client.js`
- Категория: Модерация
- Описание: перед удалением overwrite проверяется, содержит ли он только связанные с каналом ограничения; иначе меняется лишь SEND_MESSAGES.
- Наш вариант: не уничтожать независимые permission overrides.

### GAB-INT-032 — Удержание короткого server diagnostic log
- Источник: `Client.js`
- Категория: Логи
- Описание: внутренние server logs хранятся с уровнем, текстом, channel/user IDs и timestamp, после 200 записей старые удаляются.
- Наш вариант: bounded in-document diagnostic log.

### GAB-INT-033 — Передача расширения в отдельный worker
- Источник: `Client.js`
- Категория: Расширения
- Описание: выполнение пользовательского extension code уходит в worker manager.
- Наш вариант: изолировать потенциально тяжёлые/небезопасные пользовательские сценарии.

## Errors

### GAB-INT-034 — Коды ошибок вместо уникальных текстов
- Источник: `Errors/GABError.js`, `Messages.js`
- Категория: Ошибки
- Описание: ошибка имеет стабильный machine-readable code, а текст берётся из централизованного registry.
- Наш вариант: `ErrorCode` + локализуемое сообщение.

### GAB-INT-035 — Единый реестр error messages
- Источник: `Errors/Messages.js`
- Категория: Ошибки
- Описание: сообщения регистрируются по ключам; значение может быть строкой или функцией-параметризатором.
- Наш вариант: централизованный каталог ошибок.

### GAB-INT-036 — Специализированные типы GABError
- Источник: `GABError.js`
- Категория: Ошибки
- Описание: поверх базовых Error доступны TypeError и RangeError с тем же кодовым механизмом.
- Наш вариант: классифицировать ошибки по типу и machine code.

### GAB-INT-037 — Metadata внутри структурированной ошибки
- Источник: `GABError.js`
- Категория: Диагностика
- Описание: error хранит дополнительные metadata отдельно от пользовательского текста.
- Наш вариант: контекст ошибки должен быть доступен логгеру без засорения сообщения.

### GAB-INT-038 — Отдельные ошибки для разных failure domains
- Источник: `Messages.js`
- Категория: Ошибки
- Описание: есть отдельные коды для поиска сущностей, IPC/child process, extensions, Central API, БД, modlog и interactive await.
- Наш вариант: доменная taxonomy ошибок.

### GAB-INT-039 — Ошибка неизвестного event с machine code
- Источник: `Messages.js`, `EventHandler.js`
- Категория: Диагностика
- Описание: событие, отсутствующее в registry, превращается в конкретную кодированную ошибку.
- Наш вариант: ошибки маршрутизации должны явно показывать отсутствующий handler.

## Event System

### GAB-INT-040 — BaseEvent lifecycle: requirements → prerequisite → handle
- Источник: `Events/BaseEvent.js`
- Категория: Архитектура
- Описание: каждый event проходит предварительную проверку и подготовительный этап перед основным handler.
- Наш вариант: единый event pipeline.

### GAB-INT-041 — Event requirements как дешёвый early exit
- Источник: `BaseEvent.js`
- Категория: Производительность
- Описание: событие не делает БД/API работу, если requirements сразу возвращает false.
- Наш вариант: фильтровать события до дорогих операций.

### GAB-INT-042 — Prerequisite hook
- Источник: `BaseEvent.js`
- Категория: Архитектура
- Описание: отдельный hook предназначен для загрузки документов/подготовки зависимостей.
- Наш вариант: отделять подготовку данных от business logic.

### GAB-INT-043 — Event registry из конфигурации
- Источник: `Events/EventHandler.js`
- Категория: Архитектура
- Описание: список event handlers задаётся конфигом, а runtime динамически создаёт cache экземпляров.
- Наш вариант: конфигурационный event registry.

### GAB-INT-044 — Несколько handlers на одно Discord event
- Источник: `EventHandler.js`
- Категория: Архитектура
- Описание: один event может иметь набор независимых файлов-handler'ов.
- Наш вариант: композиция обработчиков вместо гигантского switch.

### GAB-INT-045 — Параллельный запуск event handlers
- Источник: `EventHandler.js`
- Категория: Производительность
- Описание: handlers одного события запускаются через `Promise.all`.
- Наш вариант: параллелить независимые обработчики.

### GAB-INT-046 — Hot reload event group
- Источник: `EventHandler.js`
- Категория: Developer tools
- Описание: можно перезагрузить все handlers конкретного события или весь event registry wildcard-операцией.
- Наш вариант: reload без restart.

### GAB-INT-047 — Extension event wrapper с изоляцией исключений
- Источник: `Extensions/EventsHandler.js`
- Категория: Надёжность
- Описание: ошибки пользовательского extension event не должны падать в основной event emitter.
- Наш вариант: catch boundary вокруг стороннего/плагинного кода.

### GAB-INT-048 — Default no-op handler для неподдержанного extension event
- Источник: `Extensions/EventsHandler.js`
- Категория: Расширения
- Описание: если для события нет специальной реализации, используется безопасный default handler.
- Наш вариант: no-op fallback для необязательных extension hooks.

## Extendables

### GAB-INT-049 — Runtime extendable registry
- Источник: `ExtendableBase.js`, `Client.js`
- Категория: Архитектура
- Описание: расширения поведения Discord.js-структур регистрируются в отдельной коллекции.
- Наш вариант: контролируемый registry runtime extensions.

### GAB-INT-050 — Enable/disable extendable
- Источник: `ExtendableBase.js`
- Категория: Developer tools
- Описание: runtime extension можно включить или снять без изменения исходного класса.
- Наш вариант: lifecycle для monkey-patch/adapter features.

### GAB-INT-051 — Extendable применяется только к указанным структурам
- Источник: `ExtendableBase.js`
- Категория: Безопасность архитектуры
- Описание: расширение содержит список типов, к которым оно применяется.
- Наш вариант: whitelist target classes.

### GAB-INT-052 — Capability-like свойства `readable` и `postable`
- Источник: `Extendables/Readable.js`, `Postable.js`
- Категория: Permissions
- Описание: объект канала получает простое свойство, отражающее возможность чтения/отправки.
- Наш вариант: унифицированные capability checks.

### GAB-INT-053 — Capability property учитывает guild permissions
- Источник: `Readable.js`, `Postable.js`
- Категория: Permissions
- Описание: `readable/postable` вычисляются по текущим permissions бота в конкретном канале.
- Наш вариант: capability getter вместо ручных проверок в каждом месте.

## Sharding / IPC

### GAB-INT-054 — Отдельный IPC abstraction поверх process messaging
- Источник: `IPC.js`
- Категория: Sharding
- Описание: IPC API скрывает детали передачи сообщений между master/shard.
- Наш вариант: единый transport layer.

### GAB-INT-055 — Broadcast IPC на все shards
- Источник: `IPC.js`, `Sharder.js`
- Категория: Sharding
- Описание: специальный target `*` отправляет сообщение всем shards и возвращает aggregate Promise.
- Наш вариант: broadcast command для синхронизации состояния.

### GAB-INT-056 — Forward event к shard по guild ID
- Источник: `IPC.js`
- Категория: Sharding
- Описание: сообщение автоматически маршрутизируется на shard, которому принадлежит guild.
- Наш вариант: guild-aware IPC routing.

### GAB-INT-057 — IPC fallback на shard 0
- Источник: `IPC.js`
- Категория: Надёжность
- Описание: при неизвестном shard ID отправитель использует shard 0 как fallback.
- Наш вариант: только для операций, где fallback безопасен.

### GAB-INT-058 — Deterministic guild→shard calculation
- Источник: `IPC.js`
- Категория: Sharding
- Описание: shard вычисляется из Discord snowflake guild ID и общего количества shards.
- Наш вариант: один canonical shard resolver.

### GAB-INT-059 — Автоматический respawn shard
- Источник: `Sharder.js`
- Категория: Надёжность
- Описание: неожиданно завершившийся shard автоматически создаётся заново, если система не находится в shutdown.
- Наш вариант: supervised worker restart.

### GAB-INT-060 — Graceful shutdown flag для отключения respawn
- Источник: `Sharder.js`
- Категория: Lifecycle
- Описание: shutdown mode отличает плановое завершение от падения.
- Наш вариант: restart policy зависит от lifecycle state.

### GAB-INT-061 — Передача runtime environment каждому shard
- Источник: `Sharder.js`
- Категория: Sharding
- Описание: child process получает token, shard ID, total shard count, host и NODE_ENV через environment.
- Наш вариант: явный immutable process context.

### GAB-INT-062 — Broadcast с aggregate result
- Источник: `Sharder.js`
- Категория: IPC
- Описание: broadcast возвращает массив результатов всех shard sends через `Promise.all`.
- Наш вариант: caller может понять состояние всей shard-группы.

### GAB-INT-063 — Shard utility с ID и count
- Источник: `ShardUtil.js`
- Категория: API
- Описание: shard metadata доступна через единый объект вместо прямого чтения environment.
- Наш вариант: runtime metadata facade.

## Logging

### GAB-INT-064 — Единый multi-level Logger
- Источник: `Logger.js`
- Категория: Логи
- Описание: уровни `error/warn/info/debug/verbose/silly` единообразны для всех процессов.
- Наш вариант: единый logging contract.

### GAB-INT-065 — Разные transports для console и файлов
- Источник: `Logger.js`
- Категория: Логи
- Описание: консольные и файловые логи имеют разные форматы и уровни.
- Наш вариант: transport-specific logging policy.

### GAB-INT-066 — Daily rotating logs
- Источник: `Logger.js`
- Категория: Логи
- Описание: файловый лог автоматически разделяется по датам.
- Наш вариант: rotation policy с retention.

### GAB-INT-067 — Отдельный лог на master/shard/worker
- Источник: `Logger.js`
- Категория: Диагностика
- Описание: имя файла и label включают роль/ID процесса.
- Наш вариант: process-scoped log streams.

### GAB-INT-068 — Structured metadata в логах
- Источник: `Logger.js`
- Категория: Логи
- Описание: к сообщению можно прикладывать структурированный контекст вроде user/guild/channel IDs.
- Наш вариант: metadata-first logging.

### GAB-INT-069 — Error stack как отдельный объект логгера
- Источник: `Logger.js`
- Категория: Логи
- Описание: Error передаётся отдельно от metadata и сериализуется специально.
- Наш вариант: не превращать stack trace в обычную строку metadata.

### GAB-INT-070 — Автоматическая отправка исключений в Sentry
- Источник: `Logger.js`
- Категория: Наблюдаемость
- Описание: Logger при наличии DSN сам отправляет Error в Sentry.
- Наш вариант: error reporting интегрируется на уровне logger.

### GAB-INT-071 — Sentry context process/release/environment
- Источник: `Logger.js`
- Категория: Наблюдаемость
- Описание: ошибки маркируются process role, release и environment.
- Наш вариант: единый telemetry context.

## Extensions / Sandbox

### GAB-INT-072 — Песочница для пользовательского кода
- Источник: `Extensions/API/Sandbox.js`, `ExtensionManager.js`
- Категория: Расширения
- Описание: extension выполняется в ограниченном VM context, а не напрямую в основном runtime.
- Наш вариант: sandbox для пользовательских скриптов.

### GAB-INT-073 — Ограниченный require whitelist
- Источник: `Sandbox.js`
- Категория: Безопасность
- Описание: extension видит только заранее зарегистрированные модули/API.
- Наш вариант: explicit allowlist зависимостей.

### GAB-INT-074 — Scope-gated API modules
- Источник: `Sandbox.js`, `ScopeManager.js`
- Категория: Безопасность
- Описание: доступ к guild/channel/config API разрешается только при наличии соответствующего scope.
- Наш вариант: capability scopes для plugins.

### GAB-INT-075 — Защита свойства через getter scope check
- Источник: `ScopeManager.js`
- Категория: Безопасность
- Описание: даже чтение конкретного свойства может каждый раз проверять scope.
- Наш вариант: lazy capability checks для чувствительных данных.

### GAB-INT-076 — Extension storage с лимитом размера
- Источник: `Extensions/API/Modules/Extension.js`
- Категория: Расширения
- Описание: plugin получает key-value storage с жёстким лимитом размера.
- Наш вариант: per-plugin storage quota.

### GAB-INT-077 — CRUD API extension storage
- Источник: `Extension.js`
- Категория: Расширения
- Описание: storage предоставляет write/get/delete/clear и помечает родительский документ изменённым.
- Наш вариант: простое durable plugin storage API.

### GAB-INT-078 — Safe API wrappers вместо сырых Discord objects
- Источник: `API/Structures/*`, `Utils.js`
- Категория: Безопасность
- Описание: plugin получает ограниченные API objects, а не оригинальные Discord.js структуры.
- Наш вариант: façade objects с разрешёнными методами.

### GAB-INT-079 — Wrapping Collection/Array в safe API classes
- Источник: `API/Utils/Utils.js`
- Категория: Расширения
- Описание: коллекции и массивы автоматически превращаются в безопасные wrapper-объекты.
- Наш вариант: единый adapter для выдачи данных plugins.

### GAB-INT-080 — Единый serialization/error boundary для plugin API
- Источник: `API/Utils/Utils.js`
- Категория: Надёжность
- Описание: Discord errors преобразуются в доменные API errors, а send/edit options нормализуются в одном месте.
- Наш вариант: adapter boundary между plugin и Discord.

### GAB-INT-081 — Safe Embed builder с Discord limits
- Источник: `API/Structures/Embed.js`
- Категория: UX / Надёжность
- Описание: builder централизованно валидирует лимиты title/description/footer/field count/name/value.
- Наш вариант: reusable validated embed builder.

### GAB-INT-082 — Chainable Embed builder
- Источник: `Embed.js`
- Категория: API
- Описание: методы `set*`/`addField` возвращают сам объект и позволяют строить embed цепочкой.
- Наш вариант: fluent builders для сложных UI-объектов.

### GAB-INT-083 — API Message edit/delete/pin с проверкой scope
- Источник: `API/Structures/Message.js`
- Категория: Безопасность
- Описание: каждая чувствительная операция проверяет scope перед выполнением.
- Наш вариант: authorization at operation boundary.

### GAB-INT-084 — Root-message exception для reply
- Источник: `Message.js`
- Категория: UX
- Описание: исходному сообщению разрешён reply без отдельного send scope, последующие сообщения требуют его.
- Наш вариант: минимальные права для базового interaction response.

### GAB-INT-085 — Extension run timeout
- Источник: `ExtensionManager.js`
- Категория: Надёжность
- Описание: VM получает timeout из версии расширения.
- Наш вариант: hard execution timeout для plugins.

### GAB-INT-086 — Неакцептованная версия extension не выполняется
- Источник: `ExtensionManager.js`
- Категория: Безопасность
- Описание: version lifecycle содержит accepted-флаг, и только принятая версия запускается.
- Наш вариант: approval gate перед исполнением стороннего кода.

### GAB-INT-087 — Статус последнего запуска extension
- Источник: `ExtensionManager.js`
- Категория: Расширения
- Описание: результат исполнения сохраняется как code/description в конфигурации extension.
- Наш вариант: last-run health/status для plugin.

### GAB-INT-088 — Extension code отделён от metadata/version
- Источник: `ExtensionManager.js`
- Категория: Архитектура
- Описание: metadata хранится отдельно, а исходный код загружается по code ID только при запуске.
- Наш вариант: code artifact и manifest должны быть разделены.

### GAB-INT-089 — Extension worker получает только нужный context
- Источник: `ExtensionManager.js`
- Категория: Безопасность
- Описание: worker получает guild/message/event и конкретные документы, необходимые для запуска.
- Наш вариант: минимальный execution context.

### GAB-INT-090 — Extension event allowlist
- Источник: `Constants.js`, `Extensions/EventsHandler.js`
- Категория: Безопасность
- Описание: пользовательские extensions могут подписываться только на заранее разрешённые Discord events.
- Наш вариант: whitelist event subscriptions.

## Constants / UX

### GAB-INT-091 — Централизованный semantic color palette
- Источник: `Constants.js`
- Категория: UX
- Описание: цвета привязаны к смыслу ответа: error, warning, permission, success, response, info, prompt.
- Наш вариант: semantic UI palette вместо случайных цветов.

### GAB-INT-092 — Централизованные статусные шаблоны
- Источник: `Constants.js`
- Категория: UX
- Описание: ban/unban/join/leave/name/icon/nickname/message/avatar/username events используют единый каталог embed builders.
- Наш вариант: event presentation templates.

### GAB-INT-093 — Унифицированные emoji navigation constants
- Источник: `Constants.js`
- Категория: UX
- Описание: back/stop/forward и numbered emojis вынесены в единый набор.
- Наш вариант: общий navigation vocabulary для pagination UI.

### GAB-INT-094 — API endpoint registry
- Источник: `Constants.js`
- Категория: Архитектура
- Описание: адреса внешних API централизованы и параметризуются функциями.
- Наш вариант: external integration registry.

### GAB-INT-095 — Explicit user-agent для внешних API
- Источник: `Constants.js`
- Категория: Интеграции
- Описание: запросы к внешним сервисам имеют идентифицирующий User-Agent.
- Наш вариант: единый HTTP client policy.

### GAB-INT-096 — API response envelope
- Источник: `Constants.js`
- Категория: API
- Описание: ответы внутреннего API используют единый формат `{ err, data }` с success/notFound/badRequest/internalError.
- Наш вариант: стандартизировать service/API response contract.

### GAB-INT-097 — Human-readable verification-level mapping
- Источник: `Constants.js`
- Категория: UX
- Описание: технические уровни verification превращаются в понятные описания для пользователя.
- Наш вариант: display mapping для enum/technical values.

### GAB-INT-098 — Numbered-menu constants 1–10
- Источник: `Constants.js`
- Категория: UX
- Описание: выбор элементов через цифры имеет единый набор reaction symbols.
- Наш вариант: общий selection vocabulary.

### GAB-INT-099 — SafeMode как отдельный recovery contract
- Источник: `Boot.js`, `Constants.js`
- Категория: Надёжность
- Описание: аварийный режим не пытается загрузить все обычные подсистемы.
- Наш вариант: минимальный recovery runtime.

## Worker

### GAB-INT-100 — Отдельный worker для math evaluation
- Источник: `Worker.js`
- Категория: Производительность / Безопасность
- Описание: вычисления выполняются вне основного shard runtime.
- Наш вариант: worker для CPU-heavy задач.

### GAB-INT-101 — Запрет опасных mathjs-функций
- Источник: `Worker.js`
- Категория: Безопасность
- Описание: import/createUnit/eval/parse/simplify/derivative отключены перед выполнением пользовательских выражений.
- Наш вариант: capability-restricted expression evaluator.

### GAB-INT-102 — Унифицированный worker command protocol
- Источник: `Constants.js`, `Worker.js`
- Категория: Архитектура
- Описание: worker actions именуются константами и принимают структурированные payloads/callbacks.
- Наш вариант: typed-ish worker protocol вместо произвольных сообщений.

### GAB-INT-103 — Base64 transport для бинарного worker result
- Источник: `Worker.js`
- Категория: IPC
- Описание: binary emoji output передаётся между процессами как base64 вместе с флагом animated.
- Наш вариант: явный binary transport envelope.

### GAB-INT-104 — Worker-level unhandled rejection boundary
- Источник: `Worker.js`
- Категория: Надёжность
- Описание: необработанные Promise rejection в extension worker перехватываются и логируются вместо silent crash.
- Наш вариант: process-level safety boundary.

## Event cleanup / state consistency

### GAB-INT-105 — Cascade cleanup при удалении канала
- Источник: `Events/channelDelete/GAB.ChannelDelete.js`
- Категория: Data integrity
- Описание: удаление Discord channel очищает все связанные bot state: channel document, disabled/enabled command/filter/status lists, RSS, translations, voicetext, room data и заменяет устаревшие target channels.
- Наш вариант: централизованный reference cleanup при удалении Discord entity.

### GAB-INT-106 — Lazy channel document creation при message event
- Источник: `Events/messageDelete/GAB.MessageDelete.js`
- Категория: Data integrity
- Описание: если channel ещё не имеет bot-state document, он создаётся непосредственно при событии.
- Наш вариант: lazy state creation с безопасным default.

### GAB-INT-107 — Уменьшение агрегированных stats при удалении сообщения
- Источник: `Events/messageDelete/GAB.MessageDelete.js`
- Категория: Статистика
- Описание: удалённое сообщение корректирует today's/server и member message counters при соблюдении timestamp/statistics условий.
- Наш вариант: события удаления должны компенсировать ранее начисленные агрегаты.

### GAB-INT-108 — Reverse side-effect при удалении vote-trigger сообщения
- Источник: `Events/messageDelete/GAB.MessageDelete.js`
- Категория: Economy
- Описание: удаление сообщения, за которое ранее начислялись points следующему сообщению, может откатить этот point.
- Наш вариант: side-effect ledger или обратные операции для event-derived rewards.

### GAB-INT-109 — Ignore own/bot messages в audit-like handlers
- Источник: `MessageDelete.js`, `MessageUpdate.js`
- Категория: Логи
- Описание: message audit события фильтруют сообщения бота и системные источники до обработки.
- Наш вариант: явные source filters для noisy events.

### GAB-INT-110 — Audit deleted message с исходным содержимым
- Источник: `MessageDelete.js`, `Constants.js`
- Категория: Модерация
- Описание: лог удалённого сообщения сохраняет автора, канал, содержимое, ID и timestamp.
- Наш вариант: configurable message audit snapshot.

### GAB-INT-111 — Audit edited message показывает before/after
- Источник: `MessageUpdate.js`, `Constants.js`
- Категория: Модерация
- Описание: edit audit сохраняет исходный и текущий текст в одном событии.
- Наш вариант: before/after snapshots для изменений.

### GAB-INT-112 — Join event как единый onboarding pipeline
- Источник: `GuildMemberAdd.js`
- Категория: Onboarding
- Описание: вход участника может одновременно отправить публичное приветствие, DM, выдать роли и записать результат в server log.
- Наш вариант: composable onboarding pipeline.

### GAB-INT-113 — Независимые ошибки выдачи нескольких join-ролей
- Источник: `GuildMemberAdd.js`
- Категория: Надёжность
- Описание: выдача новых ролей выполняется параллельно; ошибка одной роли не блокирует остальные.
- Наш вариант: partial success для batch role assignment.

### GAB-INT-114 — Leave event удаляет member-specific feature state
- Источник: `GuildMemberRemove.js`
- Категория: Data integrity
- Описание: уход пользователя удаляет связанные translation/spam state и другие member-specific данные в каналах.
- Наш вариант: cascade cleanup при уходе пользователя.

### GAB-INT-115 — Guild join blocklist gate
- Источник: `GuildCreate.js`
- Категория: Безопасность
- Описание: guild blocklist проверяется до создания состояния; заблокированный сервер покидается сразу.
- Наш вариант: deny-at-ingress для серверов.

### GAB-INT-116 — Rejoin detection
- Источник: `GuildCreate.js`
- Категория: Lifecycle
- Описание: существующий server document означает rejoin, новый — first join, и оба сценария имеют разные сообщения/логи.
- Наш вариант: различать first-install и restore/rejoin.

### GAB-INT-117 — Автоматическое создание server defaults при первом входе
- Источник: `GuildCreate.js`
- Категория: Onboarding
- Описание: новый guild получает полноценный server document через централизованный default factory.
- Наш вариант: один источник truth для default configuration.

### GAB-INT-118 — Синхронизация списка guild после join/leave
- Источник: `GuildCreate.js`, `GuildDelete.js`
- Категория: Sharding
- Описание: изменение списка серверов инициирует IPC update и повторную публикацию sharded data.
- Наш вариант: event-driven global cache synchronization.

### GAB-INT-119 — Status-message templates для guild changes
- Источник: `GuildUpdate.js`, `Constants.js`
- Категория: UX
- Описание: смена имени, иконки и region превращается в отдельные настраиваемые status events.
- Наш вариант: granular audit/status toggles.

### GAB-INT-120 — Humanized region change
- Источник: `GuildUpdate.js`
- Категория: UX
- Описание: технический region code преобразуется в читаемый текст и сопровождается flag emoji.
- Наш вариант: presentation mapper для технических enum.

### GAB-INT-121 — Randomized join/ban/unban status message pool
- Источник: `GuildMemberAdd.js`, `GuildBanAdd.js`, `GuildBanRemove.js`
- Категория: UX
- Описание: статусное сообщение выбирается случайно из настроенного набора.
- Наш вариант: message pool вместо одного шаблона.

### GAB-INT-122 — Public status + private DM onboarding split
- Источник: `GuildMemberAdd.js`, `GuildMemberRemove.js`
- Категория: UX
- Описание: серверный status message и личное сообщение пользователю являются независимыми настройками.
- Наш вариант: раздельные delivery channels.

### GAB-INT-123 — Channel-local status message gate
- Источник: event handlers
- Категория: Конфигурация
- Описание: перед отправкой status event проверяется bot-enabled state целевого канала.
- Наш вариант: per-channel feature gate перед любым автоматическим сообщением.

## Статус

- Исследование `Internals/` продолжается.
- Обработаны и cross-check'нуты core-файлы Boot/Client/Constants/Errors/Events/Extendables/IPC/Logger/Sharding/Worker и доступные Extension API-компоненты.
- Следующий обязательный шаг: завершить оставшиеся файлы `Internals/Events/` и убедиться, что ни один файл/подкаталог не пропущен, затем закрыть `Internals/` и перейти к `Modules/`.
