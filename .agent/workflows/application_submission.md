---
description: Automate the "Last Mile" of the application process (Submission).
---

# Workflow: Application Submission

This workflow handles the submission of prepared application artifacts to job portals.

## Inputs
- `tracking/opportunities.yaml` (Target URLs and status)
- `applications/YYYY-MM-DD-Company/` (The artifacts to submit)
- `SSOT.md` (Candidate details for form filling)

## 1. Preparation
- Identify the target opportunity in `tracking/opportunities.yaml` with status `Drafting` or `Ready`.
- Verify that the `applications/` folder contains a validated `cv_bullets.md` (or PDF) and `cover_letter.md`.

## 2. Browser Automation (Antigravity)
- **Action**: Launch browser and navigate to the application URL.
- **Constraint**: If a file upload dialog appears, the agent may need to pause or use specific browser tools to handle it. If not possible, alert the user to upload manually.
- **Form Filling**: Use `SSOT.md` and `prompts/antigravity_agent_profile.md` context to fill standard fields (Name, Email, LinkedIn, etc.).

## 3. Submission / Handoff
- **Low Risk**: If the form is simple and data is verified, proceed to "Review" page.
- **High Risk**: Do NOT press the final "Submit" button without explicit user instruction unless the user has authorized "Auto-Submit" for this session.
- **Alternative**: If automation fails, provide a "Copy-Paste" packet for the user to do it manually in seconds.

## 4. Logging
- Take a screenshot of the confirmation page or submitted state.
- Update `tracking/opportunities.yaml`:
    - Set status to `Applied`.
    - Log date of submission.
