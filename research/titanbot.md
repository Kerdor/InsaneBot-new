# Research Journal — codebymitch/TitanBot

Источник: `codebymitch/TitanBot`
Ветка: `main`
Статус: 🔵 АКТИВЕН

## Просмотрено

### Root / Bootstrap
- recursive tree `main` (`truncated=false`);
- `README.md`;
- `src/app.js`;
- `src/handlers/loaders/commandLoader.js`.

### Уже закрытые каталоги
- Birthday;
- Community;
- Core;
- Economy;
- Fun;
- Giveaway;
- JoinToCreate;
- Leveling;
- Logging;
- Moderation;
- Music;
- Reaction_roles.

### Reaction_roles
Команды/handlers/services/status:
- `src/commands/Reaction_roles/reactroles.js`;
- `src/handlers/interactionHandlers/reactionRolesSelectMenu.js`;
- `src/services/reactionRoleService.js`;
- `src/utils/panelStatus.js`;
- `src/utils/database/keys.js` (reaction-role keys + legacy canonicalization).

Зафиксировано в `ideas/TITAN_REACTION_ROLES.md` — TRR-001–TRR-170.

Существенные находки: setup до 5 ролей и guild limit 5 panels; runtime limit 25 roles; Administrator-only management; channel/ManageRoles/role hierarchy/managed/dangerous permission validation; partial invalid-role acceptance; String Select Menu self-assignment; zero-value selection для снятия всех ролей панели; persistent guild+message metadata; rollback orphan message при DB failure; ephemeral dashboard; autocomplete без network fetch; 10-minute dashboard sessions; add/remove role через Role Select/String Select; live panel rebuild; last-role auto deletion; checkbox delete confirmation; text-edit modal; repost удалённой панели; automatic message-ID migration/recovery; panel status scanning; guild-only interaction; whitelist role validation; partial add/remove failures; added/removed/skipped result; audit logging; canonical/legacy DB keys; robust DB list handling; malformed record isolation; guild-wide reconciliation; stale-record cleanup; centralized typed errors и safe interaction lifecycle.

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
- `ideas/MODERATION.md` — MOD-001–MOD-135;
- `ideas/TITAN_MUSIC.md` — TM-001–TM-154;
- `ideas/TITAN_REACTION_ROLES.md` — TRR-001–TRR-170.

## Точная точка продолжения

`src/commands/Reaction_roles/` и связанные reaction-role handler/service/status/database-key paths — **ЗАКРЫТЫ**.

Следующий каталог по фактическому recursive tree `src/commands/`:
**`src/commands/Search/`**.

Продолжать строго по порядку дерева `src/commands/`. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
