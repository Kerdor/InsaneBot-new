# TITAN CONFIG — Банк идей

Находки `codebymitch/TitanBot` (main), `Core/configWizard.js`.

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
