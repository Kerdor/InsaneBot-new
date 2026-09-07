# Research Journal — GAwesomeBot/bot

Источник: `GAwesomeBot/bot`
Ветка: `indev-4.0.2`
Статус: 🔵 АКТИВЕН

## Начало исследования

Фактический recursive tree ветки `indev-4.0.2` проверено через Git tree API; `truncated=false`.

Корневой порядок исследования:
1. `Commands/`
2. `Configurations/`
3. `Database/`
4. `Internals/`
5. `Modules/`
6. `Temp/`
7. `Web/`

### Commands — в процессе

Обнаружены `Commands/PM/`, `Commands/Private/`, `Commands/Public/`, `Commands/Shared/`.

#### `Commands/PM/` — ЗАВЕРШЁН

Проверены все 11 файлов:
- `_base.js`
- `afk.js`
- `config.js`
- `giveaway.js`
- `help.js`
- `join.js`
- `poll.js`
- `profile.js`
- `remindme.js`
- `say.js`
- `servernick.js`

Связанный `Commands/Private/giveaway.js` также просмотрен как фактический исполнитель DM giveaway relay.

Зафиксировано **GAB-PM-001–GAB-PM-125** в `ideas/GAWESOME_COMMANDS_PM.md`.

#### `Commands/Private/` — ЗАВЕРШЁН

Проверены все 4 файла:
- `giveaway.js`
- `index.js`
- `poll.js`
- `say.js`

Зафиксировано **GAB-PR-001–GAB-PR-049** в `ideas/GAWESOME_COMMANDS_PRIVATE.md`.

Основные новые находки после сверки с PM: отдельный Private execution namespace; повторяемый server resolution с membership gate; blocklist gate; отдельный channel resolution; lazy channel-state creation; remote say с авторской атрибуцией и проверкой VIEW_CHANNEL/SEND_MESSAGES; poll owner-end и vote-revoke flows; anonymous DM voting; pagination по 10 вариантов; callback validation; command-specific timeouts; poll default No/Yes; giveaway state-dependent join/leave/end flows; secret prize separation; natural duration parser и safe fallback; maintainer bypass; addressable nested state updates; correlation через initMsg; private-layer reuse общих search/permission primitives.

## Точная точка продолжения

`Commands/PM/` и `Commands/Private/` полностью просмотрены.

Следующий каталог по строгому порядку дерева `Commands/`: **`Commands/Public/`**.

После `Public` продолжать `Shared`. Только после полного завершения `Commands/` переходить к `Configurations/`.

Другие репозитории не трогать до полного завершения GAwesomeBot.
