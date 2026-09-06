# MUSIC DEPLOY — Банк идей

Находки `ItzSudhan/Discord-MusicBot` (v5) из deployment/configuration файлов.

- MUSIC-D001 — Docker image использует Alpine Node base image для компактного runtime.
- MUSIC-D002 — Docker build выполняет dependency install и отдельный deployment/build script до запуска приложения.
- MUSIC-D003 — Container стартует единым `node index.js` entrypoint после подготовки окружения.
- MUSIC-D004 — Heroku Procfile выделяет bot runtime как `worker`, запускаемый через package script.
- MUSIC-D005 — Heroku `app.json` описывает deploy metadata, repository, logo, keywords и buildpack прямо в репозитории.
- MUSIC-D006 — One-click deployment manifest объявляет обязательные environment variables с human-readable descriptions.
- MUSIC-D007 — Deployment manifest отдельно описывает web dashboard URL и даёт localhost default для локального запуска.
- MUSIC-D008 — Replit configuration содержит минимальный run command и закрепляет Nix channel, отделяя platform runtime settings от application code.
- MUSIC-D009 — Docker и PaaS deployment используют существующие package scripts/entrypoint вместо отдельных копий логики запуска.
- MUSIC-D010 — Docker Compose разделяет bot и Lavalink на независимые сервисы с отдельными restart policies.
- MUSIC-D011 — Compose использует `depends_on`, чтобы бот запускался после объявления зависимости на Lavalink.
- MUSIC-D012 — Bot и Lavalink связываются через отдельную внутреннюю Docker network без публикации этой сети наружу.
- MUSIC-D013 — Конфигурация бота монтируется в контейнер read-only, позволяя менять runtime config без пересборки образа.
- MUSIC-D014 — Lavalink configuration также монтируется read-only из хоста, отделяя инфраструктурную конфигурацию от образа.
- MUSIC-D015 — Lavalink node можно полностью self-host'ить рядом с ботом через Compose, используя hostname сервиса как внутренний адрес.
- MUSIC-D016 — Lavalink отдельно настраивает допустимые audio sources и может отключать встроенный источник при использовании plugin-based реализации.
- MUSIC-D017 — Audio node имеет независимые настройки buffer duration и frame buffer duration для компромисса между устойчивостью и задержкой.
- MUSIC-D018 — Audio processing quality параметризуется отдельно: Opus encoding quality и resampling quality.
- MUSIC-D019 — Stuck-track threshold задаётся отдельной инфраструктурной настройкой.
- MUSIC-D020 — Seek ghosting можно включить как отдельную оптимизацию поведения буфера во время seek.
- MUSIC-D021 — Lavalink ограничивает глубину загрузки YouTube playlist числом страниц.
- MUSIC-D022 — Lavalink player update interval настраивается отдельно от Discord bot logic.
- MUSIC-D023 — Prometheus metrics endpoint предусмотрен как опциональный выключаемый компонент.
- MUSIC-D024 — Lavalink request logging имеет отдельные переключатели для client info, headers, query string и payload.
- MUSIC-D025 — Для request payload предусмотрено ограничение максимальной длины логируемого тела.
- MUSIC-D026 — File logging имеет отдельный путь и rolling policy с ограничением размера файла и количеством хранимых исторических файлов.
