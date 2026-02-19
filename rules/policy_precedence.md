# Policy Precedence & Authority Hierarchy

**Version:** 1.0
**Date:** 2026-02-19
**Purpose:** When instructions conflict across system files, this document defines which source wins. All agents and operators must apply this order.

---

## Authority Hierarchy (Highest → Lowest)

| Priority | Source | Scope | Rationale |
|---|---|---|---|
| **1 (Highest)** | `SSOT.md` — Credibility Policy (§0–§1) | All claims, evidence, language, identity | Non-negotiable factual and ethical layer. Nothing overrides it. |
| **2** | `rules/safety_guardrails.md` | File system, privacy, external actions | Protects against irreversible or harmful agent actions |
| **3** | `rules/agent_operating_rules.md` | Process discipline, planning, traceability | Defines how agents must operate |
| **4** | `.agent/workflows/*.md` | Mission-level sequencing, artifact structure | Workflow specs; may refine but cannot override higher tiers |
| **5** | `prompts/*.md` | Task-specific drafting instructions | Closest context to execution; highest drift risk — must stay in bounds |
| **6 (Lowest)** | Ad-hoc user instructions in a session | Single-session overrides | Can only operate within the space permitted by tiers 1–5 |

---

## Conflict Resolution Rules

### Rule 1 — SSOT Credibility Policy is Absolute
If any prompt, workflow, or user instruction requires producing content that violates `SSOT.md §1.2` (Banned Claims) or `§1.4` (Mandatory Claim Structure), the agent **must refuse** and explain the conflict. There are no exceptions.

### Rule 2 — Prompts May Refine, Not Override
A prompt in `prompts/` may add specificity (e.g., "use bullet format") but may not weaken a rule from a higher tier (e.g., remove an evidence requirement). If the prompt says something contradicts SSOT, SSOT wins.

### Rule 3 — When in Doubt, Be More Restrictive
If two sources are ambiguous, apply the stricter interpretation. A false-negative (removing a claim that could have stayed) is safer than a false-positive (including a claim that shouldn't be there).

### Rule 4 — Document Conflicts, Don't Silently Resolve Them
If an agent detects a conflict between sources, it must flag it explicitly rather than silently applying one over the other. Output format:
```
POLICY CONFLICT DETECTED:
- Source A: [file + line] says [X]
- Source B: [file + line] says [Y]
- Applying: [which source wins, per hierarchy above]
- Recommended fix: [how to resolve the conflict in the source files]
```

---

## Known Conflicts & Resolutions (Log)

| Date | Conflict | Resolution Applied |
|---|---|---|
| 2026-02-19 | `prompts/application_factory.md` required "Orchestrated" in vocabulary; SSOT §1.2 bans "orchestrated agents" | "Orchestrated" removed from preferred vocab in prompt (Tier 5 yields to Tier 1) |
| 2026-02-19 | `prompts/application_factory.md` accepted `jd` as evidence source; SSOT §1.4 requires candidate proof | `jd` removed as valid `source_type` in prompt gate (Tier 5 yields to Tier 1) |
