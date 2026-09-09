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
