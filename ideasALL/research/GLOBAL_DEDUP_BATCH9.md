# GLOBAL DEDUP — BATCH 9

Тематическая область: финальная сверка `GAwesomeBot/Commands/Public/` после закрытия source-specific pass.

## Объём проверки

Повторно сверены все зафиксированные `GAB-PUB-001–109` с каноническим global bank `GD-001–287`, включая Batch 1–8 и тематические файлы.

## Результат

Новых канонических механик после `GD-285–287` не обнаружено.

Все оставшиеся Public-находки относятся к уже существующим кластерам:

- внешние search/info/provider-команды → существующий integrations/search/information канон;
- pagination, embeds, progress-message reuse, partial failure, humanized durations и structured errors → существующий UX/architecture/integration канон;
- Reddit/NSFW provider behavior → существующий filtering/integration канон;
- calculator, conversion, timezone и weather → существующий utility/integration канон;
- moderation commands и ModLog workflows → существующий moderation/modlog канон;
- points, ranks, weekly stats и leaderboards → существующий economy/progression/stats канон;
- channel cooldown/quiet/count и server to-do/lottery → уже канонизированы ранее, в том числе GD-230–259;
- `countdown.js`, `nick.js`, `roleinfo.js` → уже выделены отдельно как GD-285–287.

## Контроль дубликатов

Command interface не выделяется в отдельный `GD`, если underlying mechanic уже присутствует в global bank. Provider-specific варианты сохраняются только как детали существующего кластера, когда они не меняют саму систему.

## Итог

**Global Dedup завершён на `GD-287`.**

Нумерация `GD-288+` не создаётся искусственно: новых самостоятельных механик в финальной GAwesome Public сверке нет.

Следующий этап — построение RoadMap реализации на основе полного канонического банка `GD-001–287`.

`bot/main.py` и другая реализация InsaneBot не изменялись.
