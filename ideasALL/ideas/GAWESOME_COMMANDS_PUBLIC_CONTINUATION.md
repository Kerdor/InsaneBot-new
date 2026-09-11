# GAwesomeBot — Commands/Public — continuation

Источник: `GAwesomeBot/bot`, branch `indev-4.0.2`.

Этот файл продолжает source-specific проход по `Commands/Public/`. Проверенные здесь команды сверены с уже собранным global bank; новые глобальные механики здесь не создаются, если они уже канонизированы.

## Проверенные файлы

- `info.js` — server information card; уже канонизирована как **GD-258**.
- `invite.js` — выдача bot invite URL; самостоятельной новой механики не обнаружено.
- `joke.js` — внешний joke provider, progress message, ограничение длины результата и error fallback; отдельной новой механики относительно уже собранного UX/integration слоя нет.
- `list.js` — server to-do list; уже канонизирована как **GD-248**.
- `lottery.js` — scaled points lottery; уже канонизирована как **GD-249**.
- `messages.js` — weekly message leaderboard / total weekly messages; покрывается существующим stats/leaderboard каноном.
- `translate.js` — перевод с явными source/target и специальным source `?` для автоопределения языка; базовая translation integration уже есть в общем банке.
- `twitter.js` — получение твитов через RSS с количеством результатов, progress message и pagination; provider-specific вариант уже покрыт stream/integration каноном.
- `wiki.js` — Wikipedia random/search, summary → full-content fallback для коротких summary, ограничение длинного текста ссылкой на статью и optional main-image fallback; отдельной системы не образует.
- `wolfram.js` — повторная проверка подтверждает **GAB-PUB-025–028**: progress-message reuse, pod aggregation, image fallback, отдельные no-result/error ветки.
- `xkcd.js` — latest comic или comic по номеру, timestamp и error fallback; отдельной новой системы не добавляет.
- `unban.js` — поиск пользователя среди банов, confirmation, unban и ModLog; базовый moderation workflow уже покрыт.
- `unmute.js` — action/permission/hierarchy checks, проверка факта mute, unmute и ModLog; базовый moderation workflow уже покрыт.
- `year.js` — exact countdown + humanized summary; уже канонизирована как **GAB-PUB-109**.
- `youtube.js` — поиск video/playlist/channel, ограничение количества результатов и pagination; provider-specific search уже покрыт integration каноном.

## Вывод

Этот набор файлов проверен и не требует новых `GD-*` механик на текущем этапе. Однако `Commands/Public/` в целом ещё не закрыт: необходимо добрать оставшиеся файлы из полного дерева директории и только после этого объявлять source-specific Public pass завершённым.
