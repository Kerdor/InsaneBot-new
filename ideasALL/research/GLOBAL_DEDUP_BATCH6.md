# GLOBAL DEDUP — BATCH 6

Тематические области: GAwesomeBot command-layer mechanics — PM / Private / подтверждённые Public-механики.

Правило: исходные IDs сохраняются; одинаковые механики объединяются, а уникальные UX, поведение, настройки, ограничения и архитектурные варианты сохраняются внутри канона.

> Граница: Public-каталог GAwesome в `GAWESOME_COMMANDS_PUBLIC.md` содержит дополнительные подтверждённые элементы, которые ещё нужно добрать отдельным проходом. Поэтому этот batch фиксирует только уже подтверждённые и сверенные механики; он не объявляет весь Public каталог закрытым.

## PM / Private

### GD-230 — DM profile setup wizard
Источники: GAB-PM-010–035.
Канон: многошаговый личный мастер с текущими значениями, публичностью, background URL, bio, `.`/`default`/`none`, quit, per-step timeout, сохранением старого значения при timeout и финальной ссылкой на профиль.

### GD-231 — Personal server aliases
Источники: GAB-PM-044–060.
Канон: пользовательские алиасы серверов; адресация по имени/ID/alias, ambiguity handling, overwrite confirmation, удаление и устойчивое разрешение актуального guild.

### GD-232 — DM control plane for server actions
Источники: GAB-PM-061–074, GAB-PM-118–122.
Канон: DM может быть control-plane для серверных действий; внутренние статусы resolution отделены от пользовательского UX, а membership/permissions повторно проверяются после выбора guild.

### GD-233 — Private server-operation relay
Источники: GAB-PR-001–012, GAB-PR-048–049.
Канон: узкий execution layer для `poll`/`giveaway`/`say`, общий server/channel resolution, membership gate, server blocklist, channel-type validation и correlation с исходным DM UI.

### GD-234 — DM poll management
Источники: GAB-PR-013–026.
Канон: повторный запуск владельцем может завершить активный poll, повторный голос превращается в revoke/re-vote flow; voting проходит через DM, варианты paginated, нумерация глобальная, шаги имеют разные timeout.

### GD-235 — DM giveaway management
Источники: GAB-PR-027–040; GAB-PM-075–104.
Канон: creator/participant/new-user состояния имеют разные flows; join/leave/end через confirmation, secret prize отделён от title, duration parser/default, remote permission и maintainer bypass.

### GD-236 — DM workflow progress/error editing
Источники: GAB-PM-063, GAB-PM-068, GAB-PM-115–117; GAB-PR-041–043.
Канон: длинный DM workflow использует одно progress/prompt message, редактирует его при переходе состояний/ошибках и трактует timeout как нормальную ветку завершения.

## Public / confirmed mechanics

### GD-237 — Dynamic permission-aware help menu
Источники: GAB-PUB help.js.
Канон: help строится из зарегистрированных public/PM/shared/extension command metadata; скрывает недоступные команды по admin level/channel disable, группирует по категориям и использует интерактивное меню; `help <command>` показывает command-specific usage/description.

### GD-238 — Per-channel command cooldown
Источник: GAB-PUB-032–036.
Канон: cooldown хранится на уровне канала, duration вводится естественным текстом, имеет hard cap, status/clear shortcuts.

### GD-239 — Channel-wide quiet mode
Источник: GAB-PUB-037–040.
Канон: канал можно перевести в indefinite/timed quiet; `all` распространяет режим на все каналы сервера; есть duration cap.

### GD-240 — Persistent interactive counters
Источники: GAB-PUB-041–047.
Канон: lazy creation через prompt, symbolic increment/decrement syntax, nonnegative floor, stop/delete action, paginated list и понятный empty-state.

### GD-241 — Structured message archive export
Источники: GAB-PUB-048–056.
Канон: bounded history fetch с cursor, экспорт в JSON с embed/attachment/edit/source metadata, отдельная диагностика permission и отдельная обработка send failure.

### GD-242 — Filtered bulk message cleanup
Источники: GAB-PUB-057–061.
Канон: массовая очистка поддерживает text substring/exact-text/author filters и before/after message-ID boundaries при лимите Discord bulk delete.

### GD-243 — Emoji jumbo renderer
Источник: GAB-PUB-emoji.js.
Канон: несколько emoji преобразуются worker-ом в один PNG/GIF; animated output сохраняет отдельные caveats.

### GD-244 — Global custom emoji inspector
Источник: GAB-PUB-emotes.js.
Канон: по custom emoji показываются ID/name, guild, creator, animated/managed state, allowed roles и creation time; без аргумента выводится каталог emoji текущего сервера.

### GD-245 — URL redirect safety inspection
Источник: GAB-PUB-expand.js.
Канон: URL проверяется на redirect chain и для каждого шага показывается safe/unsafe status с нормализованными причинами риска.

### GD-246 — Fuzzy category resolution
Источник: GAB-PUB-fortune.js.
Канон: category принимается по точному совпадению либо по близкому Levenshtein match; при невалидном вводе показывается полный каталог допустимых категорий.

### GD-247 — Temporary private talk rooms
Источник: GAB-PUB-room.js.
Канон: пользователь создаёт text/voice room с deny-by-default, явным owner/member allowlist; room можно удалить или добавить участников; voice room автоматически удаляется после ухода всех.

### GD-248 — Server to-do list
Источник: GAB-PUB-list.js.
Канон: серверный список задач с числовыми ID, добавлением, редактированием, удалением, done/complete toggle и полным просмотром.

### GD-249 — Scaled points lottery
Источник: GAB-PUB-lottery.js.
Канон: channel-scoped lottery с несколькими multiplier sizes, динамической ценой билета, лимитом билетов на пользователя, creator/admin/maintainer end control и вычисляемым призовым фондом.

### GD-250 — Weekly guild statistics reset
Источник: GAB-PUB-stats.js.
Канон: weekly guild stats имеют отдельную destructive reset operation с confirmation и admin gate.

### GD-251 — Command-usage statistics
Источники: GAB-PUB-info.js, GAB-PUB-stats.js.
Канон: бот считает использования команд и показывает top-used commands в серверной статистике; также может включать command count в server info card.

### GD-252 — Rank-specific leaderboard
Источник: GAB-PUB-ranks.js.
Канон: leaderboard можно строить отдельно для конкретного rank, сортируя участников по rank score; общий rank view показывает пороги и распределение участников по rank.

### GD-253 — Configurable server prefix with length guard
Источник: GAB-PUB-prefix.js.
Канон: серверный prefix изменяется через отдельную настройку, поддерживает quoted input и имеет максимальную длину.

### GD-254 — RSS feed alias/catalog access
Источник: GAB-PUB-rss.js.
Канон: сохранённые RSS feeds имеют server-local aliases; команда может читать alias или URL, ограничивать число статей и выводить результаты через pagination; без аргумента показывает каталог feeds.

### GD-255 — NSFW image-provider gate
Источники: GAB-PUB-e621.js, GAB-PUB-safebooru.js.
Канон: NSFW image providers доступны только в NSFW channels; результат ограничивается server default/max count и выводится через pagination с metadata.

### GD-256 — Bitly shorten/expand utility
Источник: GAB-PUB-shorten.js.
Канон: при наличии credential бот умеет shorten обычный URL и expand bit.ly; capability недоступна при отсутствии token.

### GD-257 — User points leaderboard surface
Источник: GAB-PUB-points.js.
Канон: points command показывает свои очки, очки конкретного пользователя и top-N non-zero участников; bot accounts исключаются.

### GD-258 — Server information card
Источник: GAB-PUB-info.js.
Канон: единая server info card объединяет creation/region/verification, command prefix/admin count, channel/role/emoji/member counts, activity counters, public listing и Discord feature flags.

### GD-259 — Per-answer visual variation for simple fun command
Источники: GAB-PUB-081–082.
Канон: ответы простого random/fun command могут иметь индивидуальные presentation metadata и искусственную задержку для UX-эффекта.

## Cross-theme notes

- GD-232/233 не дублируют generic API/dashboard GD-022: здесь именно Discord DM → guild operation control-plane.
- GD-238/239 не объединяются с moderation mute GD-134: quiet подавляет command processing, а mute — конкретного пользователя.
- GD-249 расширяет economy/gambling domain, но остаётся отдельной механикой lottery с динамической ценой билета.
- GD-255 использует общую filtering/NSFW инфраструктуру, но provider-specific gate остаётся частью image search surface.
- GD-251/252/257 расширяют существующие stats/progression/economy surfaces, а не создают новые leaderboard frameworks.
