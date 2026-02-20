# Project Changelog

*This file tracks significant structural shifts, policy updates, and file additions/removals to provide historical context to agents. Agents **must** review this file before making destructive changes.*

## [2026-02-19] - SSOT Consolidation & Legacy Deletion
- **Action**: Removed `SSOT_LEGACY.md`.
- **Context**: A previous agent interaction successfully identified `SSOT_LEGACY.md` as redundant/outdated and deleted it. The user reported that this file was previously used as a secondary path in some older `application_factory` operations.
- **Verification**: A deep search of the `prompts/`, `.agent/workflows/`, and `rules/` directories confirmed no remaining dependencies on `SSOT_LEGACY.md`. All active workflows now correctly depend solely on the generalized, primary `SSOT.md` (Version 1.1) and `opportunity_intel.yaml`.
- **Lesson**: Agents must always consult this changelog and `memory.md` before removing files. `SSOT.md` is the single source of truth for the candidate's core identity, while target-specific framing lives in `tracking/opportunities.yaml` and `opportunity_intel.yaml`.
