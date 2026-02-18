# TechCareer System: Architectural Context

## 1. System Overview
**Name:** TechCareer "AntiGravity" Pack
**Objective:** Orchestrate a verifiable, consistent campaign to return "Danny Jackson" to a stable technical income via "returner" or "train-to-hire" roles.
**Core Philosophy:** "Evidence-Safe High-Agency." The system favors truth, verification, and high-quality artifacts over volume or exaggeration.

## 2. Core Entities & Personas

### 2.1 The Subject: Danny Jackson
*   **Profile:** 10+ years in Delivery/Implementation/Support.
*   **Current Pivot:** Moving to "AI-Accelerated Data/Automation Engineer" (n8n, Python, SQL).
*   **Key Differentiator:** "Reliability & Risk Reduction." Uses AI to accelerate coding but owns the *verification* and *delivery*.
*   **Source of Truth:** Defined strictly in `SSOT.md`.

### 2.2 The Agent System: AntiGravity
*   **Role:** Strategic partner and execution engine.
*   **Operating Tone:** "Consultancy-Ready." Professional, dry, evidence-based.
*   **Banned Behaviors:**
    *   Inventing metrics/claims (Hallucination).
    *   Using "LinkedIn Influencer" hype language (e.g., "Game-changer", "Unlocking potential").
    *   Apologizing for career gaps or pivots.

## 3. Component Architecture

### 3.1 Data Layer
*   **`SSOT.md` (Single Source of Truth):**
    *   The database of all approved claims, skills, and history.
    *   **Rule:** If a claim isn't here or marked "VERIFIED", it cannot be used in an application.
*   **`tracking/opportunities.yaml`:**
    *   Structured tracking of job leads.
    *   Schema includes: `fit_score`, `fit_reasons`, `risks`, `requirements`, `actions`, `evidence`.

### 3.2 Logic Layer (Prompts)
*   **Application Factory (`prompts/application_factory.md`):**
    *   **Input:** Opportunity Data + SSOT.
    *   **Process:**
        1.  **Map:** Match JD keywords to SSOT evidence.
        2.  **Filter:** Enforce "Consultant's Lens" (Low-Risk, High-Upside).
        3.  **Draft:** Generate CV Bullets, Cover Letter, Claims Table.
    *   **Output:** Markdown artifacts in `applications/{Date}-{Company}/`.
*   **Agent Profile (`prompts/antigravity_agent_profile.md`):**
    *   Global behavioural instructions for all agent interactions.
*   **Opportunity Intelligence Agent (`prompts/opportunity_intel.md`):**
    *   **Input:** Job Description, Company Name, signals.
    *   **Process:** Diagnoses team context, risk profile, and framing strategy.
    *   **Output:** Strategic intelligence brief (YAML).

### 3.3 Execution Layer (Workflows)
*   **Weekly Loop:**
    1.  **Radar:** Scan for leads -> Update `opportunities.yaml`.
    2.  **Factory:** Select top 3 -> Run Application Factory -> Generate artifacts.
    3.  **Review:** User verifies "Claims Table" -> Submit.
    4.  **Log:** Update status to "Applied".

## 4. Key Directives for Improvement
The user is specifically seeking to optimize the **Connection between SSOT and Application Factory**:
*   **Challenge:** ensuring the "AI-Accelerated" narrative lands as *senior/reliable* rather than *junior/dependent*.
*   **Goal:** The research agent should find ways to make the "Application Factory" output more punchy, specific, and valuable to a hiring manager, minimizing "generic" AI feel.
