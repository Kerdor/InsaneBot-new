# MUSIC WEB — Банк идей

Находки `ItzSudhan/Discord-MusicBot` (v5) из `api/` и `dashboard/`.

- MUSIC-W001 — Веб-панель работает как отдельный Express + Next.js слой поверх Discord-клиента.
- MUSIC-W002 — Веб-сервер запускается через отдельный `Server` EventEmitter-класс, которому передаётся основной Discord client.
- MUSIC-W003 — Express раздаёт статический публичный сайт из отдельного каталога.
- MUSIC-W004 — Скомпилированные Next.js `_next` assets подключаются отдельным static route.
- MUSIC-W005 — Сессии веб-панели используют `express-session` с настройкой `secure`, зависящей от HTTPS URL.
- MUSIC-W006 — Для Discord OAuth используется Passport Strategy, а профиль пользователя и access/refresh tokens сохраняются в session user object.
- MUSIC-W007 — OAuth scope автоматически фильтрует application scopes перед передачей Discord Strategy.
- MUSIC-W008 — Авторизация вынесена в отдельный Express middleware: отсутствие пользователя перенаправляет на `/login`, авторизованный запрос проходит дальше.
- MUSIC-W009 — API routes автоматически подключаются перебором файлов в `api/routes`, поэтому добавление нового route-файла не требует ручного списка импортов.
- MUSIC-W010 — После OAuth callback сессия явно сохраняется перед redirect на главную страницу.
- MUSIC-W011 — Есть отдельные web-маршруты для home, login, logout, dashboard и server list; защищённые страницы используют auth middleware.
- MUSIC-W012 — Dashboard API отдаёт runtime-статистику бота: commands ran, users, servers, songs played.
- MUSIC-W013 — Public data API отдаёт имя бота, версию, список slash-команд с описаниями, invite URL и признак текущей авторизации.
- MUSIC-W014 — Invite URL генерируется динамически из client ID, permissions и scopes текущей конфигурации.
- MUSIC-W015 — Frontend получает public bot data через единый `getData()` helper вместо прямого fetch в каждой странице.
- MUSIC-W016 — Dashboard frontend имеет отдельный typed API helper `getDashboard()` и интерфейс данных для статистики.
- MUSIC-W017 — Dashboard показывает статистику отдельными hoverable stat cards с названием, числом и иконкой.
- MUSIC-W018 — Пока API не ответил, статистические карточки показывают состояние `Loading` вместо пустого блока.
- MUSIC-W019 — Общий dashboard layout вынесен в `Content`, который автоматически добавляет боковую навигацию ко всем защищённым страницам.
- MUSIC-W020 — Navbar подсвечивает текущий раздел на основе `router.pathname`.
- MUSIC-W021 — В navbar есть постоянная нижняя Logout-кнопка, отделённая от основных разделов через Spacer.
- MUSIC-W022 — Страница списка серверов представляет каждый сервер компактной Avatar-карточкой с tooltip имени и переходом по `/servers/{id}`.
- MUSIC-W023 — Внешний вид avatar сервера получает случайный цвет из набора вариантов при рендере.
- MUSIC-W024 — Server component принимает минимальный контракт `icon/name/id`, отделяя данные сервера от его визуального представления.
- MUSIC-W025 — Главная страница рекламирует возможности бота отдельными feature cards и содержит быстрые CTA Login, Dashboard и GitHub.
- MUSIC-W026 — Главная страница автоматически редиректит пользователя на `data.redirect`, если API возвращает redirect-назначение.
- MUSIC-W027 — Login и Logout реализованы как промежуточные страницы с автоматическим client-side redirect на API endpoint и текстом состояния для пользователя.
- MUSIC-W028 — NextUI тема задаётся глобально через `NextUIProvider`, в проекте используется dark theme по умолчанию.
- MUSIC-W029 — Общие CSS reset/baseline стили подключаются через кастомный Next.js `_document` и `CssBaseline.flush()`.
- MUSIC-W030 — Веб-модель сервера предусматривает представление текущего трека, currentTime/duration, queue и независимых loop-флагов song/queue, даже если полноценное управление ещё не реализовано.
- MUSIC-W031 — API и frontend разделяют public-информацию и защищённую runtime-статистику: data endpoint доступен без auth, dashboard endpoint требует session user.
