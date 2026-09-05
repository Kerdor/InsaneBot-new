# Python Discord — Recruitment / Talent Pool

## PDIS-R001 — Message-context nomination via Discord Context Menu
Пользователя можно номинировать прямо с конкретного сообщения через Discord Context Menu, сохраняя ссылку на исходное сообщение как доказательный контекст.

## PDIS-R002 — Optional nomination context modal
Перед созданием номинации модальное окно позволяет добавить свободный дополнительный контекст; поле необязательное и ограничено с учётом автоматически добавляемой ссылки на источник.

## PDIS-R003 — Automatic source-message attribution
Каждая nomination из сообщения автоматически содержит jump URL исходного сообщения, а не полагается только на текстовое описание модератора.

## PDIS-R004 — Immediate private nomination confirmation + staff-channel event
После номинации пользователь получает ephemeral-подтверждение, а отдельный staff-канал получает публичное событие о новой номинации.

## PDIS-R005 — Relay nomination updates into active review thread
Если по пользователю уже идёт review thread, новые номинации/контекст автоматически пересылаются прямо в этот thread.

## PDIS-R006 — Force nomination from any channel
Staff-команда позволяет принудительно добавить пользователя в talent pool из любого канала с необязательной причиной.

## PDIS-R007 — Multiple aliases for high-frequency staff action
Часто используемая staff-команда имеет набор коротких aliases (`fw`, `fa`, `fn`, `forcewatch`) для быстрого вызова.

## PDIS-R008 — Persistent switch for automated review
Автоматический review можно включать/выключать отдельной командой, а состояние хранится в Redis и переживает перезапуск.

## PDIS-R009 — Safe autoreview shutdown with execution lock
При отключении autoreview loop сначала захватывается lock, чтобы не отменить выполняющийся review посередине операции.

## PDIS-R010 — Autoreview status command
Отдельная команда показывает текущее состояние автоматического review без изменения настройки.

## PDIS-R011 — Review eligibility based on multiple independent gates
Кандидат проходит несколько условий одновременно: активная nomination, ещё не reviewed, минимальный возраст nomination, недавняя активность и наличие пользователя на сервере.

## PDIS-R012 — Two-dimensional review priority scoring
Приоритет review рассчитывается из количества nomination entries и возраста nomination с настраиваемым весом между этими факторами.

## PDIS-R013 — Review capacity by simultaneous and total limits
Система ограничивает одновременно открытые reviews и общее количество недавних reviews, чтобы очередь голосований не разрасталась бесконтрольно.

## PDIS-R014 — Minimum interval between automated reviews
Даже при наличии кандидатов следующий review не публикуется раньше заданного минимального интервала.

## PDIS-R015 — Redis-backed last-review timestamp
Время последнего review сохраняется отдельно в Redis; при отсутствии значения система явно допускает ранний первый запуск.

## PDIS-R016 — Activity-aware automatic pruning
Активные, но ещё не reviewed nominations автоматически удаляются из talent pool после заданного периода полной бездеятельности.

## PDIS-R017 — Reviewed nominations protected from inactivity pruning
Даже неактивная nomination не удаляется автоматическим prune, если пользователь уже прошёл review.

## PDIS-R018 — Activity indicators in administrative nomination list
В списке nominations можно визуально помечать пользователей, которые пока не соответствуют требованию недавней активности.

## PDIS-R019 — Multiple administrative ordering modes
Staff может просматривать talent pool в сгруппированном виде либо отдельно сортировать nominations от старых к новым и наоборот.

## PDIS-R020 — Grouped queue view by workflow state
Один список одновременно показывает `Being Reviewed`, `Recent Nominations` и остальные nominations в порядке autoreview priority.

## PDIS-R021 — Recent nominations cooldown bucket
Недавние nominations выводятся отдельной группой и временно не допускаются до autoreview, вместо того чтобы просто скрываться.

## PDIS-R022 — Nomination batch splitting under Discord message limit
Большое количество nomination entries автоматически разбивается на несколько сообщений перед публикацией в review thread.

## PDIS-R023 — Reverse chronological nomination evidence
При формировании review новые nomination entries выводятся первыми, чтобы свежий контекст был виден раньше старого.

## PDIS-R024 — Pinning split evidence messages in reverse order
Разбитые сообщения с доказательствами pin-ятся в обратном порядке, чтобы ключевой заголовок оставался первым в списке pins.

## PDIS-R025 — Dedicated voting thread per candidate
Каждый review создаёт отдельный Discord thread, куда складываются nomination evidence и обсуждение кандидата.

## PDIS-R026 — Reviewer acknowledgement reaction + decision reactions
Review содержит отдельную случайную реакцию для отметки ознакомления и стандартные positive/negative реакции для решения.

## PDIS-R027 — Vote archive with decision and reaction statistics
После завершения голосования система переносит его в архив, сохраняя результат, дату, jump URL thread и количество уникальных reviewer/up/down reactions.

## PDIS-R028 — Archive preserves vote body while removing live voting message
В архив переносится очищенное тело review без служебных opening/closing абзацев, после чего исходное voting-сообщение удаляется.

## PDIS-R029 — Automatic thread archival after vote completion
Связанный review thread автоматически архивируется после переноса результата, с graceful fallback если thread больше недоступен.

## PDIS-R030 — Thread bump integration for active review
После создания review thread он автоматически регистрируется в отдельной системе thread bumping, если соответствующий модуль доступен.

## PDIS-R031 — Nomination lifecycle metadata
Nomination хранит не только активность, но и время завершения, причину завершения, статус reviewed и связанный review thread ID.

## PDIS-R032 — Query nomination by actor and nominee
API позволяет найти конкретную nomination entry по паре `nominee + actor`, что удобно для адресного редактирования или проверки вклада конкретного сотрудника.

## PDIS-R033 — Flexible nomination API filters
API поддерживает независимые фильтры по user, active, reviewed и ordering, позволяя строить разные административные представления поверх одной модели.

## PDIS-R034 — Typed API boundary with Pydantic models
Ответы внешнего API валидируются через типизированные Pydantic-модели до использования в Discord-логике.

## PDIS-R035 — Bulk activity lookup for candidate queues
Активность всех кандидатов запрашивается одним API-вызовом с массивом user IDs, вместо отдельного запроса на каждого пользователя.

## PDIS-R036 — Ephemeral error isolation for nomination failures
Ошибки пользовательского nomination flow обрабатываются отдельно от основного канала: инициатор получает приватную ошибку, а staff workflow не загрязняется техническими деталями.
