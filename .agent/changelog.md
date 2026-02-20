# Project Changelog

*This file tracks significant structural shifts, policy updates, and file additions/removals to provide historical context to agents. Agents **must** review this file before making destructive changes.*

## [2026-02-19] - SSOT Consolidation & Legacy Deletion
- **Action**: Removed `SSOT_LEGACY.md`.
- **Context**: A previous agent interaction successfully identified `SSOT_LEGACY.md` as redundant/outdated and deleted it. The user reported that this file was previously used as a secondary path in some older `application_factory` operations.
- **Verification**: A deep search of the `prompts/`, `.agent/workflows/`, and `rules/` directories confirmed no remaining dependencies on `SSOT_LEGACY.md`. All active workflows now correctly depend solely on the generalized, primary `SSOT.md` (Version 1.1) and `opportunity_intel.yaml`.
- **Lesson**: Agents must always consult this changelog and `memory.md` before removing files. `SSOT.md` is the single source of truth for the candidate's core identity, while target-specific framing lives in `tracking/opportunities.yaml` and `opportunity_intel.yaml`.

## [2026-02-19/20] - Phase 1-4 Architectural Upgrades (ChatGPT 5.2 Review)
- **Action**: Implemented a massive architectural overhaul across schemas, prompts, and tracking.
- **Context**: Executed 4 phases of upgrades to address state drift, hallucination risks, and HITL friction.
- **Changes**:
  - **Phase 1**: Made `tracking/opportunities.yaml` the single source of truth. Created `scripts/render_radar.py` to dynamically generate `OPPORTUNITY_RADAR.md`. Added strict schema validation to `opportunity_intel.md`. Created `rules/policy_lint.yaml` for deterministic failure states.
  - **Phase 2**: Refactored `application_factory.md` to use a 3-stage Evidence Assembly Pipeline (Select, Assemble, Compose) and integrated a mandatory `BRIDGE_NARRATIVE_BLOCK`.
  - **Phase 3**: Introduced `schema/approval_manifest.yaml` to allow for exception-only "Auto-Approvals", and forced `application_factory.md` to output a `review_delta.md` during packet revisions.
  - **Phase 4**: Hard-coded quantitative objective scoring (`bridge_alignment`, `data_trajectory`, `stability`, `salary_floor`) into `schemas/opportunity.yaml` to prevent strategic drift into legacy roles.
- **Lesson**: Agents must strictly follow the `opportunity.yaml` schema enum values. Applications should never generate unverified metrics; they must only extract verified `claim` strings from `claim_inventory.yaml` and assemble them.
