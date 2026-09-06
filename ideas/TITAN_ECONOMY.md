# TITAN ECONOMY — Банк идей

Находки `codebymitch/TitanBot` (main), первые команды `Economy/`.

- TITAN-E001 — Economy balance разделяет wallet и bank и показывает bank capacity и общий total.
- TITAN-E002 — Balance command принимает optional user и позволяет посмотреть баланс другого пользователя.
- TITAN-E003 — Bot accounts явно исключены из economy balance с отдельной validation error.
- TITAN-E004 — Beg command использует отдельный cooldown и конфигурируемые min/max reward.
- TITAN-E005 — Beg имеет вероятностный success/failure outcome и разные случайные flavor messages для каждого результата.
- TITAN-E006 — Cooldown error показывает пользователю оставшееся время в человекочитаемых minutes/seconds.
- TITAN-E007 — Crime system предлагает несколько типов преступлений с индивидуальными reward ranges и risk.
- TITAN-E008 — Crime success probability вычисляется из risk конкретного выбранного типа.
- TITAN-E009 — Failed crime одновременно создаёт jail duration и взымает штраф из wallet.
- TITAN-E010 — Размер штрафа зависит от среднего потенциального дохода выбранного crime, но не превышает имеющийся wallet.
- TITAN-E011 — Jail state блокирует повторный crime до `jailedUntil` и показывает оставшиеся минуты.
- TITAN-E012 — Fish system имеет редкости добычи от common до legendary и вероятностные диапазоны выпадения.
- TITAN-E013 — Рыбалка даёт случайный тип добычи внутри выбранной rarity tier.
- TITAN-E014 — Предмет fishing rod даёт +50% к денежной награде за рыбалку.
- TITAN-E015 — Fishing cooldown составляет отдельный action-specific timer и сохраняется вместе с economy data.
- TITAN-E016 — Economy state хранит action-specific timestamps (`lastBeg`, `lastFish`, `cooldowns.crime`) вместо одного общего cooldown.
- TITAN-E017 — Cooldown responses оформлены как структурированные rate-limit errors с machine-readable remaining time/type.
