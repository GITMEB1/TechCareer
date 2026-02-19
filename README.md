# AntiGravity Context Pack — Danny Jackson (v1.1)

**Purpose:** Give Google AntiGravity a stable, auditable “mission pack” to help Danny convert overlooked opportunities into consistent income and career stability.

## What this pack is
A set of **rules, schemas, and mission briefs** designed for an **agent-first workflow**:
- The agent produces **Artifacts** (plans, checklists, drafts, evidence tables) you can review.
- Work is broken into small, verifiable missions so you stay in control.
- **SSOT.md** acts as the canonical source of truth for all claims and facts.

## How to use in AntiGravity

### 1. Check Project Status
Open `task.md` in the root to see current status and next steps.

### 2. Run Workflows
Use the agent to execute workflows found in `.agent/workflows/`. You can ask the agent to "Run the [Workflow Name]".

**Available Workflows:**
- **Opportunity Radar** (`opportunity_radar.md`): Scan and rank new job opportunities.
- **Application Factory** (`application_factory.md`): Generate tailored CVs, cover letters, and evidence tables for a specific role.
- **Application Submission** (`application_submission.md`): Final polish and submission steps.
- **Networking Outreach** (`networking_outreach.md`): Draft outreach messages to recruiters or contacts.

### 3. Review Artifacts
- **Applications**: Generated materials are saved in `applications/[Date-CompanyName]/`.
- **Tracking**: Opportunity logs are maintained in `tracking/`.

## Project Structure

- **`.agent/workflows/`**: Interactive workflows for the agent to follow.
- **`applications/`**: Output directory for generated application packs.
- **`prompts/`**: System prompts used to steer agent behavior (e.g., `opportunity_intel.md`).
- **`rules/`**: Operational constraints and safety guardrails (`agent_operating_rules.md`, `safety_guardrails.md`).
- **`schemas/`**: YAML/JSON schemas ensuring structured data output (`opportunity.yaml`).
- **`tracking/`**: Logs and trackers for opportunities and networking.
- **`SSOT.md`**: **CRITICAL**. The single source of truth for Danny's experience, skills, and approved phrasings.

## Ground Rules
- **No invented metrics.** If a number isn’t evidenced in `SSOT.md` or provided context, the agent must mark it as “UNVERIFIED”.
- **No irreversible commands.** The agent must never run destructive terminal commands without explicit confirmation.
- **Agent Operating Rules**: Strictly followed guidelines in `rules/agent_operating_rules.md`.

## Key Files
- `SSOT.md` — Canonical facts and claims.
- `rules/agent_operating_rules.md` — Master behavioral contract.
- `schemas/opportunity.yaml` — Opportunity data structure.
