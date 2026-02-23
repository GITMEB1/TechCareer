---
description: Generate tailored application artifacts (CV, Cover Letter) for a specific opportunity — evidence-safe and credibility-optimised.
version: 3.0
---

# Workflow: Application Factory (v3.0)

## Inputs Required (Non-negotiable)
- **Target Opportunity**: YAML entry from `tracking/opportunities.yaml` OR JD text + URL.
- **SSOT**: `SSOT.md` (read-only facts, policies, approved phrasing).
- **Opportunity Intel**:
  - **Pivot Track:** `opportunity_intel.yaml` (diagnostic rigour).
  - **Velocity Track:** `speed_mode_intel.md` (3-point mental sandbox).

**If Intel is missing: STOP.**
Output: "Missing opportunity intel — run Intel phase first."

---

## 0) Track Router (MANDATORY)
Determine `deployment_track` from the selected opportunity.

### 0.1 If `deployment_track == Velocity` (Deterministic Template Compilation)
You are **strictly forbidden** from generating prose.

You must output **exactly one JSON object** with only these keys:
```json
{
  "COMPANY_NAME": "...",
  "TARGET_PAIN_POINT": "...",
  "STACK_REQUIREMENT": "..."
}
```

Rules:
1. Values must be extracted from opportunity/JD/intel context; no extra narrative.
2. Do not output markdown, bullets, or commentary.
3. Do not draft cover-letter sentences.
4. After the JSON object, output one instruction line:
   `Run: python3 scripts/compile_track_a.py --input-json '<JSON>' --template templates/track_a_velocity_cover_letter.md --output applications/YYYY-MM-DD-CompanyName/cover_letter_final.md`

**STOP.** Do not execute Pivot Track stages.

### 0.2 If `deployment_track == Pivot`
Proceed through the full Stage 1–6 pipeline below.

---

## 1) Setup
- Create `applications/YYYY-MM-DD-CompanyName/`
- Create:
  - `evidence_check.md` (log claims + evidence links/paths)
  - `language_gate.md` (log banned-phrase scans + fixes applied)

---

## 2) Analysis & Pain Point Extraction
- Read JD and extract:
  - top 5 requirements (must-haves)
  - top 3 pain signals (what is expensive/slow/risky)
  - tone/culture signals (documentation, ownership, speed vs stability)
- Read `opportunity_intel.yaml` (if present) to align risks.

**MANDATORY OUTPUT:** Before proceeding, output this JSON block:
```json
{
  "pain_analysis": {
    "pain_points": [
      {
        "category": "COST|RISK|VELOCITY",
        "description": "e.g. 'Slow deployment cycles causing feature delay'",
        "ssot_match": "e.g. 'AntiGravity Context Pack (Velocity Track)'"
      }
    ],
    "nightmare_scenario": "The implicit fear driving this hire (e.g. 'Data loss during migration')"
  }
}
```

---

## 2.5) Intel Binding (MANDATORY - Before Drafting)
**If Pivot Track:** Output this block verbatim:

```text
INTEL_BINDING:
Framing Strategy: "[Insert verbatim from intel.framing_strategy]"
Primary Risk: "[Insert verbatim from intel.risk_profile.primary_risk_factor]"
Persona: "[Insert verbatim from intel.decision_maker_persona.role]"

Application Plan:
- Opening Hook: [How strategy shapes the first 2 lines]
- Evidence Selection: [Which project/role mitigates the Primary Risk]
- Tone Calibration: [Adjusting for Persona's bias/risk tolerance]
```

**If Velocity Track:** Output this simplified block:
```text
VELOCITY_BINDING:
Primary Pain Point: "[From mental sandbox]"
Target SSOT Capability: "[Which skill solves it]"
```

**STOP.** Do not proceed to drafting until this binding is complete.

---

## 2.7) Pre-Draft Claim Inventory (MANDATORY)
Before writing ANY artifact, produce a `claim_inventory.yaml` listing every claim you intend to make:

```yaml
claims:
  - id: "C-01"
    claim: "[Exact phrasing you plan to use]"
    ssot_section: "[Section number + field name]"
    evidence_label: "VERIFIED|SUPPORTED|OPERATIONAL_PROOF|UNVERIFIED"
    evidence_ref: "[URL, file path, or SSOT quote]"
```

**Rules:**
- Any claim with `evidence_label: UNVERIFIED` → DELETE before drafting.
- Any claim using a metric from SSOT §8 (Evidence Backlog) → DELETE unless you can provide VERIFIED external proof.
- `jd` is NOT a valid evidence source for candidate capability claims.
- User must approve this inventory before you proceed.

**STOP 1:** Do not proceed to Assembly until the claim inventory is approved.

---

## 3) Stage 2: Assemble Arguments (MANDATORY)

Instead of drafting prose immediately, you must assemble the core arguments utilizing the `id` from your approved claim inventory.

### 3.1 CV Bullets Assembly
Create a skeletal list of 3–6 bullets mapping exactly to the claim IDs `[C-XX]` that you intend to use.

### 3.2 Value Proposition Memo Assembly (The Bridge Narrative Block)
You must construct the following `BRIDGE_NARRATIVE_BLOCK` template with constrained variable slots.
**Constraint:** All three points MUST explicitly cite specific claim IDs `[C-XX]`.

1) **Legacy Credibility:** `[SSOT role/action]`
2) **Modernization Proof:** `[SSOT project/tooling]`
3) **Role-Relevant Transfer:** `[Specific JD pain solved]`
4) **The Close:** "I would welcome a brief discussion on how this 'Risk-First' approach could stabilize your `[Project/Goal]`."

**STOP 2:** Output ONLY the `ARGUMENT_BLOCKS` (CV Bullets + Bridge Narrative Block) alongside their Claim IDs. Wait for user approval. Do NOT compose the final cover letter yet.

---

## 4) Stage 3: Compose Artifacts (Evidence-Safe & High-Density)

Only after `ARGUMENT_BLOCKS` are approved, compose the final `cv_bullets.md` and `cover_letter.md`.

### Global Drafting Constraints
1. **Deterministic Mapping:** Every single capability/experience sentence in your final output MUST tie back to a previously selected claim ID in the inventory. No net-new claims are allowed during this stage.
2. **Claim Source Lock:** Capability statements must predictably use:
    > `[Skill/Capability]` + demonstrated by + `[specific artifact/role]` + resulting in + `[observable outcome]`
3. **Anti-Cringe Constraints (Vocabulary Check):**
    - **BANNED:** Strictly enforce the FULL 'Banned claims' and 'Tone Hazards' lists found in SSOT Section 1.2 (including Soft Absolutes, Unsourced Reputation Claims, and Consultancy-Speak). No exceptions.
    - **PREFERRED:** "Engineered", "Optimized", "Validated", "Reduced", "Stabilized", "Diagnosed", "Documented", "Mitigated".

### 4.1 Compile `claims_table.md`
Map every claim utilized into markdown table format. Include columns: Claim Made, Status (VERIFIED/SUPPORTED/OPERATIONAL_PROOF), Evidence (URL / file path / SSOT section), Notes.

**STOP 3:** Compose final artifacts strictly from assembled blocks.

---

## 4) Evidence & Language Gate (MANDATORY JSON & MANIFEST Check)

**Before user review**, you must validate your draft against `rules/policy_lint.yaml` and output this JSON block.

If `gate_status` is `FAIL`, you MUST regenerate the artifacts before proceeding.

```json
{
  "banned_language_check": {
    "violations_found": true/false,
    "violating_phrases": []
  },
  "evidence_traceability_check": {
    "claims_in_output": [
      {
        "claim": "...",
        "source_type": "ssot|portfolio|intel",
        "source_reference": "exact SSOT section or artifact path",
        "evidence_label": "VERIFIED|SUPPORTED|OPERATIONAL_PROOF",
        "verifiable": true/false
      }
    ]
  },
  "evidence_density_check": {
    "paragraphs_checked": 0,
    "paragraphs_meeting_density_rule": 0,
    "status": "PASS/FAIL"
  },
  "gate_status": "PASS|FAIL"
}
```

**Failure Conditions:**
- Any banned phrase found (SSOT 1.2 or `rules/policy_lint.yaml`).
- Any claim with `verifiable: false`.
- Evidence Density < 100% (every paragraph must have grounding).

### 4.2 Generate Approval Manifest & Delta Review
If `gate_status` is `PASS`, output `approval_manifest.yaml` to determine if manual review is required:

```yaml
approval_manifest:
  mode: auto|manual
  reasons:
    - "NEW_CLAIM_ID"
    - "UNVERIFIED_EVIDENCE"
    - "POLICY_LINT_HIT"
  reviewer: "Danny"
  approved_at: null
```

*Note: If `reasons` is empty, set `mode: auto`.*

If regenerating a previously reviewed packet, you MUST also output a `review_delta.md`:
```markdown
## Delta Summary
- Added claims: [C-ID-123]
- Removed claims: [C-ID-045]
- Tone shift: "neutral" -> "risk-first"
- New review blockers: none
```

---

## 5) Review Request (User Gate)
User reviews based on the `approval_manifest.yaml`:
- If `mode: auto`, you may proceed to Final Compilation.
- If `mode: manual`, the user must explicitly approve the flagged `reasons`, the `claims_table.md`, and any tone/language shifts.

---

## 6) Final Compilation
- Produce final polished `cv_final.md` and `cover_letter_final.md` (optional)
- Update `evidence_check.md` with any new proof links/paths gathered during review
