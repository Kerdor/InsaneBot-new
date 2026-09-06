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
- Moderation.

### Music
Команды:
- `src/commands/Music/join.js`;
- `src/commands/Music/music.js`;
- `src/commands/Music/nowplaying.js`;
- `src/commands/Music/play.js`;
- `src/commands/Music/queue.js`.

Сервисы/UI/handlers:
- `src/services/music/musicActions.js`;
- `src/services/music/musicEmbeds.js`;
- `src/services/music/musicVoiceState.js`;
- `src/services/music/permissions.js`;
- `src/services/music/playerHandler.js`;
- `src/services/music/playerStore.js`;
- `src/services/music/prefixSupport.js`;
- `src/services/music/riffySetup.js`;
- `src/handlers/musicButtons.js`;
- `src/config/music/lavalink.js`.

### Существенные находки Music
- Единый `/music` интерфейс управляет pause/resume/skip/stop/shuffle/loop/volume/seek/remove/move/clear/leave/24-7.
- `/play` поддерживает поиск, playlist load, duplicate protection, requester metadata и автоматический старт idle player.
- Music state изолирован по guild, хранит volume/loop/shuffle/previous tracks/player message/queue pagination/idle timers.
- Previous track history ограничена 20; queue page state хранится отдельно для каждого пользователя.
- Stop при очереди от 5 треков требует повторного подтверждения в течение 15 секунд.
- Skip временно отключает track-loop и восстанавливает сохранённый loop на следующем trackStart.
- Queue имеет страницы по 10 треков и first/previous/next/last navigation; queue UI ephemeral и permission-aware.
- Now Playing показывает title/artist/requester/progress/duration/volume/loop/queue/artwork и автоматически обновляется каждые 15 секунд.
- Постоянное player message редактируется, а при его исчезновении создаётся заново; UI failure не ломает playback.
- Queue end запускает idle disconnect через 30 секунд, если 24/7 выключен; перед disconnect выполняется повторная проверка состояния player.
- Voice-state automation игнорирует ботов, автоматически pause'ит пустой voice channel и resume'ит его при возвращении пользователя; `autoPaused` отделяет это от ручной паузы.
- Все controls требуют same voice channel; кнопки и slash actions используют общий permission layer.
- Lavalink availability, node availability, voice permissions и connection timeout проверяются до playback.
- Voice connection ждёт `connectionRestored` до 12 секунд после resolve.
- Поддерживается несколько Lavalink nodes, environment/file/JSON configuration и fallback single-node configuration.
- Riffy получает Discord voice gateway packets через raw VoiceStateUpdate/VoiceServerUpdate и маршрутизирует payload на соответствующий shard.
- Node logging throttled: первый connect логируется отдельно, reconnect может быть silent, error/disconnect ограничены одним сообщением за 5 минут на node.
- TrackError, TrackStuck, PlayerError и PlayerDisconnect имеют отдельные lifecycle paths.
- Shutdown уничтожает все активные players с изоляцией ошибок отдельных sessions.
- Music actions вынесены в переиспользуемый сервис; slash/prefix и button UI используют общий action layer.

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
- `ideas/TITAN_MUSIC.md` — TM-001–TM-154.

## Точная точка продолжения

`src/commands/Music/` и связанные Music services/handler/config paths — **ЗАКРЫТЫ**.

Следующий каталог по фактическому recursive tree `src/commands/`:
**`src/commands/Reaction_roles/`**.

Продолжать строго по порядку дерева `src/commands/`. GAwesomeBot и последующие источники не трогать до полного завершения TitanBot.
