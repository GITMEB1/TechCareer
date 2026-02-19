# TechCareer Repository — Critical Architecture & Process Review

**Date:** 2026-02-19  
**Reviewer:** Codex (GPT-5.2-Codex)  
**Scope:** End-to-end review of repository purpose, logic, workflows, governance, and execution quality.

---

## 1) What this project is for

This repository is a **career operations system** for a single candidate (Danny Jackson), designed to run in an **agent-first mode**. It aims to turn opportunity discovery into a repeatable pipeline:

1. Find opportunities (`Opportunity Radar`).
2. Produce role-specific materials (`Application Factory`).
3. Support last-mile form submission (`Application Submission`).
4. Drive proactive outreach (`Networking Outreach`).

Its strategic differentiator is credibility control through:
- A canonical source of truth (`SSOT.md`),
- Guardrail docs (`rules/`),
- Structured artifact schemas (`schemas/`),
- Per-application evidence and language-risk logs (`applications/...`).

In intent, this is not just a folder of job docs; it is a **lightweight operating system for career recovery and income stability**.

---

## 2) How it works (actual operating model)

### 2.1 Governance layer
- `SSOT.md` defines identity, experience timeline, claims policy, and banned language.
- `rules/agent_operating_rules.md` defines process behavior (plan-first, traceability, verification).
- `rules/safety_guardrails.md` adds file/system and privacy constraints.

### 2.2 Process layer
Workflow specs in `.agent/workflows/` define mission-level behavior:
- Weekly scan and ranking (`opportunity_radar.md`)
- Opportunity-intel-gated drafting (`application_factory.md`)
- Assisted application execution (`application_submission.md`)
- Networking variants (`networking_outreach.md`)

### 2.3 Data layer
- Tracking state in `tracking/opportunities.yaml` + dashboard markdown.
- Structuring contracts in `schemas/*.yaml`.
- Application artifacts in `applications/YYYY-MM-DD-Company/`.

### 2.4 Prompt layer
`prompts/` contains system prompt packs for specific sub-agents, including opportunity intelligence and application generation.

---

## 3) Executive diagnosis

## Overall maturity score: **6.2 / 10**

### Strengths
- Strong evidence-safety intent and anti-hallucination posture.
- Good decomposition into workflows and artifacts.
- Explicit candidate positioning and risk-aware framing.
- Reusable application pack pattern.

### Core weakness pattern
The repo has **excellent strategic intent but weak enforcement mechanics**. Many critical controls are “policy-only” rather than executable checks, creating drift between intended process and produced artifacts.

---

## 4) Critical findings (high-value issues)

## F1 — Schemas are pseudo-specs, not enforceable schemas (**High impact**)
Current files under `schemas/` are template YAML examples, not JSON Schema/OpenAPI/CUE/typed contracts. There is no validator script or CI check proving conformance.

**Impact:**
- Agents can produce structurally invalid data without detection.
- Downstream automation cannot reliably parse fields.
- “Validation” is claimed in workflow docs but not technically implemented.

**Missed opportunity:**
The project brands itself on operational rigor but lacks machine-enforced rigor at its core interface boundary.

**Recommendation:**
Replace schema templates with formal JSON Schema (`.schema.json`) and add `scripts/validate.py` + CI check against:
- `tracking/opportunities.yaml`
- all `applications/*/opportunity_intel.yaml`

---

## F2 — State model inconsistency across workflow, tracking, and dashboard (**High impact**)
There are conflicting status vocabularies and lifecycle states:
- Workflow expects statuses like `Drafting`/`Ready`.
- `schemas/opportunity.yaml` status enum differs.
- `tracking/OPPORTUNITY_RADAR.md` uses `Drafted`, which is not canonical.

**Impact:**
- Breaks automation and handoff logic.
- Increases operator confusion.
- Causes false progress signaling.

**Recommendation:**
Create a single finite state machine (FSM) document and enforce status enums centrally. Add a linter that rejects unknown states.

---

## F3 — Evidence policy is strong in SSOT but weakly applied in artifacts (**High impact**)
Example artifacts include claims with unsupported quantified outcomes (e.g., time savings) and inconsistent verification labeling. Some language gate checks validate against terms not listed in SSOT banned list, while missing stronger checks (e.g., unverifiable percentages).

**Impact:**
- Reputational and trust risk in candidate-facing materials.
- Potential contradiction between “evidence-safe” promise and output reality.

**Recommendation:**
Add a deterministic claims audit step:
1. Extract numeric/absolute claims via regex/NLP.
2. Require linked SSOT citation + evidence status.
3. Block finalization if unresolved.

---

## F4 — README overstates available runtime structure (**Medium-high impact**)
README references workflow usage from `.agent/workflows/` (correct), but broader user guidance assumes runtime conventions and artifacts that are not currently enforced by scripts/commands. This can mislead users into assuming “run workflow” is executable rather than instructional.

**Impact:**
- Onboarding friction.
- Expectations gap for non-expert users.

**Recommendation:**
Add a `scripts/` command surface (`make radar`, `make apply COMPANY=...`) or explicitly label current system as “manual/spec-driven.”

---

## F5 — Missing quality gates and CI baseline (**High impact**)
No automated checks for:
- YAML validity,
- schema conformance,
- forbidden phrase scanning,
- unresolved UNVERIFIED claims,
- stale deadlines in opportunities,
- missing mandatory files per application folder.

**Impact:**
Manual review burden scales poorly and quality regresses silently.

**Recommendation:**
Introduce minimal CI pipeline:
- `yamllint`
- schema validation
- policy checks (banned terms, unresolved claims)
- folder completeness check for each application pack

---

## F6 — Data model under-specifies key operational fields (**Medium impact**)
Opportunity entities lack stable fields for:
- salary range and hard floor validation,
- explicit commute-time estimate,
- deadline/source reliability score,
- owner/action timestamps,
- rejection reason taxonomy.

**Impact:**
Limits analytical learning loop and prioritization quality.

**Recommendation:**
Extend opportunity schema and build weekly “pipeline health” rollup.

---

## F7 — Prompt/config duplication drift risk (**Medium impact**)
Policy exists across `SSOT.md`, rule files, workflow docs, and prompt packs. There is no generated source hierarchy or single import path, so wording and constraints may diverge over time.

**Impact:**
- Conflicting instructions to agents.
- Subtle behavior drift.

**Recommendation:**
Define config precedence and generate prompt fragments from a single canonical policy file.

---

## F8 — Artifact quality varies significantly between opportunities (**Medium impact**)
Application folders show uneven discipline in evidence checks, language gates, and tone consistency. Some artifacts are highly strategic; others are loosely validated and include risky phrasing.

**Impact:**
Inconsistent application quality likely reduces hit rate and introduces avoidable rejection risk.

**Recommendation:**
Adopt a release checklist for every application packet with binary pass/fail gates.

---

## 5) Logic and process critique

## What is logically strong
- The North Star and role archetype targeting are clear.
- The project recognizes that “support/implementation” history must be reframed into modern engineering language without fabrication.
- Human-in-the-loop posture is appropriate for high-stakes external communication.

## Where logic is currently brittle
- “Validation” is treated as narrative, not as executable control.
- The process has a drafting-heavy bias but insufficient final-approval and audit automation.
- Tracking model cannot yet support meaningful pipeline analytics (conversion, cycle time, failure modes).

---

## 6) Structural review

## Good structure choices
- Clean top-level segmentation (`rules/`, `schemas/`, `tracking/`, `applications/`, `.agent/workflows/`).
- Predictable application folder naming.

## Structural risks
- Hidden operational dependency on `.agent/` workflows not mirrored with explicit command tooling.
- Mixed canonical artifacts (`SSOT.md` + `SSOT_Legacy.md`) can create ambiguity unless archival status is explicit.
- Markdown-heavy process without machine-readable audit outputs.

---

## 7) High-value insights likely missed

1. **This project is one automation layer away from being a real “career CRM.”**  
   With strict schemas + CI + metrics, this can become a compounding advantage rather than static docs.

2. **Your strongest moat is not prompt wording; it is evidence governance.**  
   Competitors can copy prompts, but few maintain disciplined claim integrity under pressure.

3. **Current opportunity ranking is too qualitative.**  
   Add weighted scoring dimensions (fit, salary, commute, application friction, growth value) to improve decision quality.

4. **You need outcome telemetry, not just artifact creation.**  
   Track response rate, interview rate, time-to-apply, and reason-for-rejection to iterate strategically.

5. **Create two execution modes intentionally:**  
   - **Speed Mode** (good-enough applications with strict safety checks)  
   - **High-Conviction Mode** (deep tailoring for top roles)  
   Current materials imply this split but do not operationalize it.

6. **Submission workflow is the highest risk surface.**  
   Introduce a final immutable pre-submit packet (snapshot) so what is sent can always be reconstructed and audited.

---

## 8) Priority remediation roadmap

## Phase 1 (1–3 days): Control foundations
- Formalize schemas in machine-readable format.
- Add validation scripts and pre-commit/CI checks.
- Normalize status FSM across all docs/data.

## Phase 2 (3–7 days): Evidence and language hardening
- Implement claim extractor + evidence linker.
- Enforce unresolved-claim block.
- Unify banned/approved term dictionaries.

## Phase 3 (1–2 weeks): Analytics and optimization
- Add pipeline metrics in `tracking/` (conversion funnel, cycle times).
- Introduce weighted opportunity scoring model.
- Add weekly retrospective artifact with action deltas.

---

## 9) Conclusion

This repository has a **high-quality strategic blueprint** and a thoughtful credibility ethos. The primary gap is execution reliability: too many controls are advisory rather than enforceable. If you convert policy into automated gates, this can become a genuinely differentiated system for career outcomes, not just polished documentation.

**Bottom line:** keep the philosophy; harden the mechanics.
