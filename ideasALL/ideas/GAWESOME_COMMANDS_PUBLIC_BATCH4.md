# GAwesomeBot — Commands/Public — batch 4

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Продолжение `GAWESOME_COMMANDS_PUBLIC_BATCH3.md`. Механики подтверждены просмотром исходников.

## Animal / media commands

- **GAB-PUB-287 — Cat image progress UX:** получение случайной картинки начинается с отдельного progress-сообщения.
- **GAB-PUB-288 — Cat fetch failure recovery:** ошибка внешнего источника превращается в отдельный friendly error, а не в необработанное исключение.
- **GAB-PUB-289 — Dog image progress UX:** dog-команда использует тот же двухэтапный fetch → result паттерн.
- **GAB-PUB-290 — Cat fact configurable count:** количество cat facts определяется suffix и ограничивается серверными default/max limits.
- **GAB-PUB-291 — Cat fact pagination:** несколько фактов показываются через интерактивные страницы.
- **GAB-PUB-292 — Dog fact configurable count:** dog facts используют серверные default/max limits для количества результатов.
- **GAB-PUB-293 — Dog fact pagination:** несколько dog facts выдаются через PaginatedEmbed.
- **GAB-PUB-294 — Emoji jumbo worker isolation:** генерация jumbo-emoji выполняется через отдельный worker вместо блокировки основного процесса.
- **GAB-PUB-295 — Emoji animated-format detection:** итоговый jumbo-файл автоматически выбирает GIF для animated emoji и PNG для static.
- **GAB-PUB-296 — Emoji multi-input normalization:** переносы строк заменяются пробелами, а emoji извлекаются как набор аргументов.
- **GAB-PUB-297 — Emoji processing progress replacement:** временное сообщение о генерации удаляется перед публикацией готового результата.
- **GAB-PUB-298 — Emoji animation caveat disclosure:** animated jumbo сопровождается предупреждением о framerate и возможном обрезании отдельных emoji.

## Custom emoji inspection

- **GAB-PUB-299 — Emotes server inventory mode:** команда без аргумента показывает все custom emoji текущего сервера.
- **GAB-PUB-300 — Emotes static/animated separation:** inventory разделяется на static и animated группы.
- **GAB-PUB-301 — Emotes custom-only validation:** unicode emoji явно отделяются от custom emoji и получают специальное объяснение.
- **GAB-PUB-302 — Emotes raw-ID fallback:** даже неизвестный глобальный emoji можно запросить по raw ID.
- **GAB-PUB-303 — Emotes global lookup:** custom emoji ищется глобально, поэтому команда может показать emoji из другого сервера.
- **GAB-PUB-304 — Emotes creator metadata:** карточка emoji пытается показать создателя и имеет fallback на Unknown User.
- **GAB-PUB-305 — Emotes integration flag:** managed-by-integration состояние показывается отдельно.
- **GAB-PUB-306 — Emotes usage-role inspection:** карточка показывает роли, которым разрешено использовать emoji; отсутствие ограничений означает Everyone.
- **GAB-PUB-307 — Emotes animated-state disclosure:** animated/static состояние явно показывается в карточке.
- **GAB-PUB-308 — Emotes creation timestamp:** карточка содержит timestamp создания emoji.

## Fun / discovery

- **GAB-PUB-309 — Fortune typo tolerance:** близко написанная категория fortune может быть автоматически распознана через Levenshtein distance.
- **GAB-PUB-310 — Fortune category menu on invalid input:** неправильная категория возвращает список допустимых вариантов прямо в ответе.
- **GAB-PUB-311 — Fortune fetch progress:** fortune использует отдельную стадию подготовки до внешнего запроса.
- **GAB-PUB-312 — Joke progress UX:** joke-команда сначала показывает состояние загрузки, затем результат.
- **GAB-PUB-313 — Joke external-error logging:** ошибка внешнего API записывается в debug log с guild context.
- **GAB-PUB-314 — Number fact random default:** отсутствие числа означает запрос случайного факта, а не ошибку usage.
- **GAB-PUB-315 — Number fact early numeric validation:** явно заданный нечисловой аргумент отбрасывается до вызова API.
- **GAB-PUB-316 — Year countdown dual-format:** countdown до нового года одновременно показывает точные дни/часы/минуты/секунды и humanized duration.
- **GAB-PUB-317 — Year target normalization:** цель countdown всегда вычисляется как полночь 1 января следующего года.

## Help / discoverability

- **GAB-PUB-318 — Help command metadata lookup:** help <command> собирает сведения отдельно из PM, Public и Shared namespaces.
- **GAB-PUB-319 — Help extension lookup:** установленные command extensions также участвуют в поиске справки.
- **GAB-PUB-320 — Help unknown-command branch:** неизвестная команда получает отдельное сообщение вместо пустой справки.
- **GAB-PUB-321 — Help permission-filtered command list:** общий список показывает только команды, которые пользователь реально может запускать в текущем канале.
- **GAB-PUB-322 — Help disabled-channel filtering:** команды, отключённые именно в текущем канале, исключаются из help.
- **GAB-PUB-323 — Help extension permission filtering:** extension-команды фильтруются по собственному admin level пользователя.
- **GAB-PUB-324 — Help category grouping:** команды группируются по категориям, а категории получают собственные emoji-кнопки.
- **GAB-PUB-325 — Help command alignment:** usage-строки выравниваются по длине самого длинного command key для читаемого списка.
- **GAB-PUB-326 — Help empty-category state:** категория без доступных команд явно показывает No Commands Enabled Here.
- **GAB-PUB-327 — Help extension conditional page:** страница Extensions показывается только при наличии доступных extensions.
- **GAB-PUB-328 — Help long-lived reaction menu:** help menu живёт значительно дольше обычного временного интерактивного сообщения.

## Server information / observability

- **GAB-PUB-329 — Info server creation timestamp:** server info показывает точную дату создания guild.
- **GAB-PUB-330 — Info voice-region metadata:** текущий voice region отображается с human-readable названием и региональным флагом.
- **GAB-PUB-331 — Info deprecated-region warning:** устаревший voice region явно помечается как DEPRECATED.
- **GAB-PUB-332 — Info verification-level display:** verification level входит в отдельный блок server metadata.
- **GAB-PUB-333 — Info channel-type breakdown:** отдельно считаются text, voice и category channels.
- **GAB-PUB-334 — Info online-member count:** общий member count сопровождается числом currently-online участников.
- **GAB-PUB-335 — Info operational counters:** карточка показывает сообщения сегодня и использование команд за неделю.
- **GAB-PUB-336 — Info feature capability detection:** специальные Discord guild features перечисляются только при их наличии.
- **GAB-PUB-337 — Info owner identity:** серверная карточка содержит владельца и его avatar.
- **GAB-PUB-338 — Info public-discovery disclosure:** если сервер опубликован через activity listing, карточка сообщает об этом и даёт invite URL.
- **GAB-PUB-339 — Info shard disclosure:** server info показывает shard, обслуживающий guild.

## Lists / personal activity

- **GAB-PUB-340 — Todo numeric ID addressing:** каждый todo item получает отдельный числовой ID для последующего управления.
- **GAB-PUB-341 — Todo ID collision avoidance:** генератор ID проверяет существование кандидата и увеличивает offset при конфликте.
- **GAB-PUB-342 — Todo completion toggle:** `done/complete` не только устанавливает статус, а переключает completed ↔ incomplete.
- **GAB-PUB-343 — Todo inline edit:** действие над существующим ID без специального keyword заменяет content элемента.
- **GAB-PUB-344 — Todo post-mutation full refresh:** после добавления/удаления/изменения бот снова показывает актуальный список.
- **GAB-PUB-345 — Todo empty-state guidance:** пустой список сразу объясняет синтаксис добавления нового item.
- **GAB-PUB-346 — Messages self shortcut:** специальный `me` показывает личную статистику сообщений без member search.
- **GAB-PUB-347 — Messages bot exclusion:** статистика сообщений не применяется к bot members.
- **GAB-PUB-348 — Messages top-eight ranking:** общий список активности ограничивается восемью наиболее активными участниками.
- **GAB-PUB-349 — Messages total footer:** leaderboard одновременно показывает общее число сообщений и число активных участников.
- **GAB-PUB-350 — Reminders bounded display:** даже при большом числе reminders в embed выводятся максимум 25 записей.

## Poll / countdown / quiet state

- **GAB-PUB-351 — Poll duplicate-vote protection:** участник не может повторно проголосовать, пока не удалит существующий vote.
- **GAB-PUB-352 — Poll vote-by-number-or-name:** голос можно отдать как номером варианта, так и его точным текстом без учёта регистра.
- **GAB-PUB-353 — Poll result percentages:** результаты показывают и абсолютное число голосов, и процент.
- **GAB-PUB-354 — Poll winner footer:** текущий лидер выводится отдельно вместе с общим числом голосов.
- **GAB-PUB-355 — Poll result pagination:** большое количество вариантов разбивается на страницы по 10.
- **GAB-PUB-356 — Countdown duplicate-event guard:** повторное создание countdown с тем же ID не создаёт вторую запись.
- **GAB-PUB-357 — Countdown channel ownership:** countdown хранит канал, в котором был создан, и показывает его в общем списке.
- **GAB-PUB-358 — Countdown expiry ordering:** общий список countdown сортируется по ближайшему времени завершения.
- **GAB-PUB-359 — Countdown stale-channel filtering:** countdown для уже исчезнувшего канала не показывается в списке.
- **GAB-PUB-360 — Quiet all-channel switch:** специальный `all` отключает bot_enabled сразу во всех каналах сервера.
- **GAB-PUB-361 — Quiet timed auto-restore:** timed quiet автоматически включает bot_enabled обратно после истечения duration.
- **GAB-PUB-362 — Quiet duration hard cap:** временный quiet ограничен максимум одним часом.
- **GAB-PUB-363 — Quiet indefinite fallback:** отсутствие валидной duration означает бессрочный quiet текущего канала.

## Moderation / safety

- **GAB-PUB-364 — Nuke exact-text filter:** без специального префикса поиск сообщений использует exact case-insensitive text match.
- **GAB-PUB-365 — Nuke substring filter:** префикс `:` переключает фильтр на substring search по содержимому.
- **GAB-PUB-366 — Nuke author filter:** mention target позволяет удалить сообщения конкретного участника.
- **GAB-PUB-367 — Nuke before/after boundaries:** специальные `>` и `<` позволяют ограничивать выборку сообщениями относительно ID.
- **GAB-PUB-368 — Nuke absolute deletion cap:** одна операция ограничена максимум 100 сообщениями.
- **GAB-PUB-369 — Nuke result slicing after fetch:** сначала выбирается bounded history, затем результат дополнительно обрезается до запрошенного количества.
- **GAB-PUB-370 — Unban original-reason preview:** перед подтверждением unban показывается первоначальная причина бана.
- **GAB-PUB-371 — Unban actor confirmation:** destructive действие требует явного ответа самого инициатора команды.
- **GAB-PUB-372 — Unmute muted-state guard:** снятие mute запрещено, если target уже не находится в muted state.
- **GAB-PUB-373 — Unmute dual hierarchy check:** одновременно проверяется возможность действия ботом и положение target относительно модератора.

## Technical / response UX

- **GAB-PUB-374 — Ping send-time measurement:** ping-команда измеряет фактическое время отправки собственного сообщения отдельно от websocket heartbeat.
- **GAB-PUB-375 — Ping shard context:** latency response дополнена номером shard.
- **GAB-PUB-376 — Weather optional-field rendering:** clouds/rain/snow/wind добавляются в карточку только если соответствующие данные присутствуют.
- **GAB-PUB-377 — Weather API capability gate:** отсутствие OpenWeather token превращает команду в явно недоступную функцию.
- **GAB-PUB-378 — Weather normalized description:** описание погоды нормализуется в Title Case перед отображением.
- **GAB-PUB-379 — XKCD alt-image fallback:** если основной comic image отсутствует, используется alternate field как fallback.
- **GAB-PUB-380 — YouTube heterogeneous result URLs:** один search может сформировать разные URL для video, playlist и channel.
- **GAB-PUB-381 — Twitter default result count:** если count не распознан, используется серверный default count.
- **GAB-PUB-382 — Twitter leading-at normalization:** username с `@` и без `@` приводятся к одному виду.
- **GAB-PUB-383 — Translate auto-detection pipeline:** auto-detect реализован как отдельный detect → translate этап, а не специальный тип результата.
- **GAB-PUB-384 — Shorten dual-purpose input:** одна команда различает обычный long URL и уже сокращённый Bitly URL по входу.
- **GAB-PUB-385 — Shorten API failure isolation:** ошибка Bitly API возвращается как friendly embed, не раскрывая внутреннюю ошибку пользователю.

## Текущая граница

Добавлен батч **GAB-PUB-287–GAB-PUB-385**. `Commands/Public/` ещё не закрыт: остаются Public-файлы, которые нужно досмотреть и затем провести финальную сверку каталога. После полного закрытия Public только тогда переходить к `Commands/Shared/`.
