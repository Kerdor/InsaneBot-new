# GAwesomeBot — Commands/Public — batch 6

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Продолжение batch 5. Здесь только новые детали, не являющиеся точными повторами уже зафиксированных GAB-PUB-001–452.

## Role information

- **GAB-PUB-453 — Role inventory pagination threshold:** полный список ролей режется на страницы по 25 ролей, но при малом объёме пытается объединиться в один embed.
- **GAB-PUB-454 — Role inventory hierarchy ordering:** список ролей показывается от самой высокой позиции к самой низкой, а не в алфавитном порядке.
- **GAB-PUB-455 — Personal role permission aggregation:** roleinfo рассчитывает суммарный permission bitfield всех ролей текущего пользователя.
- **GAB-PUB-456 — Effective Administrator warning:** при наличии Administrator отдельно предупреждается, что он обходит остальные permissions и overrides.
- **GAB-PUB-457 — Role member count:** карточка конкретной роли показывает количество участников с этой ролью.
- **GAB-PUB-458 — Role position disclosure:** конкретная роль показывает свою позицию в иерархии сервера.
- **GAB-PUB-459 — Role mentionability disclosure:** карточка явно сообщает, если роль можно упоминать всем пользователям.
- **GAB-PUB-460 — Role hoist disclosure:** карточка отдельно показывает, если роль отображается отдельно в member list.
- **GAB-PUB-461 — Role integration-management disclosure:** managed role помечается как управляемая интеграцией.
- **GAB-PUB-462 — Role color-preserving presentation:** цвет embed для конкретной роли берётся из цвета самой роли, а отсутствие цвета отображается как None.
- **GAB-PUB-463 — Role zero-permission state:** роль без дополнительных permissions получает отдельное понятное состояние вместо пустого permission блока.
- **GAB-PUB-464 — Role lookup failure guidance:** не найденная роль сопровождается подсказкой посмотреть полный список ролей без аргументов.

## Lottery details

- **GAB-PUB-465 — Lottery unique participant count:** число участников отделяется от числа билетов через дедупликацию user IDs.
- **GAB-PUB-466 — Lottery dynamic ticket price:** стоимость следующего билета растёт от текущего количества уникальных участников и multiplier.
- **GAB-PUB-467 — Lottery per-user ticket cap:** один пользователь может купить максимум пять билетов в одной лотерее.
- **GAB-PUB-468 — Lottery no-refund policy:** после покупки билета бот явно сообщает, что возврата нет.
- **GAB-PUB-469 — Lottery creator/admin end authority:** завершить лотерею досрочно может её создатель, Bot Admin или maintainer.
- **GAB-PUB-470 — Lottery zero-winner state:** завершение лотереи с отсутствием победителя имеет отдельный результат вместо обычного winner flow.
- **GAB-PUB-471 — Lottery prize tracks total tickets:** текущий приз вычисляется от общего количества проданных билетов, поэтому несколько билетов одного пользователя увеличивают prize pool.
- **GAB-PUB-472 — Lottery affordability guard:** старт lottery проверяет баланс инициатора относительно выбранного multiplier и предлагает выбрать меньший размер.
- **GAB-PUB-473 — Lottery default-size fallback:** отсутствие ответа на выбор размера или неизвестный вариант приводит к standard 2x.
- **GAB-PUB-474 — Lottery humanized expiry:** время объявления победителя показывается относительно текущего момента через humanized duration.
- **GAB-PUB-475 — Lottery live economics card:** вызов команды во время lottery показывает одновременно цену следующего билета, multiplier, текущий prize и число ticket holders.

## Wikipedia lookup

- **GAB-PUB-476 — Wikipedia random mode:** команда без аргумента выбирает случайную статью вместо ошибки usage.
- **GAB-PUB-477 — Wikipedia one-result search:** поиск по запросу ограничивается одним кандидатом, после чего открывается выбранная статья.
- **GAB-PUB-478 — Wikipedia short-summary expansion:** слишком короткий summary (<100 символов) заменяется полным содержимым статьи.
- **GAB-PUB-479 — Wikipedia long-content external continuation:** описание длиннее Discord-safe лимита обрезается и получает прямую ссылку на полную статью.
- **GAB-PUB-480 — Wikipedia image best-effort fallback:** ошибка получения main image не ломает сам результат статьи.

## Command documentation / contracts

- **GAB-PUB-481 — Public commandData usage contract:** базовый Public-шаблон предусматривает передачу commandData с name/usage/description, чтобы команды могли строить единообразные usage/error ответы.
- **GAB-PUB-482 — Public document injection catalog:** базовый контракт заранее перечисляет server/channel/member/user документы и их query-варианты как стандартные зависимости команды.
- **GAB-PUB-483 — Public main-object service access:** базовый шаблон формализует доступ команды к client, configJS, Utils/utils и Constants через main object.
- **GAB-PUB-484 — PM metadata cross-reference from Public:** базовый контракт рекомендует получать дополнительные сведения о команде через metadata lookup по command name.

## Small UX / validation details

- **GAB-PUB-485 — Timezone friendly unknown-zone response:** неизвестная timezone не приводит к исключению; пользователь получает отдельное conversational объяснение.
- **GAB-PUB-486 — Translation fenced-result presentation:** перевод помещается в отдельный fenced code block для визуального отделения результата от служебного текста.
- **GAB-PUB-487 — Twitter progress message replacement:** внешний поиск tweets сначала занимает отдельное progress-сообщение, которое удаляется перед показом пагинации.
- **GAB-PUB-488 — Twitter invalid-account state reuse:** отсутствие RSS-результатов превращается в понятное состояние аккаунта без публичных tweets, а не в пустой paginator.
- **GAB-PUB-489 — YouTube result-type footer labeling:** paginator каждой карточки явно сообщает, является ли результат video, playlist, channel или неизвестным типом.
- **GAB-PUB-490 — YouTube published-at metadata:** timestamp результата берётся непосредственно из `publishedAt` API и отображается в карточке.
- **GAB-PUB-491 — Weather precipitation-window normalization:** rain/snow показываются в унифицированном формате количества осадков за последние 3 часа независимо от того, пришёл API-ключ `1h` или `3h`.
- **GAB-PUB-492 — Weather country-qualified title:** результат погоды идентифицирует город вместе с ISO country code.
- **GAB-PUB-493 — Weather visual condition icon:** карточка погоды использует внешний weather-condition icon как thumbnail.
- **GAB-PUB-494 — XKCD date reconstruction:** дата комикса собирается из отдельных year/month/day полей API для timestamp карточки.
- **GAB-PUB-495 — Shorten input-mode detection:** URL автоматически классифицируется как Bitly-expand либо обычный shorten по prefix распознаванию.

## Batch 7 — additional Public mechanics

### Command contract / presentation

- **GAB-PUB-496 — Public command base as executable documentation:** `_base.js` служит живой документацией интерфейса Public-команды.
- **GAB-PUB-497 — Explicit document/query-document distinction:** базовый контракт разделяет документы состояния и query-документы для мутаций.
- **GAB-PUB-498 — Standardized command dependency surface:** client/config/constants/services передаются через единый main object.

### Cooldown control

- **GAB-PUB-499 — Channel-local command cooldown:** cooldown хранится на уровне канала.
- **GAB-PUB-500 — Cooldown removal aliases:** `.` и `clear` снимают cooldown.
- **GAB-PUB-501 — Five-minute cooldown ceiling:** cooldown ограничен максимумом пяти минут.
- **GAB-PUB-502 — Cooldown status mode:** вызов без аргументов показывает текущее состояние.
- **GAB-PUB-503 — Cooldown disabled-state guidance:** отсутствие cooldown сопровождается инструкцией по созданию.
- **GAB-PUB-504 — Humanized cooldown duration:** длительность показывается в человекочитаемом виде.

### Active giveaway runtime

- **GAB-PUB-505 — Giveaway self-entry prohibition:** создатель не может участвовать в собственном giveaway.
- **GAB-PUB-506 — Join/enroll aliases:** участие доступно через несколько естественных алиасов.
- **GAB-PUB-507 — Duplicate-entry guard:** повторное участие не создаёт второй entry.
- **GAB-PUB-508 — Runtime participant count:** активный giveaway показывает актуальное число участников.
- **GAB-PUB-509 — Invalid creator resilience:** пропавший создатель отображается безопасным placeholder.
- **GAB-PUB-510 — Self-service giveaway leave via DM:** участник может выйти из giveaway через PM-команду.
- **GAB-PUB-511 — Active giveaway read-only default:** вызов без аргумента только показывает состояние и инструкции.

### Moderation

- **GAB-PUB-512 — Kick capability preflight:** до confirmation проверяются возможности бота и иерархия target.
- **GAB-PUB-513 — Kick resolved-identity confirmation:** confirmation показывает resolved display/custom name и member representation.
- **GAB-PUB-514 — Kick reason preview:** причина видна до выполнения действия.
- **GAB-PUB-515 — Kick DM before mutation:** уведомление target отправляется до kick.
- **GAB-PUB-516 — Kick DM failure isolation:** невозможность отправить DM не отменяет kick.
- **GAB-PUB-517 — Kick ModLog after mutation:** ModLog создаётся после успешного действия.
- **GAB-PUB-518 — Self-kick joke branch:** отсутствие target запускает отдельную интерактивную ветку.
- **GAB-PUB-519 — Mute duplicate-state guard:** повторный mute блокируется.
- **GAB-PUB-520 — Unmute missing-state guard:** unmute блокируется, если target не muted.
- **GAB-PUB-521 — Channel-scoped mute semantics:** mute/unmute привязаны к конкретному каналу.
- **GAB-PUB-522 — Moderation reason normalization:** пустая причина заменяется стандартной.
- **GAB-PUB-523 — Unban original-reason preview:** перед unban показывается исходная причина бана.
- **GAB-PUB-524 — Unban dual-reason audit:** отдельно отображаются историческая причина и новая причина unban.
- **GAB-PUB-525 — Unban actor-specific confirmation:** confirmation адресован инициатору.
- **GAB-PUB-526 — Unban extended confirmation window:** unban получает более длинное окно подтверждения.
- **GAB-PUB-527 — Unban cancellation neutrality:** отказ/таймаут подтверждения не меняет ban state.
- **GAB-PUB-528 — Live ban-list target lookup:** unban ищет target среди фактических банов guild.
- **GAB-PUB-529 — Flexible unban matching:** поддерживаются ID, tag, username и mention-like input.
- **GAB-PUB-530 — Unban ID-format guidance:** ошибка lookup подсказывает использовать ID.
- **GAB-PUB-531 — Split moderation hierarchy errors:** отдельно объясняются проблемы прав бота и иерархии модератора.

### Points

- **GAB-PUB-532 — Points self shortcut:** `points me` — отдельная self-service ветка.
- **GAB-PUB-533 — Points bot exclusion:** bot accounts исключены из points.
- **GAB-PUB-534 — Lazy user points record:** отсутствующий user document создаётся как нулевой.
- **GAB-PUB-535 — Top-ten points leaderboard:** без target показывается максимум 10 лидеров.
- **GAB-PUB-536 — Positive-points filtering:** leaderboard учитывает только points > 0.
- **GAB-PUB-537 — Points empty-state action hint:** пустое состояние объясняет, как получить points.

### Streamers

- **GAB-PUB-538 — Concurrent streamer checks:** статусы watchlist проверяются параллельно.
- **GAB-PUB-539 — Offline omission:** офлайн streamers не создают пустые карточки.
- **GAB-PUB-540 — Per-streamer visual metadata:** карточка содержит preview, platform, game и watch URL.
- **GAB-PUB-541 — Platform-specific styling:** YouTube и Twitch имеют разные визуальные признаки.
- **GAB-PUB-542 — Watchlist cardinality-aware empty state:** сообщение различается для одного и нескольких offline streamers.
- **GAB-PUB-543 — Dashboard setup guidance:** пустой watchlist объясняет, где его настроить.

### Tags

- **GAB-PUB-544 — Admin-controlled tag inventory visibility:** право полного списка tags является отдельной policy.
- **GAB-PUB-545 — Tag oversized-content externalization:** длинный tag content публикуется во внешнем Gist вместо обрезки.
- **GAB-PUB-546 — Tag URL escaping:** URL внутри tag listing экранируются angle brackets.
- **GAB-PUB-547 — Tag state badges:** inventory визуально различает locked и command tags.
- **GAB-PUB-548 — Combined command+lock state:** tag может одновременно иметь оба флага.
- **GAB-PUB-549 — Tag clear confirmation:** массовое удаление выполняется только после явного подтверждения.
- **GAB-PUB-550 — Tag defaults restore:** отдельная операция восстанавливает default tags.
- **GAB-PUB-551 — Tag destructive-action timeout:** clear/overwrite имеют ограниченное окно ответа.
- **GAB-PUB-552 — Tag prompt cleanup:** confirmation-ответ пользователя удаляется после обработки.
- **GAB-PUB-553 — Command-tag permission split:** права обычных и command tags регулируются отдельно.
- **GAB-PUB-554 — Locked-tag mutation block:** lock отдельно влияет на возможность изменения tag.
- **GAB-PUB-555 — Empty-value deletion shorthand:** пустое значение или `.` удаляет существующий tag.
- **GAB-PUB-556 — Case-normalized tag IDs:** идентификаторы tags приводятся к lowercase.

### Media / search

- **GAB-PUB-557 — Anime numeric result suffix:** последнее число запроса используется как количество результатов.
- **GAB-PUB-558 — Anime count policy fallback:** невалидный count нормализуется через server default/max policy.
- **GAB-PUB-559 — Anime selector-before-detail:** сначала список результатов, затем подробная карточка выбранного anime.
- **GAB-PUB-560 — Anime metadata-rich detail card:** карточка объединяет даты, эпизоды, рейтинг, возраст, synopsis и poster.
- **GAB-PUB-561 — App Store multi-query batching:** несколько app-запросов можно обработать одной командой.
- **GAB-PUB-562 — App Store per-query failure isolation:** ошибка одного приложения не отменяет остальные результаты.
- **GAB-PUB-563 — App Store compact summary:** используется первая строка длинного description.
- **GAB-PUB-564 — App Store free/paid normalization:** free и paid получают разные понятные состояния.
- **GAB-PUB-565 — GIF moderation-aware rating:** GIPHY rating зависит от NSFW policy канала/сервера.
- **GAB-PUB-566 — GIF result/error separation:** отсутствие результата и техническая ошибка разделены.
- **GAB-PUB-567 — Random-animal progress UX:** animal-команды сначала показывают состояние загрузки.
- **GAB-PUB-568 — Fact count follows shared server policy:** cat/dog facts используют общие default/max limits.
- **GAB-PUB-569 — Animal-fact pagination:** несколько фактов показываются через paginator.

### Counting

- **GAB-PUB-570 — Named-counter lazy creation:** несуществующий counter предлагает создать его.
- **GAB-PUB-571 — Counter creation timeout:** создание counter имеет минутное окно подтверждения.
- **GAB-PUB-572 — Counter increment/decrement aliases:** поддерживаются `+`, `+1`, `++`, `-`, `-1`, `--`.
- **GAB-PUB-573 — Counter non-negative floor:** counter не уходит ниже нуля.
- **GAB-PUB-574 — Counter termination shortcut:** `.` удаляет counter с показом последнего значения.
- **GAB-PUB-575 — Counter inventory pagination:** список counters разбивается на небольшие страницы.
- **GAB-PUB-576 — Counter name normalization:** имена counters нормализуются в lowercase.
- **GAB-PUB-577 — Counter creation as tutorial:** после создания сразу показываются команды изменения и остановки.

### Archive / utility

- **GAB-PUB-578 — Archive hard ceiling:** archive ограничивает выгрузку максимумом 100 сообщений.
- **GAB-PUB-579 — Archive message anchor:** ID позволяет архивировать сообщения относительно конкретной точки `before`.
- **GAB-PUB-580 — Structured archive preservation:** JSON сохраняет author, IDs, content, embeds, attachments и timestamps.
- **GAB-PUB-581 — Edited timestamp preservation:** edited messages сохраняют отдельный editedAt.
- **GAB-PUB-582 — Archive guild/channel metadata:** экспорт включает names/IDs сервера и канала и время архивации.
- **GAB-PUB-583 — Archive as generated attachment:** результат отправляется готовым JSON-файлом.
- **GAB-PUB-584 — Archive permission-specific guidance:** ошибки history сопровождаются подсказками по permissions/ID.
- **GAB-PUB-585 — Conversion syntax normalization:** формы с `to` и без `to` приводятся к единому внутреннему формату.
- **GAB-PUB-586 — Conversion type-specific output:** money и units имеют разные шаблоны вывода.
- **GAB-PUB-587 — Conversion error taxonomy:** ошибки unit conversion и общие ошибки разделяются.
- **GAB-PUB-588 — Redirect-chain safety report:** URL expansion показывает всю redirect chain и unsafe причины.
- **GAB-PUB-589 — Redirect aggregate safety color:** итоговый цвет зависит от общей safe/unsafe оценки цепочки.
- **GAB-PUB-590 — Redirect reason humanization:** технические safety codes переводятся в понятные категории.
