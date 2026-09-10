# GAwesomeBot — Configurations

Источник: `GAwesomeBot/bot`
Ветка: `indev-4.0.2`
Каталог: `Configurations/`

## Command registry

- **GAB-CONF-001** — Единый реестр команд хранит PM, Public и Shared namespaces.
- **GAB-CONF-002** — Metadata команды включает человекочитаемый `usage`.
- **GAB-CONF-003** — Public-команда имеет отдельное `description`, пригодное для динамического help.
- **GAB-CONF-004** — Команды группируются по тематическим категориям для help/UI.
- **GAB-CONF-005** — Для Public-команды задаются default `isEnabled`, `isNSFWFiltered` и `adminLevel`.
- **GAB-CONF-006** — Настройки доступа команды описываются metadata, а не зашиваются отдельно в обработчике каждой команды.
- **GAB-CONF-007** — Отдельный `adminExempt` позволяет исключить отдельную команду из некоторых обычных ограничений.
- **GAB-CONF-008** — Алиасы команды задаются рядом с её metadata.
- **GAB-CONF-009** — Shared-команда вместо обычного adminLevel использует именованное permission (`perm`).
- **GAB-CONF-010** — Для developer-команд можно явно указать `perm: none`.
- **GAB-CONF-011** — Usage поддерживает литеральные значения, необязательные аргументы и альтернативный синтаксис как часть документации команды.
- **GAB-CONF-012** — PM-команды также описываются в общем registry, сохраняя единый источник metadata.
- **GAB-CONF-013** — Registry может служить исполняемой документацией: help и runtime используют одни и те же данные.
- **GAB-CONF-014** — Категория может содержать визуальный маркер/emoji для более понятной группировки команд.
- **GAB-CONF-015** — NSFW-фильтрация является свойством конкретной команды и может включаться по умолчанию.
- **GAB-CONF-016** — Некоторые NSFW-команды по умолчанию выключены, даже если их runtime handler существует.

## Global runtime configuration

- **GAB-CONF-017** — Количество Discord shards задаётся конфигурацией и допускает специальное значение `auto`.
- **GAB-CONF-018** — Базовый hosting URL вынесен в конфигурацию и используется при генерации ссылок бота.
- **GAB-CONF-019** — HTTP и HTTPS ports задаются отдельно.
- **GAB-CONF-020** — HTTPS можно включить отдельным флагом redirect при наличии certificate/private key.
- **GAB-CONF-021** — Пути certificate и private key являются отдельными настройками.
- **GAB-CONF-022** — Web server bind IP вынесен в конфигурацию.
- **GAB-CONF-023** — MongoDB connection URL и имя database вынесены в отдельный блок.
- **GAB-CONF-024** — Sentry DSN вынесен в отдельный блок конфигурации.
- **GAB-CONF-025** — OAuth invite URL хранится как шаблон с подстановкой bot ID.
- **GAB-CONF-026** — Уровень консольного логирования и уровень файлового логирования задаются независимо.
- **GAB-CONF-027** — Поддерживаются уровни `error`, `warn`, `info`, `debug`, `verbose`.
- **GAB-CONF-028** — Отдельный secret используется для подписи session hashes.
- **GAB-CONF-029** — Отдельный encryption password используется для шифрования части database values.
- **GAB-CONF-030** — Encryption IV хранится отдельно от encryption password.
- **GAB-CONF-031** — Конфигурация явно предупреждает, что изменение encryption password/IV после создания данных делает зашифрованные данные недоступными.
- **GAB-CONF-032** — Для encryption IV задаётся ограничение длины.
- **GAB-CONF-033** — Invite-ссылка сервера может быть отдельной глобальной настройкой для about/help.
- **GAB-CONF-034** — Текст и список способов поддержки проекта могут конфигурироваться отдельно от web-логики.
- **GAB-CONF-035** — Формат отображения дат вынесен в конфигурацию.
- **GAB-CONF-036** — Набор фраз, распознаваемых как положительная реакция/подтверждение, централизован.
- **GAB-CONF-037** — Набор trigger-фраз для пользовательских голосов/реакций централизован.
- **GAB-CONF-038** — Ошибочные сообщения имеют пул случайных текстов вместо одного фиксированного ответа.

## Access / maintainer configuration

- **GAB-CONF-039** — Список обычных maintainers задаётся отдельно от sudo-maintainers.
- **GAB-CONF-040** — Wiki contributors хранятся отдельным списком прав.
- **GAB-CONF-041** — Пользователи могут иметь глобальный blocklist.
- **GAB-CONF-042** — Guilds могут иметь отдельный глобальный blocklist.
- **GAB-CONF-043** — Activity-related blocklist существует отдельно от общего user/guild blocklist.
- **GAB-CONF-044** — Activity бота конфигурируется именем, типом и Twitch URL.
- **GAB-CONF-045** — Статус бота задаётся независимо от activity.
- **GAB-CONF-046** — Web header image и homepage HTML могут задаваться конфигурацией.
- **GAB-CONF-047** — PM forwarding включается отдельным глобальным boolean-флагом.
- **GAB-CONF-048** — Версия и branch бота доступны как конфигурационные идентификаторы.
- **GAB-CONF-049** — Maintainer permissions представлены именованной таблицей уровней (`eval`, `sudo`, `management`, `administration`, `shutdown`).
- **GAB-CONF-050** — Разные developer capabilities могут требовать разные уровни maintainer authority.
- **GAB-CONF-051** — Web-инъекции разделены на `headScript` и `pageScript`.

## Event routing

- **GAB-CONF-052** — Event registry связывает Discord event names с массивом обработчиков.
- **GAB-CONF-053** — На один Discord event можно назначить несколько независимых handlers.
- **GAB-CONF-054** — Event handler names хранятся без `.js`, оставляя загрузчику единый формат именования.
- **GAB-CONF-055** — Системные handlers распределяются по отдельным событиям: guild, member, role, emoji, ban, channel, message, user, presence, voice и lifecycle.
- **GAB-CONF-056** — Message event может последовательно запускать несколько независимых pipeline handlers.
- **GAB-CONF-057** — Message pipeline может включать spam, vote, AFK, username и shared-command обработчики.
- **GAB-CONF-058** — Неиспользуемые handlers можно оставить неактивными, не удаляя саму точку расширения.
- **GAB-CONF-059** — Отдельные события message create и message update могут иметь разные handler pipelines.
- **GAB-CONF-060** — User update может иметь несколько специализированных обработчиков одновременно.

## Static data / content configuration

- **GAB-CONF-061** — Уровни активности задаются внешним JSON как ordered thresholds `name + max_score`.
- **GAB-CONF-062** — Названия rank-уровней полностью отделены от алгоритма подсчёта score.
- **GAB-CONF-063** — RSS feeds хранятся внешним списком с уникальным ID и URL.
- **GAB-CONF-064** — RSS feed может иметь собственное streaming enable/disable состояние.
- **GAB-CONF-065** — Для RSS streaming хранится отдельный список разрешённых channel IDs.
- **GAB-CONF-066** — Status messages хранятся как наборы вариантов по типу события, позволяя случайный выбор текста.
- **GAB-CONF-067** — В шаблонах status messages используется placeholder `@user`.
- **GAB-CONF-068** — Join, online, offline, leave, ban и unban имеют отдельные пулы сообщений.
- **GAB-CONF-069** — Tag reactions хранятся отдельным пулом шаблонов с пользовательским placeholder.
- **GAB-CONF-070** — Предзаполненные tags хранятся как отдельные записи `id + content`.
- **GAB-CONF-071** — Large static content (например trivia dataset) может жить во внешнем JSON, а не внутри command handler.
- **GAB-CONF-072** — Trivia question dataset хранит category, question и answer как независимые поля.
- **GAB-CONF-073** — Категория trivia является частью данных вопроса и может использоваться для выбора тематического набора.
- **GAB-CONF-074** — Список profanity/NSFW-фраз вынесен из кода в отдельный JSON.
- **GAB-CONF-075** — Filter dictionary содержит варианты с заменой символов/leetspeak, а не только точные слова.
- **GAB-CONF-076** — Static dictionaries можно обновлять без переписывания логики команд.

## Architecture ideas

- **GAB-CONF-077** — Разделять runtime configuration, permission configuration и static content по разным файлам.
- **GAB-CONF-078** — Использовать template-файлы как документированный контракт обязательных настроек.
- **GAB-CONF-079** — Секреты и API credentials не смешивать с обычными runtime preferences.
- **GAB-CONF-080** — Системные defaults держать рядом с metadata команды, чтобы команда имела самодостаточное описание поведения по умолчанию.
- **GAB-CONF-081** — Внешние content dictionaries позволяют менять тексты, rank names, tags и quiz data без изменения обработчиков.
- **GAB-CONF-082** — Event routing через registry позволяет добавлять/отключать обработчики декларативно.
- **GAB-CONF-083** — Несколько handlers на одно событие позволяют собирать модульный event pipeline.
- **GAB-CONF-084** — Глобальные blocklists должны быть отдельными от локальных серверных ограничений.
- **GAB-CONF-085** — Permission levels лучше хранить как именованные capabilities, а не как набор разбросанных boolean-флагов.
- **GAB-CONF-086** — Конфигурация должна явно документировать необратимые последствия изменения криптографических параметров.
