---
description: Generate tailored application artifacts (CV, Cover Letter) for a specific opportunity.
---

# Workflow: Application Factory

This workflow generates the core application assets for a specific job target.

## Inputs Required
- **Target Opportunity**: A specific role from `tracking/opportunities.yaml` or a URL.
- **SSOT**: `SSOT.md` (read-only source of facts).

## 1. Setup
- Create a new directory in `applications/`: `YYYY-MM-DD-CompanyName`.
- Create an `evidence_check.md` file in that folder to log verification.

## 2. Analysis
- Analyze the Job Description (JD) against `SSOT.md`.
- Identify key requirements and map them to **Verified Skills**.
- **Crucial**: If a skill is missing or weak, note it. Do NOT hallucinate proficiency.

## 3. Draft Artifacts
- **CV Bullets (`cv_bullets.md`)**: Tailor strictly based on `SSOT.md` evidence. Use "AI-Accelerated" framing where appropriate.
- **Cover Letter (`cover_letter.md`)**: Draft a narrative connecting Danny's "North Star" to the role.
- **Claims Table (`claims_table.md`)**: A table mapping every claim in the CV/CL to a specific proof point in `SSOT.md`.

## 4. Review Request
- User must review the `claims_table.md`.
- **Rule**: If a claim is marked "Unverified", the user must approve or remove it.

## 5. Final Compilation
- Once approved, compile the final CV/CL (if applicable, or output text for form submission).
