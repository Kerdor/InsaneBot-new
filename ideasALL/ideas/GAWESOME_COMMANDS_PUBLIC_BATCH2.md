# GAwesomeBot — Commands/Public — batch 2

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Продолжение `GAWESOME_COMMANDS_PUBLIC.md`. Механики подтверждены просмотром исходников. Дубликаты не переносятся буквально; фиксируются отдельные UX, ограничения и поведенческие варианты.

## Channel controls / productivity

- **GAB-PUB-110 — Cooldown clear dual syntax:** channel command cooldown можно снять как словом `clear`, так и одиночной точкой `.`.
- **GAB-PUB-111 — Cooldown bounded duration feedback:** при превышении допустимой длительности команда явно сообщает, что интервал слишком большой, вместо молчаливого ограничения.
- **GAB-PUB-112 — Countdown named event keys:** countdown хранится как именованное событие, нормализованное через trim/lowercase, поэтому имя служит стабильным ключом.
- **GAB-PUB-113 — Countdown duplicate prevention:** создание countdown с уже существующим именем не перезаписывает его, а показывает текущее время истечения.
- **GAB-PUB-114 — Countdown scheduled channel:** countdown сохраняет канал, в котором был создан, и завершение может быть привязано к нему.
- **GAB-PUB-115 — Countdown stale-channel filtering:** при общем списке показываются только countdowns, чей сохранённый канал всё ещё существует.
- **GAB-PUB-116 — Countdown chronological ordering:** общий список countdowns сортируется по ближайшему времени истечения.
- **GAB-PUB-117 — Countdown paginated listing:** список countdowns разбивается на страницы по 10 записей.
- **GAB-PUB-118 — Countdown query-or-create dual mode:** наличие имени без времени проверяет существующий countdown, а `name | time`/`name in time` создаёт новый.
- **GAB-PUB-119 — Countdown explicit empty state:** при отсутствии countdowns бот объясняет, какой синтаксис использовать для создания первого.
- **GAB-PUB-120 — Prefix quoted value support:** новый серверный prefix можно передать в кавычках, чтобы явно сохранить пробелы/служебные символы как единое значение.
- **GAB-PUB-121 — Prefix hard length limit:** prefix ограничен 25 символами с отдельной ошибкой до сохранения.
- **GAB-PUB-122 — Prefix status mode:** команда prefix без аргумента показывает фактический текущий prefix сервера.
- **GAB-PUB-123 — To-do auto-ID allocation:** новый пункт server to-do list получает автоматически сгенерированный числовой ID без ручного ввода.
- **GAB-PUB-124 — To-do ID collision avoidance:** генератор ID рекурсивно пропускает уже существующие значения.
- **GAB-PUB-125 — To-do content can contain spaces:** добавление пункта сохраняет весь исходный suffix как content, а не только первое слово.
- **GAB-PUB-126 — To-do completion toggle:** действие `done`/`complete` не только ставит completed, но и позволяет повторным вызовом вернуть пункт в незавершённое состояние.
- **GAB-PUB-127 — To-do dot deletion shortcut:** одиночная `.` удаляет пункт по ID.
- **GAB-PUB-128 — To-do inline editing:** для существующего ID любое неизвестное действие трактуется как новое содержимое пункта и обновляет его.
- **GAB-PUB-129 — To-do immediate refreshed view:** после добавления/изменения/удаления пунктов бот сразу показывает обновлённый список.

## Media / emoji

- **GAB-PUB-130 — Emoji-to-image worker:** несколько emoji можно собрать в единый jumbo-файл через выделенный worker, а не обрабатывать в command handler.
- **GAB-PUB-131 — Emoji newline normalization:** переносы строк в списке emoji превращаются в пробелы перед разбором входа.
- **GAB-PUB-132 — Emoji animated output detection:** итоговый файл автоматически выбирает GIF для анимированных emoji и PNG для статических.
- **GAB-PUB-133 — Emoji animation caveat disclosure:** для сгенерированного GIF бот отдельно предупреждает о возможном отличии скорости кадров и обрезании некоторых emoji.
- **GAB-PUB-134 — Custom emoji inspection by ID:** команда emotes принимает не только Discord-emoji syntax, но и сырой числовой ID.
- **GAB-PUB-135 — Unicode/custom emoji distinction:** Unicode emoji распознаются отдельно и получают объяснение, что команда предназначена для custom emoji.
- **GAB-PUB-136 — Known-vs-unknown emoji inspection:** если custom emoji уже загружена в cache бота, показывается расширенная информация; для неизвестной — доступный минимум по ID/name/animation.
- **GAB-PUB-137 — Emoji creator attribution:** для известного custom emoji бот пытается получить и показать пользователя, создавшего emoji.
- **GAB-PUB-138 — Emoji creator failure fallback:** если API не смог определить автора emoji, используется явный `Unknown User` fallback.
- **GAB-PUB-139 — Emoji integration flag:** карточка custom emoji отдельно сообщает, управляется ли она integration.
- **GAB-PUB-140 — Emoji role restrictions:** карточка перечисляет роли, которым разрешено использовать emoji; при отсутствии ограничений прямо указывается, что использовать может everyone.
- **GAB-PUB-141 — Emoji animated flag:** тип custom emoji отображается отдельным animated yes/no признаком.
- **GAB-PUB-142 — Emoji creation timestamp:** известная emoji получает timestamp создания в embed footer.
- **GAB-PUB-143 — Server emoji inventory split:** список emoji сервера разделяется на static и animated секции.

## Help / server information

- **GAB-PUB-144 — Help command polymorphism:** поиск конкретной команды проверяет одновременно PM, Public и Shared namespaces.
- **GAB-PUB-145 — Help extension discovery:** help умеет находить команды, предоставленные установленными extensions.
- **GAB-PUB-146 — Help permission-filtered catalog:** общий список показывает только команды, которые включены, доступны по admin level и не отключены в текущем канале.
- **GAB-PUB-147 — Help category navigation:** категории команд представлены отдельными интерактивными кнопками/страницами.
- **GAB-PUB-148 — Help extension category conditional:** кнопка Extensions появляется только когда действительно есть доступные extension-команды.
- **GAB-PUB-149 — Help sorted command display:** команды внутри категории сортируются по имени перед выводом.
- **GAB-PUB-150 — Help aligned command listing:** список визуально выравнивает названия команд через общий максимальный размер строки.
- **GAB-PUB-151 — Help empty-category state:** пустая разрешённая категория получает явный текст `No Commands Enabled Here` вместо пустой страницы.
- **GAB-PUB-152 — Help long-lived interactive menu:** help-menu получает увеличенный timeout, позволяя долго листать категории.
- **GAB-PUB-153 — Help exit control:** интерактивное меню имеет отдельную кнопку выхода.
- **GAB-PUB-154 — Server info aggregate metrics:** info объединяет дату создания, voice region, verification level, channels, members, roles, emoji, сообщения и использование команд в одной карточке.
- **GAB-PUB-155 — Server info special-feature detection:** отдельный блок появляется только при наличии специальных guild features.
- **GAB-PUB-156 — Server info verification/feature flags:** 2FA requirement, verified, expanded emoji capacity, VIP regions, invite splash и vanity URL обнаруживаются независимо.
- **GAB-PUB-157 — Server info vanity/splash state:** если соответствующая feature доступна, карточка показывает фактическое значение splash/vanity URL, когда оно задано.
- **GAB-PUB-158 — Server info activity visibility gate:** публичная ссылка на activity/join page показывается только при выполнении нескольких серверных условий видимости.
- **GAB-PUB-159 — Server info shard attribution:** footer указывает shard, обслуживающий текущий сервер.

## Moderation / confirmation

- **GAB-PUB-160 — Kick quoted reason parsing:** kick поддерживает quoted argument parser и разделение target/reason через `|` или пробел.
- **GAB-PUB-161 — Kick centralized hierarchy validation:** перед действием отдельно проверяется возможность бота выполнить kick и положение target относительно модератора.
- **GAB-PUB-162 — Kick confirmation gate:** destructive kick требует явного ответа инициатора перед выполнением.
- **GAB-PUB-163 — Kick confirmation timeout:** подтверждение kick действительно ограниченное время; отсутствие ответа приводит к отмене.
- **GAB-PUB-164 — Kick confirmation message cleanup:** ответ подтверждения удаляется после обработки, чтобы не оставлять служебный мусор.
- **GAB-PUB-165 — Kick target DM notification:** перед kick бот пытается отправить target DM с причиной, модератором и сервером.
- **GAB-PUB-166 — Kick DM failure isolation:** невозможность отправить DM не блокирует сам kick.
- **GAB-PUB-167 — Kick ModLog after action:** успешный kick автоматически создаёт ModLog case.
- **GAB-PUB-168 — Kick self playful safeguard:** вызов kick без target не выполняет действие над случайным участником; бот переводит сценарий в шуточное подтверждение для автора.

## Poll / giveaway / lottery

- **GAB-PUB-169 — Poll vote by number or exact option:** голос можно отдать как номером варианта, так и точным текстом option без учёта регистра.
- **GAB-PUB-170 — Poll one-vote enforcement:** повторная попытка голосования блокируется по user ID.
- **GAB-PUB-171 — Poll vote privacy control via PM:** после голоса пользователь получает способ удалить свой голос через PM-команду.
- **GAB-PUB-172 — Poll results percentage:** результаты показывают одновременно абсолютное число голосов и процент по каждому варианту.
- **GAB-PUB-173 — Poll live winner summary:** footer сообщает текущего лидера и общее количество голосов.
- **GAB-PUB-174 — Poll results pagination:** длинные списки вариантов разбиваются на страницы по 10.
- **GAB-PUB-175 — Giveaway creator cannot enroll:** создатель giveaway явно исключён из собственного списка участников.
- **GAB-PUB-176 — Giveaway duplicate enrollment prevention:** повторный `join/enroll` не создаёт дубликат участника.
- **GAB-PUB-177 — Giveaway participant self-removal via PM:** уже записавшийся участник получает путь удаления своей заявки через PM.
- **GAB-PUB-178 — Giveaway live participant count:** публичный статус giveaway показывает текущего creator и количество участников.
- **GAB-PUB-179 — Lottery progressive ticket price:** стоимость следующего lottery ticket рассчитывается от текущего количества уникальных участников и multiplier.
- **GAB-PUB-180 — Lottery per-user ticket cap:** один пользователь не может купить больше 5 билетов в одной lottery.
- **GAB-PUB-181 — Lottery progressive prize:** потенциальный приз растёт вместе с количеством проданных билетов и multiplier.
- **GAB-PUB-182 — Lottery tiered multipliers:** lottery предлагает уровни 1x/2x/5x/10x/100x с отдельными названиями и визуальными обозначениями.
- **GAB-PUB-183 — Lottery tier affordability gate:** старт lottery проверяет, хватает ли создателю points для выбранного минимального уровня.
- **GAB-PUB-184 — Lottery default tier fallback:** отсутствие ответа или некорректный выбор размера приводит к стандартному 2x tier вместо сбоя сценария.
- **GAB-PUB-185 — Lottery no-refund disclosure:** после покупки ticket пользователю явно сообщается, что возврата нет.
- **GAB-PUB-186 — Lottery end authorization:** завершить lottery может creator, bot admin требуемого уровня или maintainer.
- **GAB-PUB-187 — Lottery no-winner branch:** завершение без победителя имеет отдельный пользовательский результат.

## Statistics / ranks

- **GAB-PUB-188 — Weekly message statistics:** messages command считает сообщения именно за текущую неделю.
- **GAB-PUB-189 — Message stats bot exclusion:** bot accounts исключаются из пользовательской статистики сообщений.
- **GAB-PUB-190 — Message stats self shortcut:** `messages me` показывает собственную недельную статистику напрямую.
- **GAB-PUB-191 — Message stats top-8:** общий рейтинг сообщений ограничивается восемью наиболее активными участниками.
- **GAB-PUB-192 — Message stats total footer:** кроме top списка показывается общее число сообщений и число активных участников.
- **GAB-PUB-193 — Message stats dead-server state:** отсутствие сообщений получает отдельный тематический empty-state.
- **GAB-PUB-194 — Rank self/member/role lookup:** ranks поддерживает запрос собственного rank, rank конкретного member и списка участников конкретного rank.
- **GAB-PUB-195 — Rank top-members ordering:** участники одного rank сортируются по rank_score и показывается top 10.
- **GAB-PUB-196 — Rank no-members branch:** существующий rank без участников получает отдельное сообщение вместо пустого списка.
- **GAB-PUB-197 — Rank missing-user state:** пользователь без rank получает отдельный ответ, а не ошибку отсутствующего документа.
- **GAB-PUB-198 — Rank bot exclusion:** bot members не рассматриваются как обычные rank participants.
- **GAB-PUB-199 — Rank catalog statistics:** вызов ranks без аргумента строит агрегат по всем rank definitions и считает участников каждого rank.
- **GAB-PUB-200 — Roleinfo 25-item pagination:** список ролей и список собственных ролей разбиваются на сегменты по 25.
- **GAB-PUB-201 — Roleinfo effective permissions aggregation:** собственные роли объединяются в единый permission bitfield для показа суммарных прав.
- **GAB-PUB-202 — Roleinfo administrator warning:** Administrator permission отдельно помечается как право, обходящее другие permission/override.
- **GAB-PUB-203 — Roleinfo role feature flags:** карточка роли отдельно показывает mentionable, hoisted и integration-managed состояния.
- **GAB-PUB-204 — Roleinfo role metrics:** карточка показывает цвет, количество участников, позицию и возраст роли.
- **GAB-PUB-205 — Roleinfo unknown-role guidance:** отсутствие роли объясняет, как получить список всех ролей.
