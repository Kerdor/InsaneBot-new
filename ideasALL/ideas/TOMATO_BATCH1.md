# Tomato6966 — Batch 1

Источник: `Tomato6966/Multipurpose-discord-bot`
Ветка: `new_2025`
Область: `commands/⌨️ Programming`

### TOM-001 — Онлайн-компиляция пользовательского кода
- Источник: Tomato6966/Multipurpose-discord-bot
- Категория: Programming / Utility
- Описание: Команда принимает code block с языком, отправляет исходный код во внешний сервис Coliru и возвращает результат выполнения.
- Механики / детали: Поддерживаются C/C++, C, Ruby, Lua, Python, Haskell и shell-варианты; язык берётся из markdown code fence. Если результат слишком длинный для сообщения, вместо него создаётся share-ссылка через сервис.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО

### TOM-002 — GitHub repository info card
- Источник: Tomato6966/Multipurpose-discord-bot
- Категория: Programming / Integrations
- Описание: Команда принимает ссылку на GitHub-репозиторий и показывает его метаданные в embed.
- Механики / детали: Проверяется формат `owner/repository`; через GitHub API получаются данные репозитория, отображаются название, описание, размер, версия/лицензия и другие метаданные; отдельно отмечаются fork и archived-репозитории; показывается avatar владельца и ссылка на репозиторий.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО

### TOM-003 — NPM package information lookup
- Источник: Tomato6966/Multipurpose-discord-bot
- Категория: Programming / Integrations
- Описание: Поиск пакета в NPM Registry с выдачей краткой карточки пакета.
- Механики / детали: Показываются latest version, license, author, дата изменения, описание и список dependencies; длинные списки maintainers/dependencies ограничиваются 10 элементами с указанием оставшегося количества.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО

### TOM-004 — NPM package size lookup
- Источник: Tomato6966/Multipurpose-discord-bot
- Категория: Programming / Integrations
- Описание: Отдельная команда для получения размера публикации и установки NPM-пакета.
- Механики / детали: Используется внешний Packagephobia API; размеры форматируются автоматически в Bytes/KB/MB/GB.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО

### TOM-005 — HTTP status meme lookup
- Источник: Tomato6966/Multipurpose-discord-bot
- Категория: Programming / Fun
- Описание: По HTTP-коду возвращается embed с описанием статуса и соответствующим изображением с http.cat.
- Механики / детали: Используется стандартный список `STATUS_CODES`; отдельно поддержан нестандартный код 599, которого нет в Node.js, но он есть на http.cat.
- Наш вариант: ⬜
- Статус: ⬜ НЕ РЕШЕНО

## Примечание
`compile.js` и `coliru.js` реализуют одну и ту же механику онлайн-компиляции, поэтому отдельной системой не считаются.
