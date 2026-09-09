# GAwesomeBot — Commands/Public — batch 8

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Продолжение полного обхода `Commands/Public/`. Только дополнительные детали поведения/UX/ограничений, не являющиеся точными повторами уже зафиксированных идей.

## Count / counters

- **GAB-PUB-591 — Counter creation confirmation:** неизвестный counter не создаётся молча; сначала запрашивается подтверждение.
- **GAB-PUB-592 — Counter creation timeout:** создание counter имеет отдельное окно ожидания ответа.
- **GAB-PUB-593 — Counter creation prompt replacement:** после подтверждения первоначальный prompt превращается в success-state вместо отправки нового сообщения.
- **GAB-PUB-594 — Counter action aliases:** увеличение и уменьшение поддерживают несколько коротких операторов (`+`, `+1`, `++`, `-`, `-1`, `--`).
- **GAB-PUB-595 — Counter delete operator:** специальный оператор `.` удаляет именованный counter.
- **GAB-PUB-596 — Counter non-negative floor:** уменьшение запрещено, когда значение уже равно нулю.
- **GAB-PUB-597 — Counter case-insensitive identity:** имя counter нормализуется к lower-case при обращении.
- **GAB-PUB-598 — Counter inventory alphabetical order:** список counters сортируется по имени перед pagination.
- **GAB-PUB-599 — Counter inventory pagination by ten:** counters выводятся блоками по десять элементов.
- **GAB-PUB-600 — Counter final-value disclosure:** при удалении показывается последнее значение удалённого counter.

## Help / command discovery

- **GAB-PUB-601 — Help command-type aggregation:** поиск конкретной команды одновременно проверяет PM, Public и Shared metadata.
- **GAB-PUB-602 — Help extension lookup:** extension-команда добавляется в результат поиска как отдельный command type.
- **GAB-PUB-603 — Help extension version metadata:** описание extension берётся из конкретной активной version document.
- **GAB-PUB-604 — Help disabled-channel filtering:** команда, отключённая именно в текущем канале, не попадает в общий help.
- **GAB-PUB-605 — Help admin-level filtering:** пользователь видит только команды, доступные его текущему Bot Admin level.
- **GAB-PUB-606 — Help category placeholders:** полностью пустая категория получает явный `No Commands Enabled Here` state.
- **GAB-PUB-607 — Help dynamic alignment:** usage/command list визуально выравнивается по длине самого длинного command key.
- **GAB-PUB-608 — Help category reaction navigation:** категории представлены отдельными emoji-кнопками, а не одним огромным embed.
- **GAB-PUB-609 — Help conditional extension page:** страница Extensions появляется только если реально есть доступные extensions.
- **GAB-PUB-610 — Help long interaction lifetime:** интерактивное help menu живёт несколько минут вместо мгновенного завершения.
- **GAB-PUB-611 — Help explicit exit control:** интерактивное меню имеет отдельный exit control.

## Archive

- **GAB-PUB-612 — Archive message-count hard cap:** запрос архива ограничивается максимумом 100 сообщений.
- **GAB-PUB-613 — Archive explicit cursor support:** пользователь может передать message ID как `before` cursor вместо использования последнего сообщения канала.
- **GAB-PUB-614 — Archive permission-specific fetch diagnosis:** ошибка fetch связывается с отсутствием Read Message History либо некорректным cursor.
- **GAB-PUB-615 — Archive message ID preservation:** каждая экспортированная запись сохраняет исходный Discord message ID.
- **GAB-PUB-616 — Archive edited-at preservation:** дата последнего редактирования сохраняется отдельно от исходного createdAt.
- **GAB-PUB-617 — Archive embed author snapshot:** автор embed внутри сообщения сериализуется отдельным вложенным объектом.
- **GAB-PUB-618 — Archive embed field preservation:** поля embed экспортируются без потери структуры.
- **GAB-PUB-619 — Archive embed footer preservation:** footer text/icon URL сохраняются отдельно.
- **GAB-PUB-620 — Archive embed media preservation:** image и thumbnail URLs сохраняются как отдельные свойства.
- **GAB-PUB-621 — Archive embed timestamp/type preservation:** timestamp и type каждого embed экспортируются явно.
- **GAB-PUB-622 — Archive archive metadata envelope:** JSON содержит server/channel identity и число архивированных сообщений на верхнем уровне.
- **GAB-PUB-623 — Archive deterministic JSON formatting:** JSON экспортируется с indentation для удобного ручного чтения.
- **GAB-PUB-624 — Archive descriptive filename:** имя файла содержит server, channel и timestamp создания архива.
- **GAB-PUB-625 — Archive send-failure isolation:** ошибка отправки готового файла превращается в отдельный user-facing error.

## Imgur upload

- **GAB-PUB-626 — Imgur attachment ingestion:** команда умеет брать Discord attachments напрямую, без обязательного URL в тексте.
- **GAB-PUB-627 — Imgur mixed input upload:** attachments и URL из одного сообщения объединяются в единый upload batch.
- **GAB-PUB-628 — Imgur multi-image album mode:** два и более файла автоматически объединяются в один Imgur album.
- **GAB-PUB-629 — Imgur sequential album uploads:** элементы album загружаются последовательно после создания album/deletehash.
- **GAB-PUB-630 — Imgur single-image direct mode:** один файл загружается без создания лишнего album.
- **GAB-PUB-631 — Imgur server-level client override:** сервер может использовать собственный Imgur client ID вместо глобального.
- **GAB-PUB-632 — Imgur maintainer credit inspection:** специальная служебная ветка показывает API credit information только maintainer.
- **GAB-PUB-633 — Imgur 10MB file guard:** размер одного upload ограничен 10 MB с отдельным понятным сообщением.
- **GAB-PUB-634 — Imgur invalid-file-type state:** неподдерживаемый тип файла имеет отдельный error branch.
- **GAB-PUB-635 — Imgur rate-limit guidance:** 403/429 приводят к rate-limit сообщению и рекомендации использовать custom client ID.
- **GAB-PUB-636 — Imgur internal-error state:** HTTP 500 отделён от generic unknown error.
- **GAB-PUB-637 — Imgur output prefers GIFV:** если upload возвращает GIFV URL, он предпочитается обычной ссылке.
- **GAB-PUB-638 — Imgur batch link presentation:** multi-upload показывает индивидуальные ссылки и отдельную album-ссылку.

## RSS / feeds

- **GAB-PUB-639 — RSS named-feed alias resolution:** сохранённый RSS feed можно вызвать по локальному имени вместо URL.
- **GAB-PUB-640 — RSS raw-URL fallback:** если имя не найдено, аргумент трактуется непосредственно как feed URL.
- **GAB-PUB-641 — RSS configurable result count:** число статей проходит через server default/max fetch limits.
- **GAB-PUB-642 — RSS long-lived paginator:** RSS paginator имеет значительно более длинное время жизни, чем обычный короткий reaction menu.
- **GAB-PUB-643 — RSS article publication formatting:** дата публикации форматируется как локализованный day/month/year + time + offset.
- **GAB-PUB-644 — RSS article direct-link field:** каждая карточка имеет прямой article URL как navigation target.
- **GAB-PUB-645 — RSS feed inventory mode:** вызов без аргумента показывает доступные server-defined feed aliases.
- **GAB-PUB-646 — RSS no-feed setup guidance:** пустой inventory направляет администратора в отдельный RSS Feeds раздел Admin Console.
- **GAB-PUB-647 — RSS fetch-error isolation:** ошибка чтения одного feed не превращается в необработанное исключение команды.

## Safebooru / NSFW gate

- **GAB-PUB-648 — NSFW command hard channel gate:** Safebooru доступен только в Discord NSFW channel.
- **GAB-PUB-649 — NSFW standard rejection embed:** вне NSFW channel используется единый NSFWEmbed вместо обычной usage-ошибки.
- **GAB-PUB-650 — Safebooru query-count parsing:** последнее числовое значение может задавать количество результатов.
- **GAB-PUB-651 — Safebooru alternate separator syntax:** query допускает `|` как separator наравне с пробелом.
- **GAB-PUB-652 — Safebooru result metadata bundle:** каждая карточка содержит uploader, tags, score и rating.
- **GAB-PUB-653 — Safebooru tag-length clipping:** очень длинный tag string обрезается до Discord field limit.
- **GAB-PUB-654 — Safebooru markup sanitization:** BBCode-like `[b]`, `[u]`, `[i]` markup удаляется из description перед выводом.
- **GAB-PUB-655 — Safebooru progress-message replacement:** progress-сообщение удаляется после успешного fetch перед запуском paginator.

## Strikes / moderation history

- **GAB-PUB-656 — Strike self-default:** без target или с `me` команда показывает strikes текущего пользователя.
- **GAB-PUB-657 — Strike lazy member-record creation:** отсутствие member document не мешает просмотру; создаётся пустая запись.
- **GAB-PUB-658 — Strike moderator snapshot resolution:** moderator ID разрешается в актуальное guild display name при просмотре истории.
- **GAB-PUB-659 — Strike relative-date presentation:** timestamp strike показывается как relative time (`fromNow`).
- **GAB-PUB-660 — Strike linked ModLog reference:** запись истории сохраняет ссылку на соответствующий ModLog entry либо явное `None`.
- **GAB-PUB-661 — Strike reverse chronological presentation:** история strikes разворачивается так, чтобы последние записи показывались первыми.
- **GAB-PUB-662 — Strike per-entry pagination:** каждый strike может занимать отдельную страницу paginator.
- **GAB-PUB-663 — Strike empty-state confirmation:** отсутствие strikes выводится как положительный clean-state, а не ошибка.

## Role information presentation

- **GAB-PUB-664 — Role inventory inline truncation markers:** страницы role inventory явно показывают, сколько ролей осталось до/после текущего сегмента.
- **GAB-PUB-665 — Role/member sections share page-size logic:** guild role inventory и собственные member roles используют одинаковый размер страницы 25.
- **GAB-PUB-666 — Role list plus effective-permission companion page:** при отсутствии аргумента команда показывает не только роли guild, но и собственные effective permissions пользователя.
- **GAB-PUB-667 — Role compact two-page optimization:** если полный role list и member-role block помещаются вместе в Discord limit, paginator не создаётся.
- **GAB-PUB-668 — Role creation-relative timestamp:** конкретная role card показывает возраст роли через relative timestamp.
- **GAB-PUB-669 — Role position computed against guild size:** position отображается как вычисляемый ordinal относительно общего количества roles.
- **GAB-PUB-670 — Role permission humanization:** raw permission flags преобразуются в человекочитаемые названия.

## Final Public coverage notes

- **GAB-PUB-671 — Public source tree cross-check:** после обхода все файлы `Commands/Public/` сверяются с recursive tree, чтобы не пропустить файл, не попавший в предыдущие батчи.
- **GAB-PUB-672 — Public duplicate cross-check:** перед закрытием каталога новые механики сверяются не только с последним батчем, но со всем диапазоном GAB-PUB-001–670.
