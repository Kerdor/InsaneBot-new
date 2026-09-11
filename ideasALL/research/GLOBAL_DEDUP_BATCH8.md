# GLOBAL DEDUP — BATCH 8

Тематические области: оставшиеся GAwesomeBot Public mechanics после полного source-specific pass.

Правило: command interface сам по себе не считается новой системой. Новым каноническим кластером становится только отдельная underlying mechanic/состояние/поведение, которого нет в `GD-001–284`.

## Новые механики

### GD-285 — Named persistent server countdowns
Источник: GAB-PUB `countdown.js`.
Канон: сервер может хранить несколько именованных countdowns с human-readable duration parser, абсолютным expiry timestamp и привязкой к каналу создания. Повторное имя не создаёт второй countdown; без аргумента показывается paginated список активных countdowns с каналом и относительным временем окончания.

Отличие от обычных reminders/events: countdown является server-local именованным объектом, доступным по имени из публичной команды и имеющим отдельный list/status surface.

### GD-286 — Self/admin nickname management
Источник: GAB-PUB `nick.js`.
Канон: пользователь может менять собственный guild nickname, а уполномоченный пользователь — nickname другого участника. Поддерживается специальное значение для сброса nickname, ограничение длины, member search и отдельные permission/hierarchy checks для target.

### GD-287 — Role inspection with effective permissions
Источник: GAB-PUB `roleinfo.js`.
Канон: отдельная role-inspection surface умеет показывать список ролей сервера и роли текущего пользователя с pagination, агрегировать effective permissions всех ролей пользователя, отдельно предупреждать об Administrator, а при указании роли показывать metadata: color, member count, position, creation time, mentionable/hoist/managed state и permissions.

## Не создаём новые GD

- `streamers.js` — command-level live-status view поверх уже существующего multi-provider stream monitoring; underlying mechanic уже канонизирован в Batch 5.
- `disable.js` / `enable.js` — command-level управление enabled/disabled state, уже покрыто configuration/help каноном.
- `count.js`, `cool.js`, `quiet.js`, `nuke.js`, `poll.js`, `strike(s).js` и остальные финальные Public-файлы уже имеют соответствующие source/global каноны.

## Cross-theme notes

- GD-285 не объединяется с персональными reminders: countdown — server-scoped named object, а reminder — personal scheduled notification.
- GD-286 относится к guild customization/member management, но не к role management: nickname и role операции имеют разные state и permission model.
- GD-287 — информационная поверхность над Discord role state; она не дублирует selfrole/admin role editing.

Результат: **3 новых канонических механики, GD-285–287.**

RoadMap пока не строится; сначала необходимо завершить общую глобальную дедупликацию всех source-specific находок.
