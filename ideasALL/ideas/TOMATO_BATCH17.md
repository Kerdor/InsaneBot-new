# Tomato6966 — Batch 17

Источник: `Tomato6966/Multipurpose-discord-bot`
Ветка: `new_2025`

## `handlers/` — финальный recursive контроль

### TOM-241 — Auto-Embed по каналу или родительской категории
- Auto-Embed может быть активен не только для конкретного текстового канала, но и для канала через его `parentId`.
- Таким образом, одной настройкой можно охватить все подходящие каналы внутри выбранной категории.
- Handler дополнительно удаляет из конфигурации несуществующие каналы при обработке сообщений.

### TOM-242 — Автоматическая очистка данных сервера при выходе бота
- При `guildDelete` бот удаляет связанные с покинутым сервером данные из множества хранилищ.
- Очищаются guild-specific записи экономики, музыки, настроек, очередей, reaction roles, blacklist, custom commands, keyword и других систем.
- Масштабируемые конфигурации (`JTC`, `Roster`, `AutoSupport`, `MenuTicket`, `MenuApply`, `Application` и др.) очищаются циклически по слотам.
- Некоторые исторические/модерационные данные намеренно сохраняются, а не удаляются.

## Проверка покрытия
- Root-level handlers из `index.js` сверены с уже обработанными Batch 14–16 и текущим Batch 17.
- `handlers/playermanagers/` и `handlers/erela_events/` уже закрыты в Batch 15.
- Дополнительно точечно перепроверены `antidiscord.js`, `ticket.js`, `ticketevent.js`, `boostlog.js`, `timedmessages.js`, `extraevents.js`, `clientvariables.js`, `dailyfact.js`, `autoembed.js`, `autonsfw.js`.
- Остальные root-level handlers дали только уже зафиксированные Setup/Events/Batch-механики либо инфраструктурные helpers; новые самостоятельные идеи не добавлены.

### Состояние
`handlers/` **ЗАВЕРШЁН**.
