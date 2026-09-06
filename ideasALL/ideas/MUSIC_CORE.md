# MUSIC CORE — Банк идей

Дополнительные архитектурные находки `ItzSudhan/Discord-MusicBot` (v5), найденные при дочитывании `lib/DiscordMusicBot.js`.

- MUSIC-K001 — При создании player guild/text/voice channel и default volume/self-deafen берутся из единой конфигурации.
- MUSIC-K002 — Player создаётся только через отдельный factory `createPlayer()`, скрывающий детали audio manager.
- MUSIC-K003 — Controller строится динамически из состояния player: иконка и стиль Play/Pause меняются в зависимости от `playing`.
- MUSIC-K004 — Состояние Loop визуально отражается цветом и emoji кнопки: track repeat, queue repeat или off.
- MUSIC-K005 — При `playerCreate` глобальные audio policy defaults копируются в состояние конкретного player, после чего player может иметь собственные значения.
- MUSIC-K006 — При `playerDestroy` stale now-playing message очищается через player-level message lifecycle.
- MUSIC-K007 — `queueEnd` при autoQueue ищет следующий связанный трек по предыдущему identifier, исключая треки из ограниченной истории уже проигранных.
- MUSIC-K008 — Ошибка autoQueue сопровождается severity + техническим сообщением Lavalink и после этого player уничтожается.
- MUSIC-K009 — `queueEnd` без autoQueue показывает временный queue-ended embed перед запуском inactivity disconnect timer.
- MUSIC-K010 — Перед inactivity destroy player повторно проверяет `playing` и `state !== DISCONNECTED`, предотвращая уничтожение уже снова используемого player.
- MUSIC-K011 — Для внешнего audio manager используются lifecycle callbacks node/player/track/load/queue как единый event-driven pipeline.
- MUSIC-K012 — Event loader автоматически подключает каждый файл из `events/` и логирует факт загрузки конкретного event name.
- MUSIC-K013 — Command loader отдельно загружает slash и context commands, регистрируя каждую команду в соответствующей Collection.
- MUSIC-K014 — Некорректная команда не ломает загрузку остальных: loader выдаёт warning с конкретным именем файла и пропускает его.
- MUSIC-K015 — `createController()` является чистой UI-фабрикой, получающей guild id и player state и возвращающей готовый ActionRow.
- MUSIC-K016 — Общий клиент хранит helpers (`getLavalink`, `getChannel`, time formatter) как свойства, чтобы команды не импортировали инфраструктуру напрямую.
- MUSIC-K017 — Audio client ведёт runtime-счётчики команд и проигранных песен независимо от persistent database.
- MUSIC-K018 — `playerMove` после фактического перемещения обновляет voiceChannel и делает короткую задержку перед resume, учитывая eventual consistency Discord voice state.
