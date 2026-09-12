# GLOBAL DEDUP V2 — Batch 4

Дата: 2026-09-12

## Scope

Строгий повторный аудит CorwinDev event batches:
- `CORWIN_BATCH4.md` (`COR-202–248`)
- `CORWIN_BATCH5.md` (`COR-249–293`)

Сверка выполнена против:
- `GD-001–287`;
- `GLOBAL_DEDUP_V2_BATCH1–3`;
- тематических систем `ideasALL/ideas`.

Правило: source IDs не удаляются. Объединение означает привязку к общей системе/кластеру с сохранением source-specific UX, ограничений, recovery и архитектурных вариантов.

---

## 1. Client / startup / errors

### COR-202–204 — shard ready / rotating presence / global guild count
**Решение:** не отдельные пользовательские системы.
- shard-ready → startup/observability;
- rotating presence → presence/status subsystem;
- global guild count → shard-aware runtime metric.

Связать с существующими runtime diagnostics и startup orchestration, но не смешивать presence UX с health/readiness.

### COR-205–206 — error code + fallback error response
**Решение:** merge в централизованный error-handling cluster (`ARCH-025`, `PDIS-B006/007`, Titan error context).

Сохранить:
- короткий user-facing error code;
- developer log correlation;
- fallback response, если основной error response не отправился.

Это полезные детали восстановления, а не отдельные системы.

---

## 2. Guild lifecycle

### COR-207–211 — guild init / welcome / join & leave logs / full cleanup
**Решение:** общий **guild lifecycle + configuration bootstrap** cluster.

- COR-207 → startup/config bootstrap, рядом с `PDIS-B001` и `DATA-007`;
- COR-208 → bot-added onboarding/welcome;
- COR-209/211 → lifecycle audit/observability;
- COR-210 → guild data cleanup/reconciliation.

COR-210 не следует поглощать обычным `guildDelete` event logging: это отдельная destructive data-cleanup policy.

### COR-212 — удаление ticket metadata при удалении channel
**Решение:** ticket data self-healing / orphan cleanup. Объединить с общими orphan-record maintenance patterns, но сохранить ticket-specific trigger.

---

## 3. Discord audit / logging

### COR-213–224 — channel, emoji, scheduled-event, role lifecycle/diff logs
**Решение:** единый **Discord audit/event logging** subsystem, а не отдельная система на каждый event.

Сохранить отдельные event types и Before/After детали:
- channel create/delete/rename/topic/pins;
- emoji create/delete/rename;
- scheduled event create/delete/update;
- role create/delete/name/color/permissions.

### COR-225 — member role diff
**Решение:** merge с существующим moderation/member audit (`PDIS-M3-003`), сохранив fallback через Audit Logs для partial member.

### COR-226 — ban/unban audit
**Решение:** существующий moderation/modlog cluster. Отдельный event type, не новая система.

---

## 4. Boost / invite / member social lifecycle

### COR-227–228 — boost/unboost templates + dedicated channel
**Решение:** существующий community/server-event announcement cluster. Template placeholders и dedicated channel — configuration details.

### COR-229–230 — invite-aware leave processing + placeholders
**Решение:** **invite tracking system**, но не отдельная leave system.

Связать с COR-249–255 ниже. Invite attribution, counters, rewards и invite-aware welcome/leave должны стать одной системой.

---

## 5. Message / progression / AFK / chatbot / sticky / custom commands

### COR-231 — DM logging
**Решение:** generic message/audit logging с отдельным DM source. Не отдельная user-facing system.

### COR-232 — message-based XP
**Решение:** существующий progression/XP cluster (`PROGRESSION`, `GD-...` progression systems). Сохранить random XP, level-up message и role reward как mechanics.

### COR-233 — message-count role rewards
**Решение:** progression/reward cluster. Отличать от XP: trigger — абсолютный message count, поэтому это отдельный mechanic внутри progression, не duplicate XP.

### COR-234–235 — AFK auto-clear + multi-user mention detection
**Решение:** один **AFK system**. Batch lookup при multi-mention — performance/UX detail.

### COR-236 — dedicated AI chatbot channel
**Решение:** external AI/chat integration cluster. Channel scoping — per-guild configuration. Не объединять с generic custom commands.

### COR-237 — sticky message re-publish
**Решение:** существующий sticky/persistent message system if present in thematic files; otherwise отдельный candidate. Core semantics: one canonical message is re-published after new messages and its message ID is persisted.

### COR-238 — prefix + mention command compatibility
**Решение:** command invocation/access layer. Связать с `CORE-012` и существующими command architecture variants.

### COR-239 — mention-only bot help
**Решение:** help/discovery UX (`PDIS-A003–005`), не отдельная система.

### COR-240 — custom commands via message events
**Решение:** existing custom commands cluster (`GD-065–072`). Normal/Embed/DM modes сохраняются.

---

## 6. Giveaway interaction feedback

### COR-241–243 — DM confirmation / ended feedback / winner DM
**Решение:** существующий Giveaway (`GD-054`) как interaction/notification variants.

Не создавать отдельные systems только из-за delivery channel.

---

## 7. Security / verification / reaction roles

### COR-244 — developer global interaction ban
**Решение:** existing global access-control/blocklist architecture (`ACCESS-001`, `ACCESS-011`, `PDIS-B005`). Это interaction-gateway enforcement variant.

### COR-245 — CAPTCHA verification
**Решение:** verification system. Это новая/важная mechanic внутри verification lifecycle, не смешивать с DEFCON account-age moderation (`PDIS-M2-001/002`).

### COR-246–247 — ephemeral reaction-role feedback + multi-select toggle
**Решение:** existing self-service role panel / reaction-role cluster (`GD-057`, `ROLE-001`, Titan TRR). Preserve multi-select toggle semantics and ephemeral result UX.

### COR-248 — component routing through customId
**Решение:** reusable **interaction/component routing** infrastructure. Связать с `ARCH-024`, persistent interactive UI and panel systems. Не делать отдельной feature.

---

## 8. Invite system — COR-249–255

### COR-249–250 — invite create/delete logs
**Решение:** invite tracking/audit details.

### COR-251–252 — inviter attribution + counters
**Решение:** один **Invite Tracking & Statistics** system.

Состояние должно учитывать как минимум:
- member → inviter relation;
- current/valid invites;
- total invites;
- left count.

### COR-253–254 — invite-aware welcome + unknown-source fallback
**Решение:** тот же invite system, как welcome integration. `System` fallback сохраняется как важный recovery/accuracy behavior.

### COR-255 — role rewards for invite milestones
**Решение:** тот же invite system + generic role-reward mechanic. Не превращать каждый reward threshold в отдельную систему.

**Cross-check:** COR-229/230 из Batch 4 и COR-249–255 образуют одну систему; источник нельзя считать двумя разными системами.

---

## 9. Message audit

### COR-256–259 — delete/edit logging + attachment + jump link
**Решение:** единый **message audit logging** cluster.

Сохранить:
- author/channel/timestamp;
- deleted content/first attachment URL;
- old/new edit content;
- jump-to-message action.

Это расширяет уже существующие deleted-message audit/recovery mechanics, но не отменяет privacy-aware/archive distinctions из V2 Batch 1.

---

## 10. Starboard

### COR-260–268 — starboard lifecycle
**Решение:** один самостоятельный **Starboard** system.

Механики внутри него:
- ⭐ threshold/update lifecycle;
- edit existing starboard message;
- delete at zero stars;
- self-star protection;
- ignore bot messages;
- guild configuration;
- empty-content rejection;
- supported image formats;
- partial reaction/message recovery.

Это не generic reaction-role system и не обычный message logging.

---

## 11. Server statistics

### COR-269–282 — dynamic statistics channels
**Решение:** merge в существующий **server counters/statistics** system (`GD-056`, related stats/community files).

Сохранить как statistic providers:
- total channels;
- text/voice/stage/forum/news;
- roles;
- members/bots;
- static/animated emoji;
- boosts;
- boost tier;
- server clock/timezone.

Template with emoji/name placeholders — presentation/config detail. Не создавать отдельную систему для каждого counter type.

---

## 12. Sticker / Thread audit

### COR-283 — sticker lifecycle audit
**Решение:** generic Discord audit/event logging cluster.

### COR-284–285 — thread lifecycle + human-readable type names
**Решение:** тот же audit cluster. Thread type normalization сохраняется как presentation helper.

---

## 13. Warn audit

### COR-286–287 — warn add/remove audit
**Решение:** existing moderation/infraction lifecycle (`PDIS-M3-006–014`). Это audit surface, не новая warn system.

---

## 14. Temporary voice channels

### COR-288–293
**Решение:** merge into **GD-055 Join-to-Create / temporary voice** cluster.

Corwin variant adds:
- voice-hub trigger;
- temporary channel DB tracking;
- empty-channel deletion;
- active temporary-channel counter;
- configurable name template;
- filtering irrelevant voice-state updates;
- dedicated voice-error handler.

**Важно:** не создавать вторую JTC system рядом с Titan `TJ-*`. Это ещё один source implementation variant. Titan has richer ownership/config/recovery; Corwin has simpler hub/counter semantics. Все детали сохранить.

---

# Cross-check / newly confirmed canonical candidates

1. **Invite Tracking & Statistics** — подтверждён как самостоятельный domain system из COR-229/230 + COR-249–255.
2. **Starboard** — самостоятельный system, не поглощать reactions/role panels.
3. **Sticky Message** — candidate; requires final cross-source search before canonical assignment.
4. **CAPTCHA Verification** — mechanic within verification system; no separate system.
5. **Discord Audit Logging** — broad infrastructure cluster, containing many event-specific variants.
6. **Temporary Voice/JTC** — one platform with multiple source variants; do not duplicate by source.

# Safety conclusion

В этом batch не найдено основания удалять какие-либо полезные source ideas. Основное исправление против прежнего подхода — не считать одинаковые domain systems разными только из-за разных event handlers, UI или storage details.

Source IDs COR-202–293 remain traceable and all unique behavior/constraints are preserved.