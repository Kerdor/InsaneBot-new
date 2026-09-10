# CorwinDev — Batch 4

Источник: `CorwinDev/Discord-Bot`, branch `main`.

Продолжение фактического обхода `src/events` после закрытия `src/commands`.

## Client / startup

### COR-202 — Shard-ready логирование
- При готовности каждого shard бот отправляет отдельный startup-log с номером shard и состоянием Ready.

### COR-203 — Периодическая смена статуса бота
- Presence автоматически меняется через заданный интервал.
- Варианты статуса могут задаваться через переменную окружения; иначе используются встроенные шаблоны.

### COR-204 — Статус с глобальным количеством серверов
- При работе через shards бот агрегирует количество guild между shards и использует его в presence.

### COR-205 — Общий error code для ошибки команды
- Ошибке выполнения генерируется короткий случайный код, который показывается пользователю и записывается в developer logs вместе с exception/stack.

### COR-206 — Ошибки команд с fallback-ответом
- При проблеме с первым error-response бот пытается отправить альтернативный вариант ответа.

## Guild lifecycle

### COR-207 — Автоматическая инициализация настроек нового сервера
- При добавлении бота создаётся базовая guild-конфигурация с prefix по умолчанию.

### COR-208 — Welcome после добавления бота
- После добавления в сервер бот ищет первый доступный текстовый канал, где у него есть право отправки, и публикует инструкцию по настройке.

### COR-209 — Логирование добавления бота на сервер
- В developer/server logs отправляются guild ID, название, число участников, владелец и глобальное количество серверов.

### COR-210 — Полная очистка guild-данных при уходе
- При удалении бота из сервера удаляются записи guild сразу из набора разных моделей/подсистем.

### COR-211 — Логирование ухода бота с сервера
- Уход из guild отправляется в отдельный лог с серверными данными и общим количеством оставшихся серверов.

### COR-212 — Удаление ticket metadata при удалении канала
- Если удалённый channel был тикетом, его запись автоматически удаляется из ticket database.

## Channel / emoji / event logs

### COR-213 — Детальные channel lifecycle logs
- Создание/удаление channel логируется с именем, ID, категорией и типом.

### COR-214 — Channel rename audit log
- Изменение имени канала сохраняет Before/After вместе с ID, категорией и типом.

### COR-215 — Channel topic audit log
- Изменение topic сохраняет старое и новое значение вместе с метаданными канала.

### COR-216 — Channel pins audit log
- Изменение закреплённых сообщений логируется с каналом и временем события.

### COR-217 — Emoji lifecycle logs
- Создание и удаление custom emoji логируются отдельно.
- Для создания сохраняется также URL изображения.

### COR-218 — Emoji rename audit log
- Изменение имени emoji записывается как Before/After с ID.

### COR-219 — Scheduled event lifecycle logs
- Создание/удаление Discord Scheduled Event логируется с названием, описанием, временем старта, privacy и типом location.

### COR-220 — Scheduled event update diff
- Изменение scheduled event логируется сравнением старого и нового имени, описания и времени.

## Role / member / moderation logs

### COR-221 — Role lifecycle logs
- Создание/удаление роли логируется с названием, ID, цветом и позицией.

### COR-222 — Role name audit log
- Изменение имени роли сохраняет Before/After.

### COR-223 — Role color audit log
- Изменение цвета роли сохраняет старое и новое hexadecimal значение.

### COR-224 — Role permissions audit log
- Изменение permissions роли логируется как Before/After списки permission flags.

### COR-225 — Member role change audit
- Добавленные и удалённые роли пользователя выводятся отдельными списками.
- При partial member источник изменений может восстанавливаться через Audit Logs.

### COR-226 — Ban/unban audit logs
- Ban и unban пользователя логируются отдельными событиями с avatar, tag, ID и timestamp.

### COR-227 — Boost/unboost announcement templates
- Для boost и unboost можно отдельно настраивать текстовые шаблоны с user/guild placeholders.

### COR-228 — Boost/unboost в выделенный канал
- События буста и снятия буста отправляются в заранее настроенный канал.

### COR-229 — Invite-aware leave processing
- При выходе участника система может уменьшить счётчик успешных invites пригласившего и увеличить его `Left`.

### COR-230 — Invite-aware leave message placeholders
- Leave-сообщение может содержать данные ушедшего пользователя, пригласившего, его invite statistics и статистику сервера.

## Message / interaction infrastructure

### COR-231 — DM logging
- Входящие DM боту логируются отдельным webhook с автором, текстом и URL вложения.

### COR-232 — Message-based XP progression
- Каждое сообщение может давать случайное количество XP при включённой системе уровней.
- При повышении уровня отправляется level message и может выдаваться role reward.

### COR-233 — Message counter rewards
- Для каждого пользователя ведётся счётчик сообщений.
- Достижение конкретного количества сообщений может выдавать роль.

### COR-234 — AFK auto-clear on message
- Когда AFK-пользователь пишет сообщение, его AFK-запись удаляется и временно показывается уведомление.
- Префикс `[AFK]` на nickname автоматически снимается.

### COR-235 — Multi-user AFK mention detection
- При упоминании нескольких пользователей бот ищет их AFK-состояния одним запросом и сообщает причины для найденных AFK пользователей.

### COR-236 — Dedicated chatbot channel
- AI-ответы могут быть включены только в конкретном guild channel.
- Сообщения этого канала отправляются во внешний chat API.

### COR-237 — Sticky message re-publish
- При новом сообщении в настроенном канале предыдущий sticky message удаляется и публикуется заново.
- ID нового sticky сохраняется в БД.

### COR-238 — Prefix command compatibility
- Помимо slash-команд бот поддерживает configurable prefix и прямой mention как префикс.

### COR-239 — Mention-only bot help
- Если пользователь просто упоминает бота без команды, бот показывает краткую help/invite/support карточку.

### COR-240 — Custom commands через message events
- Обычные prefix-сообщения также могут запускать сохранённые custom commands с режимами Normal, Embed и DM.

## Giveaway / interaction feedback

### COR-241 — Подтверждение участия в giveaway через DM
- После принятия giveaway reaction участнику отправляется подтверждение со ссылкой на исходный giveaway.

### COR-242 — Feedback об окончании giveaway
- Попытка участвовать после завершения giveaway получает отдельное уведомление пользователю.

### COR-243 — Персональное уведомление победителя giveaway
- Каждый победитель получает отдельное сообщение с призом и ссылкой на giveaway.

## Security / verification / reaction roles

### COR-244 — Developer ban на уровне interaction gateway
- Перед выполнением command/context-menu interaction проверяется глобальный user ban, заданный разработчиками.

### COR-245 — CAPTCHA verification
- Verification button запускает CAPTCHA-сессию с изображением и ожиданием текстового ответа пользователя.
- При успехе выдаётся настроенная роль.

### COR-246 — Ephemeral reaction-role feedback
- Добавление/снятие reaction role подтверждается пользователю ephemeral-сообщением.

### COR-247 — Multi-select reaction-role toggle
- Select Menu может одновременно обработать несколько выбранных ролей, переключая каждую в зависимости от текущего состояния пользователя.

### COR-248 — Component routing через custom ID
- Единый interaction handler маршрутизирует ticket, verification и reaction-role actions по `customId`.

## Отдельно отмечено
- `raw.js` в `src/events/event` фактически пустой и новых механик не добавляет.
- В `giveaway` часть lifecycle-событий дублирует уже каталогизированные giveaway mechanics; новые пункты здесь добавлены только там, где событие даёт отдельное пользовательское поведение.
- В `clientReady` присутствует shard-aware startup и глобальный status rotation.
