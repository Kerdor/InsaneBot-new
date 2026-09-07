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

Ключевые находки: глобальный AFK; многошаговый profile setup с privacy/background/Bio/quit/timeout; reminders; персональные server aliases; remote say/poll/giveaway из DM; статусы none/multi/success; DM-контроль giveaway; secret prize; duration parser; membership/blocklist/permission checks; динамический PM help; deprecated dashboard redirect; OAuth invite URL.

## Точная точка продолжения

`Commands/PM/` полностью просмотрен.

Следующий каталог по строгому порядку дерева `Commands/`: **`Commands/Private/`**.

После `Private` продолжать `Public`, затем `Shared`. Только после полного завершения `Commands/` переходить к `Configurations/`.

Другие репозитории не трогать до полного завершения GAwesomeBot.
