# TitanBot — Utility

Источник: `codebymitch/TitanBot`
Каталог механик из `src/commands/Utility/`, связанных report modules и `src/handlers/todoButtons.js`.

## Avatar

- TUTILITY-001 — Команда `/avatar` показывает аватар пользователя.
- TUTILITY-002 — Target-пользователь необязателен.
- TUTILITY-003 — При отсутствии target используется сам инициатор.
- TUTILITY-004 — Аватар получается через Discord `displayAvatarURL`.
- TUTILITY-005 — Для аватара запрашивается размер до 2048px.
- TUTILITY-006 — Используется dynamic avatar URL для GIF-анимаций.
- TUTILITY-007 — Аватар выводится крупным изображением внутри embed.
- TUTILITY-008 — В embed присутствует отдельная ссылка на скачивание.
- TUTILITY-009 — Заголовок персонализируется username выбранного пользователя.
- TUTILITY-010 — Команда логирует инициатора и target отдельно.

## First message

- TUTILITY-011 — `/firstmsg` предназначен для поиска первого сообщения канала.
- TUTILITY-012 — Команда отключена в DM.
- TUTILITY-013 — Для команды задано минимальное право SendMessages.
- TUTILITY-014 — Перед сетевой/Discord-операцией используется safe defer.
- TUTILITY-015 — Поиск первого сообщения выполняется через Discord message history.
- TUTILITY-016 — Запрашивается только одна запись истории.
- TUTILITY-017 — Используется `after: '1'` как нижняя граница поиска истории.
- TUTILITY-018 — Fetch выполняется без добавления сообщения в cache.
- TUTILITY-019 — При отсутствии сообщения возвращается отдельный успешный empty-state.
- TUTILITY-020 — Найденное первое сообщение превращается в прямую Discord-ссылку.
- TUTILITY-021 — Ссылка содержит guild ID, channel ID и message ID.
- TUTILITY-022 — Результат явно указывает название канала.
- TUTILITY-023 — Команда логирует channel ID и найденный message ID.
- TUTILITY-024 — Ошибка defer логируется отдельно до выполнения основной логики.

## User info

- TUTILITY-025 — `/userinfo` показывает подробную информацию о пользователе.
- TUTILITY-026 — Target необязателен.
- TUTILITY-027 — Без target используется инициатор.
- TUTILITY-028 — Пользователь извлекается как Discord User.
- TUTILITY-029 — Дополнительно выполняется поиск guild member в cache.
- TUTILITY-030 — Account creation date показывается как Discord relative timestamp.
- TUTILITY-031 — Join date сервера показывается как relative timestamp.
- TUTILITY-032 — Для отсутствующего member выводится `Not in server`.
- TUTILITY-033 — Показывается Discord user ID.
- TUTILITY-034 — Отдельно показывается bot-status.
- TUTILITY-035 — Показываются роли пользователя.
- TUTILITY-036 — Роли ограничиваются первыми пятью для компактности.
- TUTILITY-037 — Роли объединяются в одну строку.
- TUTILITY-038 — При отсутствии дополнительных ролей показывается `None`.
- TUTILITY-039 — Показывается highest role.
- TUTILITY-040 — Для отсутствующего member highest role имеет fallback `None`.
- TUTILITY-041 — Avatar пользователя используется как thumbnail.
- TUTILITY-042 — Результат оформляется единым embed.
- TUTILITY-043 — Команда логирует initiator и target ID.
- TUTILITY-044 — Ошибка defer не позволяет продолжить выполнение команды.

## Server info

- TUTILITY-045 — `/serverinfo` показывает сводную информацию о сервере.
- TUTILITY-046 — Guild берётся непосредственно из interaction.
- TUTILITY-047 — Owner загружается через отдельный `fetchOwner`.
- TUTILITY-048 — Показывается server ID.
- TUTILITY-049 — Показывается имя сервера в title.
- TUTILITY-050 — Иконка сервера используется как thumbnail.
- TUTILITY-051 — Показывается владелец сервера.
- TUTILITY-052 — Показывается текущее количество участников.
- TUTILITY-053 — Показывается количество каналов из cache.
- TUTILITY-054 — Показывается количество ролей из cache.
- TUTILITY-055 — Показывается Discord boost tier.
- TUTILITY-056 — Показывается количество boost subscriptions.
- TUTILITY-057 — Показывается дата создания сервера.
- TUTILITY-058 — Дата создания выводится через Discord relative timestamp.
- TUTILITY-059 — Поля server info разбиты на inline-поля для компактного вида.
- TUTILITY-060 — Команда использует safe defer/safe editReply lifecycle.
- TUTILITY-061 — В лог записывается guild ID, name и member count.

## Report

- TUTILITY-062 — `/report` объединяет пользовательский report и его настройку в одну команду.
- TUTILITY-063 — Report реализован через subcommands.
- TUTILITY-064 — `report file` принимает target user.
- TUTILITY-065 — Target user обязателен.
- TUTILITY-066 — `report file` требует reason.
- TUTILITY-067 — Reason ограничен 500 символами на уровне slash option.
- TUTILITY-068 — `report setchannel` принимает channel option.
- TUTILITY-069 — Report channel ограничен GuildText channel type.
- TUTILITY-070 — Report-команда отключена в DM.
- TUTILITY-071 — Report logic разделён на отдельные modules.
- TUTILITY-072 — Router определяет выбранный subcommand.
- TUTILITY-073 — Неизвестный subcommand обрабатывается typed user error.
- TUTILITY-074 — Отправка report выполняется ephemeral для инициатора.
- TUTILITY-075 — Report получает guild config перед маршрутизацией.
- TUTILITY-076 — Для report используется специальный logging destination `reports`.
- TUTILITY-077 — Report destination разрешается через общий logging resolver.
- TUTILITY-078 — Если report channel не настроен, отправителю объясняется, что нужно настроить.
- TUTILITY-079 — В report упоминается владелец сервера, если owner ID доступен.
- TUTILITY-080 — Report записывается через общий `logEvent` pipeline.
- TUTILITY-081 — Report использует отдельный event type.
- TUTILITY-082 — В log embed указывается reported user.
- TUTILITY-083 — В log embed указывается reporter.
- TUTILITY-084 — В log embed указывается исходный канал.
- TUTILITY-085 — Reason выводится отдельным block field.
- TUTILITY-086 — Avatar reported user используется как thumbnail report embed.
- TUTILITY-087 — Author report может быть разрешён через общий user-author helper.
- TUTILITY-088 — После успешной отправки пользователь получает подтверждение.
- TUTILITY-089 — Подтверждение явно указывает reported user.
- TUTILITY-090 — Report логирует длину reason, а не только сам факт операции.
- TUTILITY-091 — Настройка report channel требует Manage Server.
- TUTILITY-092 — `setchannel` сохраняет destination через общий logging service.
- TUTILITY-093 — После настройки пользователь получает ephemeral подтверждение.
- TUTILITY-094 — В подтверждении показывается выбранный channel.
- TUTILITY-095 — Настройка также доступна через `/logging dashboard`.
- TUTILITY-096 — Ошибка сохранения report channel преобразуется в понятную user error.
- TUTILITY-097 — Ошибка настройки логируется с контекстом.
- TUTILITY-098 — Report channel configuration переиспользует общий механизм logging destinations.
- TUTILITY-099 — Report не требует отдельного хранения конфигурации.

## To-do — personal

- TUTILITY-100 — `/todo` хранит персональный список задач пользователя.
- TUTILITY-101 — Personal todo имеет subcommand `add`.
- TUTILITY-102 — Personal todo имеет `list`.
- TUTILITY-103 — Personal todo имеет `complete`.
- TUTILITY-104 — Personal todo имеет `remove`.
- TUTILITY-105 — Task text обязателен.
- TUTILITY-106 — Каждая задача получает последовательный numeric ID.
- TUTILITY-107 — Следующий ID хранится отдельно как `nextId`.
- TUTILITY-108 — Task хранит текст.
- TUTILITY-109 — Task хранит completed-флаг.
- TUTILITY-110 — Task хранит creation timestamp.
- TUTILITY-111 — Personal todo хранится под user-specific DB key.
- TUTILITY-112 — При отсутствии пользовательских данных создаётся пустой список.
- TUTILITY-113 — При повреждённом/неполном массиве задач применяется fallback initialization.
- TUTILITY-114 — При отсутствующем nextId применяется значение 1.
- TUTILITY-115 — Empty todo list имеет отдельный embed.
- TUTILITY-116 — List показывает task ID.
- TUTILITY-117 — List визуально различает completed и pending задачи.
- TUTILITY-118 — Для задачи отображается дата создания.
- TUTILITY-119 — Complete принимает numeric task ID.
- TUTILITY-120 — Complete проверяет существование задачи.
- TUTILITY-121 — Повторное завершение уже completed task отклоняется.
- TUTILITY-122 — При завершении меняется только completed state.
- TUTILITY-123 — Remove ищет задачу по стабильному ID, а не по позиции массива.
- TUTILITY-124 — Удаление реально удаляет объект задачи из массива.
- TUTILITY-125 — После изменения список сразу сохраняется в DB.
- TUTILITY-126 — После add/complete/remove пользователь получает понятное подтверждение.
- TUTILITY-127 — Неизвестный personal subcommand возвращает typed error.
- TUTILITY-128 — Todo-команда отключена в DM.
- TUTILITY-129 — Для todo задано минимальное право SendMessages.
- TUTILITY-130 — Todo использует safe interaction lifecycle.

## To-do — shared lists

- TUTILITY-131 — Todo поддерживает отдельную группу `share` для совместных списков.
- TUTILITY-132 — Shared list можно создать через `share create`.
- TUTILITY-133 — Shared list получает пользовательское имя.
- TUTILITY-134 — Shared list получает криптографически случайный share ID.
- TUTILITY-135 — Share ID генерируется из 16 random bytes.
- TUTILITY-136 — Share ID сериализуется как hex.
- TUTILITY-137 — При создании creator автоматически становится первым member.
- TUTILITY-138 — Shared list хранит creatorId.
- TUTILITY-139 — Shared list хранит members.
- TUTILITY-140 — Shared list хранит tasks.
- TUTILITY-141 — Shared list хранит nextId.
- TUTILITY-142 — Shared list хранит createdAt.
- TUTILITY-143 — Shared list хранится под отдельным `shared_todo_<id>` ключом.
- TUTILITY-144 — Для каждого пользователя отдельно хранится список доступных shared list IDs.
- TUTILITY-145 — Один и тот же list ID не добавляется пользователю повторно.
- TUTILITY-146 — Shared list loader умеет создавать отсутствующий список только при наличии creator context.
- TUTILITY-147 — Shared list loader нормализует отсутствующие tasks в массив.
- TUTILITY-148 — Shared list loader нормализует отсутствующий members в массив.
- TUTILITY-149 — Shared list loader восстанавливает отсутствующий nextId.
- TUTILITY-150 — `share add` позволяет creator добавить пользователя.
- TUTILITY-151 — Только creator имеет право добавлять members.
- TUTILITY-152 — Повторное добавление существующего member отклоняется.
- TUTILITY-153 — При добавлении member его личный список shared list IDs также обновляется.
- TUTILITY-154 — `share view` позволяет участнику просматривать список.
- TUTILITY-155 — Просмотр чужого списка без membership запрещён.
- TUTILITY-156 — Shared list view показывает owner.
- TUTILITY-157 — Shared list view показывает всех members.
- TUTILITY-158 — При отсутствии задач отображается отдельный empty-state.
- TUTILITY-159 — Empty-state содержит интерактивную кнопку Add Task.
- TUTILITY-160 — Shared list view содержит Complete Task button.
- TUTILITY-161 — Shared list view содержит Remove Task button.
- TUTILITY-162 — Каждая shared task имеет собственный numeric ID.
- TUTILITY-163 — Shared task хранит createdBy.
- TUTILITY-164 — Shared task хранит createdAt.
- TUTILITY-165 — Shared task хранит completed.
- TUTILITY-166 — При завершении shared task хранится completedBy.
- TUTILITY-167 — При завершении shared task хранится completedAt.
- TUTILITY-168 — Shared task list визуально показывает pending/completed state.
- TUTILITY-169 — Completed task отображает пользователя, который её завершил.
- TUTILITY-170 — Shared list message можно обновлять после изменения данных.
- TUTILITY-171 — Refresh ищет исходное сообщение по message ID.
- TUTILITY-172 — Перед refresh данные перечитываются из DB.
- TUTILITY-173 — Refresh использует единый payload builder.
- TUTILITY-174 — Если source message отсутствует, refresh безопасно прекращается.
- TUTILITY-175 — Ошибка refresh логируется без падения handler.
- TUTILITY-176 — Button custom IDs кодируют list ID.
- TUTILITY-177 — Modal custom IDs кодируют list ID.
- TUTILITY-178 — Modal custom IDs могут сохранять source message ID для последующего refresh.
- TUTILITY-179 — Shared list ID валидируется regex-ом до обработки.
- TUTILITY-180 — Допустимая длина shared list ID ограничена 1–64 символами.
- TUTILITY-181 — В ID разрешены только alphanumeric, underscore и hyphen.
- TUTILITY-182 — Invalid list ID превращается в понятную user error.
- TUTILITY-183 — Add Task открывает modal вместо отдельного slash command flow.
- TUTILITY-184 — Complete Task открывает modal с вводом task ID.
- TUTILITY-185 — Remove Task открывает modal с вводом task ID.
- TUTILITY-186 — Add Task modal ограничивает текст 200 символами.
- TUTILITY-187 — Add Task modal требует непустое поле.
- TUTILITY-188 — Complete/Remove task ID вводится как text input и затем парсится в integer.
- TUTILITY-189 — Task ID должен быть положительным integer.
- TUTILITY-190 — Add shared task защищён rate limit 5 операций за 30 секунд на пользователя.
- TUTILITY-191 — Complete shared task защищён отдельным rate limit 5/30s.
- TUTILITY-192 — Remove shared task защищён отдельным rate limit 5/30s.
- TUTILITY-193 — Rate limit ключ разделяется по типу операции.
- TUTILITY-194 — Shared Add проверяет membership перед записью.
- TUTILITY-195 — Shared Complete проверяет membership перед записью.
- TUTILITY-196 — Shared Remove проверяет membership перед записью.
- TUTILITY-197 — Shared Add отклоняет пустой task text.
- TUTILITY-198 — Shared Add создаёт task через nextId и увеличивает counter.
- TUTILITY-199 — Shared Complete отклоняет несуществующий task ID.
- TUTILITY-200 — Shared Complete отклоняет уже completed task.
- TUTILITY-201 — Shared Complete записывает completedBy и completedAt.
- TUTILITY-202 — Shared Remove удаляет task по стабильному ID.
- TUTILITY-203 — После shared Add данные сохраняются до обновления view.
- TUTILITY-204 — После shared Complete данные сохраняются до обновления view.
- TUTILITY-205 — После shared Remove данные сохраняются до обновления view.
- TUTILITY-206 — После button/modal операции пользователь получает ephemeral результат.
- TUTILITY-207 — Ошибки handler оборачиваются try/catch.
- TUTILITY-208 — Ошибки shared todo handler логируются с контекстом.
- TUTILITY-209 — Shared todo view использует fallback mention, если member отсутствует в cache.
- TUTILITY-210 — Shared todo owner также имеет fallback mention.
- TUTILITY-211 — Shared todo view builder принимает guild отдельно от DB data.
- TUTILITY-212 — Shared todo button handlers вынесены в отдельный handler module.
- TUTILITY-213 — Modal handlers экспортируются отдельно от button handlers.
- TUTILITY-214 — Interaction router может различать `shared_todo_` button namespace.
- TUTILITY-215 — Button namespace содержит operation и list ID для маршрутизации.
- TUTILITY-216 — Modal namespace содержит operation, list ID и optional source message ID.
- TUTILITY-217 — Shared todo UI можно обновлять без повторного вызова slash command.
- TUTILITY-218 — Shared list ID служит одновременно persistent storage identifier и UI routing identifier.
- TUTILITY-219 — Персональные и shared todo данные разделены разными DB namespaces.
- TUTILITY-220 — Shared list member access хранится непосредственно в list record.

## Data / resilience patterns observed in Utility

- TUTILITY-221 — Utility commands разделяют router и command modules там, где subsystem сложнее одной операции.
- TUTILITY-222 — Persistent todo records допускают частично отсутствующие поля и нормализуются при чтении.
- TUTILITY-223 — User-facing errors разделяются от внутренних exception paths.
- TUTILITY-224 — Discord interaction failures не должны ломать основной command process.
- TUTILITY-225 — Для потенциально долгих Discord/API операций применяется defer перед работой.
- TUTILITY-226 — Utility responses преимущественно оформляются через общие embed helpers.
- TUTILITY-227 — Logging содержит user/guild/target context для диагностируемости.
- TUTILITY-228 — Report интегрируется с уже существующей системой logging вместо отдельного канала/таблицы.
- TUTILITY-229 — Shared todo использует DB как источник истины, а Discord message выступает как обновляемое представление.
- TUTILITY-230 — Для интерактивных объектов полезно сохранять source message ID, чтобы после mutation обновлять исходный UI.
- TUTILITY-231 — Persistent IDs лучше позиций массива для действий над задачами.
- TUTILITY-232 — Operation-specific rate limits позволяют защищать разные mutation paths независимо.
- TUTILITY-233 — Validation должна выполняться как на slash-option уровне, так и непосредственно в handler.
- TUTILITY-234 — Missing Discord cache entries не должны делать persistent records нечитаемыми.
- TUTILITY-235 — Ошибки обновления UI после успешной DB mutation должны быть изолированы от самой mutation.
- TUTILITY-236 — Empty states могут сразу содержать доступные next actions через buttons.
- TUTILITY-237 — Для irreversible/persistent user operations полезен отдельный typed error path.
- TUTILITY-238 — Utility subsystem сочетает stateless commands (avatar/serverinfo/weather) и persistent features (todo/report config).
- TUTILITY-239 — Один command namespace может объединять простые read-only utilities и stateful subcommands.
- TUTILITY-240 — Общие helpers для safeReply/safeEditReply/safeDefer уменьшают дублирование interaction error handling.
