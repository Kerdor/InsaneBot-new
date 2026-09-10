# GAwesomeBot — Modules

> Идеи и архитектурные находки из `GAwesomeBot/bot/Modules/`.
> Код исходного проекта не копируем; фиксируем поведение, UX и архитектурные приёмы.

## Conversion / external data

### GAB-MOD-001 — Двойной конвертер units → currency
- Источник: `Modules/ConversionHandler.js`
- Описание: сначала пробуется конвертация физических единиц; если она не подходит, выполняется конвертация валют.
- Наш вариант: единый `/convert`, который определяет домен автоматически.

### GAB-MOD-002 — Локальный cache валютных курсов
- Источник: `ConversionHandler.js`
- Описание: последний успешный набор курсов сохраняется локально и используется после перезапуска.
- Наш вариант: persistent cache внешних данных.

### GAB-MOD-003 — Один shard обновляет общий внешний ресурс
- Источник: `ConversionHandler.js`
- Описание: только shard 0 получает свежие валютные курсы и записывает cache, остальные читают его.
- Наш вариант: лидер для внешних API, чтобы не множить запросы по shard.

### GAB-MOD-004 — Capability flag для необязательной интеграции
- Источник: `ConversionHandler.js`
- Описание: `canConvertMoney` явно показывает, доступна ли валютная часть после ошибки API/cache.
- Наш вариант: feature capability вместо проверки API в каждой команде.

### GAB-MOD-005 — Автоматическое отключение сломанной фоновой интеграции
- Источник: `ConversionHandler.js`
- Описание: при неудачном обновлении timer очищается, capability выключается, timestamp сбрасывается.
- Наш вариант: failed integration переводится в недоступное состояние без падения бота.

## Emoji / media processing

### GAB-MOD-006 — Нормализация emoji в metadata
- Источник: `Emoji/EmojiUtil.js`
- Описание: custom emoji, raw ID и Unicode приводятся к единому `{type,url,animated}` представлению.
- Наш вариант: единый media descriptor перед обработкой.

### GAB-MOD-007 — Поддержка raw custom emoji ID
- Источник: `Emoji/EmojiUtil.js`
- Описание: emoji можно распознать даже без Discord-синтаксиса, если передан ID.
- Наш вариант: принимать как `<:name:id>`, так и чистый ID там, где это безопасно.

### GAB-MOD-008 — Определение animated custom emoji через CDN fallback
- Источник: `Emoji/EmojiUtil.js`
- Описание: при raw ID сначала проверяется GIF, затем PNG.
- Наш вариант: graceful fallback между форматами ресурса.

### GAB-MOD-009 — Skin-tone aware Unicode emoji
- Источник: `Emoji/EmojiUtil.js`
- Описание: отдельная обработка текстовых и Unicode-вариантов skin tone перед построением Twemoji URL.
- Наш вариант: не терять modifier sequence при преобразовании emoji.

### GAB-MOD-010 — Генерация GIF из нескольких emoji
- Источник: `Emoji/Emoji.js`, `PrepareFrames.js`, `PrepareEndFrames.js`
- Описание: несколько emoji преобразуются в кадры, объединяются горизонтально и экспортируются как GIF.
- Наш вариант: media-команда может собирать визуальные композиции из нескольких emoji.

### GAB-MOD-011 — Ограничение числа элементов в визуальной композиции
- Источник: `Emoji.js`
- Описание: вход очищается от пустых значений и ограничивается шестью emoji.
- Наш вариант: жёсткие лимиты до тяжёлой обработки изображения.

### GAB-MOD-012 — Унификация размеров кадров
- Источник: `PrepareFrames.js`, `Emoji.js`
- Описание: Unicode и custom emoji масштабируются до разных фиксированных размеров, а GIF-кадры приводятся к общей композиции.
- Наш вариант: нормализовать media dimensions до рендера.

### GAB-MOD-013 — PNG вместо GIF для однофреймовой композиции
- Источник: `Emoji.js`
- Описание: если итоговый GIF содержит один кадр, он перекодируется в PNG.
- Наш вариант: возвращать самый простой подходящий формат.

### GAB-MOD-014 — Quantization перед финальным GIF
- Источник: `Emoji.js`
- Описание: перед экспортом GIF применяется palette quantization.
- Наш вариант: отдельный этап оптимизации результата после композиции.

## Guild / command infrastructure

### GAB-MOD-015 — Guild resolver с несколькими стратегиями поиска
- Источник: `GetGuild.js`
- Описание: сущность разрешается по ID, owner, username/discriminator и другим формам; локальный guild используется быстрее IPC.
- Наш вариант: единый resolver с fast path → remote path.

### GAB-MOD-016 — Полиморфный resolver: single / map / member
- Источник: `GetGuild.js`
- Описание: один модуль умеет получать одну guild, коллекцию guilds и участников.
- Наш вариант: единый интерфейс entity resolution для команд.

### GAB-MOD-017 — 404 превращается в null для resolver API
- Источник: `GetGuild.js`
- Описание: отсутствие guild не считается аварией низкоуровневого resolver.
- Наш вариант: ожидаемые `not found` возвращать как отсутствие результата.

### GAB-MOD-018 — Re-sync документа после удалённого обновления
- Источник: `GetGuild.js`
- Описание: resolver умеет повторно синхронизировать состояние объекта с удалённым источником.
- Наш вариант: явный `reSync()` для stale runtime objects.

### GAB-MOD-019 — Bulk fetch коллекции сущностей
- Источник: `GetGuild.js`
- Описание: поддерживается получение свойств/участников для набора guilds, а не только по одному объекту.
- Наш вариант: bulk resolver для массовых admin operations.

## External services

### GAB-MOD-020 — Giphy wrapper с единым error taxonomy
- Источник: `Giphy.js`
- Описание: отсутствие query и отсутствие результата представлены разными доменными ошибками.
- Наш вариант: тонкие wrappers внешних API с понятными error codes.

### GAB-MOD-021 — Imgur client с общим request builder
- Источник: `Imgur.js`
- Описание: upload, album и credits используют один внутренний механизм авторизации/request construction.
- Наш вариант: общий transport layer для API-клиентов.

### GAB-MOD-022 — Upload URL напрямую во внешний image host
- Источник: `Imgur.js`
- Описание: изображение можно передать как URL без предварительного скачивания в бот.
- Наш вариант: где API позволяет — server-side URL upload.

### GAB-MOD-023 — Возврат normalized + raw API response
- Источник: `Imgur.js`
- Описание: wrapper возвращает status/body/data и одновременно raw response.
- Наш вариант: высокоуровневый результат + debug raw payload.

### GAB-MOD-024 — iTunes search/lookup одним wrapper
- Источник: `SearchiTunes.js`
- Описание: наличие идентификатора автоматически переключает endpoint search → lookup.
- Наш вариант: единый media search service с автоматическим выбором режима.

### GAB-MOD-025 — Lookup возвращает один объект, search — массив
- Источник: `SearchiTunes.js`
- Описание: форма результата зависит от семантики запроса, при пустом результате выбрасывается понятная ошибка.
- Наш вариант: API abstraction сохраняет семантику операций.

### GAB-MOD-026 — RSS parser с коротким network timeout
- Источник: `RSS.js`
- Описание: внешний feed parser имеет timeout 2 секунды.
- Наш вариант: фоновые интеграции никогда не ждут бесконечно.

### GAB-MOD-027 — RSS incremental delivery по последней ссылке
- Источник: `StreamingRSS.js`
- Описание: сохраняется link последней опубликованной статьи; публикуются только новые элементы после неё.
- Наш вариант: cursor-based polling для RSS.

### GAB-MOD-028 — Recovery при потерянном RSS cursor
- Источник: `StreamingRSS.js`
- Описание: если старой статьи больше нет в feed, выполняется fallback с принудительным добавлением доступных новых элементов.
- Наш вариант: не зависеть навсегда от устаревшего cursor.

### GAB-MOD-029 — Ошибка одного RSS канала не ломает остальные
- Источник: `StreamingRSS.js`
- Описание: проблема конкретного feed/channel логируется и не должна останавливать всю рассылку.
- Наш вариант: per-integration error isolation.

## Interactive UX

### GAB-MOD-030 — Reusable paginated embed
- Источник: `MessageUtils/PaginatedEmbed.js`
- Описание: данные страниц передаются массивами content/author/title/color/description/fields/image/footer и собираются общим template.
- Наш вариант: универсальный paginator вместо отдельных реализаций каждой команды.

### GAB-MOD-031 — Ограничение paginator одним автором
- Источник: `PaginatedEmbed.js`
- Описание: реакциями может управлять только пользователь, создавший исходный запрос.
- Наш вариант: owner-bound interactive sessions.

### GAB-MOD-032 — Stop reaction + timeout cleanup
- Источник: `PaginatedEmbed.js`
- Описание: меню имеет явную остановку и автоматическое завершение по timeout с удалением реакций.
- Наш вариант: каждая интерактивная сессия должна иметь lifecycle и cleanup.

### GAB-MOD-033 — Fallback cleanup реакций
- Источник: `PaginatedEmbed.js`, `ReactionMenus/BaseMenu.js`
- Описание: если массовое удаление реакций не удалось, бот удаляет реакции пользователей поштучно.
- Наш вариант: cleanup с fallback strategy.

### GAB-MOD-034 — Числовой выбор + страницы в одном reaction menu
- Источник: `ReactionBasedMenu.js`
- Описание: до 10 вариантов выбираются number emoji, а при большом списке добавляются back/forward.
- Наш вариант: маленький список → прямой выбор, большой → пагинация.

### GAB-MOD-035 — `emitOnly` режим интерактивного меню
- Источник: `BaseMenu.js`
- Описание: меню может либо само изменить сообщение на результат, либо только emit-нуть выбранный индекс вызывающему коду.
- Наш вариант: UI-компоненты отделяются от бизнес-логики через callback/event mode.

### GAB-MOD-036 — Корректировка глобального индекса после пагинации
- Источник: `BaseMenu.js`
- Описание: локальный номер варианта преобразуется в глобальный индекс через `page * 10`.
- Наш вариант: paginator скрывает расчёт абсолютного индекса от команд.

### GAB-MOD-037 — Help menu как отдельный тип reaction UI
- Источник: `HelpMenu.js`
- Описание: help имеет default page, named pages, info reaction и опциональную страницу extensions.
- Наш вариант: специализированные UI-меню могут переиспользовать общий lifecycle.

## Parsing / reminders

### GAB-MOD-038 — Два синтаксиса duration parser
- Источник: `MessageUtils/DurationParser.js`
- Описание: поддерживаются `event | duration` и естественный формат `... in duration`.
- Наш вариант: короткий машинный и естественный пользовательский синтаксис.

### GAB-MOD-039 — Reminder parser сохраняет отдельный ID
- Источник: `ReminderParser.js`
- Описание: каждое напоминание получает уникальный ID и expiry timestamp.
- Наш вариант: reminders должны быть адресуемыми сущностями, а не просто таймерами.

### GAB-MOD-040 — Таймер reminder привязан к persistent document
- Источник: `ReminderParser.js`, `SetReminder.js`
- Описание: timer создаётся из сохранённого документа, а перед отправкой повторно читается актуальная запись из БД.
- Наш вариант: runtime timer → persistent state → fresh read перед выполнением.

## Timeouts / timers

### GAB-MOD-041 — Таймеры длиннее лимита Node.js
- Источник: `Timeouts/Base.js`, `Timeout.js`, `Interval.js`
- Описание: timeout/interval разбиваются на несколько `MAX = 2147483647` ms сегментов.
- Наш вариант: long-duration scheduler, не зависящий от лимита native timer.

### GAB-MOD-042 — Long interval сохраняет `timeLeft`
- Источник: `Interval.js`
- Описание: большой интервал сначала ждёт сегменты, затем вызывает listener и перезапускает полный цикл.
- Наш вариант: корректные периодические задачи на месяцы/годы.

### GAB-MOD-043 — `ref/unref` для фоновых таймеров
- Источник: `Timeouts/Base.js`
- Описание: timer можно исключить из удержания процесса живым и вернуть обратно.
- Наш вариант: управляемые process-lifecycle semantics для фоновых задач.

### GAB-MOD-044 — Timer special identifier
- Источник: `Timeouts/Base.js`
- Описание: timeout хранит логический идентификатор для конкретного типа/задачи.
- Наш вариант: именованные scheduler entries.

## Moderation / stateful services

### GAB-MOD-045 — ModLog как CRUD service
- Источник: `ModLog.js`
- Описание: один static service умеет create/update/delete/enable/disable для moderation cases.
- Наш вариант: ModLog не только logger, а полноценный case service.

### GAB-MOD-046 — Sequence ID для ModLog case
- Источник: `ModLog.js`
- Описание: case ID увеличивается на сервере и сохраняется вместе с сообщением.
- Наш вариант: человекочитаемый последовательный case number.

### GAB-MOD-047 — Связь DB case ↔ Discord message
- Источник: `ModLog.js`
- Описание: запись хранит `message_id`, позволяя редактировать или удалить исходное сообщение при изменении case.
- Наш вариант: persistent reference между audit record и его Discord presentation.

### GAB-MOD-048 — Возможность редактировать причину case после создания
- Источник: `ModLog.js`
- Описание: case message содержит подсказку, как изменить reason, а update синхронно меняет DB и Discord message.
- Наш вариант: editable moderation records.

### GAB-MOD-049 — Channel-scoped voice text
- Источник: `Voicetext.js`
- Описание: для voice channel автоматически создаётся связанный text channel с marker в topic и наследованием parent category.
- Наш вариант: временный/постоянный текстовый companion для voice.

### GAB-MOD-050 — Доступ к voicetext через member overwrite
- Источник: `Voicetext.js`
- Описание: видимость companion-channel выдаётся только текущим участникам voice и снимается после выхода.
- Наш вариант: динамический access control по membership в voice.

## Server onboarding / state

### GAB-MOD-051 — Инициализация нового guild из внешних defaults
- Источник: `NewServer.js`
- Описание: новый server document получает default RSS, tags, ranks, status messages и tag reactions.
- Наш вариант: onboarding-конфигурация как атомарный набор дефолтов.

### GAB-MOD-052 — Автоматическое определение admin roles
- Источник: `NewServer.js`
- Описание: роли с `MANAGE_GUILD` автоматически добавляются в список bot admins, кроме managed/@everyone.
- Наш вариант: initial admin bootstrap из Discord permissions.

### GAB-MOD-053 — Приветствие владельца при добавлении бота
- Источник: `NewServer.js`
- Описание: bot admins получают onboarding DM с prefix/help ссылкой и иногда номером сервера среди подключённых.
- Наш вариант: owner onboarding после join.

## Polls / trivia

### GAB-MOD-054 — Poll state хранится на уровне channel
- Источник: `Polls.js`
- Описание: канал хранит ongoing flag, creator, title, options и responses.
- Наш вариант: интерактивные feature states принадлежат channel scope.

### GAB-MOD-055 — Poll results как отдельный calculation layer
- Источник: `Polls.js`
- Описание: подсчёт votes, percentages и winner отделён от start/end lifecycle.
- Наш вариант: расчёт результата без привязки к presentation.

### GAB-MOD-056 — Tie как отдельное состояние результата
- Источник: `Polls.js`
- Описание: одинаковое максимальное число голосов сбрасывает winner в null.
- Наш вариант: явно моделировать ничью, а не выбирать первый вариант.

### GAB-MOD-057 — Trivia с несколькими допустимыми ответами
- Источник: `Trivia.js`
- Описание: правильные ответы могут храниться через `|` и проверяться по очереди.
- Наш вариант: aliases/accepted answers для quiz content.

### GAB-MOD-058 — Fuzzy answer matching только для длинных текстов
- Источник: `Trivia.js`
- Описание: короткие/числовые ответы требуют точного совпадения, длинные допускают Levenshtein distance < 3.
- Наш вариант: fuzzy matching применять только там, где он не создаёт много ложных совпадений.

### GAB-MOD-059 — Ограничение очков за попытки trivia
- Источник: `Trivia.js`
- Описание: правильный ответ приносит point только в первые три попытки; участник отдельно получает personal score.
- Наш вариант: reward degradation по числу попыток.

### GAB-MOD-060 — Автоматический выбор новой trivia-вопроса без повторов
- Источник: `Trivia.js`
- Описание: прошлые вопросы записываются и исключаются до исчерпания набора.
- Наш вариант: session-local question history.

## Analytics / presentation

### GAB-MOD-061 — Weekly activity reset с наградой top-3
- Источник: `ClearServerStats.js`
- Описание: при очистке weekly stats сообщения + voice формируют activity score, после чего top-3 получают points.
- Наш вариант: периодический leaderboard settlement.

### GAB-MOD-062 — Stopwatch с human-readable единицами
- Источник: `Stopwatch.js`
- Описание: duration автоматически выводится в μs/ms/s с двумя знаками.
- Наш вариант: reusable performance measurement для diagnostics.

### GAB-MOD-063 — Live-state transition для streamer alerts
- Источник: `StreamChecker.js`
- Описание: уведомление отправляется только при переходе offline → live; состояние хранится в server document.
- Наш вариант: event-on-state-change вместо спама при каждом polling cycle.

### GAB-MOD-064 — Единый streamer adapter для Twitch и YouTube
- Источник: `StreamerUtils.js`
- Описание: разные API приводятся к общему результату `name/type/game/url/image/preview`.
- Наш вариант: provider adapters с общей моделью.

## Safe text / utility behavior

### GAB-MOD-065 — Удаление Discord markdown и neutralization mentions
- Источник: `RemoveFormatting.js`
- Описание: перед выводом наружу текст очищается от markdown и `@everyone/@here/user mention` превращается в безопасный текст.
- Наш вариант: safe-render helper для пользовательского контента.

### GAB-MOD-066 — Dynamic RegExp из пользовательского списка
- Источник: `RegExpMaker.js`
- Описание: значения экранируются перед объединением в один regex.
- Наш вариант: безопасный компилятор keyword-list → regex.

### GAB-MOD-067 — URL validation отдельным utility
- Источник: `IsURL.js`
- Описание: URL проверяется централизованным regex helper до передачи внешним сервисам.
- Наш вариант: единый URL validator.

### GAB-MOD-068 — Shard data merge modes
- Источник: `GetValue.js`
- Описание: результат межпроцессного запроса можно объединять как `int`, `obj`, `arr` или Discord Collection/map.
- Наш вариант: типизированные aggregation strategies для shard metrics.

### GAB-MOD-069 — Message Of The Day как persistent scheduler
- Источник: `MessageOfTheDay.js`
- Описание: last-run хранится в документе, timer восстанавливается после перезапуска и channel проверяется перед отправкой.
- Наш вариант: persistent recurring announcements.

### GAB-MOD-070 — MessageOfTheDay re-schedules itself после выполнения
- Источник: `MessageOfTheDay.js`
- Описание: после отправки следующая задача создаётся из актуального server document.
- Наш вариант: recurring job всегда перечитывает свежую конфигурацию.

## Temporary storage / updates

### GAB-MOD-071 — Metadata-driven temporary storage
- Источник: `Temp.js`
- Описание: временные каталоги регистрируются в `metadata.json` с type/id/prefix/persistent.
- Наш вариант: temp files должны иметь lifecycle metadata.

### GAB-MOD-072 — Persistent temporary entries
- Источник: `Temp.js`
- Описание: entry может помечаться persistent и переживать обычную уборку до явного удаления.
- Наш вариант: разделять ephemeral и recoverable temp artifacts.

### GAB-MOD-073 — ID-based temp path
- Источник: `Temp.js`
- Описание: путь строится детерминированно из prefix + ID, что позволяет восстановить расположение после рестарта.
- Наш вариант: predictable temporary artifact addressing.

### GAB-MOD-074 — Централизованный module barrel
- Источник: `Modules/index.js`, `Modules/MessageUtils/index.js`, `Modules/Utils/index.js`
- Описание: инфраструктурные модули экспортируются через единые entrypoints.
- Наш вариант: стабильный public API для внутренних utilities.

## Encryption / Central updater

### GAB-MOD-075 — Password derivation из нескольких runtime secrets
- Источник: `Encryption.js`
- Описание: encryption key выводится через PBKDF2 из client ID + configured password + owner ID.
- Наш вариант: ключ не хранить напрямую, а детерминированно получать из нескольких секретов.

### GAB-MOD-076 — Version API с compatibility check
- Источник: `GAwesomeClient.js`
- Описание: remote API version сравнивается по major version; несовместимый major блокируется.
- Наш вариант: protocol compatibility guard перед использованием Central API.

### GAB-MOD-077 — Update lifecycle download → unpack → patch → verify → cleanup
- Источник: `GAwesomeClient.js`
- Описание: обновление разбито на явные стадии, каждая имеет собственный progress event/log.
- Наш вариант: upgrade pipeline с checkpointable stages.

### GAB-MOD-078 — Проверка целостности каждого patched file
- Источник: `GAwesomeClient.js`
- Описание: после копирования байты patch source сравниваются с target; повреждение останавливает установку.
- Наш вариант: post-update integrity verification.

### GAB-MOD-079 — Download resume/recovery через temporary storage
- Источник: `GAwesomeClient.js`, `Temp.js`
- Описание: скачанная версия сохраняется в persistent temp entry и может быть обнаружена через `checkDownload()`.
- Наш вариант: обновления должны переживать промежуточный restart.

### GAB-MOD-080 — Extension execution с timeout sandbox
- Источник: `ExtensionRunner.js`
- Описание: extension code загружается отдельно и запускается в VM с заданным timeout; load/runtime errors изолируются логированием.
- Наш вариант: пользовательские расширения никогда не исполняются напрямую в основном runtime.
