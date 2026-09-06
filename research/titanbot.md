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

### Moderation
Полностью просмотрен каталог `src/commands/Moderation/` и ключевой moderation service.

Команды:
- `ban.js`;
- `cases.js`;
- `dm.js`;
- `kick.js`;
- `lock.js`;
- `massban.js`;
- `masskick.js`;
- `purge.js`;
- `say.js`;
- `timeout.js`;
- `unban.js`;
- `unlock.js`;
- `untimeout.js`;
- `usernotes.js`;
- `warn.js`.

Сервисы:
- `src/services/moderation/moderationService.js`;
- `src/services/moderation/warningService.js`.

Зафиксированы: централизованный ModerationService, двойная role hierarchy validation (moderator + bot), owner bypass, permission-aware ban отсутствующих пользователей, self/bot protection, case IDs, warning IDs/counters/timestamps, фиксированные timeout durations, kickable/moderatable checks, unban ban-list validation, mass ban/kick с частичными результатами и лимитом 20 целей, per-command abuse protection, purge limits/old-message handling, channel lock/unlock через @everyone overwrite, staff DM anonymous/sanitization/error handling, say channel/permission/sanitization flow, paginated cases UI с owner-only controls и timeout, типизированные user notes и их lifecycle, centralized typed error handling и guild isolation.

## Уже зафиксировано в ideas

- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md`;
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065;
- `ideas/TITAN_JOINTOCREATE.md` — TJ-001–TJ-080;
- `ideas/TITAN_LEVELING.md` — TL-001–TL-100;
- `ideas/TITAN_LOGGING.md` — TLOG-001–TLOG-100;
- `ideas/MODERATION.md` — MOD-001–MOD-135, включая новый пакет codebymitch/TitanBot MOD-044–MOD-135.

## Существенные находки

### Moderation
- ModerationService централизует ban/kick/timeout/untimeout/unban и выдаёт единый слой hierarchy/permission/error checks.
- Для модератора и бота используются отдельные role hierarchy проверки; owner получает bypass.
- Ban отсутствующего на сервере пользователя разрешён только при Manage Server/Administrator/owner.
- Каждая ключевая операция возвращает Case ID и пишет action metadata; warnings дополнительно имеют warning ID, порядковый номер и total count.
- Mass ban/kick обрабатывают цели независимо, ограничивают вход 20 пользователями и разделяют successful/skipped/failed.
- Cases имеют фильтр по action/user, configurable limit 1–50, страницы по 5 записей и 120-секундный owner-only collector.
- User notes отделены от moderation cases и поддерживают типы, add/view/remove/clear, sanitization, metadata автора/времени и newest-first view.
- Purge ограничен 1–100 сообщениями, использует bulk delete и автоматически удаляет собственный ответ через 3 секунды.
- Lock/unlock изменяют SendMessages для @everyone и передают audit reason.
- Staff DM поддерживает anonymous mode, sanitization, 2000-char limit и отдельную обработку Discord 50007.
- Say умеет выбрать text/announcement channel, проверяет права обеих сторон и возвращает jump link.

## Точная точка продолжения

`src/commands/Moderation/` — **ЗАКРЫТ**.

Следующий каталог по фактическому recursive tree `src/commands/`:
**`src/commands/Music/`**.

Продолжать строго с `Music/`; GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
