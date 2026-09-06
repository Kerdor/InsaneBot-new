# PYTHON-DISCORD — Backend continuation

## PDIS-B008 — Startup presence announcement
- После успешного подключения bot автоматически отправляет короткий embed в специальный dev-log канал.
- В debug mode сообщение не публикуется, чтобы не засорять рабочий лог.
- Это отдельный startup heartbeat/visibility сигнал для команды.

## PDIS-B009 — Lazy import тяжёлого backend-модуля
- Package `__init__` откладывает импорт внутреннего sync cog до фактического `setup`.
- Это уменьшает import-time side effects и стоимость загрузки модуля.
- Паттерн полезен для расширений, которые подключают тяжёлые/побочные зависимости только при активации.
