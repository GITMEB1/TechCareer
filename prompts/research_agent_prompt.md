# Prompt for Google 3.0 Pro Deep Research Agent

**Role:** Google 3.0 Pro Deep Research
**Objective:** Critically analyze the provided "TechCareer AntiGravity System" architectural context and optimize the high-value intersection between the **SSOT (Single Source of Truth)** and the **Application Factory**.

**Core Question:**
"How can we maximize the interview conversion rate for a 'returning-to-tech' candidate (10y exp -> Data/Auto) by refining the way the SSOT feeds into the Application Factory?"

**Reference Materials:**
(Please ingest the attached `architectural_context.md` which summarizes the system.)

**Target Analysis Areas:**

1.  **Narrative Logic ("AI-Accelerated Developer"):**
    *   **Critique:** Does the current positioning statement in the SSOT (focused on reliability/risk reduction) effectively counter the bias against career gaps and platform pivots?
    *   **Improvement:** Suggest concrete phrasing or structural changes to the SSOT that make the "AI-Accelerated" claim feel like a *feature* (seniority leverage) rather than a *bug* (skill gap filler).

2.  **Prompt Engineering (Application Factory):**
    *   **Critique:** The current prompt enforces "No Cringe / No Hallucinations." Does it *also* successfully enforce "High Value Signal"? Or does it risk producing dry, forgettable applications?
    *   **Improvement:** Propose specific instructions or "Examples of Excellence" to add to the `application_factory.md` prompt that force the agent to extract specific, numerical, or improved outcome data from the SSOT more aggressively.

3.  **Data Structure (SSOT & Opportunity Tracking):**
    *   **Critique:** Is the current `opportunities.yaml` schema capturing the *right* data to feed the Application Factory? Are we missing a "Company Pain Point" field that would allow better tailoring?
    *   **Improvement:** Suggest 1-2 critical fields to add to the Opportunity Schema or SSOT that would drastically improve the personalization of the generated Cover Letter.

**Deliverable:**
*   A prioritized list of 3-5 "High Impact Interventions" to the system architecture.
*   For each intervention:
    *   **The Problem:** Why the current setup is suboptimal.
    *   **The Fix:** Specific text to add/edit in `SSOT.md`, `application_factory.md`, or `opportunities.yaml`.
    *   **The Expected Value:** Why this change increases interview probability.
