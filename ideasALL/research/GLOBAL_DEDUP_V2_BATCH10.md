# GLOBAL DEDUP V2 — Batch 10

## Scope

Второй cross-check после Batch 1–9. Цель — повторно пройти уже проверенные тематические банки и финальные GAwesome Public findings, чтобы поймать пропущенные дубли между кластерами.

Проверены повторно:
- `GAWESOME_COMMANDS_PUBLIC_CONTINUATION.md`;
- `COMMUNITY.md`;
- `EVENTS.md`;
- `FILTERING.md`;
- `FUN.md`;
- `GAMES.md`;
- `GAMES_TRIVIA_ADVANCED.md`;
- `ECONOMY_ADVANCED.md`;
- `CUSTOMIZATION.md`;
- `MODERATION.md`;
- `COMMAND_CATALOG.md` как raw catalog (без превращения команд в отдельные systems).

Правило: ничего полезного не удалять. Если найденная механика уже существует — объединять её в существующий domain cluster, сохраняя source ID, UX, ограничения, recovery и варианты поведения.

---

## 1. GAwesome Public residual cross-check

### `countdown.js`
Уже корректно выделен как `GD-285` в Batch 8. Это server-scoped named countdown, а не обычный personal reminder.

### `nick.js`
Уже корректно выделен как `GD-286`. Self/admin nickname management не объединять с nickname enforcement из moderation: изменение nickname и принудительное enforcement имеют разные lifecycle и purpose.

### `roleinfo.js`
Уже корректно выделен как `GD-287`. Это inspection surface над role state, а не self-role выдача или role editing.

### `streamers.js`
Повторно подтверждено: это command-level live-status surface над существующим multi-provider stream monitoring. Нового standalone system не создаёт. Сохранить provider-specific presentation, server-tracked streamer list и pagination.

**Решение:** новых GD нет.

---

## 2. Community / Events second pass

`COMM-001–013` повторно сопоставлены:
- giveaway → `GD-054`;
- JTC → `GD-055`;
- counters → `GD-056`;
- reaction/self-service roles → `GD-057` / role cluster;
- birthday → `GD-058`;
- user notes → `GD-059`;
- moderation case management → moderation/modlog cluster;
- ticket claim/priority/limits/transcripts → ticket platform.

`EVENT-001–020` подтверждают ту же картину:
- giveaway/birthday → соответствующие domain systems;
- scheduled announcements, reminders, recurring events, QOTD, daily tasks и temporary events используют общий scheduler, но не должны автоматически сливаться в одну пользовательскую систему;
- background tasks остаются infrastructure capability.

**Новых standalone systems не найдено.**

---

## 3. Filtering second pass

`FILTER-001–018` — единый **Filtering / Content Control** domain, а не 18 систем.

Обязательно сохранить внутри него:
- guild + channel scope;
- thread inheritance;
- nickname/display-name filtering;
- safe nickname fallback;
- hit-count/timeframe autoban;
- per-user hit window/reset;
- word-boundary и case-insensitive matching;
- анализ poll/attachments/forwarded snapshots/embeds/components;
- edited-message recheck;
- modlog case types для filter hit и filter ban;
- trusted-user automod immunity;
- compiled-regex cache и invalidation;
- paginated DM export;
- bulk add/remove;
- отдельную presentation/reason configuration.

Это подтверждает существующий Filtering/Automod cluster из предыдущей дедупликации. Нового standalone system нет.

---

## 4. Games / Trivia second pass

`GAME-*` и `TRIVIA-*` не создают отдельную систему на каждую игру или helper.

### Games
Мини-игры, casino, expandable game catalog, rankings/statistics и economy rewards относятся к Games/Fun + соответствующим progression/economy mechanics.

### Trivia
`TRIVIA-001–014` — расширение одной Trivia system.

Сохранить:
- объединение нескольких question sets;
- user-uploaded YAML sets + schema validation + list/delete + attachment timeout/cancel;
- per-list CONFIG и возможность запретить override server config;
- AUTHOR/DESCRIPTION metadata;
- score threshold termination;
- separate answer/inactivity timers;
- bot-as-player option;
- randomized answer/reveal messages и spoiler mode;
- flexible answer normalization/matching;
- conditional economy reward, tie split и max-balance protection;
- persistent participant statistics;
- one active session per channel;
- force-stop path;
- independent async task lifecycle и safe NotFound/Forbidden termination.

**Решение:** одна Trivia system с богатым набором mechanics. Нового standalone system нет.

---

## 5. Economy advanced second pass

`ECONA-001–009` повторно подтверждены как детали существующей Economy domain:
- per-user PayDay cooldown;
- role-dependent PayDay;
- slot combination/payout table;
- min/max bet validation;
- independent gambling cooldown;
- payout-table presentation/DM fallback;
- balance clamp at max;
- paginated economy leaderboard;
- global vs server economy mode.

Не создавать отдельные системы для PayDay cooldown, slot payout table или balance clamp.

---

## 6. Customization second pass

`CUST-001–032` повторно сверены.

Главное правило сохранено:
- custom command и alias — разные underlying mechanics;
- keyword/regex trigger — отдельные mechanics внутри customization;
- placeholders, randomized responses, raw view, metadata и per-command cooldown — свойства custom-command platform;
- server/global alias с сохранёнными аргументами — отдельная alias mechanic;
- server-scoped configuration остаётся `GD-071`/configuration architecture;
- auto-role после join не смешивается с self-service roles.

Новых standalone systems нет.

---

## 7. Moderation second pass

`MOD-*` повторно сверены с moderation, infraction, cleanup, mute, nickname-enforcement, tickets и filtering clusters.

Особенно подтверждены важные distinction rules:
- warn/infraction lifecycle ≠ user notes;
- nickname enforcement ≠ обычный nickname edit (`GD-286`);
- mute ≠ channel quiet;
- ticket moderation channel ≠ generic moderation case;
- filter hit ≠ filter-ban case;
- hierarchy checks и service helpers — reusable safety infrastructure, не отдельные systems.

Новых standalone systems из thematic `MODERATION.md` не найдено.

---

## 8. Raw COMMAND_CATALOG cross-check

`COMMAND_CATALOG.md` содержит названия command surfaces, dashboard/API surfaces и architecture findings. Он намеренно не превращается в отдельный canonical source: command name сам по себе не равен standalone system.

При cross-check:
- music commands → existing Music/Audio clusters;
- dashboard/API → web/control-plane architecture;
- command/event loaders → cog/command lifecycle;
- DB helpers → storage architecture;
- Lavalink helper → audio runtime;
- logger → observability;
- global/guild deploy/destroy → command deployment lifecycle.

**Новых standalone systems только из command names не создаём.**

---

## 9. Cross-source duplicate check

Повторный проход подтверждает несколько важных границ:

1. `GD-285 Countdown` ≠ personal reminder.
2. `GD-286 Nickname Management` ≠ Nickname Enforcement.
3. `GD-287 Role Inspection` ≠ Self-service Roles ≠ Role Editing.
4. Trivia question-set management ≠ generic file upload system.
5. Economy reward mechanics ≠ generic scheduler.
6. Filtering ≠ generic moderation case storage, хотя filter events создают cases.
7. Ticket panel recovery ≠ generic persistent panel feature; domain state и reusable recovery infrastructure должны сосуществовать.
8. Music health/statistics ≠ generic bot healthcheck.
9. Extension update ≠ bot self-update.
10. Command surface ≠ standalone system без самостоятельного underlying lifecycle/state.

---

## Итог Batch 10

### Новых standalone systems

**0 подтверждённых.**

### Что дополнительно подтверждено

- GAwesome residual mechanics уже полностью закрыты `GD-285–287`.
- `streamers.js` остаётся частью existing streams monitoring.
- Filtering, Trivia, Economy Advanced, Customization и Moderation не содержат пропущенных самостоятельных systems при повторной сверке.
- Raw command catalog не должен раздувать canonical bank за счёт названий команд.

Исходные тематические/source-specific файлы не изменяются и не удаляются.
RoadMap всё ещё **не начинаем**: следующим шагом остаётся продолжение all-files cross-source audit и затем финальная проверка канонического банка на пропуски/дубли.
