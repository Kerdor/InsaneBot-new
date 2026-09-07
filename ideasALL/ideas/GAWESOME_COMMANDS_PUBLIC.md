# GAwesomeBot — Commands/Public

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Статус: **в работе**. Ниже фиксируются механики, подтверждённые просмотром исходников Public-команд. Дубликаты с уже существующим банком не переносятся буквально; сохраняются отличающиеся UX/поведение/ограничения.

## Search / information

- **GAB-PUB-001 — Anime result picker:** поиск аниме возвращает несколько результатов как интерактивное меню; каждый результат имеет отдельную карточку.
- **GAB-PUB-002 — Anime result metadata:** карточка аниме может показывать даты показа, количество эпизодов, длительность, рейтинг и возрастной рейтинг.
- **GAB-PUB-003 — Anime result synopsis truncation:** длинное описание обрезается до безопасного размера embed и получает ссылку на полный текст.
- **GAB-PUB-004 — Anime configurable result count:** число результатов ограничивается серверными `default_count`/`max_count` настройками.
- **GAB-PUB-005 — Anime numeric suffix:** последнее числовое значение после поискового запроса трактуется как количество результатов; при некорректном формате используется значение по умолчанию.
- **GAB-PUB-006 — App Store multi-query:** команда принимает несколько названий приложений и формирует отдельный результат для каждого.
- **GAB-PUB-007 — App Store compact preview:** результат приложения показывает разработчика, иконку, краткое описание, рейтинг, цену и ссылку на страницу.
- **GAB-PUB-008 — App Store per-item failure:** отсутствие одного приложения не ломает остальные результаты; ошибка становится отдельной карточкой.
- **GAB-PUB-009 — Avatar by member search:** аватар можно получить по участнику через общий поиск пользователя.
- **GAB-PUB-010 — Avatar by raw user ID:** числовой ID может быть разрешён отдельно через API fetch пользователя.
- **GAB-PUB-011 — Avatar self shortcut:** отсутствие цели или специальное `me` позволяет обращаться к собственному аватару.
- **GAB-PUB-012 — Avatar fallback:** если пользователь не найден, команда показывает аватар самого бота вместо пустого ответа.
- **GAB-PUB-013 — Reddit default subreddit:** отсутствие subreddit автоматически использует `all`.
- **GAB-PUB-014 — Reddit path normalization:** `/r/name` и `name` нормализуются в один запрос.
- **GAB-PUB-015 — Reddit safety filtering:** NSFW-посты отбрасываются, если текущий канал не помечен NSFW.
- **GAB-PUB-016 — Reddit filtering telemetry:** ответ может сообщать, сколько NSFW результатов было отфильтровано.
- **GAB-PUB-017 — Reddit state-specific errors:** banned/private/quarantined/nonexistent/empty subreddit состояния обрабатываются разными ветками UX.
- **GAB-PUB-018 — Reddit result pagination:** результаты Reddit листаются через интерактивную пагинацию.
- **GAB-PUB-019 — Reddit result context:** карточка содержит автора, время, комментарии, score и permalink.
- **GAB-PUB-020 — Urban Dictionary random mode:** отсутствие поискового слова позволяет получить случайный результат.
- **GAB-PUB-021 — Urban Dictionary pagination:** несколько определений листаются интерактивно.
- **GAB-PUB-022 — Urban Dictionary rich fields:** определение может показывать пример, автора, голоса и прямую ссылку.
- **GAB-PUB-023 — Urban Dictionary tag footer:** теги результата выводятся отдельно в footer.
- **GAB-PUB-024 — Urban Dictionary length protection:** слишком длинное определение ограничивается до допустимого размера embed.
- **GAB-PUB-025 — Wolfram progress message:** тяжёлый внешний запрос сначала создаёт статус `Fetching...`, а затем используется уже существующее сообщение для результата/ошибки.
- **GAB-PUB-026 — Wolfram pod aggregation:** несколько pod-результатов преобразуются в поля одного embed.
- **GAB-PUB-027 — Wolfram image fallback:** если у pod нет пригодного plaintext, используется изображение результата.
- **GAB-PUB-028 — Wolfram explicit no-result branch:** отсутствие результатов и ошибка API имеют отдельные ответы.

## Utility / productivity

- **GAB-PUB-029 — Calculator help mode:** `calc help ...` использует тот же вычислительный backend для получения справки по функциям.
- **GAB-PUB-030 — Calculator progress UX:** вычисление начинается с отдельного `Calculating...` сообщения, чтобы пользователь видел, что запрос принят.
- **GAB-PUB-031 — Calculator worker isolation:** математические вычисления выполняются через отдельный worker-тип, а не напрямую в command handler.
- **GAB-PUB-032 — Channel command cooldown:** cooldown команды хранится на уровне канала.
- **GAB-PUB-033 — Cooldown natural duration:** длительность cooldown задаётся естественным текстом вроде `30s`/`2m` через duration parser.
- **GAB-PUB-034 — Cooldown hard cap:** длительность cooldown ограничена пятью минутами.
- **GAB-PUB-035 — Cooldown clear shortcut:** `clear` и `.` снимают cooldown.
- **GAB-PUB-036 — Cooldown status mode:** вызов без аргумента сообщает текущий cooldown либо объясняет, как его установить.
- **GAB-PUB-037 — Quiet indefinite mode:** `quiet` без duration выключает обработку команд в текущем канале бессрочно.
- **GAB-PUB-038 — Quiet timed mode:** duration включает автоматическое возвращение бота через заданное время.
- **GAB-PUB-039 — Quiet all-channels mode:** специальный `all` позволяет отключить бота сразу во всех каналах сервера.
- **GAB-PUB-040 — Quiet duration cap:** временный quiet ограничен одним часом.
- **GAB-PUB-041 — Count lazy creation:** обращение к несуществующему счётчику запускает интерактивный вопрос о его создании.
- **GAB-PUB-042 — Count confirmation cleanup:** ответ пользователя после подтверждения может быть удалён, чтобы не засорять канал.
- **GAB-PUB-043 — Count symbolic operations:** поддерживаются несколько эквивалентных обозначений инкремента/декремента (`+`, `++`, `+1`, `-`, `--`, `-1`).
- **GAB-PUB-044 — Count nonnegative floor:** счётчик не позволяет уменьшить значение ниже нуля.
- **GAB-PUB-045 — Count stop action:** специальный `.` завершает и удаляет счётчик, сохраняя пользователю финальное значение в сообщении.
- **GAB-PUB-046 — Count list pagination:** список всех счётчиков разбивается на страницы по 10 элементов.
- **GAB-PUB-047 — Count empty-state guidance:** отсутствие счётчиков объясняет, какой командой создать первый.
- **GAB-PUB-048 — Archive bounded fetch:** архивирование ограничено максимум 100 сообщениями.
- **GAB-PUB-049 — Archive cursor support:** можно указать ID последнего сообщения, относительно которого получать архив.
- **GAB-PUB-050 — Archive structured export:** архив сохраняется в JSON-файл, а не только публикуется текстом.
- **GAB-PUB-051 — Archive preserves embeds:** JSON сохраняет основные компоненты embed: author, color, URL, description, fields, footer, image, thumbnail, timestamp, title, type.
- **GAB-PUB-052 — Archive preserves attachments:** вложения архивируются отдельными именами и URL.
- **GAB-PUB-053 — Archive edit metadata:** сохраняются исходное и изменённое время сообщения.
- **GAB-PUB-054 — Archive source metadata:** JSON содержит сервер, канал, количество сообщений и время создания архива.
- **GAB-PUB-055 — Archive permission diagnosis:** ошибка чтения истории прямо объясняется отсутствием `Read Message History` или неверным cursor ID.
- **GAB-PUB-056 — Archive send-failure isolation:** ошибка отправки готового архива обрабатывается отдельно от ошибки чтения истории.

## Moderation

- **GAB-PUB-057 — Nuke content filter:** массовое удаление может выбирать сообщения по подстроке текста через префикс `:`.
- **GAB-PUB-058 — Nuke author filter:** массовое удаление может выбирать сообщения конкретного упомянутого участника.
- **GAB-PUB-059 — Nuke exact-text filter:** без специальных префиксов фильтр может искать точное совпадение текста сообщения.
- **GAB-PUB-060 — Nuke message-ID boundaries:** можно задавать границу `before` или `after` по ID.
- **GAB-PUB-061 — Nuke result cap:** команда принимает максимум 100 удаляемых сообщений.
- **GAB-PUB-062 — Mute centralized action check:** перед mute проверяются одновременно возможности бота и иерархия пользователя.
- **GAB-PUB-063 — Mute duplicate prevention:** уже замьюченный участник не может быть замьючен повторно.
- **GAB-PUB-064 — Mute reason persistence:** причина передаётся в ModLog независимо от текста пользовательского подтверждения.
- **GAB-PUB-065 — Mute quoted argument parser:** цель и причина могут разделяться `|` или обычным пробелом с поддержкой quoted arguments.
- **GAB-PUB-066 — Quiet vs mute distinction:** quiet выключает команды на уровне канала, mute ограничивает конкретного участника; два независимых уровня подавления активности.
- **GAB-PUB-067 — Strike lazy member state:** просмотр strikes автоматически создаёт состояние участника, если оно ещё не существует.
- **GAB-PUB-068 — Strike self default:** без цели `strikes` показывает собственные нарушения; `me` также явно поддерживается.
- **GAB-PUB-069 — Strikes paginated history:** история предупреждений/страйков выводится по одному элементу на страницу.
- **GAB-PUB-070 — Strike moderator attribution:** каждая запись связывает причину с модератором и временем.
- **GAB-PUB-071 — Strike ModLog linkage:** strike хранит ссылку на соответствующую запись ModLog.
- **GAB-PUB-072 — Reason command edits existing case:** причина существующего ModLog обновляется отдельной командой вместо создания новой записи.
- **GAB-PUB-073 — Reason typed error mapping:** известные ошибки ModLog переводятся в понятные пользователю сообщения, неизвестные ошибки пробрасываются дальше.

## UX / robustness

- **GAB-PUB-074 — Per-command invalid usage:** команды используют специализированные invalid-usage ответы вместо единого немого отказа.
- **GAB-PUB-075 — Progress-message reuse:** внешние долгие операции предпочитают редактировать уже отправленный progress message вместо создания серии сообщений.
- **GAB-PUB-076 — Per-item partial failure:** пакетные команды стараются продолжать обработку остальных элементов, если один внешний запрос завершился ошибкой.
- **GAB-PUB-077 — User-facing fallback content:** многие команды имеют осмысленный fallback вместо пустого результата, включая альтернативный контент самого бота.
- **GAB-PUB-078 — Humanized durations:** пользовательские интервалы отображаются человекочитаемо через duration humanizer.
- **GAB-PUB-079 — URL-safe external search links:** результаты внешних каталогов содержат прямую ссылку на первоисточник результата.
- **GAB-PUB-080 — Structured error logging:** ошибки команд логируются с guild/channel/user IDs для последующей диагностики.

## Техническая граница текущего прохода

`Commands/Public/` **ещё не закрыт**. Следующий проход должен добрать полностью не просмотренные/повторно проверить все Public-файлы, затем сверить этот файл с существующим банком и только после этого объявить директорию завершённой.
