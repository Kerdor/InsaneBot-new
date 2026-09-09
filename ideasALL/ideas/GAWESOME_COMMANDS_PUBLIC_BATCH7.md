# GAwesomeBot — Commands/Public — batch 7

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Продолжение batch 6. Добавлены только детали, которые дают отдельный UX/behavior/constraint и не являются точными дублями уже зафиксированных GAB-PUB-001–495.

## Moderation — ban / kick / unban

- **GAB-PUB-496 — Ban optional message-prune days:** ban принимает дополнительное числовое значение перед reason и использует его как количество дней удаления сообщений, ограничивая значение 31.
- **GAB-PUB-497 — Ban non-member ID targeting:** ban может работать по user ID даже когда пользователь уже не является участником guild; member-only checks применяются отдельно.
- **GAB-PUB-498 — Ban member-search reason fallback:** если первый token не найден как member, команда пробует повторный поиск, объединяя предполагаемый target и reason, чтобы частично восстановить неоднозначный ввод.
- **GAB-PUB-499 — Ban edited-confirmation cancellation:** изменение confirmation-message останавливает collector и не позволяет продолжить destructive action.
- **GAB-PUB-500 — Ban confirmation-message cleanup:** подтверждающее сообщение пользователя удаляется перед выполнением ban, если бот может его удалить.
- **GAB-PUB-501 — Ban DM-before-action ordering:** уведомление пользователя по DM выполняется до самого ban; ошибка DM не должна блокировать moderation action.
- **GAB-PUB-502 — Ban self-confirmation joke guard:** вызов ban без target не приводит к реальному self-ban даже после положительного ответа; используется отдельная playful confirmation branch.
- **GAB-PUB-503 — Kick edited-confirmation cancellation:** kick collector также прекращает обработку, если confirmation message был отредактирован.
- **GAB-PUB-504 — Kick confirmation-message cleanup:** после ответа на kick confirmation бот пытается удалить ответ, не считая невозможность удаления критической ошибкой.
- **GAB-PUB-505 — Kick self-confirmation joke guard:** вызов kick без target имеет безопасную self-target joke branch вместо реального действия.
- **GAB-PUB-506 — Unban mention normalization:** unban умеет принимать Discord mention вида `<@ID>` и нормализует его до user ID перед поиском среди bans.
- **GAB-PUB-507 — Unban case-insensitive identity matching:** поиск ban entry допускает ID, full tag и username без чувствительности к регистру.
- **GAB-PUB-508 — Unban previous-reason preview:** confirmation показывает не только новую причину unban, но и исходную причину, по которой пользователь был заблокирован.
- **GAB-PUB-509 — Unban confirmation response cleanup:** ответ на unban confirmation удаляется после получения, чтобы служебные подтверждения не оставались в канале.
- **GAB-PUB-510 — Unban bot-permission preflight:** наличие `BAN_MEMBERS` проверяется до загрузки списка bans и до начала confirmation flow.

## Moderation — mute / unmute

- **GAB-PUB-511 — Mute immediate-action model:** mute после прохождения target/permission/state checks выполняется без отдельного confirmation collector.
- **GAB-PUB-512 — Unmute immediate-action model:** unmute симметрично выполняется сразу после проверок, без destructive confirmation.
- **GAB-PUB-513 — Mute reason stored separately from action text:** ModLog получает пользовательскую reason, тогда как внутреннее описание role operation содержит технический context channel/member/issuer.
- **GAB-PUB-514 — Unmute reason stored separately from action text:** unmute сохраняет ту же раздельную модель human reason и internal operation context.
- **GAB-PUB-515 — Channel-scoped mute state:** mute/unmute проверяют состояние участника относительно конкретного канала, а не как глобальный guild mute flag.

## Tags

- **GAB-PUB-516 — Tag typing indicator for inventory generation:** перед построением полного tag inventory бот включает typing indicator, потому что генерация может включать внешние uploads.
- **GAB-PUB-517 — Tag list permission is configurable:** право просмотра полного списка tags отдельно настраивается как admin-only/non-admin режим.
- **GAB-PUB-518 — Tag creation permission split by command mode:** создание обычных tags и command-tags может иметь разные permission gates.
- **GAB-PUB-519 — Tag deletion permission split by command mode:** удаление обычного tag и command-tag использует разные configurable policies.
- **GAB-PUB-520 — Tag update blocked by lock regardless of normal update policy:** locked tag нельзя обновлять обычным пользователем даже если общий update flow разрешён.
- **GAB-PUB-521 — Tag metadata replacement is atomic:** подтверждённое обновление tag одновременно заменяет content, command flag и lock flag.
- **GAB-PUB-522 — Tag URL preview suppression:** ссылки в сохранённом tag content автоматически заключаются в `<...>`, чтобы при вызове tag Discord не разворачивал previews.
- **GAB-PUB-523 — Tag long-content external raw link:** при выносе длинного tag в Gist пользователю показывается raw URL, пригодный для прямого чтения содержимого.
- **GAB-PUB-524 — Tag defaults replacement semantics:** загрузка defaults полностью заменяет текущий список tags, а не объединяет default set с существующими.
- **GAB-PUB-525 — Tag mutation audit logging:** создание, обновление и удаление tags пишутся в server log с типом INFO и issuer/channel context.

## Economy / points / lottery UX

- **GAB-PUB-526 — Points bot exclusion:** points lookup явно запрещает bots как валидных владельцев currency.
- **GAB-PUB-527 — Points lazy account initialization:** просмотр points участника без существующего user document создаёт базовый user document с нулевым балансом.
- **GAB-PUB-528 — Points positive-balance leaderboard:** общий points leaderboard исключает пользователей с нулевым или отрицательным балансом до сортировки.
- **GAB-PUB-529 — Points leaderboard hard top-10:** публичный список самых богатых ограничен десятью пользователями.
- **GAB-PUB-530 — Points singular/plural-aware presentation:** currency UI меняет форму названия валюты для ровно одного point против нескольких.
- **GAB-PUB-531 — Lottery creator cannot self-enroll:** создатель active lottery не может покупать собственные tickets.
- **GAB-PUB-532 — Giveaway creator cannot self-enroll:** создатель active giveaway также явно исключён из participant flow.
- **GAB-PUB-533 — Giveaway duplicate-entry protection:** повторная попытка join существующего participant не создаёт второй entry и объясняет пользователю способ выхода.
- **GAB-PUB-534 — Giveaway DM self-service withdrawal:** участник может убрать себя из giveaway через DM-команду без необходимости писать в публичный канал.
- **GAB-PUB-535 — Giveaway live participant count:** запрос giveaway без action показывает текущий participant count и creator.

## Utility / media edge behavior

- **GAB-PUB-536 — 8ball randomized response latency:** задержка перед ответом выбирается случайно из заранее заданного набора, а не имеет одну фиксированную величину.
- **GAB-PUB-537 — Fortune fuzzy category matching:** категория fortune принимается при достаточно близком опечатанном вводе через Levenshtein distance.
- **GAB-PUB-538 — Fortune category list on invalid input:** вместо generic usage ошибка fortune перечисляет допустимые категории прямо в ответе.
- **GAB-PUB-539 — GIF NSFW mode follows channel policy:** Giphy search mode переключается между PG-13 и R на основе moderation NSFW filter, disabled-channel exceptions и channel NSFW state.
- **GAB-PUB-540 — GIF provider attribution:** успешный GIF результат явно указывает GIPHY как источник.
- **GAB-PUB-541 — GIF direct-media URL exposure:** результат содержит отдельную ссылку на прямой URL изображения, помимо embed preview.
- **GAB-PUB-542 — Anime result list preserves search order:** reaction selector формируется в том же порядке, в котором API вернул найденные anime results.
- **GAB-PUB-543 — Anime episode-duration disclosure:** карточка anime отдельно показывает episode count и продолжительность эпизода, если API её предоставляет.
- **GAB-PUB-544 — Anime age-rating disclosure:** при наличии age rating он выводится отдельным полем результата.
- **GAB-PUB-545 — YouTube default-to-max correction:** некорректное количество результатов YouTube приводит к server-configured max count перед дополнительным hard cap 10.
- **GAB-PUB-546 — Weather wind omission when unavailable:** поле wind не создаётся, если API не вернул положительную wind speed.
- **GAB-PUB-547 — Weather cloud omission when unavailable:** cloudiness field показывается только при наличии соответствующего API блока.
- **GAB-PUB-548 — Year countdown exact New Year target:** команда считает не просто год вперёд, а следующий January 1 at 00:00:00 и выводит одновременно точный breakdown и humanized duration.

## Archive / conversion / command-state details

- **GAB-PUB-549 — Archive UTC-normalized timestamps:** экспорт архива приводит message timestamps и archive timestamp к единой Europe/London timezone presentation с UTC offset.
- **GAB-PUB-550 — Archive clean-content dual capture:** экспорт сохраняет одновременно raw `content` и Discord-normalized `cleanContent`.
- **GAB-PUB-551 — Archive author identity snapshot:** JSON archive сохраняет username, discriminator, user ID, bot flag и avatar URL автора сообщения как snapshot.
- **GAB-PUB-552 — Archive attachment filename preservation:** вложения экспортируются с исходным filename и attachment URL.
- **GAB-PUB-553 — Conversion optional `to` keyword:** converter принимает синтаксис как с промежуточным `to`, так и без него.
- **GAB-PUB-554 — Conversion compact amount-unit syntax:** число и исходная единица могут быть переданы слитно, после чего parser разделяет numeric prefix и unit suffix.
- **GAB-PUB-555 — Conversion typed result presentation:** money и physical-unit conversions используют разные output formatting paths.
- **GAB-PUB-556 — Channel cooldown clear resets both state fields:** очистка command cooldown сбрасывает не только duration, но и ongoing-state flag.
