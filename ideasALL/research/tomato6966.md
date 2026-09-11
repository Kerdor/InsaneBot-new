# Research Journal — Tomato6966/Multipurpose-discord-bot

Источник: `Tomato6966/Multipurpose-discord-bot`
Ветка: `new_2025`

## Batch 1
### `commands/⌨️ Programming`
- Просмотрены `coliru.js`, `compile.js`, `github.js`, `httpstatus.js`, `npm.js`, `npmpkgsize.js`.
- `compile.js` и `coliru.js` — одна и та же механика, объединены.
- Зафиксированы `TOM-001–005` в `ideas/TOMATO_BATCH1.md`.

## Batch 2
### `commands/⚙️ Settings`
- Просмотрены все 20 файлов области Settings.
- Зафиксированы `TOM-006–011` в `ideas/TOMATO_BATCH2.md`.
- `prefix.js` сверён с `CORE-012`; money/AFK/music settings сверены с существующим банком.
- Закомментированные `toggledjonly.js` / `togglerequestonly.js` не учитывались.

## Batch 3
### `commands/⚜️ Custom Queue(s)`
- Обработан единственный `savedqueue.js` целиком.
- Зафиксированы `TOM-012–020` в `ideas/TOMATO_BATCH3.md`.

## Batch 4
### `commands/🎤 Voice`
- Обработан единственный `voice.js` целиком по всем веткам.
- Зафиксированы `TOM-021–033` в `ideas/TOMATO_BATCH3.md`.
- Найдены lock/unlock, stage/unstage, kick, invite, ban/unban, trust/untrust, user limit, bitrate и ownership transfer для временных Join-to-Create voice-каналов.

## Batch 5
### `commands/🎮 MiniGames`
- Проверена вся директория MiniGames.
- Зафиксированы `TOM-034–058` в `ideas/TOMATO_BATCH4.md`.
- Отключённые `.js.disabled` файлы не учитывались.
- `uno.js` и `poker-night.js` не учитывались как рабочие игровые механики.

## Batch 6
### `commands/🎶 Music`
- Проверена вся директория Music по дереву `new_2025` и просмотрены оставшиеся команды/варианты поведения.
- Зафиксированы `TOM-059–072` в `ideas/TOMATO_BATCH5.md`.
- Новые механики: previous/similar треки, DM-grab текущего трека, playtop, moveme, radio-каталог и RadioBrowser search, reconnect radio, восстановление shuffle, dedupe очереди, queue status, Music Mix, Song of the Day и отдельный режим поиска похожих треков.
- Базовые play/search/playlist/skip/pause/resume/restart/seek/forward/rewind/volume/clearqueue/removetrack/stop и loop-варианты сверены и не размножены.
- `voteskip.js` и `removevoteskip.js` содержат полностью закомментированный код.
- `lyrics.js` и `searchplaylist.js` в текущей ветке не выполняют заявленную механику.
- В `move.js` обнаружен дефект: заявленные `from/to` игнорируются, фактически последний трек переносится в начало; полноценной позиционной механикой это не считается.
- `autoplay.js` и остальные оставшиеся базовые варианты также проверены.
- `commands/🎶 Music` **ЗАВЕРШЁН**.

## Batch 7
### `commands/🏫 School Commands`
- Проверены все 5 файлов: `calc.js`, `calculator.js`, `e.js`, `pi.js`, `remind.js`.
- Зафиксированы `TOM-073–077` в `ideas/TOMATO_BATCH6.md`.
- `calc.js` и `calculator.js` оставлены отдельными идеями: текстовый математический ввод и интерактивный calculator UI.
- `e.js` и `pi.js` дают отдельные команды вывода большого количества знаков математических констант.
- `remind.js` реализует отложенное пользовательское напоминание с составной длительностью и сохранением контекста пользователя/канала/сервера.
- `commands/🏫 School Commands` **ЗАВЕРШЁН**.

## Batch 8
### `commands/👀 Filter`
- Проверены все файлы области Filter: `3d.js`, `bassboost.js`, `china.js`, `chipmunk.js`, `cleareq.js`, `clearfilter.js`, `darthvader.js`, `equalizer.js`, `nightcore.js`, `pitch.js`, `rate.js`, `slowmo.js`, `speed.js`, `tremolo.js`, `vibrate.js`, `vibrato.js`.
- Зафиксированы `TOM-078–092` в `ideas/TOMATO_BATCH7.md`.
- Найдены 8D rotation, Bass Boost presets, Equalizer presets, сброс EQ/filter, China/Chipmunk/Darth Vader/Nightcore/Slowmo/Tremolo/Vibrato/Vibrate эффекты и ручные pitch/speed/rate.
- `cleareq.js` не добавлен отдельно: механика сброса EQ совпадает с `clearfilter.js`.
- `speed.js` и `rate.js` сохранены отдельно от `pitch.js`, так как управляют разными параметрами timescale.
- `commands/👀 Filter` **ЗАВЕРШЁН**.

## Batch 9
### `commands/👑 Owner`
- Проверены все 19 файлов области Owner.
- Зафиксированы `TOM-093–106` в `ideas/TOMATO_BATCH8.md`.
- Найдены смена аватара/имени бота, глобальная смена prefix, интерактивная настройка статуса с двумя текстами/placeholders/типом/Twitch URL/state, управление owner list, выход с сервера, reload одной/всех команд, архитектурный full hot-reload, PM2 restart, global/guild slash deploy, полный reset данных guild, управление рекламой и owner diagnostic card.
- `addmoney.js` / `removemoney.js` сверены с существующими `ECON-014–016` и не добавлены.
- `stopbot.js` не добавлен как рабочая механика: фактический stop недостижим из-за раннего `return`.
- `reloadbot.js` отключён ранним `return`; его архитектурный hot-reload сохранён как `TOM-101` с соответствующей пометкой.
- `restartbot.js` использует PM2, но содержит небезопасное отсутствие owner-check; это отмечено в идее.
- `detailedeval.js` / `eval.js` не добавлены отдельно как пользовательские системы.
- `commands/👑 Owner` **ЗАВЕРШЁН**.

## Batch 10 — `commands/💪 Setup`
### Часть 1: `TOM-107–116`
- Проверена первая часть Setup по recursive tree.
- `TOM-107`: массовое включение/выключение нескольких категорий команд через multi-select; выбранные категории переключаются за одну операцию.
- `TOM-108`: Number Counter с назначением канала, хранением текущего номера, отображением следующего номера и reset.
- `TOM-109`: ежедневные автоматические факты в выбранном канале, с включением/выключением и отображением настройки.
- `TOM-110`: Anti-New-Account с минимальным возрастом аккаунта, выбором `kick`/`ban`, дополнительным DM-сообщением и просмотром настроек.
- `TOM-111`: Anti-Spam с лимитом сообщений за 10 секунд, whitelist каналов и отдельным mute threshold.
- `TOM-112`: Anti-Link с whitelist каналов и ссылок/доменов, а также отдельным mute threshold.
- `TOM-113`: произвольное DM-сообщение пользователю при бусте сервера.
- `TOM-114`: Boost Log в отдельном канале с тремя настраиваемыми шаблонами: start/stop/again; поддерживается `{member}`.
- `TOM-115`: Ghost-Ping Detector с отдельным log channel и настраиваемым максимальным временем между ping и удалением сообщения.
- `TOM-116`: Epic Games Account Verification с verification channel и независимым action-log channel.
- Redirect-файлы `setup-antimassmention.js`, `setup-antimasspings.js`, `setup-antipings.js`, `setup-auditlog.js` не считались самостоятельными механиками.

### Часть 2: `TOM-117–145`
- Проверена следующая крупная часть Setup.
- Зафиксированы AI-Chat, Anti-Caps, Anti-Discord Links, Anti-Mention, scheduled backups, per-channel Auto-Delete, Auto-Embed, Auto-Meme, Auto-NSFW, массовый Auto-Warn toggle и модульный Anti-Nuke (`TOM-117–127`).
- Затем полностью просмотрены Application, Auto-Support, Custom Commands и глобальные Embed settings (`TOM-128–145`).
- Application: до 100 systems, автосоздание раздела, кастомная панель, анкета, accept/deny/ticket messages, temporary/accept roles, пять результатов и Last Verify.
- Auto-Support: несколько systems, до 25 options, индивидуальный Embed/plain response и переустановка панели.
- Custom Commands: до 25 на guild и выбор Embed/plain.
- Embed: глобальный цвет, footer icon/text и thumbnail toggle.
- `setup-antispam.js` сверён с уже записанным `TOM-111`; redirect'ы и повторные blacklist-настройки отдельно не размножались.

### Часть 3: `TOM-146–156`
- Продолжен последовательный просмотр Setup после `setup-embed.js`, начиная с `setup-joinlist.js` и далее по крупному соседнему блоку файлов.
- `TOM-146`: интерактивная смена языка с reset/status и выбором нескольких локалей.
- `TOM-147`: отдельный канал для логирования выполнения административных команд.
- `TOM-148–149`: до 25 Member Counter систем и расширенные placeholders для пользователей, members, ботов, статусов, каналов, threads и ролей.
- `TOM-150`: Menu Apply — до 100 конфигураций и до 25 вариантов в одной панели, с сохранением channel/message IDs.
- `TOM-151–152`: Menu Ticket — до 100 конфигураций, до 25 options, general access/closed category и независимый claim с двумя кастомными сообщениями.
- `TOM-153`: постоянная Music Request панель с набором интерактивных music controls.
- `TOM-154`: включение/выключение Valid-Code обработки сообщений с валидными code snippets.
- `TOM-155`: Joinlist с шестью типами условий по данным нового участника и четырьмя действиями (`kick`, `ban`, `timeout`, `setnickname`), включая составные timeout, ban days и `{random}` nickname.
- `TOM-156`: до 100 независимых JTC systems; для каждой можно создать trigger VC или использовать текущий VC, настроить имя временных комнат и сохранить отдельную конфигурацию.
- `setup-boost.js` сверён с `TOM-113–114` и не добавлен повторно.
- `setup-logger.js` сверён с существующим Audit Logger; новых самостоятельных требований не выделено.
- `setup-radio.js` сверён с `TOM-064–066`; новых самостоятельных radio-механик не выделено.
- `setup-admin.js` сверён с существующим permission/ACL слоем; новых самостоятельных требований не выделено.
- `setup-serverstats.js` — redirect на `setup-membercount`, отдельно не считается.

### Состояние
`commands/💪 Setup` **НЕ ЗАВЕРШЁН**.

## Точка продолжения
Продолжать `commands/💪 Setup` с оставшихся файлов после текущего обработанного блока. Следующие кандидаты — продолжение после `setup-music.js`/`setup-menuticket.js` по recursive tree; Economy не начинать до полного закрытия Setup.

## Статус
Tomato6966/Multipurpose-discord-bot — **В РАБОТЕ**.
