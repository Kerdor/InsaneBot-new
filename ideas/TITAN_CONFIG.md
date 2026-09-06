# TITAN CONFIG — Банк идей

Находки `codebymitch/TitanBot` (main), `src/config/**`.

## Уже зафиксировано

- TITAN-G001 — Server configuration dashboard показывает текущие prefix, moderator role, log channel, bot presence, theme и setup status в одном embed.
- TITAN-G002 — Configuration dashboard использует String Select Menu для выбора конкретной настройки без отдельных команд.
- TITAN-G003 — Dashboard содержит отдельную кнопку запуска/re-run setup wizard, причём label/style меняется после завершения wizard.
- TITAN-G004 — Setup wizard выполняется через DM, чтобы не засорять серверный канал настройками.
- TITAN-G005 — Wizard сообщает пользователю в ephemeral follow-up, что вопросы пришли в DM.
- TITAN-G006 — При закрытых DM бот показывает пошаговую инструкцию, как разрешить direct messages с сервера.
- TITAN-G007 — Внутри одного пользователя запрещается несколько одновременно активных wizard sessions через Set.
- TITAN-G008 — Каждый wizard prompt имеет отдельный parser/validator и поддерживает `skip` для сохранения текущего значения.
- TITAN-G009 — Wizard поддерживает `cancel`, который прекращает дальнейшие вопросы, не откатывая уже сохранённые изменения.
- TITAN-G010 — Ответы wizard собираются пошагово и сохраняются сразу после успешной валидации, а не одним финальным commit.
- TITAN-G011 — После каждого изменения dashboard пытается обновиться, показывая новое значение без ожидания окончания всего wizard.
- TITAN-G012 — Timeout ответа на отдельный вопрос составляет 3 минуты, после чего wizard завершается с понятной причиной.
- TITAN-G013 — Channel/role можно задавать как mention или raw Discord ID; IDs дополнительно проверяются существованием внутри текущего guild.
- TITAN-G014 — Для nullable settings предусмотрено явное значение `none` для очистки текущей настройки.
- TITAN-G015 — Prefix валидируется по длине и запрещённым пробелам непосредственно в wizard parser.
- TITAN-G016 — Dashboard автоматически показывает ссылки/подсказки на другие configuration surfaces, например `/commands dashboard` для command access.
- TITAN-G017 — Dashboard имеет inactivity timeout 10 минут как UX-защиту от устаревшего интерактивного сообщения.
- TITAN-G018 — Настройки moderator role и log channel отображаются через реальные Discord mentions, если соответствующие сущности доступны в cache.
- TITAN-G019 — Theme summary централизованно показывает primary/success/warning/error цвета и объясняет, что они применяются глобально.

## Полный `src/config/**` аудит

### Bot / application configuration

- TITAN-G020 — Presence конфигурируется отдельным объектом `presence`, отделяя online-status от activity entries.
- TITAN-G021 — Presence status допускает Discord-состояния online, idle, dnd и invisible.
- TITAN-G022 — Activity поддерживает одновременно несколько activity lines вместо одной фиксированной строки.
- TITAN-G023 — Activity хранит и `name`, и `state`, что позволяет использовать Custom Status с отображаемым state отдельно от обязательного API name.
- TITAN-G024 — Тип Discord activity задаётся числовым Discord API mapping, включая Playing, Streaming, Listening, Watching, Custom и Competing.
- TITAN-G025 — Список bot owners загружается из comma-separated `OWNER_IDS` с trim и удалением пустых значений.
- TITAN-G026 — Default command cooldown вынесен в единую глобальную настройку в секундах.
- TITAN-G027 — Регистрацию slash-команд можно переключать флагом удаления старых команд перед re-register.
- TITAN-G028 — `TEST_GUILD_ID` сохраняется как совместимая с tutorial/setup настройка, даже если runtime-регистрация его не использует.
- TITAN-G029 — Maintenance mode можно включить через config/env и ограничить выполнение команд владельцами бота.
- TITAN-G030 — Prefix commands и slash commands могут существовать одновременно в одном боте.
- TITAN-G031 — `DISCORD_TOKEN` имеет fallback на legacy/env alias `TOKEN`.
- TITAN-G032 — Client ID и guild ID читаются из environment, а не зашиваются в исходник.
- TITAN-G033 — Конфиг имеет отдельный production/development режим через `NODE_ENV`.
- TITAN-G034 — `application.js` централизует абсолютные runtime paths для root, commands, events, config, utils, services, handlers и interactions.
- TITAN-G035 — Application config объединяет `botConfig`, database config и feature config в единый runtime object.
- TITAN-G036 — Shop-конфигурация может расширять базовый `botConfig.shop`, причём более специализированный shop config имеет приоритет.
- TITAN-G037 — Runtime config после сборки замораживается через `Object.freeze`, чтобы случайные мутации настроек не расходились по системе.
- TITAN-G038 — Environment name и boolean helpers (`isProduction`, `isDevelopment`) доступны как готовые runtime flags.

### Embed / branding

- TITAN-G039 — Цвета embed вынесены в single source of truth, чтобы разные подсистемы не держали собственные независимые палитры.
- TITAN-G040 — Есть общие semantic colors success/error/warning/info наряду с нейтральными light/dark/gray.
- TITAN-G041 — Конфиг предоставляет Discord-style palette aliases (`blurple`, `green`, `yellow`, `fuchsia`, `red`, `black`) для единообразного UI.
- TITAN-G042 — Для разных feature domains предусмотрены отдельные цвета, например giveaway, ticket, economy, birthday и moderation.
- TITAN-G043 — Ticket priority имеет собственную color map, независимую от общих статусных цветов.
- TITAN-G044 — Ticket priority config хранит не только цвет, но и emoji + human-readable label.
- TITAN-G045 — Embed footer централизованно задаёт текст и необязательную icon URL.
- TITAN-G046 — Default embed thumbnail можно глобально отключить через `null`.
- TITAN-G047 — Default embed author block допускает name, icon и URL, но каждое поле может быть `null`.

### Applications

- TITAN-G048 — Application questions являются конфигурируемым массивом объектов с текстом вопроса и required-флагом.
- TITAN-G049 — В конфиге предусмотрен отдельный default-набор application questions, а не hardcoded questions внутри command handler.
- TITAN-G050 — Цвета application статусов (`pending`, `approved`, `denied`) задаются централизованной status map.
- TITAN-G051 — Между отправками applications действует отдельный cooldown в часах.
- TITAN-G052 — Approved и denied applications имеют разные автоматические retention periods.
- TITAN-G053 — Для approved application задан более длительный срок хранения, чем для denied application.
- TITAN-G054 — Application manager roles представлены массивом role IDs и могут быть заполнены не только исходным конфигом, но и env/database setup.
- TITAN-G055 — Retention policy можно задавать независимо для каждого результата рассмотрения application.

### Economy / shop config

- TITAN-G056 — Currency имеет независимые display name, plural name и symbol.
- TITAN-G057 — Starting balance вынесен в config и применяется как отдельное правило для новых пользователей.
- TITAN-G058 — Base bank capacity отделена от upgrade-based расширений банка.
- TITAN-G059 — Daily reward amount является отдельной настройкой от work/beg payout ranges.
- TITAN-G060 — Work и beg используют независимые min/max payout ranges.
- TITAN-G061 — Economy cooldowns хранятся централизованной map с отдельными интервалами для daily/work/crime/rob.
- TITAN-G062 — Risky robbery success probability конфигурируется числом, а не hardcoded в service.
- TITAN-G063 — Failed robbery jail duration вынесена в milliseconds и может быть изменена без изменения логики rob command.
- TITAN-G064 — Shop отделён от основной bot config отдельным `src/config/shop` модулем.
- TITAN-G065 — Shop категории связываются с item types, поэтому UI может получать items по семантической категории вместо ручного списка IDs.
- TITAN-G066 — Shop поддерживает категории consumables, upgrades, tools и roles с отдельными descriptions/icons.
- TITAN-G067 — Shop transaction cooldown ограничивает слишком частые покупки.
- TITAN-G068 — Shop transaction имеет отдельный maximum quantity за одну операцию.
- TITAN-G069 — Потенциально дорогие/массовые покупки могут требовать confirmation с отдельным timeout.
- TITAN-G070 — Shop содержит configurable refund policy с enable-флагом, refund window и процентной fee.
- TITAN-G071 — Shop UI configurable: items per page, отображение out-of-stock, owned items и affordability.
- TITAN-G072 — Shop имеет отдельную rarity color palette от common до mythic.
- TITAN-G073 — Shop использует отдельные emoji для currency, quantity, price, owned, out-of-stock и item types.
- TITAN-G074 — Restock может быть периодическим событием с interval, announcement channel и кастомным message.
- TITAN-G075 — Sales поддерживают расписание скидок по дням недели и собственное announcement message.
- TITAN-G076 — Текущая цена вычисляется динамически: base price × quantity с последующим ограничением суммарной скидки в диапазоне 0..100%.
- TITAN-G077 — Цена может учитывать пользовательские признаки, например premium role.
- TITAN-G078 — Bulk quantity может автоматически давать дополнительную скидку после заданного порога.
- TITAN-G079 — Shop item может иметь maxQuantity для consumable и maxLevel для upgrade независимо друг от друга.
- TITAN-G080 — Инвентарные tools по умолчанию могут быть single-instance предметами, тогда как bank note является разрешённым multi-purchase исключением.
- TITAN-G081 — Tool может иметь durability, включая разные максимумы для разных инструментов.
- TITAN-G082 — Бессрочный item может явно обозначать `durability: null`.
- TITAN-G083 — Item effects описываются декларативно через `type` и параметры multiplier/uses/increase вместо hardcoded effect classes.
- TITAN-G084 — Consumable boost может ограничиваться количеством uses и расходоваться постепенно.
- TITAN-G085 — Upgrade effect может хранить multiplier, который применяется к базовой capacity/yield механике.
- TITAN-G086 — Role item может содержать Discord `roleId` отдельно от экономического effect.

### Ticket / giveaway / birthday defaults

- TITAN-G087 — Ticket default category, support roles, archive category и log channel являются отдельными nullable/array config values.
- TITAN-G088 — Ticket default priority задаётся в конфиге и может быть изменён без переписывания ticket creation logic.
- TITAN-G089 — Giveaway имеет отдельную default duration и независимые min/max winner limits.
- TITAN-G090 — Giveaway duration имеет собственные min/max bounds, отделённые от default duration.
- TITAN-G091 — Giveaway hosting restrictions поддерживают allowed roles и bypass roles как две разные политики.
- TITAN-G092 — Birthday default role и announcement channel являются независимыми настройками.
- TITAN-G093 — Birthday timezone является частью конфигурации, а не неявным timezone процесса.

### Verification

- TITAN-G094 — Verification panel имеет отдельно настраиваемый default message и button text.
- TITAN-G095 — Auto-verification использует явный `defaultCriteria`, а не набор неявных if-правил.
- TITAN-G096 — Auto-verification поддерживает режим `none`, который означает немедленное auto-approval для всех.
- TITAN-G097 — Auto-verification поддерживает account-age criterion с отдельным количеством дней.
- TITAN-G098 — Auto-verification поддерживает server-size criterion с threshold по числу участников.
- TITAN-G099 — Account-age requirement имеет собственные min/max safety bounds.
- TITAN-G100 — Verification config содержит human-readable descriptions для каждого criteria mode, позволяя UI строить объяснения из config.
- TITAN-G101 — После успешной verification можно отдельно включать/выключать DM notification.
- TITAN-G102 — Verification attempt cooldown отделён от общего command cooldown.
- TITAN-G103 — Для verification есть sliding time-window логика количества failed attempts.
- TITAN-G104 — `maxVerificationAttempts` и `attemptWindow` задаются независимо.
- TITAN-G105 — In-memory cooldown/attempt maps имеют явные max-entry limits против неограниченного роста памяти.
- TITAN-G106 — Verification cooldown map имеет отдельный периодический cleanup interval.
- TITAN-G107 — Audit metadata ограничивается максимальным размером в bytes.
- TITAN-G108 — Audit trail в памяти имеет отдельный maximum entry count.
- TITAN-G109 — Можно включить логирование каждого verification action отдельным флагом.
- TITAN-G110 — Можно отдельно включить сохранение verification audit history.
- TITAN-G111 — Verification safety limits вынесены в config вместо hardcoded constants.

### Welcome / goodbye

- TITAN-G112 — Welcome и goodbye используют разные template settings, а не общий message.
- TITAN-G113 — Welcome template поддерживает `{user}`, `{server}` и `{memberCount}`.
- TITAN-G114 — Goodbye template поддерживает `{user}` и `{memberCount}`.
- TITAN-G115 — Welcome и goodbye имеют независимые destination channels.
- TITAN-G116 — Member-count placeholder позволяет отображать динамический размер сервера непосредственно в шаблоне.

### Server counters

- TITAN-G117 — Counter config разделяет default name, description, type и channel-name template.
- TITAN-G118 — Counter channel name может использовать `{count}` как динамический placeholder.
- TITAN-G119 — Counter permission policy задаёт deny и allow arrays отдельно.
- TITAN-G120 — Counter action responses (`created`, `deleted`, `updated`) централизованы как templates.
- TITAN-G121 — Counter types декларативно содержат name, description и `getCount` resolver.
- TITAN-G122 — Встроенный members counter использует guild.memberCount как source of truth.
- TITAN-G123 — Bots counter и humans counter могут вычисляться отдельно из guild member cache.
- TITAN-G124 — Один counter framework может расширяться новыми count resolvers без изменения общей команды управления counters.

### Generic messages / feature flags

- TITAN-G125 — Generic bot messages централизуют no-permission, cooldown, generic-error, missing-permissions, disabled-command и maintenance responses.
- TITAN-G126 — Cooldown message использует `{time}` placeholder, позволяя одному шаблону отображать динамическое оставшееся время.
- TITAN-G127 — Feature flags организованы по функциональным доменам и позволяют глобально отключать целые подсистемы.
- TITAN-G128 — Feature flags разделяют core systems, community engagement, security/self-service и utility modules.
- TITAN-G129 — Voice/search/tools/utility/community/fun/music могут отключаться независимо друг от друга.
- TITAN-G130 — Reaction roles и JoinToCreate имеют собственные глобальные feature flags помимо локальных guild settings.
- TITAN-G131 — `music` flag получает fallback `true`, если в старом/неполном config объекте music отсутствует.

### Command aliases / categories

- TITAN-G132 — Command aliases хранятся отдельно от command implementation, позволяя менять shorthand без правки команд.
- TITAN-G133 — Alias resolution нормализует входное имя через lowercase перед lookup.
- TITAN-G134 — При отсутствии alias resolver возвращает исходное command name вместо ошибки.
- TITAN-G135 — Subcommand aliases вынесены в отдельную map и резолвятся независимо от top-level command aliases.
- TITAN-G136 — Один alias может соответствовать распространённым сокращениям, синонимам и legacy названиям команды.
- TITAN-G137 — Поддерживаются alias-группы для экономических команд (`bal`, `money`, `cash`, и т.п.).
- TITAN-G138 — Поддерживаются alias-группы для moderation actions (`mute`→`timeout`, `unmute`→`untimeout`, `clear`→`purge`).
- TITAN-G139 — Поддерживаются alias-группы для leaderboard/rank (`lvl`, `xp`, `lb`, `top`).
- TITAN-G140 — Поддерживаются alias-группы для avatar/userinfo и birthday.
- TITAN-G141 — Giveaway lifecycle aliases позволяют использовать start/stop/roll как shorthand для create/end/reroll.
- TITAN-G142 — Ticket aliases допускают короткие `t` и `new`.
- TITAN-G143 — Music now-playing aliases допускают `np` и `now`.
- TITAN-G144 — Command categories имеют отдельную icon map для dashboard/command manager UI.
- TITAN-G145 — Unknown category получает fallback icon `📁`, а не ломает UI.
- TITAN-G146 — Category key normalizer trim-ит строку, приводит к lowercase и заменяет whitespace на `_`.
- TITAN-G147 — Category display formatter умеет превращать underscore и CamelCase в человекочитаемое название.
- TITAN-G148 — Два recovery/admin commands (`commands`, `configwizard`) объявлены protected и не должны исчезать при command-access lockdown.

### Prefix restrictions

- TITAN-G149 — Prefix restrictions имеют отдельный policy layer вместо проверки slash-only условий внутри каждой команды.
- TITAN-G150 — Команда может явно выставить `prefixOnly === false` или `slashOnly === true` для запрета prefix invocation.
- TITAN-G151 — Есть глобальный список top-level slash-only commands.
- TITAN-G152 — Есть глобальный список subcommands, запрещённых через prefix независимо от команды.
- TITAN-G153 — Есть глобальный список subcommand groups, например `config`, которые остаются slash-only.
- TITAN-G154 — Отдельные команды могут иметь собственные blocked subcommands поверх глобальной политики.
- TITAN-G155 — Music имеет отдельный набор slash-only subcommands для интерактивных операций (`shuffle`, `loop`, `seek`, `remove`, `move`, `clear`, `247`).
- TITAN-G156 — Birthday `setchannel` и report `setchannel` могут быть slash-only при сохранении prefix-доступа к остальной команде.
- TITAN-G157 — Prefix restriction анализирует реальный command JSON через `toJSON()`, а не полагается только на вручную поддерживаемый список всех subcommands.
- TITAN-G158 — Для nested subcommand groups restriction layer умеет извлекать имена вложенных subcommands.
- TITAN-G159 — Перед проверкой blocked subcommand применяется alias resolution, поэтому alias не позволяет обойти slash-only запрет.
- TITAN-G160 — Если все subcommands команды заблокированы, вся команда автоматически считается slash-only.
- TITAN-G161 — Restriction API возвращает не только boolean, но и reason для понятного user-facing ответа.
- TITAN-G162 — Есть отдельный `isPrefixRestrictedCommand` helper для мест, которым нужен только boolean результат.
- TITAN-G163 — Команда без валидного `data.toJSON()` не блокируется самим restriction layer, сохраняя graceful fallback.

### PostgreSQL / persistence configuration

- TITAN-G164 — PostgreSQL table names собраны в одном `configuredTables` registry вместо разрозненных строк по сервисам.
- TITAN-G165 — Registry использует semantic aliases (`guilds`, `users`, `tickets`, `economy`, `leveling` и т.д.) поверх реальных SQL table names.
- TITAN-G166 — Table identifiers проходят allowlist validation перед использованием в SQL-related config.
- TITAN-G167 — Используется отдельный `Set` разрешённых identifiers, чтобы динамические SQL identifiers нельзя было подменить произвольной строкой.
- TITAN-G168 — Postgres имеет единый default local connection URL.
- TITAN-G169 — Поддерживается connection-string режим через `POSTGRES_URL` или `DATABASE_URL`.
- TITAN-G170 — Если connection URL не задан или равен local default, config переключается на host/port/database/user/password fields.
- TITAN-G171 — SSL policy может явно задаваться через `POSTGRES_SSL=false/0` или `true/1`.
- TITAN-G172 — SSL также автоматически включается для URL с sslmode=require/verify-ca/verify-full/prefer.
- TITAN-G173 — Railway environment/project detection включает compatible SSL settings автоматически.
- TITAN-G174 — Production environment по умолчанию использует SSL.
- TITAN-G175 — Development может работать без SSL по умолчанию.
- TITAN-G176 — Pool max/min connections вынесены в environment-driven config.
- TITAN-G177 — Pool имеет отдельный idle timeout и connection timeout.
- TITAN-G178 — `application_name` задаётся для PostgreSQL connections, позволяя отличать подключения бота на стороне БД.
- TITAN-G179 — Production использует statement timeout, тогда как development может отключать его для debugging.
- TITAN-G180 — PostgreSQL keepalives включены и имеют отдельный idle interval.
- TITAN-G181 — Connection pool поддерживает отдельные retry count, backoff base и backoff multiplier settings.
- TITAN-G182 — Database config содержит разные TTL policies для session, temp, cache, ticket и AFK данных.
- TITAN-G183 — Guild/economy/leveling/giveaway/welcome/birthday данные могут иметь `null` TTL, то есть не должны истекать автоматически.
- TITAN-G184 — Ticket TTL может быть конечным и существенно длиннее transient cache TTL.
- TITAN-G185 — Database features имеют отдельные pooling, SSL, metrics и debug flags.
- TITAN-G186 — Auto-create tables и auto-migrate schema контролируются независимыми feature flags.
- TITAN-G187 — `AUTO_MIGRATE=false` позволяет отключить автоматические миграции через environment.
- TITAN-G188 — Database health check можно полностью отключить конфигом.
- TITAN-G189 — Health check имеет interval, maxFailures и конкретный validation query (`SELECT 1`).
- TITAN-G190 — Migration config хранит expected schema version и human-readable schema label как часть runtime contract.
- TITAN-G191 — Migration table name и migration directory конфигурируются отдельно.
- TITAN-G192 — Rollback-on-failure policy является отдельным migration setting, а не неявным поведением.

### Schema version

- TITAN-G193 — Expected schema version читается из `SCHEMA_VERSION` и безопасно приводится к integer.
- TITAN-G194 — Некорректная, нечисловая или неположительная schema version заменяется безопасным значением `1`.
- TITAN-G195 — Schema label можно задавать отдельно через `SCHEMA_VERSION_LABEL`.
- TITAN-G196 — При отсутствии custom label автоматически строится label вида `baseline-v<version>`.
- TITAN-G197 — Runtime database config и migration scripts используют один и тот же schemaVersion module как single source of truth.

### Lavalink

- TITAN-G198 — Lavalink node config поддерживает JSON из environment как один из источников конфигурации.
- TITAN-G199 — JSON env payload принимается только если после parsing получается array nodes.
- TITAN-G200 — Lavalink nodes можно загружать из отдельного JSON-файла.
- TITAN-G201 — Путь к nodes file можно переопределить через `LAVALINK_NODES_FILE`.
- TITAN-G202 — При отсутствии override nodes file по умолчанию ищется в `lavalink/nodes.json` относительно project root.
- TITAN-G203 — File loader допускает как прямой array, так и объект с `nodes` array.
- TITAN-G204 — Невалидный JSON env/file не роняет startup: loader возвращает fallback.
- TITAN-G205 — Приоритет источников Lavalink: valid environment JSON → valid file → single-node environment fallback.
- TITAN-G206 — Single-node fallback использует host, port, password, secure и name из environment/defaults.
- TITAN-G207 — `LAVALINK_SECURE` поддерживает человекочитаемые boolean values `true`, `1`, `yes`.
- TITAN-G208 — Lavalink node имеет явное human-readable name, полезное для логов и диагностики.
- TITAN-G209 — Default search platform является отдельной настройкой от списка Lavalink nodes.
- TITAN-G210 — Lavalink REST API version также конфигурируется отдельно.

### Logging / API runtime

- TITAN-G211 — Runtime logging level задаётся через `LOG_LEVEL` с fallback `info`.
- TITAN-G212 — File logging можно независимо включить через `LOG_TO_FILE=true`.
- TITAN-G213 — Log files имеют отдельный directory, max size, max age/files и zipped archive policy.
- TITAN-G214 — Console logging имеет независимые enabled, colorize и timestamp settings.
- TITAN-G215 — Sentry включается автоматически только при наличии `SENTRY_DSN`.
- TITAN-G216 — Sentry environment следует `NODE_ENV`, позволяя разделять ошибки development/production.
- TITAN-G217 — API port configurable через `PORT` с default 3000.
- TITAN-G218 — CORS origin поддерживает comma-separated список origins или wildcard `*`.
- TITAN-G219 — API CORS policy централизует allowed HTTP methods.
- TITAN-G220 — API CORS policy централизует allowed headers.
- TITAN-G221 — API имеет отдельный rate-limit window и maximum request count.
- TITAN-G222 — Logging, API, database и bot settings объединяются в application config, а не импортируются каждым модулем по отдельности.

### Config validation / resilience

- TITAN-G223 — Config validation запускает environment diagnostics только вне production, чтобы не светить existence-check details в production logs.
- TITAN-G224 — Environment diagnostics проверяют наличие Discord token, client ID, guild ID и Postgres connection variables.
- TITAN-G225 — Production database validation принимает как полный connection URL, так и набор POSTGRES_* variables.
- TITAN-G226 — Config validation отделяет сбор ошибок от фактического startup behavior через отдельную `validateConfig(config)` функцию.
- TITAN-G227 — Config modules предпочитают безопасные defaults, позволяя локальному development запускаться без production-only infrastructure.
- TITAN-G228 — Разные подсистемы используют nullable config values для необязательных Discord resources вместо фиктивных IDs.
- TITAN-G229 — Environment parsing выполняется непосредственно на границе config layer, поэтому сервисы получают уже типизированные значения.
- TITAN-G230 — Configuration layer может содержать и декларативные данные, и маленькие pure resolver functions (`getCurrentPrice`, category resolver, count resolver, alias resolver).
- TITAN-G231 — Config helper functions возвращают graceful fallback вместо исключения там, где отсутствие настройки допустимо.
- TITAN-G232 — Общие config constants позволяют runtime-коду не дублировать limits, defaults и semantic labels.
