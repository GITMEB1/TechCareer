# TechCareer System: Architectural Context
**Version:** 2.0 (Post-Governance Upgrade)

## 1. System Overview
**Name:** TechCareer "AntiGravity" Pack
**Objective:** Orchestrate a verifiable, consistent campaign to return "Danny Jackson" to a stable technical income via "returner" or "train-to-hire" roles.
**Core Philosophy:** "Evidence-Safe High-Agency." The system favors truth, verification, and high-quality artifacts over volume or exaggeration. We avoid "confident nonsense."

## 2. Core Entities & Personas

### 2.1 The Subject: Danny Jackson
*   **Profile:** 10+ years in Delivery/Implementation/Support.
*   **Current Pivot:** Moving to "AI-Accelerated Data/Automation Engineer" (n8n, Python, SQL).
*   **Key Differentiator:** "Reliability & Risk Reduction." Uses AI to accelerate coding but owns the *verification* and *delivery*.
*   **Source of Truth:** Defined strictly in `SSOT.md` (v1.1+).

### 2.2 The Agent System: AntiGravity
*   **Role:** Strategic partner and execution engine.
*   **Operating Tone:** "Consultancy-Ready." Professional, dry, evidence-based.
*   **Governance:** STRICT adherence to the credibility policy.

## 3. Credibility Policy (Non-negotiable)
Derived from `SSOT.md` v1.1.

### 3.1 Banned Behaviors & Terms
*   **Inventing metrics/claims (Hallucination):** No "2x faster" or "100% reliable" without proof.
*   **Hype Language:** No "Game-changer", "Unlocking potential", "Turbocharged".
*   **Undefined Tech:** No "Self-healing", "Strictly typed" (unless true), "Orchestrated agents".
*   **Defensive Language:** No apologizing for gaps or "I don't need hand-holding".

### 3.2 Evidence Labels
*   **VERIFIED:** Has external proof (URL, Repo, Screenshot).
*   **REALITY PROOF:** Basic identity facts (Dates, Contact info).
*   **SUPPORTED:** Plausible based on SSOT role descriptions, but no public link.
*   **UNVERIFIED:** Must NOT be used in application materials.

## 4. Component Architecture

### 4.1 Data Layer
*   **`SSOT.md` (Single Source of Truth):**
    *   The database of all approved claims, skills, and history.
    *   **Rule:** If a claim isn't here or marked "VERIFIED", it cannot be used.
*   **`tracking/opportunities.yaml`:**
    *   Structured tracking of job leads.
    *   Schema includes: `fit_score`, `fit_reasons`, `risks`, `requirements`, `actions`, `evidence`.
*   **`schemas/opportunity_intel.yaml`:**
    *   Output format for deep intel analysis.

### 4.2 Logic Layer (Prompts)
*   **Application Factory (`prompts/application_factory.md` v2.0):**
    *   **Input:** Opportunity Data + SSOT + Opportunity Intel.
    *   **Process:**
        1.  **Intel Check:** Ensure `opportunity_intel.yaml` exists.
        2.  **Map:** Match JD pain points to SSOT evidence (Capability -> Pain).
        3.  **Draft:** Generate artifacts (CV, Cover Letter).
        4.  **Gate:** Run "Language Risk Gate".
    *   **Output:** Markdown artifacts in `applications/{Date}-{Company}/`.
*   **Opportunity Intelligence Agent (`prompts/opportunity_intel.md`):**
    *   **Input:** Job Description, Company Signals.
    *   **Process:** Diagnoses team context, risk profile, and framing strategy.
    *   **Output:** Strategic intelligence brief (`opportunity_intel.yaml`).

### 4.3 Execution Layer (Workflows)
*   **Weekly Loop:**
    1.  **Radar:** Scan for leads -> Update `opportunities.yaml`.
    2.  **Intel:** Run Opportunity Intel Agent -> Generate `opportunity_intel.yaml`.
    3.  **Factory:** Run Application Factory -> Generate Drafts + `claims_table.md` + `language_gate.md`.
    4.  **Review:** User verifies Claims & Language Gate -> Submit.
    5.  **Log:** Update status to "Applied".

## 5. Key Directives for Improvement
The user is specifically seeking to optimize the **Connection between SSOT and Application Factory**:
*   **Challenge:** Ensuring the "AI-Accelerated" narrative lands as *senior/reliable* rather than *junior/dependent*.
*   **Goal:** The research agent should find ways to make the "Application Factory" prompt structure more robust, ensuring it always pulls specific evidence and never hallucinates, regardless of the model ("confidence nonsense" prevention).
