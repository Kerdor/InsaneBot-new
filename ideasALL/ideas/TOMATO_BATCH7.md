# Tomato6966 — Batch 7

Источник: `Tomato6966/Multipurpose-discord-bot`
Ветка: `new_2025`

## `commands/👀 Filter`

### TOM-078 — 8D audio filter
- Применяет Lavalink rotation filter с `rotationHz: 0.2`.
- Сохраняет текущее состояние фильтра у player.

### TOM-079 — Bass Boost с уровнями
- Предустановленные уровни: `none`, `low`, `medium`, `high`, `earrape`.
- EQ применяется через наборы конфигурации; состояние EQ/filter сохраняется у player.

### TOM-080 — Набор пресетов Equalizer
- Предустановки EQ: music, pop, electronic, classical, rock/metal, full, light, gaming, bassboost, earrape.
- Для некоторых пресетов поддерживаются aliases.
- `earrape` дополнительно повышает volume на 50.

### TOM-081 — Сброс Equalizer/Filter
- `clearfilter` очищает EQ через `clearEQ()` и отправляет обновлённый filter state на node.
- Сбрасывает сохранённые состояния EQ/filter.

### TOM-082 — China voice filter
- Timescale: замедление + повышение pitch/rate для характерного эффекта.
- Состояние фильтра сохраняется у player.

### TOM-083 — Chipmunk voice filter
- Timescale с повышенной скоростью, pitch и rate.
- Состояние фильтра сохраняется у player.

### TOM-084 — Darth Vader voice filter
- Timescale с пониженным pitch и скоростью для низкого голоса.
- Состояние фильтра сохраняется у player.

### TOM-085 — Nightcore filter
- Timescale с повышенными speed/pitch/rate.
- Состояние фильтра сохраняется у player.

### TOM-086 — Ручная настройка pitch
- Пользователь задаёт множитель pitch числом.
- Есть проверка числа и диапазона `> 0` и `< 3`.

### TOM-087 — Ручная настройка speed
- Пользователь задаёт множитель speed числом.
- Есть проверка числа и диапазона `> 0` и `< 3`.

### TOM-088 — Ручная настройка rate
- Пользователь задаёт множитель rate числом.
- Есть проверка числа и диапазона `> 0` и `< 3`.

### TOM-089 — Slowmo filter
- Готовый timescale-профиль с сильным замедлением: speed `0.5`, rate `0.8`.

### TOM-090 — Tremolo filter
- Lavalink tremolo с заданными frequency/depth.
- В примере используются `frequency: 4.0`, `depth: 0.75`.

### TOM-091 — Vibrato filter
- Lavalink vibrato с `frequency: 4.0`, `depth: 0.75`.

### TOM-092 — Комбинированный Vibrate filter
- Одновременно применяет vibrato и tremolo с одинаковыми параметрами frequency/depth.

## Примечания по дубликатам
- `cleareq.js` и `clearfilter.js` проверены как варианты сброса EQ; отдельной новой механики не добавлено сверх TOM-081.
- `speed.js` и `rate.js` не объединены с `pitch.js`: это три независимых параметра Lavalink timescale.
- Все фильтры требуют активный music player; `.js` файлы области обработаны полностью.
