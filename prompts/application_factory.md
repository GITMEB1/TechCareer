---
description: Generate tailored application artifacts (CV, Cover Letter) for a specific opportunity — evidence-safe and credibility-optimised.
version: 2.0
---

# Workflow: Application Factory (v2.0)

## Inputs Required (Non-negotiable)
- **Target Opportunity**: YAML entry from `tracking/opportunities.yaml` OR JD text + URL.
- **SSOT**: `SSOT.md` (read-only facts, policies, approved phrasing).
- **Opportunity Intel**: 
  - **PIVOT MODE:** `opportunity_intel.yaml` (diagnostic rigour).
  - **SPEED MODE:** `speed_mode_intel.md` (3-point mental sandbox).

**If Intel is missing: STOP.**  
Output: "Missing opportunity intel — run Intel phase first."

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
        "ssot_match": "e.g. 'AntiGravity Context Pack (Velocity)'"
      }
    ],
    "nightmare_scenario": "The implicit fear driving this hire (e.g. 'Data loss during migration')"
  }
}
```

---

## 2.5) Intel Binding (MANDATORY - Before Drafting)
**If PIVOT MODE:** Output this block verbatim:

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

**If SPEED MODE:** Output this simplified block:
```text
SPEED_BINDING:
Primary Pain Point: "[From mental sandbox]"
Target SSOT Capability: "[Which skill solves it]"
```

**STOP.** Do not proceed to drafting until this binding is complete.

---

## 2.7) Pre-Draft Claim Inventory (MANDATORY)
Before writing ANY artifact, produce a `claim_inventory.yaml` listing every claim you intend to make:

```yaml
claims:
  - claim: "[Exact phrasing you plan to use]"
    ssot_section: "[Section number + field name]"
    evidence_label: "VERIFIED|SUPPORTED|UNVERIFIED"
    evidence_ref: "[URL, file path, or SSOT quote]"
```

**Rules:**
- Any claim with `evidence_label: UNVERIFIED` → DELETE before drafting.
- Any claim using a metric from SSOT §8 (Evidence Backlog) → DELETE unless you can provide VERIFIED external proof.
- `jd` is NOT a valid evidence source for candidate capability claims (JD describes what they want, not what Danny can do).
- User must approve this inventory before you proceed to Step 3.

**STOP.** Do not proceed to drafting until the claim inventory is approved.

---

## 3) Draft Artifacts (Evidence-Safe & High-Density)

### Global Drafting Constraints
1.  **Evidence Density:** Each paragraph must contain at least 1 **specific artifact reference** OR **SSOT-grounded action** OR **JD requirement mirrored with honest capability match**. Measurable outcomes are welcome ONLY if they have VERIFIED or SUPPORTED evidence — do NOT invent metrics to satisfy this rule. SSOT §8 (Evidence Backlog) items are BANNED from use.
2.  **Claim Source Lock:** All capability statements must use this structure:
    > `[Skill/Capability]` + demonstrated by + `[specific artifact/role]` + resulting in + `[observable outcome]`
    *Unverifiable "I have experience in..." claims are BANNED. Percentage/rate/multiplier claims require VERIFIED external proof per SSOT §8.*
3.  **Anti-Cringe Constraints (Vocabulary Check):**
    -   **BANNED:** Strictly enforce the FULL 'Banned claims' and 'Tone Hazards' lists found in SSOT Section 1.2 (including Soft Absolutes and Unsourced Reputation Claims). No exceptions.
    -   **PREFERRED:** "Engineered", "Optimized", "Validated", "Reduced", "Stabilized", "Diagnosed", "Documented".
    -   **NOTE:** "Orchestrated" is removed from the required list — it conflicts with SSOT §1.2 ban on "orchestrated agents" and risks producing banned constructions under pressure.

### 3.1 CV Bullets (`cv_bullets.md`)
- Select 3–6 bullets grounded in SSOT.
- Rewrite using the JD language *only where accurate*.
- Apply **Claim Source Lock** to every bullet.

**Forbidden:**
- Absolutes (100%, zero-defect, guaranteed, never breaks)
- Multipliers (2x/3x/10x faster)
- Undefined engineering terms (self-healing, strictly typed, orchestrated agents)

### 3.2 Value Proposition Memo (formerly Cover Letter, `cover_letter.md`)
**Strategy:** distinct from a generic cover letter. It is a "Pain-Solving Proposal".

**Structure (Strict Adherence):**
1.  **The Hook (Pain Hypothesis):** "I see you are hiring for `[Role]`. Based on the requirements for `[Requirement A]` and `[Requirement B]`, I suspect you are solving for `[Pain Point from Analysis]`."
2.  **The Bridge (Legacy Stability):** "In my 10 years of `[Legacy Role]`, I stabilized similar systems by `[Action Vector from SSOT]`. I bring the discipline of a senior support engineer who has seen every way a system can fail."
3.  **The Pivot (Modern Application):** "I have applied this operational rigour to the Modern Data Stack by `[Gap Role Activity - e.g. building schema-validated n8n pipelines]`. This allows me to bridge the gap between rapid automation and production stability."
4.  **The Close:** "I would welcome a brief discussion on how this 'Risk-First' approach could stabilize your `[Project/Goal]`."

**Constraint:** Do NOT act like a generic junior. Speak peer-to-peer about solving the problem.

### 3.3 Claims Table (`claims_table.md`) — Non-circular
Every claim must include *evidence type*:

Statuses:
- **VERIFIED (External Proof)**: include URL or file path (repo, screenshot, ticket export)
- **SUPPORTED (SSOT)**: grounded in SSOT role/project description but no external proof yet
- **UNVERIFIED (Remove)**: delete from CV/CL

Columns:
- Claim Made
- Status
- Evidence (URL / file path / SSOT section)
- Notes / rewrite if needed

---

## 4) Evidence & Language Gate (MANDATORY JSON Check)

**Before user review**, you must validate your draft. Output this JSON block. 

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
        "evidence_label": "VERIFIED|SUPPORTED",
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
- Any banned phrase found (SSOT 1.2).
- Any claim with `verifiable: false`.
- Evidence Density < 100% (every paragraph must have grounding).

---

## 5) Review Request (User Gate)
User reviews:
- `claims_table.md` (anything UNVERIFIED must be removed)
- tone: consultancy-ready, collaborative, non-defensive
- `language_gate.md` confirms no banned terms remain

---

## 6) Final Compilation
- Produce final polished `cv_final.md` and `cover_letter_final.md` (optional)
- Update `evidence_check.md` with any new proof links/paths gathered during review
