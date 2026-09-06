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

## Уже зафиксировано в ideas

- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md`;
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065;
- `ideas/TITAN_JOINTOCREATE.md` — TJ-001–TJ-080;
- `ideas/TITAN_LEVELING.md` — TL-001–TL-100.

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

## Точная точка продолжения

**Следующий раздел дерева: `src/commands/Logging/`.**

Leveling закрыт по найденным command/service/event файлам. Далее нужно полностью пройти `Logging`, затем продолжать строго по порядку дерева `src/commands/`.

Правило остаётся неизменным: GAwesomeBot не трогаем, пока TitanBot полностью не закрыт.
