# TITAN APPLICATIONS — Банк идей

Находки `codebymitch/TitanBot` (main), `Community/apply.js` и `Community/app-admin.js`.

- TITAN-A001 — Role application system позволяет пользователям выбирать доступную заявку через autocomplete, затем заполнять её через Discord Modal.
- TITAN-A002 — Каждая application привязана к Discord role, а конфигурация может задавать отдельные вопросы для каждой роли.
- TITAN-A003 — Есть глобальные default questions с возможностью переопределить их per-role.
- TITAN-A004 — Пользователь не может иметь более одной pending application одновременно.
- TITAN-A005 — После отправки application выдаётся уникальный Application ID для последующего просмотра статуса.
- TITAN-A006 — Пользователь может просматривать конкретную заявку по ID или список последних заявок; список ограничивается последними 10.
- TITAN-A007 — Статусы application представлены одновременно текстом и emoji: pending/approved/denied.
- TITAN-A008 — Staff review показывает ответы кандидата прямо в embed и предлагает две кнопки Approve/Deny.
- TITAN-A009 — После выбора Approve/Deny открывается второй Modal для необязательной причины решения.
- TITAN-A010 — Review component collector привязан к конкретному reviewer, конкретному application ID, имеет timeout и `max: 1`.
- TITAN-A011 — При approve роль автоматически выдаётся пользователю; при deny роль не выдаётся.
- TITAN-A012 — Результат review отправляется пользователю в DM с причиной и ссылкой на status command; ошибка DM не ломает обработку review.
- TITAN-A013 — Application log message сохраняется вместе с channel/message IDs и редактируется после review вместо создания нового сообщения.
- TITAN-A014 — Staff applications поддерживают фильтрацию списка по status, role и user и настраиваемый limit 1–25.
- TITAN-A015 — Application admin защищён `ManageGuild` и дополнительно проверяет собственную manager-permission policy через service.
- TITAN-A016 — `/app-admin setup` запускает интерактивный setup: Role Select Menu + несколько text inputs в Modal.
- TITAN-A017 — Setup автоматически включает application system, если он был выключен.
- TITAN-A018 — Создание application предотвращает повторную привязку той же Discord role.
- TITAN-A019 — После setup пользователя автоматически направляют в configuration dashboard для дальнейшей настройки.
- TITAN-A020 — Application configuration включает log channel, manager roles, questions и retention period как настраиваемые параметры.
- TITAN-A021 — Пользовательские ответы и application metadata сохраняются для последующего review/audit.
- TITAN-A022 — У application есть явная конфигурационная ошибка `Applications are disabled`, а не молчаливый отказ.
- TITAN-A023 — Application modal использует динамический `customId`, содержащий role ID, чтобы восстановить контекст конкретной заявки.
- TITAN-A024 — При обработке modal дополнительно проверяется существование role и наличие её application configuration перед записью.
- TITAN-A025 — Setup modal имеет собственный timeout 15 минут и фильтр по исходному пользователю.
