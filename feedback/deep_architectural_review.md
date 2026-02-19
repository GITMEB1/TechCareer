# Deep Architectural and Strategic Review — TechCareer

## Executive Summary
The system’s biggest failure is **policy simulation without policy control**: it produces compliance artifacts (`claims_table`, `language_gate`, `evidence_check`) but does not enforce consistency between those artifacts and the actual CV/cover-letter output. This creates a false sense of safety while allowing unsourced and policy-violating claims to pass into candidate-facing documents. The second-order risk is strategic: high process friction is concentrated in drafting polish, while throughput/outcome learning loops are almost absent. As built, the system can repeatedly generate “well-formed” applications without measurably improving job-search results.

## Policy Coherence Findings

### 1) SSOT credibility policy is contradicted by prompt-level drafting constraints
- `prompts/application_factory.md` requires words like “Orchestrated.”, while SSOT bans “orchestrated agents” as undefined label risk. This is a direct lexical conflict that encourages edge-case violations under pressure. (`REQUIRED: ... "Orchestrated"` vs banned undefined labels).【F:prompts/application_factory.md†L87-L90】【F:SSOT.md†L40-L41】
- The same prompt mandates measurable outcomes in every paragraph (`Evidence Density`), even though SSOT explicitly marks rates/percent/time-saved claims as backlog items not for professional use unless verified. That pressure is exactly how fabricated or inflated metrics enter output. 【F:prompts/application_factory.md†L83-L86】【F:SSOT.md†L163-L168】
- Prompt evidence gate accepts claim sources from `intel|jd|resume|portfolio`; SSOT defines acceptable evidence labels around external proof or SSOT-supported grounding. This creates a loophole where a JD phrase can be treated as claim support for candidate capability. 【F:prompts/application_factory.md†L141-L147】【F:SSOT.md†L30-L36】

### 2) Mandatory claim structure is not consistently operationalized
- SSOT mandates capability claims follow `[Skill] + demonstrated by + [artifact/role] + resulting in + [measurable outcome]`, but shipped artifacts contain many claims not in this format (e.g., “I know what production feels like”, “failure was not an option”). There is no structured rejection of these claims in gates. 【F:SSOT.md†L54-L57】【F:applications/2026-02-19-TechReturners/cover_letter.md†L12-L13】

### 3) Conflict precedence exists implicitly but not as an explicit hierarchy
- `SSOT.md` calls itself canonical and non-negotiable for credibility, but no file specifies formal precedence across SSOT vs rules vs workflow vs prompts when they disagree. 【F:SSOT.md†L4-L5】【F:SSOT.md†L29-L30】
- Likely failure mode: agents follow the nearest procedural prompt (highly specific) over policy source (broad), producing compliant-looking but policy-inconsistent outputs.

### 4) Banned language list misses common credibility-risk patterns seen in existing artifacts
Observed risky patterns not explicitly banned in SSOT §1.2:
- **Implied absolutes without banned tokens**: “failure was not an option”, “every way a system can fail”, “perfectly aligns”. 【F:applications/2026-02-19-TechReturners/cover_letter.md†L10-L13】【F:applications/2026-02-19-AareonGroup/cover_letter.md†L7-L9】
- **Reputation claims with no evidence path**: “Safe Pair of Hands reputation.” 【F:applications/2026-02-19-TechReturners/cover_letter.md†L23-L24】
- **Outcome claims using soft-absolute framing**: “absolute stability required”. 【F:applications/2026-02-19-AareonGroup/cover_letter.md†L9-L10】

Recommended additions to banned list:
- “perfectly aligns”, “failure was not an option”, “every way a system can fail”, “safe pair of hands” (unless externally referenced), “absolute stability”, “Day 1 impact” (unless evidence-linked).

## Workflow Logic Findings

### Opportunity Radar
- **Skip failure mode**: If scan/analysis is skipped or shallow, low-fit opportunities still enter pipeline because only qualitative `fit_score` exists; no validation against salary floor/commute constraints is encoded in tracking schema fields. 【F:.agent/workflows/opportunity_radar.md†L14-L24】【F:SSOT.md†L16-L20】【F:schemas/opportunity.yaml†L3-L32】
- **Undocumented dependency**: Application Factory assumes a valid tracked opportunity or URL and Intel exists. If Radar isn’t run, quality and prioritization context degrades immediately. 【F:prompts/application_factory.md†L9-L17】

### Application Factory
- **Skip Step 5 (Language Gate) damage**: banned or inflated phrasing enters final artifacts with no post-hoc detector except manual review. Existing gate evidence shows non-SSOT terms are scanned while real SSOT hazards are missed. 【F:.agent/workflows/application_factory.md†L34-L40】【F:applications/2026-02-19-AareonGroup/language_gate.md†L4-L13】
- **Detection weakness**: gate quality is self-reported markdown; no structural check ensures every claim in CV/CL appears in claims table.

### Application Submission
- **State mismatch failure**: workflow reads opportunities with status `Drafting` or `Ready`, but opportunity schema does not include either value. This can block or misroute submission handoff. 【F:.agent/workflows/application_submission.md†L15-L16】【F:schemas/opportunity.yaml†L32】
- **Audit risk**: requires screenshot + status update but not immutable payload snapshot of submitted text/files. Cannot reconstruct “what was sent” if portal-normalized content changed. 【F:.agent/workflows/application_submission.md†L29-L32】

### Networking Outreach
- **Orphan risk**: logging may be in opportunity record “or separate networking log,” but no schema for networking object exists. Results become non-queryable and disconnected from conversion analytics. 【F:.agent/workflows/networking_outreach.md†L31-L32】【F:schemas/opportunity.yaml†L3-L32】

### Human-in-the-loop gate timing (current vs optimal)
- Current formal gate occurs after draft generation (review `claims_table`/`language_gate`). This is late; risky language already generated and often emotionally sticky. 【F:.agent/workflows/application_factory.md†L41-L47】
- Better gate placement: before drafting (approve claim inventory + allowed evidence set) and before submission (approve immutable pre-submit packet).

## Data Model Findings

### Status inventory and conflicts
Distinct status values observed:
- Opportunity schema: `New, Applied, Interviewing, Waiting, Rejected, Won, Archived`. 【F:schemas/opportunity.yaml†L32】
- Application schema: `Drafting, Submitted, FollowUpSent, Interviewing, Closed`. 【F:schemas/application.yaml†L22】
- Submission workflow expects opportunity status `Drafting` or `Ready`; writes `Applied`. 【F:.agent/workflows/application_submission.md†L15-L16】【F:.agent/workflows/application_submission.md†L30-L32】
- Dashboard uses `Drafted` (not in schemas). 【F:tracking/OPPORTUNITY_RADAR.md†L8-L10】

Conflicts:
1. `Drafting`/`Ready`/`Drafted` are inconsistent and cross-entity ambiguous.
2. `Submitted` vs `Applied` duplicates same event in different vocabularies.
3. No explicit rejection sub-states (ghosted vs rejected with reason).

### Missing fields in `schemas/opportunity.yaml` for decision analytics
Missing for key questions:
- **Conversion rate**: no `application_id`, no `response_received_at`, no `interview_count`, no final outcome reason taxonomy.
- **Time-to-apply**: no `date_shortlisted`, `date_started_application`, `date_submitted` in opportunity object.
- **Why rejected**: no `rejection_reason_code`, no `rejection_notes_source`.
- **Best sources**: has `source` but no normalization, no source-level confidence, no channel attribution for networking referrals.

### Application-level model exists in schema, but not in operational state
- `schemas/application.yaml` defines an application entity, but repository has no persistent `applications.yaml` index and no serialized application records generated in app folders. This loses transition data between drafted artifacts and actual submission outcomes. 【F:schemas/application.yaml†L1-L22】

### Proposed status FSM (unified)
`Discovered -> Qualified -> IntelReady -> Drafting -> EvidenceGatePassed -> ReadyToSubmit -> Submitted -> FollowUpScheduled -> Responded -> Interviewing -> Offer|Rejected|Withdrawn -> Archived`

Rules:
- Only `Opportunity` carries funnel state.
- `Application` carries artifact state (`draft_exists`, `gate_passed`, `submitted_snapshot_id`).
- `Submitted` requires immutable submission snapshot hash + timestamp + channel.

## Evidence Integrity Findings

### Claim trace table (quantified or absolute claims found)
| Artifact | Claim | SSOT trace | Classification | Why |
|---|---|---|---|---|
| TechReturners CV | “10+ years delivering stability…” | SSOT one-liner/experience timeline supports decade framing. | Properly sourced | Grounded in SSOT positioning + timeline. 【F:applications/2026-02-19-TechReturners/cv_bullets.md†L5】【F:SSOT.md†L85-L86】【F:SSOT.md†L117-L123】 |
| TechReturners CV | “18-month upskilling sabbatical” | SSOT says Nov 2023–Present; no 18-month claim. | Sourced but weaker/derived | Derived duration may be stale or inaccurate; not an SSOT-stated number. 【F:applications/2026-02-19-TechReturners/cv_bullets.md†L5】【F:SSOT.md†L110-L115】 |
| TechReturners CV | “reducing daily search time by 60%” | SSOT evidence backlog says time-saved claims not for professional use. | Unsourced / invented-for-use | Explicitly disallowed until verified external proof. 【F:applications/2026-02-19-TechReturners/cv_bullets.md†L13】【F:SSOT.md†L163-L168】 |
| TechReturners Cover Letter | “perfectly aligns” | No SSOT basis for perfect-fit absolute. | Unsourced/inflated | Tone inflation; unverifiable absolute positioning. 【F:applications/2026-02-19-TechReturners/cover_letter.md†L10】 |
| TechReturners Cover Letter | “failure was not an option” | No SSOT evidence path. | Unsourced/inflated | Implied absolute performance claim. 【F:applications/2026-02-19-TechReturners/cover_letter.md†L12】 |
| Aareon Cover Letter | “every way a distributed system can fail” | No SSOT support for absolute breadth. | Unsourced/inflated | Over-claim by universality. 【F:applications/2026-02-19-AareonGroup/cover_letter.md†L7】 |
| Aareon Cover Letter | “absolute stability required” | No role-specific evidence proving absoluteness. | Unsourced/inflated | Strong absolute with no evidentiary anchor. 【F:applications/2026-02-19-AareonGroup/cover_letter.md†L9-L10】 |

### Claims-table audit holes
- Aareon claims table references `SSOT_Legacy.md`, while policy says SSOT is canonical; this introduces dual-truth risk. 【F:applications/2026-02-19-AareonGroup/claims_table.md†L5-L8】【F:SSOT.md†L4-L5】
- TechReturners claims table includes a banned `100% data integrity` entry as warning, but CV/CL still contain other inflated claims not listed (e.g., “perfectly aligns”, “failure was not an option”). Audit table is incomplete. 【F:applications/2026-02-19-TechReturners/claims_table.md†L10-L11】【F:applications/2026-02-19-TechReturners/cover_letter.md†L10-L13】

### Are gates enforceable or performative?
- `language_gate.md` files are checklist-style and inconsistent with SSOT banned list (Aareon scans “ninja/rockstar/synergy” but misses actual policy terms). Performative pattern detected. 【F:applications/2026-02-19-AareonGroup/language_gate.md†L4-L13】【F:SSOT.md†L37-L42】
- `evidence_check.md` entries are unchecked boxes or broad assertions, not pass/fail against explicit claims. No observed hard FAIL state blocks downstream use. 【F:applications/2026-02-19-AareonGroup/evidence_check.md†L3-L11】【F:applications/2026-02-19-TechReturners/evidence_check.md†L5-L15】

## Strategic Blind Spots

### 1) System optimizes for artifact polish, not bottleneck throughput (broken now)
- Weekly cadence targets shortlist/apply/follow-up, but model has no built-in throughput constraints or SLA enforcement beyond prose. Quality control overhead likely reduces application volume. 【F:SSOT.md†L171-L176】

### 2) Returner-specific bias handling is underdeveloped (broken now)
- Positioning for returner exists, but no explicit artifact module addresses gap-risk objections with proof assets (e.g., recency portfolio packets, skills recency matrix, “gap explanation variants by interviewer type”). Current outputs rely on rhetoric (“strategic re-platforming”) without verification strategy. 【F:SSOT.md†L64-L65】【F:applications/2026-02-19-TechReturners/cover_letter.md†L16-L17】

### 3) No outcome learning loop (broken now)
- Tracking captures opportunity discovery but not structured response/rejection analytics. System cannot adapt strategy based on failures, so it can repeatedly produce the same style regardless of outcomes. 【F:tracking/opportunities.yaml†L1-L104】【F:schemas/opportunity.yaml†L3-L32】

### 4) Networking workflow is weakly integrated (will break harder with scale)
- Outreach logging destination is ambiguous; no attribution model ties outreach touches to eventual interviews/offers. At low volume this is survivable; at higher volume it becomes unrecoverable attribution loss. 【F:.agent/workflows/networking_outreach.md†L31-L32】

## The 5 Changes With Highest Effort-to-Value Ratio

1. **Unify policy precedence and compile to one machine-readable policy map** (Low effort / Very high value)
   - Add `rules/policy_precedence.md` with explicit order: `SSOT credibility policy > safety guardrails > workflow specs > prompts > ad hoc user text`.
   - Add a generated `policy_terms.yaml` consumed by prompts and gates.

2. **Introduce claim inventory as pre-draft gate** (Medium effort / Very high value)
   - Before drafting, require a `claim_inventory.yaml` listing each intended claim + SSOT source + evidence label.
   - Block draft generation if any claim lacks label/source.

3. **Create immutable submission snapshot** (Low-medium effort / High value)
   - At submission time write `submission_snapshot.yaml` with exact submitted text, files, URL, timestamp, and screenshot path.
   - Hash snapshot and store hash in tracking row.

4. **Normalize funnel FSM across opportunity + application** (Medium effort / High value)
   - Replace ad hoc statuses (`Drafted`, `Ready`, `Drafting`) with unified FSM and transition rules.
   - Add transition validator doc + weekly state drift check.

5. **Add rejection/response telemetry with source attribution** (Medium effort / High value)
   - Extend `opportunity` records with: `date_submitted`, `date_response`, `response_type`, `rejection_reason_code`, `origin_channel` (`job_board|referral|direct|networking`).
   - Use this to produce weekly “what worked” deltas and retune targeting.
