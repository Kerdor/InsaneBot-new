# TitanBot — Handlers

Источник: `codebymitch/TitanBot`
Папка: `src/handlers/`
Статус: батч 1/завершение каталога handlers

## Interaction handler architecture

- TH-001 — Делить handlers по назначению: button, select menu, modal и domain-specific handler.
- TH-002 — Один handler может экспортировать несколько действий, сохраняя отдельные имена для роутера.
- TH-003 — Делать domain handler тонким: orchestration в handler, бизнес-операция в service.
- TH-004 — Передавать handler контекст `interaction` и `client`, а дополнительные значения — отдельным `args`.
- TH-005 — Разбирать аргументы из `customId` по разделителю только после проверки структуры.
- TH-006 — Использовать стабильные префиксы customId для namespace действий.
- TH-007 — Держать экспортируемый default handler для простого loader-case и именованные handlers для нескольких действий.
- TH-008 — Унифицировать обработку исключений через центральный `handleInteractionError`.
- TH-009 — Для простых пользовательских ошибок использовать `replyUserError` с типизированным ErrorTypes.
- TH-010 — Разделять техническое логирование ошибки и безопасное сообщение пользователю.
- TH-011 — Не позволять ошибке одного handler ломать остальные interaction handlers.
- TH-012 — Проверять состояние interaction перед `defer`, `reply` и `editReply`.
- TH-013 — Использовать безопасный defer helper, возвращающий признак успеха.
- TH-014 — Использовать безопасный edit-reply helper после defer.
- TH-015 — Обрабатывать Discord-коды уже подтверждённой/истёкшей interaction как ожидаемый lifecycle-case.
- TH-016 — Логировать customId и interaction ID при диагностике недоступной interaction.
- TH-017 — Указывать тип handler и customId в контексте централизованной ошибки.
- TH-018 — Делать permission check до тяжёлых операций.
- TH-019 — Повторно проверять права непосредственно в handler, даже если UI уже ограничен.
- TH-020 — Для server-only действий явно проверять guild context.
- TH-021 — Возвращать понятную ephemeral-ошибку вместо падения при неверном context.
- TH-022 — Разделять подготовку UI и выполнение действия.
- TH-023 — После изменения persistent state обновлять исходное сообщение, если оно является live-view.
- TH-024 — Не считать редактирование UI частью основной транзакции, если UI failure не должен ломать бизнес-операцию.
- TH-025 — Использовать отдельный cleanup после завершения временного interaction state.

## Modals / context-bound actions

- TH-026 — Связывать modal с исходным объектом через customId.
- TH-027 — Передавать ID исходного сообщения в modal для последующего refresh.
- TH-028 — Ограничивать modal-submit только пользователем, открывшим modal.
- TH-029 — Делать modal timeout длинным для сложных настроек, но конечным.
- TH-030 — Не считать timeout modal ошибкой, требующей ответа пользователю.
- TH-031 — Валидировать обязательные поля до defer, когда это возможно.
- TH-032 — Ограничивать длину пользовательского текста на уровне TextInput.
- TH-033 — Для подтверждения опасного действия требовать точную строку (`DELETE`).
- TH-034 — Делать destructive confirmation отдельным modal action.
- TH-035 — Перед destructive action повторно проверять identity инициатора.
- TH-036 — Сохранять ID исходного модератора в context для защиты продолжения workflow.
- TH-037 — После modal-submit повторно проверять актуальные права, а не доверять правам на момент открытия.
- TH-038 — Оборачивать async operation modal в defer + editReply lifecycle.
- TH-039 — Для modal context использовать короткие machine-readable customId segments.
- TH-040 — При потере context возвращать сообщение «операция истекла, начните заново».

## Countdown handler

- TH-041 — Управлять countdown через in-memory registry по уникальному countdown ID.
- TH-042 — Хранить interval прямо в runtime-состоянии countdown.
- TH-043 — Перед повторным запуском очищать старый interval.
- TH-044 — Вычислять оставшееся время от абсолютного `endTime`, а не простым декрементом.
- TH-045 — Хранить отдельное `remainingTime` для pause/resume.
- TH-046 — Использовать частый timer tick, но редактировать Discord message не чаще заданного интервала.
- TH-047 — Разделять внутреннюю частоту проверки времени и частоту Discord API updates.
- TH-048 — Форматировать countdown в `HH:MM:SS`, скрывая часы при нулевом часе.
- TH-049 — Обновлять кнопки вместе с embed, чтобы UI отражал paused/running state.
- TH-050 — Динамически менять label Pause на Resume.
- TH-051 — Иметь отдельную Cancel-кнопку.
- TH-052 — При завершении удалять управляющие кнопки.
- TH-053 — При завершении менять заголовок на Finished и показывать time-up state.
- TH-054 — При отмене менять embed на Cancelled вместо удаления сообщения.
- TH-055 — Очищать registry после finish/cancel.
- TH-056 — Очищать registry при необработанной runtime-ошибке.
- TH-057 — Ограничивать управление countdown permission `ManageMessages`.
- TH-058 — Делать expired/cancelled countdown безопасным повторно нажимаемым UI.
- TH-059 — При resume строить новый `endTime` из сохранённого remaining time.
- TH-060 — При pause фиксировать remaining time от текущего clock.
- TH-061 — Использовать ceil при отображении секунд, чтобы не показывать лишнее раннее `00`.
- TH-062 — Логировать запуск countdown с title и остатком.
- TH-063 — Ошибку единичного message edit логировать отдельно, не обязательно останавливая timer.
- TH-064 — Внешние функции countdown (`createControlButtons`, `formatTime`, start/cleanup) экспортировать для переиспользования и тестирования.

## Giveaway interaction patterns

- TH-065 — Защищать join giveaway user-level rate limit по паре user/message.
- TH-066 — Записывать interaction в rate limiter до входа в критическую секцию.
- TH-067 — Сериализовать операции одного giveaway через mutex по message ID.
- TH-068 — Читать giveaway из persistent storage внутри mutex, а не доверять устаревшему UI.
- TH-069 — Проверять одновременно временное окончание и persisted ended flags.
- TH-070 — Делать duplicate-entry проверку до изменения массива участников.
- TH-071 — Сохранять участника до обновления live embed.
- TH-072 — После join пересчитывать число участников из authoritative array.
- TH-073 — Автоматически отключать join button после окончания giveaway.
- TH-074 — Разрешать ручное завершение giveaway отдельной кнопкой.
- TH-075 — Ограничивать ручное завершение `ManageGuild`.
- TH-076 — Проверять guild context перед moderation-like giveaway actions.
- TH-077 — Выбирать winners только после повторного чтения актуального giveaway state.
- TH-078 — Сохранять `endedAt` и `endedBy` для ручного завершения.
- TH-079 — Сохранять winner IDs как часть persisted giveaway state.
- TH-080 — Переводить giveaway message в явный ENDED state с content + embed + buttons.
- TH-081 — Логировать завершение giveaway через общий logging service.
- TH-082 — Делать failure audit logging нефатальным для основной операции.
- TH-083 — Разрешать reroll только для уже завершённого giveaway.
- TH-084 — Не позволять reroll пустого списка участников.
- TH-085 — Сохранять `rerolledAt` и `rerolledBy`.
- TH-086 — Перерисовывать live giveaway embed после reroll.
- TH-087 — Показывать winners отдельным ephemeral action вместо обязательного изменения публичного сообщения.
- TH-088 — Разделять операции join/end/reroll/view на независимые handlers.
- TH-089 — Устойчиво работать с legacy `ended` и `isEnded` полями.
- TH-090 — Для отсутствующего giveaway возвращать доменную validation error, а не generic crash.
- TH-091 — Централизованный giveaway service может возвращать готовые embed/button builders для всех handlers.

## Logging dashboard interactions

- TH-092 — Иметь единый namespace customId для dashboard actions.
- TH-093 — Dashboard refresh должен сохранять текущий экран, а не всегда возвращаться на главную.
- TH-094 — Back action всегда строит актуальную main view заново.
- TH-095 — Toggle handler способен переключать отдельный event type.
- TH-096 — Поддерживать массовое включение/выключение всех событий.
- TH-097 — Поддерживать wildcard category state (`category.*`).
- TH-098 — После toggle обновлять тот экран, на котором пользователь находился.
- TH-099 — Для фильтра user/channel открывать разные modal-сценарии из общего handler.
- TH-100 — Использовать Discord User Select вместо ручного ввода user ID.
- TH-101 — Использовать Discord Channel Select вместо ручного ввода channel ID.
- TH-102 — Ограничивать типы выбираемых каналов прямо в Channel Select.
- TH-103 — В modal label давать человеку описание назначения selector-а.
- TH-104 — Ограничивать modal submit инициатором dashboard action.
- TH-105 — Использовать String Select для удаления существующего ignore filter.
- TH-106 — Ограничивать список select options первыми 25 элементами из-за Discord limit.
- TH-107 — Если фильтров нет, не открывать пустой modal, а вернуть user-input error.
- TH-108 — При удалении фильтра разбирать тип и ID из machine-readable value.
- TH-109 — Разделять destinations audit/applications/reports через единый helper.
- TH-110 — Перед сохранением log channel проверять существование выбранного канала.
- TH-111 — Проверять ViewChannel + SendMessages + EmbedLinks у бота в destination channel.
- TH-112 — После смены канала сразу refresh dashboard.
- TH-113 — Разрешать очистку destination без удаления всей logging config.
- TH-114 — Для всех dashboard actions требовать ManageGuild.
- TH-115 — Таймауты collector/modal не должны генерировать лишний пользовательский error.

## Music controls

- TH-116 — Отделять queue pagination actions от обычных playback controls.
- TH-117 — Хранить queue page отдельно для каждого пользователя.
- TH-118 — При открытии queue начинать с первой страницы.
- TH-119 — Перед pagination проверять, что playback всё ещё существует.
- TH-120 — Проверять voice-channel permission/context перед каждым music control.
- TH-121 — Динамически ограничивать previous/next/first/last страницу допустимым диапазоном.
- TH-122 — Использовать `deferUpdate` для button actions, которые редактируют исходное сообщение.
- TH-123 — Делать skip через `stop()` после временного снятия track-loop.
- TH-124 — Сохранять желаемый loop state отдельно и восстанавливать его на следующем track start.
- TH-125 — Shuffle должен менять runtime queue и refresh player message.
- TH-126 — Loop button циклически переключает none → track → queue → none.
- TH-127 — Volume controls изменяют громкость фиксированным шагом.
- TH-128 — Жёстко ограничивать volume диапазоном 0–100.
- TH-129 — Все music buttons используют общий `musicActions` service.
- TH-130 — Проверять наличие Lavalink/Riffy до обработки music interaction.
- TH-131 — Ошибку конкретной music action отправлять через общий interaction error handler.
- TH-132 — Queue UI может быть ephemeral, сохраняя guild runtime state.

## Ticket interaction patterns

- TH-133 — Перед ticket action проверять guild context.
- TH-134 — Перед management action получать ticket permission context из service.
- TH-135 — Разрешать creator-specific permission только для ограниченного набора действий.
- TH-136 — Разделять `canCloseTicket` и `canManageTicket`.
- TH-137 — Ограничивать permission context timeout несколькими секундами.
- TH-138 — Возвращать отдельную ошибку, если permission check слишком долгий.
- TH-139 — Возвращать validation error, если текущий channel не является ticket.
- TH-140 — Ticket creation ограничивать per-user rate limit.
- TH-141 — Ограничивать число открытых ticket-ов пользователя отдельным max setting.
- TH-142 — Показывать текущее количество ticket-ов и лимит в ошибке.
- TH-143 — Использовать modal для обязательной причины создания ticket.
- TH-144 — Ограничивать ticket reason 1000 символами.
- TH-145 — Для close использовать отдельный optional reason modal.
- TH-146 — Подставлять понятную fallback-причину, если close reason пуст.
- TH-147 — Для ticket actions использовать ephemeral confirmation.
- TH-148 — Использовать `InteractionHelper.safeDefer` для длительных ticket operations.
- TH-149 — Claim/unclaim делать отдельными state-changing actions.
- TH-150 — Priority менять через machine-readable argument из button customId.
- TH-151 — Pin/unpin реализовывать одним toggle handler по текущему имени канала.
- TH-152 — Для pinned ticket использовать визуальный marker в имени канала.
- TH-153 — Перемещать pinned ticket в начало категории.
- TH-154 — Возвращать unpinned ticket в нормальную позицию.
- TH-155 — Логировать pin/unpin как ticket event с metadata.
- TH-156 — Перед pin/unpin проверять наличие parent category.
- TH-157 — Использовать rate limit отдельно для ticket creation, не распространяя его на все ticket controls.
- TH-158 — Динамически импортировать редко используемую service-функцию в handler, уменьшая upfront coupling.
- TH-159 — Хранить source message ID при создании ticket modal для связи UI workflow.
- TH-160 — Ошибки modal opening отличать от ошибок самой ticket операции.

## Todo / shared state handlers

- TH-161 — Валидировать shared list ID regex-ом до любого DB access.
- TH-162 — Ограничивать shared list ID 64 символами.
- TH-163 — Передавать source message ID из button в modal для последующего refresh.
- TH-164 — Отдельно иметь handlers add/complete/remove и их modal-submit counterparts.
- TH-165 — Использовать modal для ввода task ID вместо сложного multi-step select UI.
- TH-166 — Ограничивать task text 200 символами.
- TH-167 — Ограничивать task ID положительным integer.
- TH-168 — Shared todo operations rate-limit-ить отдельно по operation type.
- TH-169 — Проверять существование списка перед изменением.
- TH-170 — Проверять membership пользователя перед каждой mutation.
- TH-171 — Не полагаться на наличие `tasks`: нормализовать его в пустой массив.
- TH-172 — Не полагаться на наличие `nextId`: восстанавливать default 1.
- TH-173 — Использовать монотонный `nextId`, не переиспользуя ID после удаления.
- TH-174 — При completion сохранять completedBy и completedAt.
- TH-175 — Не разрешать повторное completion уже выполненной задачи.
- TH-176 — При remove сохранять removed task для пользовательского confirmation text.
- TH-177 — После любой mutation обновлять исходное shared-list message.
- TH-178 — Если исходное message исчезло, mutation всё равно может завершиться успешно.
- TH-179 — Ошибка refresh live message должна быть изолирована от DB mutation.
- TH-180 — В shared view показывать owner/member/task state.
- TH-181 — Отображать completion marker и completedBy прямо в task list.
- TH-182 — Использовать ephemeral success response для shared mutations.

## Verification / role assignment

- TH-183 — Verification button сразу defer-ится ephemeral.
- TH-184 — Проверка guild должна происходить до вызова verification service.
- TH-185 — Передавать в service source (`button_click`) для аудита/аналитики.
- TH-186 — Service возвращает структурированный status вместо необходимости парсить текст.
- TH-187 — Отдельно обрабатывать `already_verified` как validation/user state.
- TH-188 — Успешную выдачу роли подтверждать roleName из service result.
- TH-189 — Verification failures идут через общий interaction error handler.
- TH-190 — Логировать guild/user context для verify action.

## Reaction-role assignment

- TH-191 — Перед обработкой select menu делать safe ephemeral defer.
- TH-192 — Reaction-role message config получать по guildId + messageId.
- TH-193 — Отсутствующий panel config считать stale/inactive state.
- TH-194 — Проверять ManageRoles у бота перед массовой обработкой ролей.
- TH-195 — FetchMe fallback использовать при отсутствии cached bot member.
- TH-196 — Получать bot highest-role position и проверять hierarchy каждой роли.
- TH-197 — Белый список доступных role IDs является authoritative source для select menu.
- TH-198 — Не доверять значениям select menu, которых нет в panel config.
- TH-199 — Нормализовать legacy object role storage в массив role IDs.
- TH-200 — Делить результаты на added/removed/skipped.
- TH-201 — Не выдавать managed roles через self-assignment.
- TH-202 — Блокировать опасные permissions при self-assignment.
- TH-203 — Проверять role.position < botRolePosition перед выдачей.
- TH-204 — Не ломать весь batch из-за одной несуществующей роли.
- TH-205 — Не ломать весь batch из-за ошибки Discord API на одной роли.
- TH-206 — Удалять роли panel, которых пользователь не выбрал.
- TH-207 — Выводить итоговое число skipped roles с причиной permission issues.
- TH-208 — Показывать пользователю одновременно добавленные и удалённые роли.
- TH-209 — Не писать audit log, если изменений фактически не было.
- TH-210 — Audit log ошибки не должны ломать выдачу ролей.
- TH-211 — Логировать member + added + removed в одном структурированном событии.

## Warning handlers

- TH-212 — Защищать warning workflow ID оригинального модератора.
- TH-213 — Не позволять другому модератору продолжить destructive warning workflow.
- TH-214 — Удаление одного warning начинать с отдельного confirmation modal.
- TH-215 — Принимать warning number в формате `#1` или `1`.
- TH-216 — Проверять integer и минимум 1.
- TH-217 — Сверять номер с текущим количеством warnings перед удалением.
- TH-218 — Удалять warning по его stable warning ID, найденному по номеру.
- TH-219 — Показывать причину удалённого warning в confirmation result.
- TH-220 — Для clear-all использовать точное текстовое подтверждение `DELETE`.
- TH-221 — Ограничивать confirmation input min/max length.
- TH-222 — Отдельно fetch target user для человекочитаемого имени.
- TH-223 — Если target user недоступен, использовать fallback `the user`.
- TH-224 — Логировать warning deletion/clear с guildId, targetId и moderatorId.
- TH-225 — Возвращать count удалённых warnings после clear-all.
- TH-226 — Использовать ephemeral response для destructive moderation result.

## Wipe-data handler

- TH-227 — Wipe workflow начинать с explicit confirmation UI.
- TH-228 — Перед wipe использовать safe ephemeral defer.
- TH-229 — Иметь централизованный список известных user-data keys.
- TH-230 — Поддерживать несколько legacy key formats при миграции/очистке данных.
- TH-231 — Проверять `exists` перед delete для каждой известной записи.
- TH-232 — Считать количество реально удалённых записей.
- TH-233 — Ошибка удаления одной записи не должна останавливать весь wipe.
- TH-234 — Собирать список ключей, удаление которых не удалось.
- TH-235 — При наличии DB list дополнительно искать неизвестные user-specific legacy keys.
- TH-236 — Дедуплицировать найденные keys через Set.
- TH-237 — Фильтровать обнаруженные keys по guildId:userId перед удалением.
- TH-238 — Ошибки prefix scan считать нефатальными.
- TH-239 — После wipe удалять interaction buttons.
- TH-240 — Показывать пользователю число удалённых records.
- TH-241 — Указывать, что wipe затронул economy/levels/items/personal data.
- TH-242 — При частичных delete errors завершать workflow, но отдельно логировать неполный результат.
- TH-243 — Cancel action должен сохранять данные и удалять confirmation controls.
- TH-244 — Cancel action логировать отдельно от успешного wipe.

## Help handlers

- TH-245 — Help back button восстанавливает исходное help menu через общий builder.
- TH-246 — Help pagination читает текущую страницу из существующего button label.
- TH-247 — Pagination имеет first/prev/next/last semantics.
- TH-248 — Pagination clamps page к диапазону 1..totalPages.
- TH-249 — Help bug-report button ведёт на внешний issue tracker через Discord Link Button.
- TH-250 — Bug report UI даёт пользователю checklist полезных данных для issue.
- TH-251 — Bug report embed может содержать avatar бота и timestamp.
- TH-252 — Category select и all-commands select используют единый help navigation flow.
- TH-253 — Help автоматически строит список команд из файловой структуры.
- TH-254 — Help нормализует command data через `toJSON()` если command builder это поддерживает.
- TH-255 — Help раскрывает subcommands в отдельные строки.
- TH-256 — Help раскрывает subcommand groups в отдельные command entries.
- TH-257 — Help исключает служебные help/commandlist commands из каталога.
- TH-258 — Help сортирует команды по display name.
- TH-259 — Help пытается сопоставить локальные команды с зарегистрированными Discord command IDs.
- TH-260 — При наличии Discord command ID использовать clickable command mention.
- TH-261 — При отсутствии registered ID использовать обычный `/command` текст.
- TH-262 — Ограничивать длину одного embed field и разбивать команды на части.
- TH-263 — Использовать несколько inline columns при большом all-command списке.
- TH-264 — Help имеет fallback icon для неизвестной категории.
- TH-265 — Ошибка чтения одной категории логируется и не ломает остальные категории.
- TH-266 — Ошибка fetch зарегистрированных commands не ломает локальную help generation.
- TH-267 — Help pagination взаимодействует через editReply, сохраняя исходное сообщение.
- TH-268 — Устаревшие help interactions Discord 40060/10062 обрабатываются без повторного ответа.
- TH-269 — Help UI имеет единый footer и timestamp.
- TH-270 — Category view имеет Back button для возврата в главный help экран.

## Loader architecture

- TH-271 — Event loader автоматически сканирует `src/events` вместо ручного списка.
- TH-272 — Event loader регистрирует `once` через client.once и обычные события через client.on.
- TH-273 — Event loader проверяет наличие name + execute перед регистрацией.
- TH-274 — Один невалидный event file не останавливает загрузку остальных.
- TH-275 — Ошибка import одного event file изолирована от остальных файлов.
- TH-276 — Event wrapper добавляет client в аргументы execute.
- TH-277 — Ошибка runtime одного event handler логируется внутри safe wrapper.
- TH-278 — Interaction loader рекурсивно обходит вложенные directories.
- TH-279 — Interaction loader автоматически поддерживает buttons/selectMenus/modals через список типов.
- TH-280 — Отсутствующая interaction directory обрабатывается как optional subsystem.
- TH-281 — Interaction loader принимает default export как один handler или массив handlers.
- TH-282 — Невалидный interaction export пропускается без остановки загрузки.
- TH-283 — Interaction loader логирует количество загруженных handlers каждого типа.
- TH-284 — Для cross-platform import использовать `pathToFileURL`.
- TH-285 — Логировать относительный путь handler-а и имя файла при загрузке.
- TH-286 — Собирать runtime interaction registry в `client[type]` collections.

## Calculate modal

- TH-287 — Calculation modal использует сохранённый calculation context по context key.
- TH-288 — Context key извлекается из customId input field.
- TH-289 — Expired calculation context выдаёт отдельную понятную ошибку.
- TH-290 — Перед evaluation проверять numeric operand через isNaN.
- TH-291 — Новое выражение строить из предыдущего expression + operator + operand.
- TH-292 — Для evaluation использовать safe math parser, а не `eval`.
- TH-293 — Форматировать обычные числа с locale grouping.
- TH-294 — Для очень больших/малых чисел использовать exponential notation.
- TH-295 — После chained operation обновлять исходное calculation message.
- TH-296 — Ошибка edit исходного сообщения не отменяет calculation result.
- TH-297 — Удалять calculation context после успешной chained operation.
- TH-298 — Возвращать новый результат как отдельный ephemeral/non-ephemeral interaction result согласно flow.

## Cross-handler reliability

- TH-299 — Использовать authoritative DB/service state вместо доверия к содержимому старого Discord message.
- TH-300 — Состояние UI должно быть восстанавливаемым из persistent state.
- TH-301 — Interaction handlers должны быть идемпотентными там, где пользователь может повторно нажать кнопку.
- TH-302 — Permission, validation и resource-not-found ошибки должны быть различимы.
- TH-303 — Runtime state, persistent state и Discord UI нужно рассматривать как три отдельных слоя.
- TH-304 — Mutation должна происходить до best-effort UI refresh, если UI не является транзакционной частью операции.
- TH-305 — Для конкурентных mutations использовать mutex/lock на объект, а не глобальную блокировку.
- TH-306 — User-specific rate limits должны включать объект действия, чтобы разные операции не блокировали друг друга.
- TH-307 — Сложные interactive workflows должны иметь конечный lifecycle и cleanup.
- TH-308 — Handler-level permission checks должны выполняться заново после modal delay.
- TH-309 — Сервисные ошибки не должны утекать пользователю сырым stack trace.
- TH-310 — Технические логи должны включать guild/user/resource IDs для воспроизводимости.
- TH-311 — Audit logging является side effect и не должен откатывать основную операцию при собственной ошибке.
- TH-312 — Большие Discord payloads следует дробить на fields/chunks до API limit.
- TH-313 — Legacy persisted fields можно читать параллельно с новыми для мягкой миграции.
- TH-314 — Handler должен корректно работать при cache miss, используя fetch fallback там, где это безопасно.
- TH-315 — Пользовательские interaction errors должны быть короткими и actionable.
- TH-316 — Временные registries должны иметь cleanup при любом terminal state.
- TH-317 — Не следует держать долгоживущую бизнес-логику непосредственно в interaction callback.
- TH-318 — Shared builders позволяют одинаково рендерить состояние из command/event/button flows.
- TH-319 — Machine-readable IDs в customId позволяют одному handler обслуживать много экземпляров одного UI.
- TH-320 — Повторная проверка resource state непосредственно перед mutation защищает от stale UI.
