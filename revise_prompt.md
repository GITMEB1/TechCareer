TOOLS (Use them)

File Search / Repo browsing: to read project files directly.

URL Context / Grounding with Google Search: ONLY to verify time-sensitive market claims or any model/tool capability assumptions you are making.

Code Execution: optional, only if you need to validate schemas or transform outputs.

NON-NEGOTIABLE GOVERNANCE (must obey)

Evidence labels:

VERIFIED = has external proof link/path

REALITY PROOF = identity/timeline facts

SUPPORTED = plausible from role descriptions but no public proof

UNVERIFIED = must NOT appear in final application copy

Banned claims/phrases: absolutes (100%/zero-defect/guaranteed), multipliers (2x/10x faster), undefined engineering labels (“self-healing”, “orchestrated agents”, “strictly typed”), hype (“game-changer”), desperation, defensive language.

Mandatory Claim Source Lock template:
“[Skill/Capability] demonstrated by [specific artifact/role] resulting in [measurable outcome]”
If measurable outcome is not VERIFIED, you must downgrade to an artifact reference + observable scope (no invented numbers).

Application Factory dependency rule:
If opportunity_intel.yaml is missing, STOP (for that application) and request it.

“Intel Binding” must appear before any drafting for a specific role.

PROJECT CONTEXT (what this repo is)
Danny has 10+ years Support/Implementation (Cloud Commerce Group/ChannelGrabber) and a modern pivot (n8n, Python, SQL, schemas, prompt/context engineering). The system currently over-optimizes for evidence density and “junior data engineer” targets, which is slowing income. We need a strategy switch toward roles that convert to interviews faster (Support/Implementation/TAM/Platform Support) while preserving a bridge to Data Engineering.

YOUR PRIMARY GOAL
Re-orient the entire system to a “Fast Income Mode” WITHOUT deleting the Evidence-Safe philosophy. Outcome = more interviews + faster hire.

INPUTS YOU MUST LOAD (from the repo via File Search)

SSOT.md (canonical constraints + approved phrasing + skills matrix + target archetypes)

prompts/application_factory.md

prompts/opportunity_intel.md

tracking/OPPORTUNITY_RADAR.md (or opportunity_radar.md equivalent)

antigravity_agent_profile.md (working style + non-negotiables)

Most recent application artifacts in applications/ relevant to NHS/UBDS:

cv_bullets.md

cover_letter.md

claims_table.md

language_gate.md
If any of these are missing, list exactly what is missing and proceed with the rest.

ALSO INGEST THIS USER DIRECTIVE (paste already present in chat context)
“Strategic Exposure: Reorientation Audit (2026-02-19)” including:

Modify SSOT rule 1.1 to allow “Role-Grounded” legacy claims (SUPPORTED) without public links

Add “Mode Toggle” (SPEED | PIVOT)

Expand radar role archetypes (Support Engineer, Implementation, TAM, Platform Ops)

Introduce SSOT_Legacy.md

Relax evidence density rules for Support/Ops applications

50/50 sourcing split: cash roles vs dream roles

WORK TO PERFORM (do in this order)

PHASE 1 — Repo Reality Scan (no writing yet)

Summarize (in bullets) the actual hard constraints and mechanisms as implemented:

Evidence labels, banned terms, claim-source-lock

Application Factory steps (including Intel Binding + gates)

Opportunity Radar targeting logic

Identify drift/contradictions between:

SSOT target archetypes vs Radar search targets

Application Factory “required words” list vs SSOT banned/approved replacements

“Evidence Density 100%” rule vs practical Support/Ops storytelling

Inspect NHS/UBDS outputs and flag:

Every banned phrase occurrence

Every “false confidence” line

Every claim that lacks an evidence label trace

Any “technobabble” (replace with accurate wording)

PHASE 2 — Market Reality (UK 2026) with grounding
Using Grounding with Google Search ONLY where needed:

Validate whether “returner / train-to-hire” programs are actually hiring right now and what titles convert fastest.

Identify 3–5 UK role archetypes with highest interview velocity for Danny’s background (Support Engineer Tier 2/3, SaaS Implementation, TAM, Platform Support, Ops/Runbook-heavy roles).
DO NOT invent stats. If you can’t verify, label as “Unknown”.

PHASE 3 — Mechanism Redesign (the important part)
Design a minimal set of changes that achieves:
A) FAST INCOME MODE (volume + speed, still credible)
B) PIVOT MODE (slower, stricter evidence density, data-engineering bridge)

You MUST produce:

A “Mode Toggle Spec”:

Input variable: strategy_mode: SPEED | PIVOT

Exactly what changes in:

Radar sourcing targets

Evidence density requirements

Cover letter structure (Lite vs Pain-Solving Proposal)

Claim-source-lock strictness

A new file proposal: SSOT_Legacy.md

What goes in it

How it is allowed to generate SUPPORTED claims without public links

What must remain UNVERIFIED until evidence is gathered

A revised Opportunity Radar schema change:

Add role_category enum: DATA_ENGINEER | SUPPORT_ENGINEER | IMPLEMENTATION | TAM | OPS

Add salary_floor, time_to_interview_estimate (qualitative only), and “cash_now_score”

A “Lite Application Factory” variant for SPEED mode:

30–45 minute max per application

Still outputs claims_table + language_gate

Still respects banned language and evidence labels

Uses simplified cover memo structure:
Hook (role fit) → Proof (2 bullets from legacy + 1 from modern) → Close (availability)

A list of EXACT questions the system should ask Danny weekly to grow evidence safely:

ticketing systems used, monitoring tools, Linux usage, SLA exposure, typical ticket volume (if unknown keep as unknown), etc.

Each question must map to (a) which SSOT section it enriches and (b) which role archetype it unlocks.

PHASE 4 — Output as STRUCTURED JSON (mandatory)
Return ONLY valid JSON, matching this schema. Do not wrap in markdown. No extra keys.

{
"repo_scan": {
"files_loaded": [{"path": "", "status": "loaded|missing", "notes": ""}],
"core_constraints": [{"name": "", "rule": "", "risk_if_violated": ""}],
"drift_findings": [{"where": "", "problem": "", "impact": "", "fix": ""}]
},
"artifact_audit": {
"targets_reviewed": [{"application": "", "files": ["cv_bullets.md","cover_letter.md"], "status": "found|missing"}],
"cringe_flags": [{"file": "", "line_quote": "", "issue_type": "hype|false_confidence|desperation|technobabble|unsupported_claim", "rewrite": ""}],
"evidence_breaks": [{"file": "", "claim": "", "current_label": "VERIFIED|REALITY_PROOF|SUPPORTED|UNVERIFIED|MISSING", "required_action": "downgrade|remove|add_evidence|rewrite"}]
},
"market_reality_uk_2026": {
"grounded_notes": [{"claim": "", "status": "grounded|unknown", "source_summary": ""}],
"high_velocity_role_archetypes": [{"role_archetype": "", "why_fast": "", "best_pitch_angle": "", "risks": ""}]
},
"mechanism_redesign": {
"mode_toggle_spec": {
"SPEED": {"radar_targets": [], "artifact_rules": [], "cover_structure": [], "time_budget_minutes": 45},
"PIVOT": {"radar_targets": [], "artifact_rules": [], "cover_structure": [], "time_budget_minutes": 120}
},
"new_files": [{"path": "SSOT_Legacy.md", "purpose": "", "rules": [], "example_entries": []}],
"schema_changes": [{"file": "", "change": "", "rationale": ""}],
"lite_application_factory": {"steps": [], "required_outputs": ["cv_bullets.md","cover_letter.md","claims_table.md","language_gate.md"]},
"weekly_questions": [{"question": "", "unlocks": ["SUPPORT_ENGINEER|IMPLEMENTATION|TAM|OPS|DATA_ENGINEER"], "writes_to": "SSOT section/path"}]
},
"today_actions": [
{"action": "", "time_minutes": 0, "expected_outcome": "", "mode": "SPEED|PIVOT"}
]
}

QUALITY BAR

Brutally honest, but precise.

No motivational language.

No invented metrics.

If you’re uncertain, mark “unknown” and propose how to verify.