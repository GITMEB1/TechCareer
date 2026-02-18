# Prompt for Google 3.0 Pro Deep Research Agent

**Role:** Google 3.0 Pro Deep Research
**Objective:** Critically analyze the **TechCareer AntiGravity System** infrastructure and optimize the *logic* that governs artifact generation, ensuring strict adherence to the "Evidence-Safe" philosophy.

**Core Question:**
"How can we harden the system's infrastructure (Prompts, Schemas, workflows) to strictly prevent 'confident nonsense' and ensure every generated application is high-signal, evidence-backed, and devoid of marketing fluff?"

**Reference Materials:**
(Please ingest the attached `architectural_context.md` which summarizes the system.)

**Target Analysis Areas:**

1.  **Governance Logic (The "Banned Words" Sync):**
    *   **Critique:** Are the "Banned Behaviors/Terms" defined in `SSOT.md` actually *enforced* by the `application_factory.md` prompt? Is there a risk of "prompt drift" where the model ignores negative constraints?
    *   **Improvement:** Propose a verifiable mechanism (e.g., a specific "Gate" step or a structured output schema for the gate) that *forces* the model to acknowledge and check these rules before writing final copy.

2.  **Intel Fidelity (The "So What?" Factor):**
    *   **Critique:** Does the `opportunity_intel.yaml` actually influence the final Cover Letter tone? Or does the Application Factory just default to a generic "I am a fit" structure?
    *   **Improvement:** Suggest specific prompt instructions or variable injections that *force* the Application Factory to quote the `intel.framing_strategy` in its reasoning block before drafting key sentences.

3.  **Schema Evolution (Capturing "Pain"):**
    *   **Critique:** Does the current `opportunities.yaml` or `opportunity_intel.yaml` schema capture enough specific "Pain Points" from the JD to allow for truly tailored evidence selection?
    *   **Improvement:** Suggest 1-2 critical fields (e.g., `primary_risk_factor`, `decision_maker_persona`) to add to `opportunity_intel.yaml` that would drastically improve the targeting of the output.

**Deliverable:**
*   A prioritized list of 3-5 "Infrastructure Hardening Actions".
*   For each action:
    *   **The Vulnerability:** Where the current logic might allow "fluff" or "hallucination".
    *   **The Fix:** Specific prompt syntax, schema field, or workflow step to add.
    *   **The Verification:** How we will know it's working (e.g., "The Language Gate log will show 0 false negatives").
