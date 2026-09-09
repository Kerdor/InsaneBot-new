# GAwesomeBot — Commands/Public — batch 5

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Продолжение `GAWESOME_COMMANDS_PUBLIC_BATCH4.md`. Добавлены только детали, которые не являются точными повторами уже зафиксированных механик.

## Command framework

- **GAB-PUB-386 — Public command base contract:** базовый шаблон Public-команд документирует стандартный вход `main/documents/msg/commandData` и доступные server/channel/member/user documents; это полезно как единый контракт для расширений.

## Server moderation / safety

- **GAB-PUB-387 — Kick confirmation timeout:** destructive kick ждёт подтверждение инициатора до 60 секунд; отсутствие/неподходящий ответ отменяет действие.
- **GAB-PUB-388 — Kick target DM notification:** после подтверждённого kick бот пытается отдельно уведомить исключённого пользователя о сервере, причине и модераторе.
- **GAB-PUB-389 — Kick notification failure isolation:** невозможность отправить DM не отменяет сам kick.
- **GAB-PUB-390 — Kick ModLog coupling:** успешный kick автоматически создаёт ModLog case с target, moderator и reason.
- **GAB-PUB-391 — Unban two-minute confirmation window:** unban использует более длинное окно подтверждения — до 120 секунд.
- **GAB-PUB-392 — Unban no-auto-notify policy:** после unban бот явно не пытается автоматически писать пользователю; уведомление не является обязательной частью операции.
- **GAB-PUB-393 — ModLog command capability disclosure:** команда status без аргументов перечисляет связанные moderation-команды, доступные через ModLog.
- **GAB-PUB-394 — ModLog state-aware enable/disable:** enable/disable сначала проверяет текущее состояние и не выполняет бессмысленную повторную операцию.
- **GAB-PUB-395 — ModLog explicit channel targeting:** включение moderation logging требует явного channel argument и отдельно проверяет существование найденного канала.

## Server statistics

- **GAB-PUB-396 — Weekly stats reset protection:** очистка серверной статистики требует отдельного подтверждения и предупреждает, что действие необратимо.
- **GAB-PUB-397 — Stats reset permission gate:** сброс weekly guild statistics доступен только Bot Admin с достаточным admin level.
- **GAB-PUB-398 — Aggregate activity score:** weekly stats объединяет сообщения и voice activity в единый activity score через отдельный calculator.
- **GAB-PUB-399 — Top-five activity members:** aggregate server stats ограничивает список самых активных участников пятью позициями.
- **GAB-PUB-400 — Top-five played games:** статистика сервера отдельно ранжирует игры по накопленному времени и показывает top 5.
- **GAB-PUB-401 — Top-five command usage:** weekly stats показывает пять наиболее используемых bot-команд.
- **GAB-PUB-402 — Richest-member stats slice:** weekly stats дополнительно показывает до пяти участников с ненулевыми GAwesomePoints.
- **GAB-PUB-403 — Dead-server stat empty states:** каждый статистический блок имеет собственное понятное empty-state сообщение вместо пустого embed.

## Streamer tracking

- **GAB-PUB-404 — Dashboard-backed streamer watchlist:** список отслеживаемых streamers хранится в server configuration и управляется через dashboard.
- **GAB-PUB-405 — Live-only streamer output:** команда показывает только реально live streamers; офлайн-записи не создают пустые карточки.
- **GAB-PUB-406 — Mixed-platform streamer cards:** Twitch и YouTube streamer results используют разные brand colors при общем формате карточки.
- **GAB-PUB-407 — Stream preview thumbnail:** live-карточка содержит preview image текущего стрима.
- **GAB-PUB-408 — Stream game context:** live-карточка одновременно показывает имя стримера и текущую игру.
- **GAB-PUB-409 — Streamer-specific empty state:** если watchlist существует, но никто не live, сообщение различает один отслеживаемый аккаунт и несколько.
- **GAB-PUB-410 — Streamer inventory empty state:** отсутствие watchlist объясняется отдельно и подсказывает администратору dashboard-настройку.

## Tags / server snippets

- **GAB-PUB-411 — Tag lock flag:** отдельный tag может быть locked, после чего обычное обновление/удаление ограничивается permission policy.
- **GAB-PUB-412 — Command-tag mode:** tag может быть помечен как command и иметь отдельные права создания/удаления.
- **GAB-PUB-413 — Separate tag permission policies:** создание, удаление, обновление, command-tags и полный список могут иметь независимые admin-only настройки.
- **GAB-PUB-414 — Locked command tag distinction:** permission check различает обычный locked tag и locked command tag.
- **GAB-PUB-415 — Tag overwrite confirmation:** изменение существующего tag требует явного подтверждения вместо молчательной перезаписи.
- **GAB-PUB-416 — Tag bulk clear confirmation:** удаление всех tags требует отдельного подтверждения с минутным timeout.
- **GAB-PUB-417 — Tag defaults restore:** сервер может полностью загрузить predefined default tag set одной операцией.
- **GAB-PUB-418 — Large tag externalization:** контент tag длиннее Discord-safe размера автоматически выносится во внешний Gist и в списке показывается ссылка.
- **GAB-PUB-419 — Tag URL escaping:** ссылки внутри tag content оборачиваются в angle brackets, чтобы Discord не создавал нежелательные rich previews.
- **GAB-PUB-420 — Tag inventory pagination:** список tags разбивается по 10 элементов на интерактивные страницы.
- **GAB-PUB-421 — Tag state badges:** inventory визуально маркирует locked и command tags отдельными badges.
- **GAB-PUB-422 — Tag missing-create guidance:** запрос несуществующего tag возвращает пример синтаксиса для его создания.
- **GAB-PUB-423 — Tag deletion shortcut:** пустой content или `.` трактуются как запрос удаления существующего tag.

## Room management

- **GAB-PUB-424 — Room delete-or-membership decision flow:** команда для существующей talk-room сначала предлагает удалить комнату, а при отказе переходит к вопросу о добавлении участников.
- **GAB-PUB-425 — Room multi-member permission grant:** несколько пользователей можно добавить в room одним ответом с разделителем `|`; каждому выдаётся VIEW_CHANNEL overwrite.
- **GAB-PUB-426 — Room partial member resolution:** не найденные участники не блокируют добавление остальных; их имена собираются отдельно для итогового предупреждения.
- **GAB-PUB-427 — Room auto-category creation:** если служебная категория talk rooms отсутствует или удалена, команда создаёт её заново и сохраняет новый ID.
- **GAB-PUB-428 — Room hidden-from-everyone model:** создаваемая room по умолчанию скрыта от `@everyone` и явно открывается создателю/выбранным участникам.
- **GAB-PUB-429 — Room creator ownership via overwrite:** создатель получает собственный VIEW_CHANNEL overwrite при создании комнаты.
- **GAB-PUB-430 — Voice-room auto-cleanup expectation:** voice talk-room объявляется как временный и должен удаляться после выхода всех участников.
- **GAB-PUB-431 — Room creation type switch:** одна команда поддерживает создание как text, так и voice room через первый argument.
- **GAB-PUB-432 — Room age-aware deletion prompt:** перед удалением существующей комнаты пользователю показывается, сколько она существует.

## Trivia / game state

- **GAB-PUB-433 — Trivia start with named set:** запуск trivia может выбрать конкретный question set вместо default.
- **GAB-PUB-434 — Trivia skip/next control:** текущий вопрос можно пропустить отдельным action без завершения всей игры.
- **GAB-PUB-435 — Trivia end alias:** завершение игры доступно как `end` и коротким `.`.
- **GAB-PUB-436 — Trivia progress inspection:** вызов команды без action во время игры показывает число завершённых вопросов и текущий score.
- **GAB-PUB-437 — Trivia active-set disclosure:** если используется не-default set, его имя показывается вместе с текущим прогрессом.
- **GAB-PUB-438 — Trivia inactive-state guidance:** вызов trivia вне активной игры объясняет, как начать новую через `start`.

## Time / utility

- **GAB-PUB-439 — Timezone database validation:** `time <timezone>` проверяется непосредственно по timezone database; неизвестная зона отклоняется до форматирования времени.
- **GAB-PUB-440 — Time current-local fallback:** отсутствие аргумента возвращает текущее время самого процесса и одновременно подсказывает формат timezone lookup.

## Translation / external lookup

- **GAB-PUB-441 — Translation dual syntax:** перевод поддерживает как `<source> to <target> <text>`, так и более короткий `<source> <target> <text>` синтаксис.
- **GAB-PUB-442 — Translation explicit uncertainty disclosure:** результат сопровождается предупреждением, что машинный перевод может быть неточным.
- **GAB-PUB-443 — Translation detection failure separation:** ошибка автоопределения языка имеет отдельный user-facing текст, отличающий её от ошибки самого перевода.

## Search / media

- **GAB-PUB-444 — Twitter empty-result explanation:** отсутствие публичных твитов объясняется отдельно от технической ошибки и связывается с несуществующим/закрытым аккаунтом.
- **GAB-PUB-445 — Twitter RSS pagination metadata:** tweet cards используют creator, timestamp, content snippet и permalink как отдельные структурированные поля.
- **GAB-PUB-446 — YouTube hard result ceiling:** даже если серверный max_count выше, YouTube command дополнительно ограничивает один запрос десятью результатами.
- **GAB-PUB-447 — YouTube missing-snippet filtering:** элементы API без snippet не превращаются в неполные карточки.
- **GAB-PUB-448 — XKCD requested-vs-latest labeling:** footer различает явно запрошенный comic ID и latest comic режим.
- **GAB-PUB-449 — XKCD publication timestamp:** карточка комикса использует дату публикации как Discord timestamp.

## URL utility

- **GAB-PUB-450 — Bitly reverse-operation support:** shorten-команда умеет не только сокращать обычные URL, но и раскрывать уже существующие bit.ly ссылки.
- **GAB-PUB-451 — Bitly unregistered-link state:** несуществующая/не зарегистрированная bit.ly ссылка получает отдельное состояние вместо общего API error.
- **GAB-PUB-452 — Shortener capability gate:** отсутствие Bitly token превращает URL-shortening в явно отключённую функцию с понятным объяснением.
