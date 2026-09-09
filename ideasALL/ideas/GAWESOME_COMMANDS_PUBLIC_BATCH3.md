# GAwesomeBot — Commands/Public — batch 3

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Продолжение `GAWESOME_COMMANDS_PUBLIC.md` и `GAWESOME_COMMANDS_PUBLIC_BATCH2.md`. Механики подтверждены просмотром исходников. Фиксируются только отличающиеся UX/поведение/ограничения.

## Room management

- **GAB-PUB-206 — Room lifecycle prompt:** команда для уже существующей talk-room сначала предлагает удалить комнату, а не выполняет удаление сразу.
- **GAB-PUB-207 — Room deletion timeout:** подтверждение удаления комнаты ограничено одной минутой.
- **GAB-PUB-208 — Room deletion state cleanup:** запись комнаты удаляется из persistent state только после успешного удаления Discord-канала.
- **GAB-PUB-209 — Room deletion failure preservation:** при неудачном удалении канал остаётся зарегистрированным, а prompt превращается в сообщение об ошибке.
- **GAB-PUB-210 — Room member-add follow-up:** отказ от удаления существующей комнаты запускает второй вопрос — нужно ли добавить участников.
- **GAB-PUB-211 — Room member batch invite:** участников можно передать пачкой через `|` или quoted-аргументы.
- **GAB-PUB-212 — Room partial member failure:** не найденные участники не ломают добавление остальных; их имена собираются в отдельный warning.
- **GAB-PUB-213 — Room lazy category creation:** если категория talk rooms отсутствует или устарела, она создаётся автоматически.
- **GAB-PUB-214 — Room private-by-default permissions:** новая talk-room закрыта для `@everyone`, а создателю и выбранным участникам выдаётся `VIEW_CHANNEL`.
- **GAB-PUB-215 — Room type selection:** создание комнаты поддерживает отдельные text и voice варианты.
- **GAB-PUB-216 — Voice room auto-cleanup disclosure:** при создании voice-room пользователь явно уведомляется об автоматическом удалении после выхода всех участников.
- **GAB-PUB-217 — Room state registration:** созданная комната сохраняет собственный channel ID в server state для дальнейшего управления.

## Links / external utilities

- **GAB-PUB-218 — Shorten capability gate:** команда сокращения ссылок заранее отключается, если Bitly token отсутствует, вместо выполнения заведомо неработающего запроса.
- **GAB-PUB-219 — Shorten doubles as Bitly expander:** если передана уже `bit.ly` ссылка, команда пытается раскрыть её в исходный URL вместо повторного сокращения.
- **GAB-PUB-220 — Shorten invalid Bitly fallback:** незарегистрированная/невалидная Bitly-ссылка получает отдельный понятный ответ.
- **GAB-PUB-221 — Shorten result direct link:** успешное сокращение возвращает непосредственно новый короткий URL.
- **GAB-PUB-222 — Translate dual syntax:** перевод принимает оба формата `<source> to <target> <text>` и `<source> <target> <text>`.
- **GAB-PUB-223 — Translate quoted text parsing:** текст перевода собирается из оставшихся parsed arguments, поэтому фраза может содержать пробелы.
- **GAB-PUB-224 — Translate auto-detect source:** специальный source `?` сначала определяет язык исходного текста, затем запускает обычный перевод.
- **GAB-PUB-225 — Translate detection-specific error:** ошибка автоопределения языка получает отдельное сообщение, отличное от ошибки самого перевода.
- **GAB-PUB-226 — Translate accuracy disclaimer:** результат сопровождается явным предупреждением, что машинный перевод может быть неточным.

## Statistics / stream tracking

- **GAB-PUB-227 — Aggregate weekly server dashboard:** stats объединяет активность пользователей, игры, очки и использование команд в одной недельной сводке.
- **GAB-PUB-228 — Activity score combines text and voice:** итоговый activity score рассчитывается из message и voice activity, а не из одного показателя.
- **GAB-PUB-229 — Stats top-5 sections:** каждая основная статистическая категория ограничивается top 5.
- **GAB-PUB-230 — Stats destructive reset confirmation:** очистка недельной статистики требует отдельного подтверждения и предупреждает о необратимости.
- **GAB-PUB-231 — Stats reset permission gate:** reset доступен только Bot Admin требуемого уровня; обычному пользователю объясняется причина отказа.
- **GAB-PUB-232 — Streamer live-only filtering:** команда показывает только отслеживаемых стримеров, которые сейчас действительно live.
- **GAB-PUB-233 — Streamer mixed-platform cards:** карточки стримеров сохраняют platform-specific color/type для Twitch и YouTube.
- **GAB-PUB-234 — Streamer live preview:** live-карточка содержит preview thumbnail и прямую ссылку на трансляцию.
- **GAB-PUB-235 — Streamer all-offline empty state:** если все отслеживаемые стримеры offline, количество проверенных стримеров отражается в сообщении.
- **GAB-PUB-236 — Streamer unconfigured state:** отсутствие отслеживаемых стримеров получает отдельную подсказку настроить tracking через dashboard.

## Tags / reusable server content

- **GAB-PUB-237 — Tag permission matrix:** права tag-команды разделены по операциям: list/create/update/delete/clear и отдельно для command-tags.
- **GAB-PUB-238 — Locked tag protection:** locked tags нельзя изменять/удалять обычным пользователям даже при разрешённых базовых tag-операциях.
- **GAB-PUB-239 — Command-tag protection:** command-tags имеют отдельные create/delete permission settings относительно обычных tags.
- **GAB-PUB-240 — Tag overwrite confirmation:** обновление существующего tag требует явного подтверждения в течение минуты.
- **GAB-PUB-241 — Tag clear confirmation:** массовое удаление всех tags требует отдельного подтверждения.
- **GAB-PUB-242 — Tag long-content gist fallback:** слишком длинное содержимое tag (>300 символов) выносится во внешний Gist вместо переполнения embed.
- **GAB-PUB-243 — Tag URL autolink protection:** URL внутри tag content оборачиваются в `<...>`, предотвращая нежелательное embed-preview поведение.
- **GAB-PUB-244 — Tag default restoration:** специальная операция `defaults` полностью загружает предустановленный набор tags.
- **GAB-PUB-245 — Tag empty-state listing:** пустой список tags получает отдельное понятное сообщение.
- **GAB-PUB-246 — Tag list pagination:** список tags делится на страницы по 10 записей.

## Trivia / games

- **GAB-PUB-247 — Trivia explicit lifecycle commands:** публичная команда имеет отдельные действия `start`, `end/.`, `skip/next` и default answer mode.
- **GAB-PUB-248 — Trivia custom set selection:** при старте можно выбрать набор вопросов; без него используется `default`.
- **GAB-PUB-249 — Trivia ongoing-state guard:** команды управления/ответа учитывают, идёт ли игра в текущем канале, и не пытаются работать с отсутствующей сессией.
- **GAB-PUB-250 — Trivia progress query:** вызов trivia без действия во время игры показывает число завершённых вопросов и текущий score.
- **GAB-PUB-251 — Trivia current-set disclosure:** если выбран не-default набор, его ID показывается в текущем статусе игры.

## Moderation / unban / unmute

- **GAB-PUB-252 — Unban lookup by ID/tag/name:** unban умеет искать ban entry по user ID, tag или username, включая mention-like ID input.
- **GAB-PUB-253 — Unban confirmation includes old/new reasons:** перед unban показывается причина первоначального бана и новая причина unban.
- **GAB-PUB-254 — Unban notification disclosure:** пользователь явно предупреждается, что после unban автоматического DM не будет.
- **GAB-PUB-255 — Unban extended confirmation timeout:** destructive unban даёт две минуты на подтверждение.
- **GAB-PUB-256 — Unban ModLog linkage:** успешный unban создаёт отдельный ModLog case с новой причиной.
- **GAB-PUB-257 — Unmute negative-state protection:** unmute отклоняется, если участник вообще не находится в muted state.
- **GAB-PUB-258 — Unmute action hierarchy validation:** перед снятием mute проверяются и права бота, и иерархия target относительно модератора.
- **GAB-PUB-259 — Unmute ModLog creation:** успешное снятие mute создаёт отдельную запись ModLog.

## External content / search

- **GAB-PUB-260 — Wikipedia random mode:** wiki без поискового запроса получает случайную статью.
- **GAB-PUB-261 — Wikipedia summary fallback:** если краткое summary слишком короткое, команда загружает полный content статьи.
- **GAB-PUB-262 — Wikipedia description length protection:** длинное описание обрезается до безопасного embed-размера и получает ссылку на полный источник.
- **GAB-PUB-263 — Wikipedia image best-effort:** падение получения main image не ломает сам результат статьи.
- **GAB-PUB-264 — XKCD latest-or-ID dual mode:** без аргумента запрашивается последний комикс, с аргументом — конкретный ID.
- **GAB-PUB-265 — XKCD source-date metadata:** карточка XKCD содержит дату публикации и номер комикса.
- **GAB-PUB-266 — XKCD fetch failure specialization:** ошибка latest и ошибка конкретного ID формулируются по-разному.
- **GAB-PUB-267 — YouTube result type labeling:** результаты поиска явно маркируются как Video, Playlist или Channel.
- **GAB-PUB-268 — YouTube result count cap:** пользовательский count ограничивается серверным максимумом и дополнительным абсолютным лимитом 10.
- **GAB-PUB-269 — YouTube paginated mixed results:** видео, плейлисты и каналы выдаются единым интерактивным списком.
- **GAB-PUB-270 — YouTube publication timestamps:** результат сохраняет дату публикации как timestamp карточки.
- **GAB-PUB-271 — YouTube typed direct URLs:** для каждого типа результата строится собственная прямая URL-ссылка.
- **GAB-PUB-272 — Number fact random mode:** numfact без аргумента использует `random` вместо обязательного числа.
- **GAB-PUB-273 — Number fact numeric validation:** если аргумент указан, нечисловое значение отклоняется до внешнего запроса.
- **GAB-PUB-274 — Joke length protection:** слишком длинная внешняя шутка обрезается до допустимой длины embed.
- **GAB-PUB-275 — Fortune fuzzy category matching:** категория fortune может быть найдена не только exact-match, но и по близкому написанию через Levenshtein distance.
- **GAB-PUB-276 — Fortune category discovery:** неверная категория получает полный список допустимых категорий вместо общего error.
- **GAB-PUB-277 — Fortune progress stage:** получение fortune начинается с отдельного progress-сообщения.

## Small UX / normalization details

- **GAB-PUB-278 — Roll classic default:** отсутствие аргументов roll использует привычный диапазон 1–6.
- **GAB-PUB-279 — Roll one-argument upper bound:** один числовой аргумент трактуется как верхняя граница диапазона.
- **GAB-PUB-280 — Roll reversed-range normalization:** диапазон `max min` автоматически нормализуется перестановкой границ.
- **GAB-PUB-281 — Twitter handle normalization:** начальный `@` у имени Twitter удаляется перед запросом RSS.
- **GAB-PUB-282 — Twitter numeric result suffix:** последний числовой аргумент трактуется как количество последних записей и ограничивается серверными default/max limits.
- **GAB-PUB-283 — Twitter RSS pagination:** найденные tweets преобразуются в отдельные страницы с author/title, snippet, timestamp и прямой ссылкой.
- **GAB-PUB-284 — Twitter invalid-account empty branch:** отсутствие пользователя или публичных tweets редактирует progress message в понятный empty-state.
- **GAB-PUB-285 — Time timezone database gate:** произвольная строка timezone не принимается — используется проверка по базе timezone.
- **GAB-PUB-286 — Time local fallback:** без аргумента команда показывает локальное время runtime и одновременно обучает синтаксису timezone lookup.

## Текущая граница

Добавлен батч **GAB-PUB-206–GAB-PUB-286**. `Commands/Public/` всё ещё не закрыт: необходимо добрать оставшиеся Public-файлы, затем сделать финальную сверку всего каталога с idea bank. Только после этого переходить к `Commands/Shared/`.
