# Research Journal — codebymitch/TitanBot

Источник: `codebymitch/TitanBot`
Ветка: `main`
Статус: 🔵 АКТИВЕН

## Стартовая сверка

Recursive tree корня проверен полностью (`truncated=false`). В репозитории присутствуют `src/`, `scripts/`, `lavalink/`, `.github/workflows/` и deployment/config/runtime files.

## Просмотрено

### Root / bootstrap
- recursive tree `main`;
- `README.md`;
- `src/app.js`;
- `src/handlers/loaders/commandLoader.js`.

### Birthday
- `src/commands/Birthday/birthday.js`;
- `src/commands/Birthday/modules/birthday_set.js`;
- `src/commands/Birthday/modules/birthday_list.js`;
- `src/commands/Birthday/modules/next_birthdays.js`.

### Community / Core / Economy
- Community application subsystem и dashboard;
- Core config wizard и command dashboard;
- Economy command family;
- `src/config/shop/items.js`.

### Fun
- `src/commands/Fun/count.js`;
- `src/services/countingGameService.js`;
- `src/commands/Fun/fight.js`;
- `src/commands/Fun/flip.js`;
- `src/commands/Fun/roll.js`.

### Giveaway
- `src/commands/Giveaway/gcreate.js`;
- `src/commands/Giveaway/gdelete.js`;
- `src/commands/Giveaway/gend.js`;
- `src/commands/Giveaway/greroll.js`;
- `src/services/giveawayService.js`.

### JoinToCreate
- `src/commands/JoinToCreate/jointocreate.js`;
- `src/commands/JoinToCreate/modules/config_setup.js`;
- `src/commands/JoinToCreate/modules/setup.js`;
- `src/services/joinToCreateService.js`;
- `src/events/voiceStateUpdate.js`.

### Leveling
- `src/commands/Leveling/leaderboard.js`;
- `src/commands/Leveling/level.js`;
- `src/commands/Leveling/leveladd.js`;
- `src/commands/Leveling/levelremove.js`;
- `src/commands/Leveling/levelset.js`;
- `src/commands/Leveling/rank.js`;
- `src/commands/Leveling/modules/level_dashboard.js`;
- `src/services/leveling/leveling.js`;
- `src/services/leveling/xpSystem.js`;
- `src/events/messageCreate.js` (leveling path).

### Logging
- `src/commands/Logging/logging.js`;
- `src/commands/Logging/modules/logging_dashboard.js`;
- `src/commands/Logging/modules/logging_channel.js`;
- `src/services/loggingService.js`;
- `src/utils/logging/loggingUi.js`;
- `src/utils/logging/logEmbeds.js`;
- `src/handlers/loggingButtons.js`;
- `src/events/channelDelete.js` (связанные cleanup paths);
- `src/events/guildMemberAdd.js`;
- `src/events/guildMemberRemove.js`;
- `src/events/guildMemberUpdate.js`;
- `src/events/userUpdate.js`;
- `src/events/roleCreate.js`;
- `src/events/roleDelete.js`;
- связанные logging call sites через repository search.

## Уже зафиксировано в ideas

- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md`;
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065;
- `ideas/TITAN_JOINTOCREATE.md` — TJ-001–TJ-080;
- `ideas/TITAN_LEVELING.md` — TL-001–TL-100;
- `ideas/TITAN_LOGGING.md` — TLOG-001–TLOG-100.

## Существенные находки

### Fun / Giveaway
- Counting Game имеет отдельное guild-scoped состояние, несколько форматов представления чисел и streak/leaderboard state.
- Giveaway имеет полный lifecycle create → join → automatic/manual end → winner announcement → reroll/delete, persistent Discord IDs и устойчивые fallback-пути при пропавших Discord objects.

### JoinToCreate
- Voice-state automation создаёт персональный временный voice channel при входе в trigger.
- Временная комната имеет owner, user limit, bitrate, category и configurable name template.
- Поддерживаются username/display name/user tag/guild/channel placeholders с Unicode normalization, sanitization, длиновыми лимитами и запретом неизвестных переменных.
- При уходе последнего участника временная комната удаляется; при уходе owner ownership передаётся оставшемуся участнику и имя комнаты обновляется.
- Повторный вход owner в trigger пытается вернуть его в уже существующую комнату.
- Есть per-guild/per-user creation cooldown, cleanup/size cap cooldown map и проверки voice state перед созданием/перемещением.
- Setup/dashboard имеют несколько интерактивных UI-подходов: buttons, select menus, modals/message collectors, confirmation для удаления и автоматическое истечение configuration session.
- Stale trigger channels очищаются из config; JTC configuration и изменения пишутся в audit log.

### Leveling
- XP выдаётся за сообщения с random range, per-user cooldown и дополнительным event rate limit.
- XP поддерживает multiplier, ignored channels, ignored roles и blacklisted users.
- XP updates защищены per-user/guild mutex от race conditions.
- Level progression использует квадратичную XP-кривую и максимум level 1000; одно начисление может дать несколько уровней.
- User state хранит current XP, total XP, level и lastMessage; чтение/запись sanitizes числовые значения.
- Level-up может выдавать role reward, публиковать configurable announcement и писать audit event; сбои side effects не ломают progression.
- Rank показывает level, XP, total XP и progress bar; leaderboard сортирует по total XP, исключает ботов и умеет переживать missing member fetch.
- Администратор может add/remove/set level; ручное изменение пересчитывает total XP.
- Leveling setup и dashboard позволяют выбирать announcement channel, XP range/cooldown, message, role rewards, ignored channels/roles и отдельно включать/выключать system/announcements.

### Logging
- Logging разделён на глобальный enable/disable, destination channels, event categories и ignore filters.
- Есть отдельные Audit, Applications и Reports destinations; Applications/Reports маршрутизируются отдельно от audit stream.
- Dashboard показывает состояние logging, количество включённых категорий, фильтры и настроенные каналы; вложенные views позволяют отдельно управлять категориями и фильтрами.
- Event taxonomy централизована через `EVENT_TYPES`, с category wildcard (`category.*`), отдельными event toggles, цветами и icon mapping.
- `logEvent` централизует guild/channel lookup, ignore checks, enable checks, permission checks, embed construction, attachments/content и error isolation.
- Audit embeds имеют общий builder с title/description/headline/quoted lines/meta/Before-After/inline/block fields/author/avatar/thumbnail/image/footer/timestamp и Discord length limits.
- Logging покрывает moderation, messages, roles, members, leveling, reaction roles, giveaways, counters, applications и reports.
- Join/leave/nickname/username изменения и создание/удаление ролей логируются отдельными событиями; username changes проходят по guilds пользователя.
- Ignore users/channels задаются интерактивными User/Channel Select и могут добавляться/удаляться без ручного ID.
- Logging channel configuration валидирует тип канала и права бота; удалённые/недоступные каналы не ломают остальной bot runtime.
- Dashboard interactions повторно проверяют `Manage Server`, ограничивают modal submission инициатором и имеют timeout/error boundaries.

## Точная точка продолжения

**Следующий раздел дерева: следующий каталог `src/commands/` после `Logging/` по фактическому recursive tree.**

`Logging` закрыт по command/modules/service/UI/handler и связанным event logging paths, доступным через repository search. Далее нужно определить следующий каталог в уже проверенном tree и продолжать строго по порядку `src/commands/`.

Правило остаётся неизменным: GAwesomeBot не трогаем, пока TitanBot полностью не закрыт.
