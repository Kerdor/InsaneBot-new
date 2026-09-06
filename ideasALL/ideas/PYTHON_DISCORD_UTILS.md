# Python Discord — Utilities

## PDIS-U001 — Consent-gated automatic attachment upload
Для текстовых вложений бот сначала предлагает пользователю загрузить их во внешний paste-сервис и требует явного подтверждения реакцией.

## PDIS-U002 — Automatic paste deletion workflow
После загрузки пользователь получает приватную ссылку удаления paste; отдельной реакцией можно удалить paste и сообщение бота.

## PDIS-U003 — Attachment deletion tracking during pending workflow
Если исходное сообщение с вложениями удалено до подтверждения, ожидающая операция автоматически отменяется.

## PDIS-U004 — Batch attachment paste
Несколько текстовых вложений одного сообщения объединяются в одну paste-операцию.

## PDIS-U005 — Reminder opt-in by third parties
Посторонний пользователь может нажать `Notify me` на чужом reminder и подписаться на его доставку без изменения самого reminder автора.

## PDIS-U006 — Expiring reminder opt-in UI
Кнопка подписки на reminder живёт ограниченное время и автоматически исчезает после истечения reminder/таймаута.

## PDIS-U007 — Reminder opt-in live participant list
После нового opt-in embed обновляется и сразу показывает актуальный список тех, кто будет уведомлён.

## PDIS-U008 — Reminder mention permissions by role tier
Обычным участникам разрешены только собственные reminders; более высокие роли получают дополнительные возможности упоминать участников, а роли — только с более высоким уровнем прав.

## PDIS-U009 — Reminder channel whitelist for regular users
Для пользователей без staff/community ролей reminders разрешены только в специально заданных каналах.

## PDIS-U010 — Per-user active reminder quota
Количество активных reminders ограничено на пользователя, чтобы система не превращалась в бесконечный scheduler.

## PDIS-U011 — Reminder content inherited from reply
Если текст reminder не указан, бот автоматически берёт содержимое сообщения, на которое пользователь отвечает.

## PDIS-U012 — Attachment/embed-safe reply fallback text
Если referenced message не имеет текста, reminder получает понятный fallback вроде `See referenced message`, вместо пустого reminder.

## PDIS-U013 — Reminder delivery reply with fallback send
Сначала reminder пытается ответить на исходное сообщение; при HTTP-ошибке автоматически переключается на обычную отправку в канал.

## PDIS-U014 — Overdue reminder detection after restart
При загрузке bot проверяет активные reminders: просроченные доставляются сразу с отдельным состоянием `should have arrived earlier`.

## PDIS-U015 — Reminder persistence with scheduler reconstruction
После перезапуска scheduler восстанавливает все активные reminders из API, а не полагается на память процесса.

## PDIS-U016 — Reminder self-service editing by separate dimensions
Reminder можно отдельно изменять по времени, содержимому и списку упоминаний, сохраняя единый общий механизм reschedule.

## PDIS-U017 — Admin modification confirmation for another user's reminder
Администратор может редактировать/удалять чужой reminder, но операция требует явного подтверждения через кнопки.

## PDIS-U018 — Timed destructive-action confirmation
Подтверждение редактирования чужого reminder автоматически отменяется по таймауту и очищает UI.

## PDIS-U019 — Bulk reminder deletion with partial-success reporting
Удаление нескольких reminders одной командой возвращает отдельно успешно удалённые и неуспешные ID, объясняя причины неудачи.

## PDIS-U020 — Reminder operation locking by resource ID
Редактирование, удаление, opt-in и доставка одного reminder сериализуются через lock конкретного ID, предотвращая гонки.

## PDIS-U021 — Extension wildcard semantics with two scopes
Для управления расширениями `*` означает текущие загруженные расширения, а `**` может включать также выгруженные.

## PDIS-U022 — Batch extension progress message
Массовая операция над расширениями сначала показывает единое состояние `in progress`, а затем редактирует его итоговым отчётом.

## PDIS-U023 — Batch extension partial-failure report
При массовом load/unload/reload бот продолжает обработку остальных расширений и в конце перечисляет только упавшие операции с ошибками.

## PDIS-U024 — Extension global operation mutex
Параллельный запуск второго batch-действия блокируется единым флагом, чтобы операции над runtime-модулями не пересекались.

## PDIS-U025 — Reload fallback to load
Если reload встречает уже выгруженное расширение, операция автоматически превращается в load вместо безусловного failure.

## PDIS-U026 — Runtime extension health map by category
Список extensions группируется по структуре модулей и одновременно показывает loaded/unloaded статус каждого элемента.

## PDIS-U027 — Safe extension unload blacklist
Критические расширения явно исключаются из wildcard unload, чтобы пользовательская команда не отключила собственную инфраструктуру управления.

## PDIS-U028 — Multi-dimensional latency probe
Команда ping одновременно измеряет latency обработки сообщения, health внешнего сайта и Discord WebSocket latency.

## PDIS-U029 — WebSocket event-rate diagnostics
Internal-инструмент ведёт счётчик каждого типа Discord socket event и показывает топ событий плюс среднюю скорость событий/сек.

## PDIS-U030 — Persistent REPL state with reset command
Internal Python REPL сохраняет переменные между вызовами и имеет отдельный `exit`-reset, который очищает историю окружения и номер строки.

## PDIS-U031 — REPL output pretty-print with truncation tiers
REPL форматирует сложные значения через pretty-printer, ограничивает число строк/символов и при превышении переносит полный вывод в paste.

## PDIS-U032 — Snekbox per-user execution lock
Пользователь не может одновременно запустить несколько sandbox jobs; повторная команда получает понятное сообщение ожидания.

## PDIS-U033 — Multi-version code rerun buttons
После выполнения sandbox-кода пользователь может одной кнопкой повторно запустить тот же job в другой поддерживаемой версии Python.

## PDIS-U034 — Version-specific runtime variants
Один и тот же execution API поддерживает обычный CPython, free-threaded и JIT-enabled варианты как отдельные selectable runtime versions.

## PDIS-U035 — Edit-and-react code rerun loop
В течение короткого окна пользователь может отредактировать исходное сообщение и подтвердить повторный запуск специальной реакцией.

## PDIS-U036 — Stale-response protection for reruns
Перед повторным запуском система проверяет, что response ID всё ещё является последним ответом этой invocation, предотвращая гонку между edit-rerun и version-button rerun.

## PDIS-U037 — Multiple-codeblock execution semantics
Несколько fenced code blocks в одном сообщении объединяются в один job, а обычный текст между ними игнорируется.

## PDIS-U038 — First-block-as-setup for timeit
Для `timeit` первый code block рассматривается как setup и не измеряется, остальные блоки объединяются в измеряемый код.

## PDIS-U039 — Output line numbering
Многострочный sandbox output автоматически получает номера строк для удобного обсуждения и поиска проблем.

## PDIS-U040 — Mention neutralisation in untrusted code output
Вывод пользовательского кода экранирует mention syntax, чтобы программа не могла случайно массово пинговать Discord-пользователей.

## PDIS-U041 — Markdown/escape attack detection in code output
Подозрительные escape-последовательности в sandbox output не выводятся напрямую: полный результат отправляется в paste, а Discord получает безопасное сообщение о блокировке.

## PDIS-U042 — ANSI stripping before external output archive
Перед отправкой полного вывода в paste ANSI escape sequences удаляются, чтобы внешний архив не получал мусорные terminal control codes.

## PDIS-U043 — Typed output-file size and count enforcement
Результаты sandbox ограничиваются одновременно максимальным размером каждого файла и общим количеством файлов; превышения превращаются в понятный список failed files.

## PDIS-U044 — Failed-file diagnostics preserve filenames
Даже если файл результата нельзя вернуть из-за размера/лимита, его имя сохраняется и показывается пользователю с причиной failure.

## PDIS-U045 — Automatic Discord-safe filename normalization
Файлы из sandbox перед отправкой получают нормализованное имя: ANSI/backslash и недопустимые Discord символы заменяются безопасными символами.

## PDIS-U046 — Shared output budget across stdout and generated text files
Лимит ответа считается общим бюджетом для stdout и содержимого текстовых файлов; маленькие файлы можно встроить целиком, большие занимают оставшийся бюджет.

## PDIS-U047 — Small-file inline exception
Очень маленькие однострочные текстовые файлы выводятся непосредственно в Discord даже при общем ограничении, чтобы ссылка не была менее удобной, чем сам текст.

## PDIS-U048 — Extension-aware output filtering
Файлы sandbox output дополнительно прогоняются через серверный filtering engine; запрещённые расширения блокируются отдельно от уже сформированного stdout.

## PDIS-U049 — Output filter circumvention alert
Если sandbox output пытается обойти фильтр, пользователю показывается нейтральное сообщение, а moderation team получает сигнал об атаке.

## PDIS-U050 — Context-sensitive sandbox output routing
Sandbox-команда может автоматически перенаправляться в специальный bot-command канал, но staff/helper роли могут обходить это правило.
