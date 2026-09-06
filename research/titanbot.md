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

## Уже зафиксировано в ideas

- `ideas/TITAN_CORE.md`;
- `ideas/TITAN_APPLICATIONS.md`;
- `ideas/TITAN_CONFIG.md`;
- `ideas/TITAN_ECONOMY.md` — E001–E045;
- `ideas/TITAN_FUN.md` — TF-001–TF-043;
- `ideas/TITAN_GIVEAWAY.md` — TG-001–TG-065.

## Существенные находки текущего батча

- Counting Game — отдельное guild-scoped состояние с несколькими системами представления чисел: decimal, hexadecimal, binary, base36, base64, Roman, math, alphabet.
- Counting Game хранит next value, last user, current/best streak и персональный leaderboard; reset сбрасывает текущую серию, но сохраняет best streak.
- Counting Game поддерживает expression/equality parsing в math mode и отдельные правила case normalization для Roman/Alphabet.
- Fun содержит random mechanics: coin flip, dice notation с modifier и ограничения 20 dice/1000 sides, а также текстовую случайную 1v1 дуэль с несколькими раундами.
- Giveaway имеет полный lifecycle: create → join → automatic/manual end → winner announcement → reroll/delete.
- Giveaway хранит Discord message/channel/guild IDs, host, participants, winner IDs, timestamps, end actor и winner announcement ID.
- Winner selection уникализирует участников и случайно выбирает до N победителей.
- Giveaway имеет отдельный per-user/per-giveaway interaction rate limit.
- Expired giveaways обрабатываются фоново; отсутствие guild/channel/message не ломает обработку остальных записей.
- Delete имеет fallback-поиск сообщения по другим text channels и после удаления из БД проверяет, что запись действительно исчезла.
- Reroll сохраняет новый набор победителей даже при недоступном исходном Discord message/channel и умеет переиспользовать существующее announcement сообщение.
- Create/end/delete/reroll/winner действия интегрированы с audit logging, причём ошибка логирования не должна ломать основную операцию.

## Точная точка продолжения

**Следующий раздел дерева: `src/commands/JoinToCreate/`.**

Уже начат просмотр:
- `src/commands/JoinToCreate/jointocreate.js` — просмотрен частично из-за размера файла; основные setup/dashboard структуры и collector-based configuration уже видны.

Дальше нужно полностью выжать `JoinToCreate`: дочерние `modules/config_setup.js`, `modules/setup.js`, затем `src/services/joinToCreateService.js`, после чего перейти к следующему разделу дерева (`Leveling`).

Правило остаётся неизменным: GAwesomeBot не трогаем, пока TitanBot полностью не закрыт.
