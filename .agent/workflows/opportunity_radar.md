---
description: Run the weekly Opportunity Radar scan to find and rank job leads.
---

# Workflow: Opportunity Radar

This workflow automates the process of finding and prioritizing job opportunities for Danny Jackson.

## 1. Initialization
- Read `SSOT.md` to refresh on "North Star" and "Target Archetypes".
- Read `rules/agent_operating_rules.md` for constraints.

## 2. Scan Phase
- **Action**: Search for roles in Greater Manchester (or Remote UK) matching:
    - Returner programs
    - Train-to-hire / Bridge roles
    - Associate Data Engineer / Automation Engineer
    - Implementation Engineer (Technical)
- **Constraint**: Ignore Senior SWE roles (5+ years exp) or unpaid internships.

## 3. Analysis Phase
- For each potential lead, evaluate against the **Skills Matrix** in `SSOT.md`.
- Assign a **Fit Score (0-10)**.
- Identify specific **Risks/Gaps**.

## 4. Output Phase
- Append findings to `tracking/opportunities.yaml` using the schema from `schemas/opportunity.yaml`.
- Create a summary artifact "Radar Board" listing the top 3 leads with rationale.

## 5. Next Actions
- Propose an application strategy for the top 3 leads.
