# TitanBot — Tickets

Источник: `codebymitch/TitanBot`
Раздел: `src/commands/Ticket/` и связанные service/database/handler/config paths

## Ticket system

- **TT-001** — Единая ticket-система с панелью создания тикетов.
- **TT-002** — Persistent-конфигурация ticket-панели.
- **TT-003** — Кастомный текст панели.
- **TT-004** — Ограничение текста панели Discord-лимитом 2000 символов.
- **TT-005** — Кастомная подпись кнопки создания тикета.
- **TT-006** — Ограничение label кнопки 80 символами.
- **TT-007** — Настраиваемая staff role для управления тикетами.
- **TT-008** — Выбор staff role через Role Select.
- **TT-009** — Настраиваемая категория открытых тикетов.
- **TT-010** — Выбор категории через Channel Select.
- **TT-011** — Ограничение выбора категории только GuildCategory.
- **TT-012** — Отдельная категория для закрытых/архивных тикетов.
- **TT-013** — Настраиваемая категория закрытых тикетов через Channel Select.
- **TT-014** — Лимит одновременно открытых тикетов на пользователя.
- **TT-015** — Настройка лимита открытых тикетов в диапазоне 1–10.
- **TT-016** — Значение лимита по умолчанию 3.
- **TT-017** — Переключатель DM-уведомления пользователя при закрытии.
- **TT-018** — Dashboard для настройки ticket-системы.
- **TT-019** — Отображение текущих ticket-настроек в dashboard.
- **TT-020** — Обновление dashboard после изменения настройки.
- **TT-021** — Эфемерный dashboard, не засоряющий канал.
- **TT-022** — Сессия dashboard привязана к инициатору.
- **TT-023** — Collector dashboard принимает взаимодействия только инициатора.
- **TT-024** — Ограниченный срок жизни collector для выбора роли/категории.
- **TT-025** — Таймаут role/category collector 60 секунд.
- **TT-026** — Таймаут ожидания modal-ввода 120 секунд.
- **TT-027** — Безопасное завершение dashboard-сессии после timeout.
- **TT-028** — Refresh/reload dashboard без создания новой конфигурации.
- **TT-029** — Проверка доступности ticket panel message.
- **TT-030** — Восстановление панели через repost после удаления сообщения.
- **TT-031** — Обнаружение отсутствующей панели без падения системы.
- **TT-032** — Инструкция администратора repost-нуть панель при её отсутствии.
- **TT-033** — Live-обновление существующей панели после изменения текста.
- **TT-034** — Live-обновление label кнопки после изменения конфигурации.
- **TT-035** — Сохранение конфигурации на уровне guild.

## Ticket creation and lifecycle

- **TT-036** — Создание отдельного текстового канала под каждый тикет.
- **TT-037** — Уникальный ticket number на guild.
- **TT-038** — Инкремент ticket counter отдельно для каждого сервера.
- **TT-039** — Форматирование номера тикета с ведущими нулями.
- **TT-040** — Использование ticket number в имени/идентификации тикета.
- **TT-041** — Ticket record привязан к guild и channel.
- **TT-042** — Persistent ticket record в БД.
- **TT-043** — Хранение creator пользователя в ticket record.
- **TT-044** — Хранение состояния open/closed тикета.
- **TT-045** — Хранение времени создания тикета.
- **TT-046** — Хранение времени закрытия тикета.
- **TT-047** — Хранение claim state.
- **TT-048** — Хранение пользователя, взявшего тикет.
- **TT-049** — Хранение времени claim.
- **TT-050** — Хранение priority тикета.
- **TT-051** — Хранение feedback/rating данных.
- **TT-052** — Проверка существующего открытого тикета пользователя перед созданием.
- **TT-053** — Ограничение количества открытых тикетов пользователя.
- **TT-054** — Быстрый PostgreSQL-запрос для подсчёта открытых тикетов.
- **TT-055** — Fallback на DB key scan при отсутствии оптимизированного PostgreSQL пути.
- **TT-056** — Ticket list не считает служебные counter keys тикетами.
- **TT-057** — Permission context загружает ticket config и ticket data параллельно.
- **TT-058** — Guild-only защита ticket interactions.
- **TT-059** — Creator имеет право закрыть собственный тикет.
- **TT-060** — Staff role получает право управлять тикетом.
- **TT-061** — ManageChannels даёт ticket-management доступ.
- **TT-062** — Проверка прав через единый ticket permission context.
- **TT-063** — Timeout permission-check запроса 2.5 секунды.
- **TT-064** — Отдельная typed ошибка для rate-limit при permission check.

## Permissions and channel security

- **TT-065** — Permission validation перед операциями с ticket channel.
- **TT-066** — Проверка возможности управлять каналами до destructive actions.
- **TT-067** — Разделение прав creator и staff.
- **TT-068** — Централизованная функция проверки ticket management permissions.
- **TT-069** — Запрет управления тикетом пользователем без подходящей роли/права.
- **TT-070** — Безопасное завершение interaction при отсутствии guild context.

## Claim / close / reopen / priority

- **TT-071** — Claim тикета staff-пользователем.
- **TT-072** — Сохранение claimedBy и claimedAt.
- **TT-073** — Unclaim снимает claimedBy.
- **TT-074** — Unclaim снимает claimedAt.
- **TT-075** — Только claimer может сделать unclaim без расширенных прав.
- **TT-076** — ManageChannels позволяет staff снять чужой claim.
- **TT-077** — Логирование claim/unclaim событий.
- **TT-078** — Закрытие переводит ticket в closed state.
- **TT-079** — При закрытии фиксируется close timestamp.
- **TT-080** — Настраиваемая категория для закрытых тикетов.
- **TT-081** — Архивирование закрытого тикета через перенос в closed category.
- **TT-082** — DM creator после закрытия при включённой настройке.
- **TT-083** — Ошибка DM не должна ломать закрытие тикета.
- **TT-084** — Priority-система с несколькими уровнями.
- **TT-085** — Priority `none` как состояние по умолчанию.
- **TT-086** — Priority `low`.
- **TT-087** — Priority `medium`.
- **TT-088** — Priority `high`.
- **TT-089** — Priority `urgent`.
- **TT-090** — Для priority используются label, emoji и color.
- **TT-091** — Логирование изменения priority.
- **TT-092** — Pin ticket message/channel state как отдельная операция.
- **TT-093** — Unpin ticket как отдельная операция.
- **TT-094** — Логирование pin/unpin событий.

## Delete / transcripts

- **TT-095** — Удаление тикета с configurable delay.
- **TT-096** — Предупреждение перед фактическим удалением канала.
- **TT-097** — Логирование delete event до удаления канала.
- **TT-098** — Попытка сформировать transcript перед удалением.
- **TT-099** — Отправка transcript в отдельный настроенный канал.
- **TT-100** — Настраиваемый transcript channel.
- **TT-101** — Проверка возможности отправить transcript в destination channel.
- **TT-102** — Transcript generation failure не блокирует удаление тикета.
- **TT-103** — Transcript send failure не блокирует удаление тикета.
- **TT-104** — Transcript/delete ошибки изолируются и логируются.
- **TT-105** — Удаление Discord channel после завершения ticket cleanup.
- **TT-106** — Обработка уже отсутствующего channel без падения.
- **TT-107** — Отдельный audit/log event для удаления тикета.

## Logging

- **TT-108** — Отдельный ticket logging subsystem.
- **TT-109** — Отдельный ticket logs channel.
- **TT-110** — Разделение общего ticket log и transcript destination.
- **TT-111** — Настройка logs channel через dashboard.
- **TT-112** — Ticket log event type `open`.
- **TT-113** — Ticket log event type `close`.
- **TT-114** — Ticket log event type `delete`.
- **TT-115** — Ticket log event type `claim`.
- **TT-116** — Ticket log event type `unclaim`.
- **TT-117** — Ticket log event type `priority`.
- **TT-118** — Ticket log event type `pin`.
- **TT-119** — Ticket log event type `unpin`.
- **TT-120** — Ticket log event type `feedback`.
- **TT-121** — Проверка SendMessages перед ticket logging.
- **TT-122** — Проверка EmbedLinks перед ticket logging.
- **TT-123** — Ticket log может содержать attachment.
- **TT-124** — Ошибка логирования не ломает основную ticket-операцию.
- **TT-125** — Централизованный ticket logging helper.

## Feedback

- **TT-126** — Система оценки закрытого тикета.
- **TT-127** — Rating хранится вместе с ticket feedback.
- **TT-128** — Comment к feedback хранится отдельно от rating.
- **TT-129** — Timestamp создания feedback.
- **TT-130** — Timestamp обновления feedback.
- **TT-131** — Только creator тикета может отправить feedback.
- **TT-132** — Feedback modal для текстового комментария.
- **TT-133** — Отдельный modal handler для feedback comment.
- **TT-134** — Feedback сохраняется в отдельной persistence-модели.
- **TT-135** — Feedback logging отделён от feedback save.
- **TT-136** — Ошибка feedback logging не отменяет сохранение feedback.
- **TT-137** — Статистика количества feedback по тикетам.
- **TT-138** — Средняя оценка тикетов в guild statistics.

## Statistics / administration

- **TT-139** — Ticket statistics по guild.
- **TT-140** — Количество открытых тикетов.
- **TT-141** — Количество закрытых тикетов.
- **TT-142** — Среднее время закрытия тикета.
- **TT-143** — Количество оставленных feedback.
- **TT-144** — Средний rating.
- **TT-145** — Dashboard показывает состояние ticket system.
- **TT-146** — Dashboard позволяет менять staff role.
- **TT-147** — Dashboard позволяет менять open category.
- **TT-148** — Dashboard позволяет менять closed category.
- **TT-149** — Dashboard позволяет менять max-open-ticket limit.
- **TT-150** — Dashboard позволяет менять DM-on-close.
- **TT-151** — Dashboard позволяет менять transcript channel.
- **TT-152** — Dashboard позволяет менять logs channel.
- **TT-153** — Dashboard позволяет менять panel text.
- **TT-154** — Dashboard позволяет менять create-button label.
- **TT-155** — Изменения настроек сохраняются до следующего запуска бота.

## Robustness / architecture

- **TT-156** — Ticket service отделён от command/UI слоя.
- **TT-157** — Ticket database helpers отделены от business logic.
- **TT-158** — Ticket permissions вынесены в отдельный utility module.
- **TT-159** — Ticket logging вынесен в отдельный utility module.
- **TT-160** — Button interactions вынесены в отдельный handler.
- **TT-161** — Feedback interactions вынесены в отдельные handlers.
- **TT-162** — Typed ticket-related errors для предсказуемой обработки.
- **TT-163** — Параллельная загрузка независимых конфигурационных данных.
- **TT-164** — Ошибки отдельных подсистем изолируются.
- **TT-165** — Graceful handling missing guild/channel/message.
- **TT-166** — DB records используются для восстановления состояния после рестарта.
- **TT-167** — Ticket counter и ticket records разделены в persistence layer.
- **TT-168** — Обработка legacy/неожиданного состояния ticket records без падения.
- **TT-169** — Ticket list/statistics строятся на persistent records, а не только на Discord cache.
- **TT-170** — Единый lifecycle ticket: create → open → claim → priority/pin → close → feedback → transcript/delete.
