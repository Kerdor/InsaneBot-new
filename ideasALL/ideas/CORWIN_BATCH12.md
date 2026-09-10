# CorwinDev — Batch 12

Источник: `CorwinDev/Discord-Bot`, branch `main`.

Продолжение полного обхода после закрытия `src/packages`: root/startup и файлы, связывающие запуск, sharding и внешние сервисы.

## Startup / infrastructure

### COR-355 — Проверка актуальности версии при запуске
- При старте бот запрашивает последний GitHub release.
- Если удалённая версия новее локальной, в консоль выводится предупреждение с предложением обновиться.
- Сравнение версий выполняется как числовые `major/minor/patch`, а не простым сравнением строк.

### COR-356 — Публикация метрик и команд в Top.gg
- При наличии `TOPGG_TOKEN` бот периодически отправляет в Top.gg агрегированное количество серверов и число shards.
- При запуске дополнительно публикуются доступные slash-команды.
- Количество guild собирается через `broadcastEval` со всех shards.

### COR-357 — Автоматическое восстановление умершего shard
- `ShardingManager` запускает shards с `respawn: true`, поэтому завершившийся shard автоматически восстанавливается.
- События неожиданной смерти shard логируются отдельно.

### COR-358 — Логирование shard reconnect/disconnect
- Для каждого shard отдельно логируются события `shardDisconnect` и `shardReconnecting` через webhook.
- В сообщениях указывается номер shard и состояние соединения.

### COR-359 — Единый override webhook credentials через `.env`
- Если заданы `WEBHOOK_ID` и `WEBHOOK_TOKEN`, они подставляются сразу во все настроенные webhook endpoints.
- Это позволяет использовать один набор webhook credentials вместо хранения отдельных credentials для каждого канала логов.

## Проверено дополнительно
- `src/assets/utils/forhumans.js` — форматирование duration в years/days/hours/minutes/seconds; новой пользовательской механики относительно каталога не добавляет.
- `src/assets/utils/static.js` — fallback `defaultPFP` и `DummyUser`; служебные значения.
- `src/dev.js` — CLI-скрипт выдачи developer badge; функциональность уже представлена через developer tooling/README и не вынесена в новый отдельный ID.
- `package.json` — scripts/dependencies/metadata; отдельной пользовательской механики сверх уже каталогизированной не добавляет.
- `.env.example` — переменные конфигурации уже отражены соответствующими системами.
- `README.md` — документация и список уже исследованных возможностей.
- `Dockerfile`, `.replit`, `replit.nix`, `start.bat`, `start.sh`, `.editorconfig`, `.gitignore`, `.vscode/settings.json`, `.github/FUNDING.yml`, `.github/dependabot.yml`, `.github/workflows/codeql.yml`, `LICENSE`, `package-lock.json` — инфраструктура/служебные файлы; новых пользовательских механик не найдено.
