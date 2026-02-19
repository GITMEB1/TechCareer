# Verification & Regression Audit — Round 2

**Date:** 2026-02-19  
**Scope:** Mitigation verification + hardening audit after critical review.

## Verification Scorecard

| Review #1 Issue | Current Evidence | Status | Notes |
|---|---|---|---|
| Policy contradiction: banned term conflict (`orchestrated`) | SSOT §1.2 bans only **"orchestrated agents"** while Application Factory requires **"Orchestrated"** in every draft. | **PARTIALLY MITIGATED** | Direct lexical conflict reduced, but requirement still nudges risky wording and can produce policy-adjacent drift. |
| JD-as-evidence loophole | `evidence_traceability_check` still allows `source_type: "resume|portfolio|intel|jd"`. | **UNRESOLVED** | JD remains an accepted evidence source for capability claims. |
| Performative language gates | Tech Returners gate checks only one phrase; Aareon gate still checks generic buzzwords (e.g., ninja, rockstar, synergy). | **UNRESOLVED** | Gates are not aligned with SSOT §1.2 banned categories (absolutes, multipliers, undefined labels, tone hazards). |
| Fabricated metric in Tech Returners bullets | Tech Returners CV still includes **"reducing daily search time by 60%"**. | **UNRESOLVED** | Metric remains and is in SSOT §8 evidence backlog category (time-saved claims). |

## Section 1 — Mitigation Verification

### 1) "Orchestrated" conflict
- The hard contradiction appears softened from exact-token conflict, because SSOT bans `orchestrated agents` specifically, not the standalone verb/adjective.
- However, Application Factory still hard-requires the term `Orchestrated` in draft vocabulary, which can push outputs toward the banned phrase family and policy ambiguity.
- **Verdict:** **Partially mitigated, not structurally resolved.**

### 2) JD-as-evidence loophole
- The gate JSON schema still whitelists `jd` in `source_type`.
- This permits claims to be justified by employer requirements rather than candidate proof.
- **Verdict:** **Unresolved.**

### 3) Language gate realism
- The Aareon gate remains anchored to generic resume cringe terms; it does not systematically scan SSOT §1.2 classes (soft absolutes/multipliers/undefined labels/tone hazards).
- Tech Returners gate captures one explicit phrase correction but does not show category-level scanning.
- **Verdict:** **Unresolved.**

### 4) Fabricated metrics
- The 60% reduction metric is still present in `cv_bullets.md` and is not accompanied by external proof references.
- **Verdict:** **Unresolved.**

## Section 2 — Hardening Audit (New Controls)

### A) Pre-Draft Claim Inventory (Step 2.7)
- No Step **2.7** section is present in `prompts/application_factory.md`.
- Existing stops are at Intel Binding (2.5), then drafting begins at 3.
- Therefore the intended "pre-draft claim inventory" gate is either missing or not merged.

**Assessment:**
1. **Positioning:** Not early enough because it is absent.
2. **Rules for blocking UNVERIFIED / SSOT §8 metrics:** Not explicit in pre-draft flow; currently enforced only in later gate (section 4), after draft generation risk already occurs.
3. **Most likely hallucinated compliance path:** Agent emits a plausible-looking gate JSON with `verifiable: true` defaults and non-audited `source_reference` text, then proceeds without deterministic claim extraction.

### B) Soft Absolutes & Unsourced Reputation claims
- SSOT §1.2 currently lists Absolutes, Multipliers, Undefined Engineering Labels, and Tone Hazards.
- Explicit categories named "Soft Absolutes" and "Unsourced Reputation Claims" are not present as labeled sections.

**Missed violations in existing cover letters:**
- Tech Returners: "my career trajectory perfectly aligns" (soft absolute).
- Tech Returners: "failure was not an option" (absolute framing).
- Tech Returners: "I know what 'production' feels like" (unsourced reputation signal).
- Tech Returners: "Safe Pair of Hands reputation" (reputation claim without cited proof).
- Aareon: "every way a distributed system can fail" (soft absolute).
- Aareon: "absolute stability required" (absolute framing likely non-verifiable).

**Suggested additions (consultancy-speak hardening):**
- world-class, best-in-class, proven track record, trusted advisor, thought leader, unparalleled, end-to-end ownership (unless evidenced), transformative, seamlessly, robust at scale (unless evidenced), mission-critical expert.

## Section 3 — System Cohesion

### 1) Precedence hierarchy
- No `rules/policy_precedence.md` exists.
- `rules/agent_operating_rules.md` includes process and evidence posture, but no explicit source-of-authority tie-breaker across SSOT vs prompts vs workflow docs.

**Risk remains:** in conflicting instructions, agents can cherry-pick or obey nearest-context prompt wording over global policy.

### 2) Open-loop outcomes
- `schemas/opportunity.yaml` includes status values but no structured rejection-reason taxonomy, no feedback fields, and no conversion telemetry model.
- `tracking/opportunities.yaml` currently tracks opportunity status but does not capture rejection reasons or closed-loop postmortems.

**Verdict:** system remains largely **open-loop** (activity tracked, learning signal under-captured).

## Last-mile deficiencies (blocking production-grade posture)
1. **No deterministic enforcement layer:** Policy checks are still narrative/manual and can be bypassed by performative PASS outputs.
2. **No authority precedence model:** Missing tie-breaker doc means unresolved prompt/policy conflicts remain a systemic failure mode.
3. **No outcome telemetry loop:** Rejection reasons and funnel metrics are not first-class data, so strategy cannot improve reliably over time.
