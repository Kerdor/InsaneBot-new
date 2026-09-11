# GLOBAL DEDUP — BATCH 5

Тематические области: Roles / Progression / Social / Stats / Reports / Events / Integrations / Stream Integrations / Modlog / Quality & Release.

Правило: исходные IDs сохраняются; одинаковые механики объединяются, а уникальные UX, поведение, настройки, ограничения и архитектурные варианты сохраняются внутри канона.

## Roles

### GD-161 — Self-role toggle
Источники: ROLE-001.
Канон: пользователь самостоятельно добавляет или снимает доступную роль; явные add/remove варианты остаются UX-вариантами одной механики.

### GD-162 — Self-role catalog
Источники: ROLE-002.
Канон: пользователь может получить список доступных selfroles.

### GD-163 — Self-role administration
Источники: ROLE-003–004.
Канон: массовая настройка selfroles, очистка конфигурации и автоматическое удаление недействительных role IDs; иерархия ролей проверяется до применения.

### GD-164 — Managed role editing
Источники: ROLE-005–006.
Канон: редактирование имени/цвета управляемой роли с проверкой иерархии Discord; hex-цвет поддерживается как вариант ввода.

## Progression

### GD-165 — Message XP progression
Источники: PROG-001–002.
Канон: сообщения дают XP, XP формирует уровни и хранится для пользователя в рамках сервера.

### GD-166 — Level role rewards
Источники: PROG-003.
Канон: достижение уровня автоматически выдаёт настроенную роль.

### GD-167 — Server leveling configuration
Источник: PROG-004.
Канон: leveling имеет серверные настройки, позволяющие управлять правилами прогрессии и наград.

### GD-168 — Progression rank leaderboard
Источник: PROG-005.
Канон: отдельный rank/leaderboard для XP/уровней; не объединяется с общей economy leaderboard GD-040 или игровыми статистиками.

## Social

### GD-169 — Family/social relations
Источники: SOCIAL-001–003.
Канон: социальные связи между пользователями, включая family/родственные отношения, выделены в самостоятельный social domain.

### GD-170 — AFK status
Источники: SOCIAL-004–007.
Канон: пользователь устанавливает AFK, бот хранит список AFK и уведомляет при упоминании; возвращение/активность снимает AFK.

### GD-171 — Social interaction
Источник: SOCIAL-008.
Канон: fun/social взаимодействие между двумя пользователями.

### GD-172 — Social relationships
Источники: SOCIAL-009–014.
Канон: дружба/отношения оформляются как пользовательские связи с запросом, accept/decline и просмотром списка связей; романтика остаётся типом связи.

### GD-173 — Social compatibility
Источник: SOCIAL-011.
Канон: вычисляемый/рандомизированный compatibility score между двумя пользователями.

### GD-174 — Social leaderboard
Источник: SOCIAL-015.
Канон: отдельные социальные рейтинги не смешиваются с economy/progression leaderboards.

## Stats

### GD-175 — Server counters
Источники: STAT-001–005; также GD-056.
Канон: динамические member/bot/boost/voice counters с автоматическим обновлением; существующий server counters cluster расширяется без создания дубликата.

### GD-176 — User activity statistics
Источники: STAT-006–007.
Канон: накопление текстовой и voice activity пользователя.

### GD-177 — Activity leaderboards
Источники: STAT-008–012.
Канон: рейтинги по общей активности, сообщениям, voice activity, XP и economy; XP/economy используют специализированные каноны GD-168/GD-040, но входят в общий stats surface.

### GD-178 — Server growth statistics
Источник: STAT-013.
Канон: история роста числа участников сервера.

### GD-179 — Moderation statistics
Источники: STAT-014–015.
Канон: агрегированная статистика moderation cases и наиболее часто модерируемых пользователей; не заменяет историю cases GD-136.

### GD-180 — Channel activity statistics
Источники: STAT-016, STAT-023.
Канон: активность и количество сообщений по каналам.

### GD-181 — Activity heatmap
Источник: STAT-017.
Канон: распределение активности по часам/временным периодам в виде heatmap.

### GD-182 — Period statistics
Источник: STAT-018.
Канон: статистика за выбранный период, а не только lifetime counters.

### GD-183 — Personal/server stats cards
Источники: STAT-019–020.
Канон: сводная статистика конкретного пользователя или сервера.

### GD-184 — Game statistics
Источник: STAT-021.
Канон: отдельная статистика игровых действий/результатов; не сливается автоматически с общим activity leaderboard.

### GD-185 — Invite statistics
Источник: STAT-022.
Канон: статистика приглашений/инвайтов как отдельный stats domain.

### GD-186 — Voice time statistics
Источник: STAT-024.
Канон: накопление времени пользователя в voice channels.

### GD-187 — Statistics visualization
Источник: STAT-025.
Канон: charts/графики как отдельный presentation layer для статистики.

## Reports

### GD-188 — Built-in user reports
Источник: REPORT-001.
Канон: отдельная система пользовательских жалоб/репортов, не являющаяся ticket workflow; репорт получает номер и может проходить через text/DM flow.

### GD-189 — Report server selection
Источник: REPORT-002.
Канон: если пользователь имеет несколько общих серверов, DM-flow позволяет выбрать сервер назначения репорта.

### GD-190 — Report anti-spam windows
Источник: REPORT-003.
Канон: несколько anti-spam окон и ограничение одного активного интерактивного report flow на пользователя.

### GD-191 — Report attachments
Источник: REPORT-004.
Канон: вложения являются частью пользовательского репорта.

### GD-192 — Report staff communication tunnel
Источники: REPORT-005–006.
Канон: staff и автор репорта могут общаться через DM tunnel; поддерживаются файлы и закрытие tunnel отдельным действием.

### GD-193 — Sequential report numbering
Источник: REPORT-007.
Канон: отдельная последовательная нумерация репортов на сервере.

## Events

### GD-194 — Persistent scheduled event instances
Источники: EVENT-001–007, EVENT-013–016.
Канон: запланированные event instances сохраняются в persistent storage, переживают restart и исполняются background scheduler; giveaway recovery является специализированным вариантом.

### GD-195 — Giveaway workflow
Источники: EVENT-001–007; GD-054.
Канон: giveaway с условиями участия, несколькими победителями, автоматическим выбором, reroll и восстановлением после restart; существующий giveaway cluster расширяется этими вариантами.

### GD-196 — Birthday automation
Источники: EVENT-008–012; GD-058.
Канон: дата рождения хранится, учитывается timezone пользователя, поздравление публикуется в настроенном канале.

### GD-197 — Recurring events
Источник: EVENT-015.
Канон: scheduler поддерживает повторяющиеся события, а не только одноразовые задания.

### GD-198 — QOTD/daily task events
Источники: EVENT-017–018.
Канон: периодические Question of the Day и daily tasks как специализированные scheduled event types.

### GD-199 — Temporary server events
Источник: EVENT-019.
Канон: временное событие сервера имеет срок жизни и автоматически завершается.

## Integrations

### GD-200 — External service integrations
Источники: INT-001–019.
Канон: интеграции с внешними сервисами/API/webhooks реализуются как отдельные providers/use-cases; конкретные Spotify, Giphy, Imgur, Twitch, GitHub, RSS, OpenAI, Wikipedia, anime/movie/news/weather/translation/dictionary/game/social integrations сохраняются как варианты каталога.

### GD-201 — Integration management/configuration
Источники: INT-024–030.
Канон: интеграции включаются/отключаются на сервере, credentials отделены от guild settings, используется общий registry токенов с устойчивыми ключами и операциями add/update/remove/clear; одно credential set может переиспользоваться несколькими модулями.

### GD-202 — Integration dashboard/web interface
Источники: INT-021–022; существующий web/dashboard слой GD-022.
Канон: web UI для управления интеграциями с OAuth login; не создаётся отдельный общий dashboard cluster.

### GD-203 — Bot API for integrations
Источник: INT-023; GD-022.
Канон: внешний API предоставляет интеграциям программный доступ к функциям бота.

### GD-204 — Webhook authenticity validation
Источник: INT-020.
Канон: входящие webhooks проверяют HMAC/signature до обработки payload.

## Stream integrations

### GD-205 — Multi-provider stream monitoring
Источник: STREAM-001.
Канон: Twitch/YouTube/Picarto/Kick и другие providers приводятся к общей модели stream monitor.

### GD-206 — Multiple independent stream alerts
Источник: STREAM-002.
Канон: сервер может иметь несколько независимых stream subscriptions/alerts.

### GD-207 — Transition-based live alerts
Источники: STREAM-003–004.
Канон: persisted live/offline state позволяет уведомлять только при переходах; live alert может автоматически удаляться после offline.

### GD-208 — YouTube stream filtering
Источники: STREAM-005–006.
Канон: можно игнорировать reruns и scheduled streams, чтобы они не считались обычным live transition.

### GD-209 — Configurable stream mentions
Источники: STREAM-007–008.
Канон: alert поддерживает configurable mention target (`@everyone`, `@here`, role) или режим без mention.

### GD-210 — Stream watch action
Источник: STREAM-009.
Канон: alert содержит кнопку/действие перехода к просмотру стрима.

### GD-211 — Stream API quota control
Источник: STREAM-010.
Канон: manual checks имеют cooldown для ограничения API quota.

### GD-212 — Stream OAuth token refresh
Источник: STREAM-011.
Канон: bearer/OAuth token автоматически обновляется при истечении.

### GD-213 — Shared stream credentials migration
Источник: STREAM-012.
Канон: provider credentials мигрируют из cog-local storage в общий credential registry GD-201.

### GD-214 — Missing-secret owner warning
Источник: STREAM-013.
Канон: при отсутствии обязательного secret owner получает одноразовое предупреждение вместо повторного спама.

### GD-215 — Resilient stream polling
Источник: STREAM-014.
Канон: ошибки API классифицируются, отдельный проблемный stream не останавливает общий polling task.

## Modlog

### GD-216 — Sequential moderation case numbering
Источники: MODLOG-001.
Канон: moderation cases получают стабильный последовательный номер в пределах сервера; расширяет GD-136.

### GD-217 — Moderation case lookup
Источники: MODLOG-002–005, MODLOG-012.
Канон: case можно найти по номеру, получить историю пользователя, компактный/пагинированный список или выполнить lookup по raw user ID без Member fetch.

### GD-218 — Moderation case editing audit
Источники: MODLOG-006–008.
Канон: reason case можно изменить с учётом hierarchy; хранится `amended_by` и timestamp; отсутствие номера может означать последний case как UX shortcut.

### GD-219 — Human-readable case timestamps
Источник: MODLOG-009.
Канон: case metadata отображает Discord-friendly timestamp.

### GD-220 — Configurable case rendering
Источник: MODLOG-010.
Канон: case history поддерживает embed и plain/non-embed rendering.

### GD-221 — Typed moderation cases
Источник: MODLOG-011.
Канон: cases различают типы действий/подсистем, позволяя строить фильтрацию и отчётность поверх общей case model.

## Quality & Release

### GD-222 — Automated test CI
Источник: QUALITY-001; GD-029.
Канон: тесты запускаются автоматически в CI.

### GD-223 — Separate lint pipeline
Источник: QUALITY-002.
Канон: lint/style checks являются отдельным автоматическим quality stage.

### GD-224 — Code security scanning
Источники: QUALITY-003, QUALITY-008.
Канон: CodeQL/Bandit и аналогичные security-oriented scans интегрируются в repository automation.

### GD-225 — Reproducible dependency set
Источник: QUALITY-004.
Канон: зависимости фиксируются/компилируются так, чтобы установка и release были воспроизводимыми.

### GD-226 — Automated contribution metadata checks
Источник: QUALITY-005.
Канон: CI автоматически проверяет обязательные contribution/repository metadata.

### GD-227 — Translation automation
Источник: QUALITY-006.
Канон: перевод/локализация имеет автоматизированный workflow.

### GD-228 — Staged release workflow
Источник: QUALITY-007.
Канон: подготовка и публикация релиза разделены на отдельные контролируемые этапы.

### GD-229 — Git blame noise control
Источник: QUALITY-009.
Канон: repository configuration позволяет исключать шумные массовые изменения из git blame.

## Cross-theme notes

- ROLE-001 selfrole и существующий GD-057 self-service role panels не являются двумя разными системами: GD-161 описывает пользовательскую toggle-механику, GD-163 — её административную конфигурацию.
- STAT-001–005 расширяют существующий GD-056 server counters; новый cluster не создаётся.
- XP leaderboard из STAT-011 связан с GD-168, economy leaderboard — с GD-040.
- Moderation statistics не заменяют moderation case history GD-136/GD-217.
- REPORTS намеренно не объединены с TICKETS: report — отдельный канал пользовательской жалобы и DM communication tunnel.
- EVENT-020 background tasks покрываются общим GD-015; в Batch 5 сохраняются только event-specific механики.
- Giveaways и birthdays уже существовали как GD-054/GD-058 и расширены без создания дублей.
- Integration dashboard/API не создают отдельную архитектуру поверх GD-022.
- Stream credentials используют общий credential registry GD-201; OAuth refresh остаётся provider-specific поведением.
- Modlog case model расширяет GD-136; отдельные lookup/edit/render механики сохранены только там, где они добавляют самостоятельный UX или metadata.
- Quality/release mechanics относятся к development/repository lifecycle и не являются runtime системами бота.
