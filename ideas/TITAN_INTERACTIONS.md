# TitanBot — Interactions

Источник: `codebymitch/TitanBot`
Папка: `src/interactions/`
Статус: проверено по фактическому дереву `buttons/`, `modals/`, `selectMenus/`.

## Registration architecture

- TI-001 — Разделять interaction definitions по типу: `buttons`, `modals`, `selectMenus`.
- TI-002 — Держать definition-файлы рядом с предметной областью, а сложную логику в handlers.
- TI-003 — Один handler может обслуживать несколько customId через массив definitions.
- TI-004 — Один action может регистрироваться под несколькими именами без дублирования execute-функции.
- TI-005 — Генерировать повторяющиеся interaction definitions через `map`, если различается только имя.
- TI-006 — Использовать константы customId из domain service вместо копирования строк по файлам.
- TI-007 — Разрешать definition wrapper преобразовать domain handler в унифицированный `{ name, execute }` формат.
- TI-008 — Поддерживать default export как object для одиночного interaction.
- TI-009 — Поддерживать default export как array для группы interactions.
- TI-010 — Для legacy/неоднородных handlers нормализовать `execute`: функция напрямую или `handler.execute`.
- TI-011 — Выносить общий handler в один модуль, а definitions делать максимально тонкими.
- TI-012 — Держать machine-readable customId стабильным между UI и loader.
- TI-013 — Разделять публичное имя interaction в registry и фактический customId namespace.
- TI-014 — Позволять нескольким UI entry points вызывать одну бизнес-операцию.
- TI-015 — Не дублировать бизнес-логику между button/select/modal реализациями.

## Button definitions

- TI-016 — Countdown pause и cancel могут использовать один stateful handler с разными action names.
- TI-017 — Музыкальные кнопки можно регистрировать автоматически из массива domain constants.
- TI-018 — Giveaway actions можно получать из metadata самого handler-а (`customId`, `execute`).
- TI-019 — Ticket actions могут регистрироваться напрямую готовыми handler objects.
- TI-020 — Для одного counter action допустим default-export handler object без дополнительной обёртки.
- TI-021 — Verification button может иметь один стабильный customId и один execute.
- TI-022 — Warning destructive actions разделяются на конкретное удаление и clear-all.
- TI-023 — Wipe-data confirmation имеет отдельные confirm/cancel interactions.
- TI-024 — Help pagination регистрирует first/prev/next/last через один execute.
- TI-025 — Logging dashboard использует единый handler для toggle/refresh/back/filter actions.
- TI-026 — Todo shared UI разделяет открытие modal и фактический modal-submit handler.
- TI-027 — Feedback button может одновременно поддерживать rating, comment и decline actions.
- TI-028 — Один interaction module может экспортировать несколько связанных handlers.

## Modal definitions and input contracts

- TI-029 — Modal definition может напрямую ссылаться на domain handler без промежуточного wrapper.
- TI-030 — Modal customId должен включать достаточно контекста для последующего workflow.
- TI-031 — Config modal кодирует `key:guildId` в customId.
- TI-032 — Ticket feedback comment кодирует `guildId:channelId` в modal customId.
- TI-033 — Shared todo modal кодирует `listId` и source message ID для refresh.
- TI-034 — Warning modal кодирует target user и original moderator.
- TI-035 — Modal input names должны быть стабильными machine-readable IDs.
- TI-036 — Human-readable labels и placeholders не должны использоваться как идентификаторы данных.
- TI-037 — TextInput можно ограничивать `required`, `minLength`, `maxLength` на UI-уровне.
- TI-038 — Paragraph TextInput подходит для длинного ticket feedback comment.
- TI-039 — Short TextInput подходит для warning number/task ID.
- TI-040 — Modal может быть промежуточным этапом между button и окончательной mutation.
- TI-041 — Modal opening может не делать DB operation до фактического submit.
- TI-042 — Modal submit должен повторно валидировать context, а не доверять UI.

## Config modal

- TI-043 — Универсальный config modal может обновлять разные настройки через один handler.
- TI-044 — Role/channel settings принимать через mention или raw numeric ID.
- TI-045 — Nullable config settings поддерживать значением `none`.
- TI-046 — Boolean config parser принимать несколько человекочитаемых true/false вариантов.
- TI-047 — Prefix validation запрещает whitespace и ограничивает длину.
- TI-048 — Channel Select/Role Select предпочтительнее ручного ID для selector-based config actions.
- TI-049 — После успешного config update возвращать человекочитаемый summary изменённой настройки.
- TI-050 — Для channel/role summary использовать cache, но иметь mention fallback по ID.
- TI-051 — Перед сохранением config делегировать бизнес-валидацию ConfigService.
- TI-052 — Ошибки config modal отдавать через централизованный typed user error.
- TI-053 — Техническую ошибку config modal логировать отдельно от сообщения пользователю.

## Ticket feedback workflow

- TI-054 — Feedback rating привязывать к конкретному ticket через guildId + channelId.
- TI-055 — Некорректный feedback customId завершать безопасным user-facing error без DB access.
- TI-056 — Ticket feedback загрузку из DB оборачивать отдельной try/catch.
- TI-057 — Отсутствующий ticket считать stale feedback context.
- TI-058 — Только ticket creator может отправлять feedback.
- TI-059 — Повторную оценку блокировать по persisted `feedback.rating`.
- TI-060 — Рейтинг хранить вместе с timestamp отправки.
- TI-061 — Для рейтингов иметь человекочитаемые star labels.
- TI-062 — Неизвестный rating label может иметь числовой fallback.
- TI-063 — Сохранение feedback и audit logging — отдельные операции с независимой обработкой ошибок.
- TI-064 — Ошибка logging feedback не должна отменять сохранённую оценку.
- TI-065 — После отправки feedback удалять все feedback controls.
- TI-066 — После отправки feedback показывать подтверждение через embed + timestamp/footer.
- TI-067 — Comment feedback открывать отдельным modal action.
- TI-068 — Comment ограничивать 1000 символами на уровне TextInput.
- TI-069 — Comment trim-ить и отклонять пустой результат после trim.
- TI-070 — Comment может существовать без rating (`rating ?? null`).
- TI-071 — Written feedback хранить отдельно с собственным timestamp.
- TI-072 — Feedback decline не требует DB mutation и просто закрывает UI.
- TI-073 — Feedback workflow может быть реализован и button-, и select-menu entry point с одинаковой бизнес-логикой.
- TI-074 — Для rating select использовать значение select menu как machine-readable rating.
- TI-075 — Для button rating передавать rating как customId argument.

## Shared todo modal pipeline

- TI-076 — Button action только открывает modal, mutation выполняется на modal submit.
- TI-077 — Source message ID передаётся через modal context для обновления live view.
- TI-078 — Shared list ID валидируется regex-ом до обращения к БД.
- TI-079 — Membership проверяется заново на каждом mutation.
- TI-080 — Add/complete/remove имеют отдельные rate limits.
- TI-081 — Add modal создаёт task с monotonic ID.
- TI-082 — Complete modal требует положительный integer task ID.
- TI-083 — Remove modal использует task ID и показывает удалённый task в результате.
- TI-084 — После mutation обновлять исходное сообщение, но не считать UI refresh обязательным для успеха mutation.
- TI-085 — Если source message отсутствует, DB mutation всё равно может завершиться успешно.
- TI-086 — UI refresh ошибки логировать как warning, не как fatal mutation error.
- TI-087 — Успешные modal mutations возвращать ephemeral confirmation embed.

## Warning destructive workflow

- TI-088 — Button открытия warning modal сохраняет identity исходного модератора в customId.
- TI-089 — Modal submit повторно сверяет текущего пользователя с original moderator.
- TI-090 — Delete warning принимает пользовательский формат `#N` и `N`.
- TI-091 — Номер warning проверяется как integer >= 1.
- TI-092 — Warning number сопоставляется с актуальным массивом warnings перед mutation.
- TI-093 — Mutation выполняется по stable warning ID, а не по номеру из UI.
- TI-094 — Clear-all требует отдельной destructive confirmation modal.
- TI-095 — Confirmation string может быть строго case-sensitive `DELETE`.
- TI-096 — Confirmation input можно ограничить ровно шестью символами.
- TI-097 — После destructive mutation возвращать количество затронутых записей.
- TI-098 — Результат удаления конкретного warning может показывать исходную причину.
- TI-099 — Недоступный target user не должен блокировать moderation result; использовать fallback name.
- TI-100 — Destructive warning actions использовать ephemeral results.

## Logging selector/modal chain

- TI-101 — Logging dashboard button может открывать modal, внутри которого находится User Select/Channel Select.
- TI-102 — User Select ограничивать одним значением.
- TI-103 — Channel Select ограничивать одним значением.
- TI-104 — Channel Select фильтровать разрешённые Discord channel types.
- TI-105 — LabelBuilder использовать для описания назначения selector-а.
- TI-106 — Modal submit ожидать через `awaitModalSubmit` после открытия modal.
- TI-107 — Collector filter должен проверять и user ID, и ожидаемый modal customId.
- TI-108 — Modal collector иметь конечный timeout, например 5 минут.
- TI-109 — Timeout collector не считать ошибкой, требующей дополнительного ответа.
- TI-110 — При выборе destination channel делать cache lookup с API fetch fallback.
- TI-111 — Перед сохранением destination проверять ViewChannel + SendMessages + EmbedLinks.
- TI-112 — После изменения logging settings сразу refresh исходного dashboard.
- TI-113 — Remove filter использовать String Select со значением `type:id`.
- TI-114 — Ограничивать select options первыми 25 элементами.
- TI-115 — Пустой список filters обрабатывать отдельным user-input error.
- TI-116 — Add/remove filter modal использовать разные customId namespaces.
- TI-117 — Dashboard interaction может обновлять текущий view вместо возврата на главный экран.
- TI-118 — Toggle category/all state через один handler и machine-readable event type.

## Music interaction surface

- TI-119 — Queue открывать отдельным ephemeral interaction, не изменяя публичный player message.
- TI-120 — Queue page хранить по user ID, чтобы два пользователя могли иметь разные страницы.
- TI-121 — Перед queue pagination повторно проверять наличие current track.
- TI-122 — Перед playback control проверять, что пользователь находится в допустимом voice context.
- TI-123 — Pagination ограничивать диапазоном существующих страниц.
- TI-124 — First/Prev/Next/Last должны быть независимыми действиями при общем renderer.
- TI-125 — Pause/resume/skip/stop/shuffle/loop/volume использовать единый music handler.
- TI-126 — Skip при track-loop требует временного изменения loop state.
- TI-127 — Volume buttons менять значение фиксированным шагом и clamp-ить его.
- TI-128 — После state-changing music action refresh player UI.
- TI-129 — Отсутствие Lavalink должно блокировать music interaction понятным configuration error.
- TI-130 — Music interaction error должен знать customId конкретного действия.

## Countdown interaction surface

- TI-131 — Countdown buttons работают поверх runtime registry, а не через DB.
- TI-132 — Invalid/expired countdown ID обрабатывать без падения.
- TI-133 — Управление countdown ограничивать ManageMessages.
- TI-134 — Pause сохраняет remaining time относительно текущего clock.
- TI-135 — Resume пересоздаёт absolute endTime из remaining time.
- TI-136 — Pause/Resume меняет label управляющей кнопки.
- TI-137 — Cancel переводит countdown в cancelled visual state и убирает controls.
- TI-138 — Finish переводит countdown в finished visual state и убирает controls.
- TI-139 — Повторное нажатие по очищенному countdown registry должно дать безопасное expired-сообщение.

## Verification interaction

- TI-140 — Verification button является тонким adapter к verification service.
- TI-141 — Verification button работает только внутри guild.
- TI-142 — Verification service получает source metadata для аналитики/аудита.
- TI-143 — Service status `already_verified` превращается в понятную validation error.
- TI-144 — Успешный result содержит roleName для подтверждения пользователю.
- TI-145 — Verification interaction использует ephemeral defer/edit lifecycle.

## Reaction-role select surface

- TI-146 — Reaction-role select является thin adapter к существующему handler.
- TI-147 — Select interaction передаёт `interaction` и `client` в domain handler.
- TI-148 — Panel config определяется через guildId + messageId.
- TI-149 — User-selected values нельзя считать authoritative без проверки panel whitelist.
- TI-150 — Batch role assignment должен возвращать added/removed/skipped результат.
- TI-151 — Ошибка одной роли не должна прерывать обработку остальных.
- TI-152 — Role hierarchy проверяется непосредственно перед mutation.

## Loader-facing interaction organization

- TI-153 — Вложенные directories позволяют группировать interactions по domain: music, ticket, help, etc.
- TI-154 — Имена файлов могут совпадать в разных domain directories без конфликта registry при уникальных customId.
- TI-155 — Definition layer может быть полностью декларативным.
- TI-156 — Domain handler может экспортировать как named handlers, так и default handler.
- TI-157 — Interaction loader должен одинаково уметь загружать object и array definitions.
- TI-158 — Для динамически генерируемых definitions полезно сохранять один источник истины для action IDs.
- TI-159 — Registration layer не должен знать внутреннюю структуру domain service.
- TI-160 — Перенос UI action из button в select/modal не должен требовать переписывания бизнес-сервиса.
