# MUSIC CONTEXT — Банк идей

Механики `ItzSudhan/Discord-MusicBot` (v5), найденные в `commands/context/play.js`.

- MUSIC-X001 — Context Menu `Play Song`: запуск поиска/проигрывания прямо через меню действий над Discord-сообщением.
- MUSIC-X002 — Context command получает содержимое целевого сообщения по `targetId`, сначала пытаясь взять его из cache и только затем делая fetch.
- MUSIC-X003 — Context Menu использует тот же audio pipeline, что и slash `play`: проверка Lavalink, создание player, подключение, поиск и обработка load types.
- MUSIC-X004 — Контекстный play работает с содержимым любого выбранного сообщения как поисковым запросом, не требуя ручного копирования текста.
- MUSIC-X005 — Context Menu наследует Stage Channel recovery для `suppress`/request-to-speak.
- MUSIC-X006 — Context Menu показывает такой же UX результата, как обычный play: added-to-queue, requester, duration, thumbnail и playlist statistics.
- MUSIC-X007 — Контекстный ответ `Searching...` автоматически удаляется через TTL после завершения операции.
