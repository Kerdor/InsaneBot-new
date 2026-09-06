# TitanBot Utils — utility-layer mechanics

Источник: `codebymitch/TitanBot`
Каталог: `src/utils/`

## Общие utility / command pipeline

- **TU-001** — Единый helper для объявления slash-команд через `defineSlashCommand`.
- **TU-002** — Проверка обязательной формы command export до загрузки команды.
- **TU-003** — Общий pipeline отделяет объявление команды от её исполнения.
- **TU-004** — Централизованная валидация chat-input payload до выполнения команды.
- **TU-005** — Рекурсивная схема command options с вложенными options.
- **TU-006** — Лимит числа options на уровне схемы.
- **TU-007** — Лимит длины имени command и option при runtime validation.
- **TU-008** — Тип option валидируется диапазоном Discord-типа.
- **TU-009** — Значения command options допускают string/number/boolean/null через единую схему.
- **TU-010** — Ошибка валидации содержит machine-readable `errorCode`.
- **TU-011** — Ошибка валидации содержит список проблем с path/message/code.
- **TU-012** — Контекст команды прокидывается в validation error.
- **TU-013** — Prefix-команды могут исполняться через mock interaction, совместимый со slash API.
- **TU-014** — Mock interaction сохраняет user/member/channel/guild контекст исходного message.
- **TU-015** — Mock interaction предоставляет Discord-подобные getters для string/user/member/channel/role/integer/boolean.
- **TU-016** — Prefix execution поддерживает subcommand и subcommand group.
- **TU-017** — Prefix execution может использовать отдельный `prefixExecute`.
- **TU-018** — Slash-only команды автоматически исключаются из prefix execution.
- **TU-019** — Prefix execution повторно проверяет default member permissions.
- **TU-020** — Prefix execution использует общий ResponseCoordinator вместо отдельной логики ответа.
- **TU-021** — Prefix parser сначала проверяет наличие prefix, затем очищает его.
- **TU-022** — Пустая команда после prefix игнорируется.
- **TU-023** — Аргументы prefix-команды поддерживают одинарные и двойные кавычки.
- **TU-024** — Кавычки позволяют передавать аргумент с пробелами как единое значение.
- **TU-025** — Имена prefix-команд нормализуются в lowercase.
- **TU-026** — Alias subcommand разрешается до сопоставления с command definition.
- **TU-027** — Prefix parser умеет различать обычные options, subcommands и subcommand groups.
- **TU-028** — Неправильный subcommand превращается в structured validation result.
- **TU-029** — Validation result перечисляет доступные subcommands.
- **TU-030** — Usage line строится автоматически из command definition и найденных options.

## Response / interaction lifecycle

- **TU-031** — ResponseCoordinator является единым gate для ответа ровно один раз.
- **TU-032** — Coordinator прикрепляется непосредственно к interaction и переиспользуется всеми helper-слоями.
- **TU-033** — Coordinator отслеживает `_replyMessage`, finalized state и finalized reason.
- **TU-034** — После финального usage-response дальнейшие ответы блокируются.
- **TU-035** — Существующий reply автоматически превращается в edit вместо второго initial reply.
- **TU-036** — Prefix response отправляется через channel.send.
- **TU-037** — Slash response после defer превращается в editReply.
- **TU-038** — Повторный ответ после already-replied превращается в followUp.
- **TU-039** — При удалённом reply Coordinator может перейти к отправке нового сообщения.
- **TU-040** — Usage error форматируется в единый embed.
- **TU-041** — Prefix usage учитывает subcommand group/subcommand/option placeholders.
- **TU-042** — InteractionHelper централизует safe defer/reply/edit/followUp/showModal.
- **TU-043** — InteractionHelper автоматически defer-ит slash-команды перед долгим выполнением.
- **TU-044** — Prefix-командам defer заменяется локальным состоянием без Discord API defer.
- **TU-045** — Ответы для Components V2 очищаются от неподходящих flags/ephemeral параметров.
- **TU-046** — Ошибки expired/already-acknowledged interaction превращаются в безопасный no-op.
- **TU-047** — Отдельный набор Discord error codes считается interaction unavailable.
- **TU-048** — При удалённом reply edit может fallback-нуться в followUp.
- **TU-049** — Если interaction ещё не отвечен, `safeEditReply` использует reply fallback.
- **TU-050** — `safeReply` выбирает reply/edit/followUp по текущему lifecycle state.
- **TU-051** — `universalReply` одинаково обслуживает prefix и slash источники.
- **TU-052** — Safe execute может отключить auto-defer через option.
- **TU-053** — Safe execute измеряет длительность defer и предупреждает о превышении окна.
- **TU-054** — Command execution прекращается, если defer не удался.
- **TU-055** — Decorator может автоматически оборачивать command method в safe execution.
- **TU-056** — Interaction validation проверяет наличие id/user и максимальный возраст interaction.
- **TU-057** — Отдельный validator знает Discord codes expired interaction и already replied.
- **TU-058** — `safeDeferInteraction` проверяет expiry до вызова API.
- **TU-059** — `safeShowModal` запрещает открывать modal после reply/defer.
- **TU-060** — Wrapper для handler ловит expired interaction отдельно и не шумит stack trace.

## Dashboard / collectors / components

- **TU-061** — Общий dashboard session helper обслуживает одновременно select-menu и button collectors.
- **TU-062** — Dashboard interaction принимается только от пользователя-владельца сессии.
- **TU-063** — Dashboard interaction дополнительно привязывается к исходному reply message ID.
- **TU-064** — Для button matcher поддерживается точное значение, массив значений или predicate function.
- **TU-065** — Несколько collectors останавливаются общей `stopAll` функцией.
- **TU-066** — Dashboard имеет единый timeout с configurable duration.
- **TU-067** — При timeout компоненты dashboard удаляются.
- **TU-068** — Dashboard timeout может иметь кастомный callback вместо стандартного сообщения.
- **TU-069** — Ошибка collector handler не ломает collector lifecycle.
- **TU-070** — Ошибка collector interaction может сначала deferUpdate, затем показать user error.
- **TU-071** — Collector-managed custom IDs исключаются из глобального interaction dispatcher.
- **TU-072** — Список collector-managed prefixes централизован.
- **TU-073** — Confirmation buttons создаются единым helper с Confirm/Cancel.
- **TU-074** — Pagination row имеет first/prev/current/next/last controls.
- **TU-075** — Pagination buttons автоматически disabled на первой/последней странице.
- **TU-076** — Current page button может быть disabled и использоваться только как индикатор.
- **TU-077** — Select menu helper задаёт customId/placeholder/min/max/options единообразно.
- **TU-078** — Button helper ограничивает customId Discord-лимитом.
- **TU-079** — Button helper ограничивает label Discord-лимитом.
- **TU-080** — Button helper нормализует строковое имя ButtonStyle.
- **TU-081** — Неверный emoji не ломает создание button.
- **TU-082** — Link button имеет отдельный helper и автоматически получает Link style.
- **TU-083** — Button row ограничивает количество buttons пятью.
- **TU-084** — Ошибка одного button не ломает построение остальных buttons row.
- **TU-085** — Для button config автоматически различаются URL-button и customId-button.
- **TU-086** — Panel status умеет рекурсивно искать customId внутри nested components.
- **TU-087** — Panel marker может быть button marker или select marker.
- **TU-088** — Panel status сначала проверяет сохранённый message ID, затем выполняет scan последних сообщений.
- **TU-089** — При восстановлении панели возвращается найденный новый message ID.
- **TU-090** — Panel status различает отсутствие configured channel и удалённую panel message.
- **TU-091** — Есть специализированные status helpers для ticket/verification/reaction-role panels.
- **TU-092** — Panel status formatter выдаёт человекочитаемый Active/Missing/Deleted/Repost hint.

## Validation / sanitization

- **TU-093** — Общая string validation проверяет тип, непустоту и max length.
- **TU-094** — String validation может обрезать превышающий лимит текст вместо полного отказа.
- **TU-095** — Number validation запрещает NaN и отрицательные значения.
- **TU-096** — Discord ID validation ограничивает формат числовым ID Discord длиной 18–20.
- **TU-097** — customId validation требует непустую строку.
- **TU-098** — customId validation ограничивает длину 100 символами.
- **TU-099** — customId validation запрещает символы вне `[a-zA-Z0-9_-]`.
- **TU-100** — Required-properties validator возвращает false и логирует полный список missing props.
- **TU-101** — URL validator использует native URL parser вместо самодельной regex.
- **TU-102** — Range validator централизует min/max проверки.
- **TU-103** — Enum validator проверяет значение по allowlist.
- **TU-104** — Markdown sanitizer экранирует `*`, `_`, backticks, brackets, pipe и tilde.
- **TU-105** — Generic input sanitizer trim-ит, ограничивает длину и удаляет control characters.
- **TU-106** — Mention sanitizer извлекает ID из Discord mention-like строки.
- **TU-107** — HTML sanitizer экранирует ampersand, angle brackets, quotes и apostrophe.
- **TU-108** — Разные sanitizers предназначены для разных output contexts вместо одного универсального escaping.
- **TU-109** — GuildConfigSchema допускает passthrough дополнительных полей для совместимости.
- **TU-110** — Zod defaults используются как механизм нормализации отсутствующих значений.
- **TU-111** — Legacy fields принимаются schema-слоем, но затем удаляются при normalize.
- **TU-112** — Nested logging config мигрируется из нескольких старых flat fields.
- **TU-113** — Schema validation перед сохранением может выбрасывать typed validation error.
- **TU-114** — Validation error хранит path каждой проблемной настройки.

## Abuse protection / permissions

- **TU-115** — Risky commands определяются по explicit flag, имени или категории.
- **TU-116** — Команда может явно выключить inherited abuse protection.
- **TU-117** — Для risky command можно задать индивидуальные maxAttempts/windowMs.
- **TU-118** — Abuse protection key изолирует guild, user и command.
- **TU-119** — DM scope отделён от guild scope в protection key.
- **TU-120** — Повторные blocked attempts собираются в отдельное anomaly window.
- **TU-121** — После достижения anomaly threshold пишется отдельное security warning.
- **TU-122** — Cooldown duration форматируется в компактные `m/s` значения.
- **TU-123** — Abuse state можно полностью сбросить одной операцией.
- **TU-124** — Permission guard читает `default_member_permissions` прямо из SlashCommand JSON.
- **TU-125** — Значение permission bitfield преобразуется в BigInt.
- **TU-126** — Guild owner имеет bypass permission checks.
- **TU-127** — Moderation commands могут принимать configured moderator role как альтернативу native permission.
- **TU-128** — Moderator access принимает Administrator как глобальный bypass.
- **TU-129** — Отдельно проверяется user permission и bot permission.
- **TU-130** — Bot permission check принимает конкретный channel override.
- **TU-131** — Bot permission check возвращает полный список отсутствующих permissions.
- **TU-132** — Permission denial логируется с command/guild/user контекстом.
- **TU-133** — Audit permission check может хешировать user ID перед записью в лог.
- **TU-134** — Permission audit различает granted и denied события.

## Rate limiting / state / concurrency

- **TU-135** — Простая in-memory rate limiter хранит count + windowStart по ключу.
- **TU-136** — Новый/истёкший rate-limit window автоматически создаёт новый счётчик.
- **TU-137** — Rate limiter возвращает boolean allowed/blocked.
- **TU-138** — Отдельный status helper сообщает limited/remaining/attempts.
- **TU-139** — Rate-limit state можно удалить по одному ключу.
- **TU-140** — Все rate limits можно очистить глобально.
- **TU-141** — Ошибка самого rate limiter fail-open'ится и разрешает операцию вместо блокировки приложения.
- **TU-142** — Mutex serializes operations по произвольному key.
- **TU-143** — Следующая mutex-задача ждёт Promise предыдущей.
- **TU-144** — Ошибка предыдущей mutex-задачи не ломает очередь следующей.
- **TU-145** — Mutex автоматически удаляет lock после завершения последней задачи.
- **TU-146** — MemoryStorage предоставляет одинаковый async API для get/set/delete/list/exists.
- **TU-147** — MemoryStorage поддерживает TTL в секундах.
- **TU-148** — Expired values удаляются лениво при следующем доступе.
- **TU-149** — `list(prefix)` автоматически исключает expired keys.
- **TU-150** — MemoryStorage поддерживает atomic-like increment/decrement API на уровне abstraction.
- **TU-151** — `clear()` удаляет как values, так и expiration metadata.

## Logging / observability

- **TU-152** — AsyncLocalStorage используется для автоматической передачи trace context между async operations.
- **TU-153** — Trace ID генерируется через crypto UUID.
- **TU-154** — Interaction trace context включает interaction/guild/channel/user/command identifiers.
- **TU-155** — Button/modal/select interaction логируется по customId как command-like field.
- **TU-156** — Trace context автоматически прикрепляется к каждому logger record.
- **TU-157** — Logger нормализует event name в единый schema.
- **TU-158** — Error code автоматически выводится из errorCode/code/type/error.code.
- **TU-159** — У каждого log record есть предсказуемые guildId/userId/command/traceId поля.
- **TU-160** — Production и development имеют разные default log levels.
- **TU-161** — Alias-ы `warning`, `err`, `information` нормализуются в стандартные Winston levels.
- **TU-162** — Неверный LOG_LEVEL не ломает запуск, а откатывается к default.
- **TU-163** — Неверный LOG_LEVEL генерирует startup warning.
- **TU-164** — Daily rotating error log ограничивается размером и сроком хранения.
- **TU-165** — Combined log имеет отдельный retention period.
- **TU-166** — Exceptions и unhandled rejections пишутся в отдельные rotating logs.
- **TU-167** — В production startup/status сообщения могут повышаться до warn, чтобы не теряться при строгом log level.
- **TU-168** — Logger имеет stream adapter для библиотек, ожидающих `.write()`.

## Log embed presentation

- **TU-169** — Общий builder стандартного audit/log embed.
- **TU-170** — Единый helper для `Label: Value` строк.
- **TU-171** — Meta entries объединяются в одну компактную строку через bullet separator.
- **TU-172** — Quoted log block оформляется через Markdown `>`.
- **TU-173** — Description автоматически собирается из headline/lines/meta секций.
- **TU-174** — Description ограничивается Discord embed description лимитом.
- **TU-175** — Field labels очищаются от emoji-prefix перед сравнением/выводом.
- **TU-176** — Comparison helper автоматически разделяет before/after поля.
- **TU-177** — Остальные comparison fields сохраняются отдельно от before/after.
- **TU-178** — Footer может показывать executor tag + avatar.
- **TU-179** — При отсутствии executor footer может показывать guild name/icon.
- **TU-180** — Content section helper добавляет именованный блок только если content существует.
- **TU-181** — Rating helper преобразует числовой рейтинг в звёзды и `/5`.
- **TU-182** — Rating автоматически clamped в диапазон 1–5.
- **TU-183** — User author helper получает tag/avatar через API.
- **TU-184** — Если user fetch не удался, author получает fallback `User <id>`.
- **TU-185** — Standard embed builder отдельно принимает inlineFields и обычные fields.
- **TU-186** — Embed title/field name/value ограничиваются Discord limits перед отправкой.
- **TU-187** — Embed timestamp включён по умолчанию, но его можно выключить.
- **TU-188** — Role audit показывает name/color/id/permissions/hoist/managed/position.
- **TU-189** — Role audit может дополнительно показать число участников с ролью.
- **TU-190** — Список отображаемых role permissions ограничен, а остаток показывается счётчиком.

## Welcome / moderation / economy helpers

- **TU-191** — Welcome templates имеют централизованные default welcome/goodbye сообщения.
- **TU-192** — Welcome token replacement заменяет все вхождения каждого token.
- **TU-193** — Welcome formatter поддерживает user mention/tag/username/discriminator/id.
- **TU-194** — Welcome formatter поддерживает server/guild name/id/member count aliases.
- **TU-195** — Отсутствующий user/guild object не ломает formatting и получает fallback values.
- **TU-196** — Embed field value helper обрезает длинный текст с визуальным ellipsis.
- **TU-197** — Moderation action names централизованно мапятся на audit event types.
- **TU-198** — Moderation log data автоматически извлекает target ID из форматированной строки.
- **TU-199** — Moderation log data автоматически извлекает executor ID/tag.
- **TU-200** — Причина moderation action ограничивается отдельным embed-safe лимитом.
- **TU-201** — Metadata moderation event превращается в human-readable fields, исключая служебные IDs.
- **TU-202** — Case ID добавляется в title moderation log.
- **TU-203** — Moderation case storage имеет отдельный key на case и bounded guild case list.
- **TU-204** — Case list ограничивается последними 1000 кейсами.
- **TU-205** — Cases можно фильтровать по target user/moderator/action.
- **TU-206** — Cases поддерживают limit + offset pagination.
- **TU-207** — Ошибка генерации case ID имеет timestamp fallback.
- **TU-208** — Economy key builder валидирует guild/user IDs до формирования storage key.
- **TU-209** — Bank capacity зависит от base capacity и bank level.
- **TU-210** — Bank upgrade может умножать capacity.
- **TU-211** — Inventory bank notes могут дополнительно увеличивать capacity.
- **TU-212** — Currency formatter локализует число через `toLocaleString`.
- **TU-213** — Economy read normalizes missing fields через defaults.
- **TU-214** — Economy starting balance может переопределять default wallet.
- **TU-215** — Balance update ограничивает wallet снизу нулём.
- **TU-216** — Balance update ограничивает bank сверху вычисленной capacity.
- **TU-217** — XP update одновременно проверяет level-up и переносит остаток XP.
- **TU-218** — Cooldown helper возвращает boolean, remaining milliseconds и human-readable text.
- **TU-219** — Work reward использует random amount + random job narrative.
- **TU-220** — Crime helper возвращает структурированный success/fine/amount/message outcome.
- **TU-221** — Rob outcome проверяет нулевой баланс цели до random roll.
- **TU-222** — Rob success ограничивает украденную сумму долей баланса цели.
- **TU-223** — Shop item formatter объединяет номер, emoji, name, price и description.
- **TU-224** — Economy inventory содержит разные item types: tool/upgrade/consumable.
- **TU-225** — Shop item может иметь effect/value или multiplier metadata.

## Database abstraction / key registry

- **TU-226** — DatabaseWrapper скрывает конкретный backend за единым async API.
- **TU-227** — PostgreSQL является primary backend, MemoryStorage — degraded fallback.
- **TU-228** — Degraded mode явно отражается в runtime status.
- **TU-229** — Schema version mismatch не маскируется fallback-ом и останавливает database initialization path.
- **TU-230** — Database status показывает initialized/connectionType/isDegraded/isAvailable/degradedReason.
- **TU-231** — Generic DB set может валидировать guild config перед записью.
- **TU-232** — DB wrapper имеет get/set/delete/list/exists/increment/decrement uniform API.
- **TU-233** — Helper functions `getFromDb/setInDb/deleteFromDb` fail-safe и возвращают defaults/boolean.
- **TU-234** — Canonical database key registry запрещает разрозненное ручное формирование ключей.
- **TU-235** — Key registry предоставляет singular key builders и prefix builders.
- **TU-236** — Legacy key patterns централизованно сопоставляются с canonical keys.
- **TU-237** — Canonicalizer оставляет уже canonical key без изменений.
- **TU-238** — Для canonical key можно получить legacy variants для read-time compatibility.
- **TU-239** — Key parser превращает storage key в routing metadata: type/guild/user/channel/message IDs.
- **TU-240** — Key parser выделяет temp/cache storage как отдельные namespaces.
- **TU-241** — Temp-backed entity types централизованы в allowlist.
- **TU-242** — Structured list planner строит SQL query plan вместо одного generic scan.
- **TU-243** — Structured list planner может добавлять static singleton keys и dynamic DB rows.
- **TU-244** — Guild-wide list plan объединяет economy, levels, tickets и singleton config keys.
- **TU-245** — Migration умеет переносить legacy economy keys в structured economy table.
- **TU-246** — Migration умеет переносить legacy level keys в structured user-level table.
- **TU-247** — Migration умеет переносить legacy counters в guild row.
- **TU-248** — Migration имеет dry-run режим.
- **TU-249** — Migration имеет force режим для повторного запуска.
- **TU-250** — Migration пишет completion marker, чтобы не выполнять повторно уже завершённую миграцию.
- **TU-251** — Migration возвращает summary migrated/skipped/errors.
- **TU-252** — Если canonical key уже существует, legacy запись может быть пропущена и удалена.
- **TU-253** — Migration создаёт parent guild/user rows перед переносом structured records.
- **TU-254** — Migration имеет timestamp resolver для Date/string/number legacy formats.
- **TU-255** — Ошибка миграции одной записи увеличивает error counter, но не ломает обработку остальных.
- **TU-256** — Database schema является single source of truth и используется runtime + migration script.
- **TU-257** — PostgreSQL schema использует foreign keys с cascade deletion для guild/user dependent data.
- **TU-258** — Часто используемые поля получают отдельные SQL indexes.
- **TU-259** — Expiration timestamps для temp/cache/ticket/giveaway/AFK индексируются отдельно.
- **TU-260** — Общий PostgreSQL trigger поддерживает `updated_at` автоматически.
- **TU-261** — Ticket DB helper считает открытые тикеты через SQL при доступном PostgreSQL.
- **TU-262** — Ticket DB helper имеет fallback scan по storage keys при отсутствии PostgreSQL.
- **TU-263** — Ticket statistics вычисляют open/closed counts.
- **TU-264** — Ticket statistics вычисляют среднее время закрытия.
- **TU-265** — Ticket statistics вычисляют feedback count и average rating.
- **TU-266** — Ticket number counter форматируется минимум тремя цифрами.
- **TU-267** — Ticket permission context загружает config и ticket data параллельно.
- **TU-268** — Ticket creator получает право закрыть свой ticket отдельно от staff permissions.
- **TU-269** — Ticket management доступен через ManageChannels или configured staff role.
- **TU-270** — Ticket logging различает lifecycle и transcript channels.
- **TU-271** — Ticket logging перед отправкой проверяет SendMessages + EmbedLinks.
- **TU-272** — Ticket feedback логируется тем же logging pipeline, что и lifecycle events.
- **TU-273** — Ticket priority имеет визуальные emoji/status mappings.
- **TU-274** — Ticket transcript log может содержать message count, duration и subject.
- **TU-275** — Ticket logging configuration возвращает enabled + lifecycle/transcript channel IDs.
- **TU-276** — Log channel validator отдельно проверяет channel type и required permissions.

## Safe math / small helpers

- **TU-277** — Calculator использует собственный parser вместо `eval`.
- **TU-278** — Math parser токенизирует числа, identifiers, operators и parentheses.
- **TU-279** — Поддерживаются unary minus и right-associative exponentiation.
- **TU-280** — Поддерживаются `+ - * / % ^`.
- **TU-281** — Поддерживаются `sin/cos/tan/sqrt/abs/log/log10/exp`.
- **TU-282** — Поддерживаются constants `pi` и `e`.
- **TU-283** — Unicode `×`, `÷`, `π`, `√` нормализуются в parser input.
- **TU-284** — Degree notation преобразуется в radians через `deg` preprocessing.
- **TU-285** — Unknown identifiers отклоняются до вычисления.
- **TU-286** — Некорректные числа и несколько decimal points отклоняются.
- **TU-287** — Mismatched parentheses обнаруживаются до evaluation.
- **TU-288** — RPN evaluator проверяет достаточное количество operands.
- **TU-289** — Нефинитный результат математического выражения отклоняется.
- **TU-290** — SQL identifier helper требует безопасный identifier regex.
- **TU-291** — SQL identifier должен входить в explicit allowlist.
- **TU-292** — Отдельный helper может безопасно quote-ить уже validated SQL identifier.
