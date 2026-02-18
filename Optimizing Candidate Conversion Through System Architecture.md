# **TechCareer AntiGravity System: Architectural Optimization for High-Velocity Career Pivots**

## **1\. Introduction: The Physics of Career Inertia in the Algorithmic Age**

The contemporary technical labor market, particularly as it has evolved through the inflection point of 2025, presents a distinct set of physical properties that govern the trajectory of professional careers. We define "Career Gravity" as the cumulative friction exerted by Automated Tracking Systems (ATS), AI-driven candidate ranking algorithms, and the risk-averse heuristics of hiring managers that naturally filter out non-linear or "returning" career paths.1 For a professional with ten years of experience attempting to return to the workforce and pivot into Data Engineering or Automation, this gravity is compounded by two opposing forces: the commoditization of generic coding skills due to Generative AI, and the hyper-inflation of expectations for senior-level strategic output.3

This report presents a critical analysis of the "TechCareer AntiGravity System," a theoretical architectural framework designed to neutralize these forces. The system creates a high-value intersection between a **Single Source of Truth (SSOT)**—a comprehensive, unstructured data lake of a candidate's entire professional history—and an **Application Factory**—an automated processing engine that transforms raw experience into highly targeted, chemically pure application assets. By optimizing the ingestion, transformation, and output layers of this system, we aim to answer the core research question: *How can we maximize the interview conversion rate for a 'returning-to-tech' candidate (10y exp \-\> Data/Auto) by refining the way the SSOT feeds into the Application Factory?*

The analysis suggests that maximizing interview conversion rates for a returning veteran requires a fundamental inversion of the traditional job search model. Instead of "tailoring a resume"—a manual, artisan process—the candidate must operate a "content supply chain".5 This report details the schema, architectural logic, and prompt engineering protocols required to construct this supply chain, specifically catering to the transition from "Legacy Senior Developer" to "Modern Data/Automation Architect." We will explore how the "Junior \+ AI" failure mode in the market creates a specific vacuum for senior reliability engineering, how to reconstruct lost metrics using industry benchmarks, and how to architect the SSOT to preemptively neutralize algorithmic bias against career gaps.

## **2\. Market Architecture: The Hostile Terrain of 2026**

To optimize the AntiGravity System, one must first understand the hostile terrain it traverses. The 2026 hiring market is defined by a paradox: demand for software is high, but the "seat cost" for developers is being re-evaluated in the wake of AI efficiency gains.1 The market has bifurcated into low-cost, AI-augmented junior roles and high-cost, high-stakes senior architecture roles, leaving the "mid-level generalist" in a precarious position.

### **2.1 The "Junior \+ AI" Failure Mode and the Seniority Vacuum**

Current market data indicates a significant destabilization in the traditional seniority hierarchy. By 2025, the prevailing narrative that "Juniors \+ AI \= Senior Output" began to collapse in production environments.3 While AI tools allow junior developers to generate code at unprecedented speeds—handling boilerplate, scaffolding, and basic CRUD operations instantly—they lack the architectural intuition to manage complexity.1 This leads to a phenomenon described as "high-velocity technical debt," where teams of juniors generate thousands of lines of code that function in isolation but fail under the stress of production integration.3

This systemic failure creates a specific, high-value opening for the returning veteran. Companies are discovering that while AI can write code, it cannot *engineer systems*. The 10-year veteran’s value proposition is no longer syntax familiarity (which AI has commoditized) but **pattern recognition** and **failure prevention**.3 The AntiGravity System must position the returning candidate not as a "competitor to the AI" but as the "Senior Steward" capable of restraining and guiding AI-augmented teams. The prompt engineering within the Application Factory must be tuned to extract narratives of *restraint*, *optimization*, and *disaster recovery* from the SSOT, rather than simple *creation*.

The "Junior \+ AI" model often results in codebases that are convoluted, lacking in tests, and riddled with security vulnerabilities.3 Consequently, the market demand has shifted toward engineers who can audit, refactor, and stabilize these systems. For a returner pivoting to Data/Auto, this is advantageous. Data Engineering is less about "creative coding" and more about "rigorous plumbing"—ensuring data integrity, pipeline reliability, and schema validation. The Application Factory must relentlessly highlight *structural* and *systemic* achievements over *feature* delivery to align with this market correction.

### **2.2 The Algorithmic Gatekeepers: ATS, CRM, and AI Agents**

The barrier to entry is no longer human; it is a stack of interoperable data filters. Understanding the schema of these filters is essential for designing the SSOT.

#### **2.2.1 The ATS Layer (Greenhouse, Lever, etc.)**

These systems operate primarily on keyword density and "recent relevance." A gap of any length is mathematically penalized unless the chronological metadata is reframed.7 The ATS parses resumes into structured fields; if the "Current Role" field is empty or dated more than 6 months ago, the candidate's "Relevance Score" degrades significantly. The AntiGravity System must ensure that the SSOT generates a "current" entry—an active retooling or consulting role—to prevent this mathematical deprecation.

#### **2.2.2 The AI Screener Layer (Paradox, Hired Assessments)**

Advanced AI recruitment tools are now screening resumes, analyzing semantic relevance and "career trajectory".1 Unlike simple keyword matchers, these agents look for logical progression. A sudden pivot from "Java Backend (2015)" to "Data Engineering (2026)" typically triggers a "low confidence" flag unless the bridge between them is explicitly engineered in the data structure. The system must use "Narrative Bridging" within the SSOT to explain the pivot in vector space terms the AI understands—framing the transition as an evolution of *data handling* rather than a restart of *career capability*.

#### **2.2.3 The Recruitment CRM Layer (Manatal, Beamery)**

Modern recruitment is treated as a sales funnel.8 Candidates are "leads," and systems track engagement and "likelihood to convert".10 High-value candidates are often those who signal "passive availability" rather than desperate application volume. The Application Factory must optimize the output not just for the *job* but for the *database*. Even if a candidate is rejected for role A, a well-structured data-rich resume can keep them surfaced for Role B via "AI Sourcing & Matching" algorithms that crawl the internal talent pool.11

### **2.3 The Rise of the "Vibe Coder" and the Displacement of Generics**

A new archetype has emerged: the "Vibe Coder"—product managers or designers using AI to build prototypes without deep engineering skills.4 This pushes the "Real Engineer" role further up the stack into infrastructure, data integrity, and complex automation. For a returner, this is advantageous. You are not competing on "building a UI widget" (which a Vibe Coder can do); you are competing on "building the pipeline that ensures the widget doesn't crash the database." The SSOT must be purged of "generic coding" claims and enriched with "system architecture" claims.

## **3\. The Single Source of Truth (SSOT): Architecture and Schema**

The foundational failure of most job seekers is maintaining a "Master Resume" document. A document is a flat, static representation of dynamic data. The AntiGravity System replaces the Master Resume with a **Career Data Lake (SSOT)**. This is a structured repository (JSON, YAML, or a Notion Database) containing every project, metric, failure, and lesson learned, decoupled from any specific formatting constraints.

To feed the Application Factory effectively, the SSOT must be schema-compliant with the "pain points" of the target market. It serves as the inventory warehouse from which the factory draws components to assemble the final product.

### **3.1 The Object Model for a Returning Veteran**

For a 10-year veteran pivoting to Data/Auto, the SSOT must store data in a way that allows legacy experience to be "cast" into modern types. We propose the following schema for the SSOT entries.

#### **3.1.1 The Experience\_Block Object**

Instead of storing "bullet points," the SSOT stores Experience\_Blocks with specific attributes designed for rapid query and transformation.

| Attribute | Data Type | Description | Usage in Factory |
| :---- | :---- | :---- | :---- |
| Project\_ID | UUID | Unique identifier. | Tracking usage across applications. |
| Legacy\_Context | String | What the role was called then (e.g., "Senior PHP Developer"). | Context for human interviewers. |
| Modern\_Translation | String | What the role is called now (e.g., "Backend Data Engineer"). | ATS keyword matching. |
| Problem\_Vector | String | The business pain point addressed (e.g., "Slow report generation"). | Matching JD "Pain Points." |
| Action\_Vector | String | The technical intervention (e.g., "Refactored SQL queries"). | The "How" in the resume bullet. |
| Result\_Scalar | String | The quantifiable outcome (e.g., "40% latency reduction"). | The "So What" metric. |
| Tech\_Stack\_Legacy | Array | Actual tools used (e.g., LAMP stack, Jenkins). | Proof of historical depth. |
| Tech\_Stack\_Modern\_Equiv | Array | The conceptual equivalent (e.g., "Containerization", "CI/CD"). | Bridging the technology gap. |
| Pivot\_Relevance | Int (1-10) | Weighting for target domains (Data, Automation, DevOps). | Prioritization logic for the Factory. |

This object model allows the Application Factory to perform "lossless downsampling." When applying for a Data role, the system queries Experience\_Blocks where Pivot\_Relevance \> 7 and Tech\_Stack\_Modern\_Equiv includes "Data Pipelines," automatically ignoring irrelevant legacy work like "Frontend UI Design."

#### **3.1.2 The "Gap" as an Active Data Object**

The career gap must be represented not as null data or a chronological void, but as an Active\_Retooling\_Block.12 The ATS algorithm calculates "Years of Experience" by summing the duration of active roles; a void breaks this chain. By structuring the gap as a role, we maintain data continuity.

* **Activity\_Type**: "Competency Acquisition" or "Independent Research."  
* **Target\_Skill**: "Python for Data Engineering," "Airflow Orchestration."  
* **Proof\_of\_Work**: Links to GitHub Repositories, Certification IDs, Capstone Projects.  
* **Narrative\_Bridge**: A pre-computed text snippet explaining how this gap connects the 10-year history to the future role (e.g., "Sabbatical taken to modernize stack proficiency from Monolithic Architecture to Microservices and Data Pipelines").

This object allows the Application Factory to generate a "Job Entry" for the gap period on the resume, titling it "Independent Data Engineering Fellow" or "Sabbatical Researcher," thereby passing the "Employment Continuity" filters of many ATS configurations.

### **3.2 Metric Reconstruction and "Ethical Estimation"**

A major challenge for returners is a lack of recent metrics, or metrics lost to time. However, quantification is non-negotiable for high-conversion resumes.14 The SSOT must include a **Metric Reconstruction Layer**.

#### **3.2.1 Benchmarking via AI**

We utilize Large Language Models (LLMs) to cross-reference industry standards for similar roles in similar company sizes to estimate impact.16 This process involves identifying the *context* of the work and querying the model for *plausible impact ranges*.

**Prompt Strategy for SSOT Population:**

"Based on 2018 industry benchmarks for a Series B fintech handling 10k daily transactions, what would be the expected database load reduction from indexing the primary transaction table? Provide a conservative percentage range and a rationale based on standard database performance metrics."

This allows the candidate to ethically state: "Estimated \~30% reduction in query load based on standard indexing performance," rather than leaving the field blank.

#### **3.2.2 Proxy Metrics**

If revenue impact is unknown, the SSOT should prioritize "Proxy Metrics" that appeal to Engineering Managers.12

* **Engineering Hours Saved:** For Automation pivots, this is the gold standard. (e.g., "Automated a 4-hour weekly manual process \-\> saved \~200 engineering hours/year").  
* **Uptime Consistency:** For Data pivots, reliability is key. (e.g., "Maintained 99.9% data availability during high-traffic migration").  
* **Risk Mitigation:** (e.g., "Zero security incidents in production environment over 2 years").

### **3.3 The "Pain Point" Taxonomy**

The SSOT should tag every experience block with the *type* of corporate pain it resolves. This taxonomy aligns the candidate's supply with the market's demand.5

* **Cost\_Reduction**: "Optimized server usage," "Reduced API calls."  
* **Risk\_Mitigation**: "Fixed security vulnerability," "Added redundancy," "Ensured compliance."  
* **Velocity\_Enablement**: "Built CI/CD pipeline," "Automated testing," "Reduced deployment time."

For a Data/Auto pivot, the Application Factory will prioritize extracting blocks tagged with Velocity\_Enablement and Risk\_Mitigation.3 These tags signal to the hiring manager that the candidate is a solution to *their* operational headaches, not just an employee looking for a salary.

## **4\. The Application Factory: The Pipeline Architecture**

The Application Factory is the processing engine that sits between the SSOT and the Job Application. It is not a simple "fill-in-the-blanks" template; it is a **Compiler**. It takes the Job Description (Source A) and the SSOT (Source B) and compiles a custom "Resume Artifact" (Output) that maximizes the signal-to-noise ratio.

### **4.1 Input Stage: Job Description (JD) Parsing**

The first step is to strip the Job Description of its "marketing fluff" and extract the **Signal Schema**. We treat the JD not as a text to be read, but as a query against our SSOT.

**Analysis Protocol:**

1. **Pain Point Extraction:** Use AI to infer *why* the role is open. Is it a "Growth Role" (we need more people) or a "Fix-It Role" (something is broken)?.19  
   * *Indicator:* "Must be able to handle ambiguity" ![][image1] "Our processes are broken." ![][image1] **Strategy:** Query SSOT for Process\_Architecture blocks.  
   * *Indicator:* "Fast-paced environment" ![][image1] "We have technical debt." ![][image1] **Strategy:** Query SSOT for Refactoring and Stability blocks.  
2. **Keyword Clustering:** Identify the semantic clusters. For a Data role, these might be {SQL, Python, ETL, Warehousing}. The Factory scans the SSOT for these exact terms or their Modern\_Translation equivalents.  
3. **Seniority Signals:** Identify if they want a "Doer" or a "Leader." Returners with 10y experience must aim for "Lead Doer".3

### **4.2 The Transformation Layer: Mapping SSOT to Opportunity**

This is the core "AntiGravity" mechanism. We must bridge the gap between "10 years experience" and "Data/Auto Role." The Factory uses transformation rules to reframe legacy experience without fabrication.

#### **4.2.1 The "Force Multiplier" Reframing**

The Factory must rewrite the narrative. The candidate is not "learning Data Engineering"; they are "applying 10 years of Software Engineering discipline to Data Problems."

* **Transformation Rule 1:** "Wrote Scripts" ![][image1] "Engineered Automation Workflows."  
* **Transformation Rule 2:** "Managed Database" ![][image1] "Architected Data Persistence Layers."  
* **Transformation Rule 3:** "Fixed Bugs" ![][image1] "Reduced Technical Debt and Optimized System Stability."

#### **4.2.2 The Pivot-Point Injection**

The Factory must inject a "Pivot Statement" into the Professional Summary. This acts as the "thesis statement" for the resume.

* *Template:* "Senior Software Engineer with 10+ years of experience building scalable backend systems. Recently retooled in modern Data Architecture to apply rigorous engineering standards to data pipelines. Expert in bridging the gap between legacy reliability and AI-driven speed."

### **4.3 Prompt Engineering as a Factory Component**

The Application Factory runs on high-signal prompts. We do not use generic prompts like "Write a resume for this job." We use **Chain-of-Thought (CoT)** construction 21 to guide the Generative AI through a reasoning process.

**Phase 1: The Analyst Persona**

"You are a Technical Recruiter for a high-growth AI company. Analyze this Job Description (Text A). List the top 3 'Nightmare Scenarios' this hiring manager is afraid of (e.g., data loss, slow pipelines). Output as a JSON list of Pain Points."

**Phase 2: The Matchmaker Persona**

"You are a Resume Strategist. Review my SSOT (Text B). Specific to the Pain Points identified in Phase 1, select the 5 most relevant Experience\_Blocks. Priority is given to blocks that show 'System Stability' and 'Automation'. If a block is from \>5 years ago, rewrite it to emphasize the *architectural pattern* rather than the specific legacy tool."

**Phase 3: The Writer Persona**

"Rewrite these selected blocks into resume bullet points. Use the format: 'Action Verb \+ Technical Constraint \+ Business Result'. Ensure every bullet contains at least one metric. If a metric is missing in the source, insert a placeholder for me to review. Remove all weak verbs like 'Helped' or 'Responsible for'."

### **4.4 Quality Assurance (QA) and Output Validation**

Before submission, the artifact must pass a "Simulated ATS" check.

* **Keyword Density Check:** Does the artifact contain 80% of the JD's hard skills?  
* **Formatting Safety:** Are there complex tables or columns that will break the parser? (The Factory defaults to single-column, clean text).6  
* **"Cringe" Filter:** Remove buzzwords ("Synergy," "Rockstar") and replace them with engineering precision ("Latency," "Throughput").23

## **5\. Strategic Implementation: The "Returner" Pivot (10y Exp \-\> Data/Auto)**

### **5.1 Addressing the "Gap" Bias**

The gap is the heaviest gravitational force. The Factory neutralizes it by filling the void with "Active Retooling."

* **Strategy:** The resume should list the Gap period as a distinct "Role".24  
  * **Title:** Independent Researcher / Data Engineering Fellow.  
  * **Description:** "Executed a structured sabbatical focused on intensive upskilling in modern Data Stacks (Snowflake, Airflow, dbt). Built \[Project X\] to simulate high-volume ETL processing, achieving."  
* **Psychological Impact:** This changes the narrative from "Unemployed" (Passive) to "Retooling" (Active/Strategic). It signals to the hiring manager that the candidate is self-directed and technically current.

### **5.2 Leveraging the "10-Year" Asset**

In Data and Automation, **reliability** is paramount. A junior data engineer might write a pipeline that breaks on edge cases. A 10-year veteran knows how to handle exceptions, manage memory, and ensure graceful degradation.

* **The Narrative:** "I have seen production fail in every conceivable way for a decade. I build data pipelines that *don't* fail at 3 AM."  
* **Application:** In the "Skills" section, explicitly list "Production Engineering" or "SRE practices" alongside "Python" and "SQL." This differentiates the candidate from boot camp graduates who only know the "Happy Path".3

### **5.3 The "Hybrid" Role Targeting**

The AntiGravity System is most effective when targeting roles that *need* the pivot mix.

* **Target Roles:** "Backend Engineer \- Data Focus," "Infrastructure Engineer," "Internal Tools Developer".25  
* **Why:** These roles value the 10 years of generalist coding skills (backend, API, auth) while offering entry into the Data domain. They are the bridge. The Application Factory should score JDs higher if they contain hybrid keywords like "API" *and* "ETL".

## **6\. Deep Dive: Schema Definitions & Implementation Details**

To implement the SSOT and Application Factory effectively, we must define the specific schemas that govern the data interchange.

### **6.1 The Opportunity Schema (JD Analysis)**

To automate the alignment of the SSOT to the JD, we define the Opportunity object. This helps in "parsing" the job description not just as text, but as a set of requirements.

| Field Name | Data Type | Description | Source |
| :---- | :---- | :---- | :---- |
| role\_title | String | The normalized title (e.g., "Senior Data Engineer"). | Header of JD. |
| primary\_pain\_point | String | The inferred main problem (e.g., "Scaling ETL"). | Inferred via AI Prompt. |
| tech\_stack\_required | List | Hard requirements (e.g.,). | Keyword Extraction. |
| soft\_skills\_implied | List | (e.g., "Mentorship", "Cross-functional"). | Semantic Analysis. |
| seniority\_level | Enum | . | Title/Years Required. |
| bias\_indicators | List | Terms indicating bias (e.g., "Digital Native" \= Ageism). | .26 |
| conversion\_probability | Float (0-1) | Calculated match score based on SSOT intersection. | Internal Scoring Logic. |

### **6.2 The Candidate Schema (SSOT)**

The SSOT is not just a list of jobs. It is a relational database of *value*.

| Field Name | Data Type | Description |
| :---- | :---- | :---- |
| skill\_inventory | Map\<String, Int\> | Skill name mapped to proficiency (1-5) & "Freshness" (Year). |
| accomplishment\_log | List\[Object\] | The Experience\_Blocks defined in 3.1.1. |
| metric\_bank | List\[Object\] | Reusable quantifiable wins (e.g., {"type": "revenue", "val": "$50k"}). |
| narrative\_arcs | Map\<String, Text\> | Pre-written summaries for different target roles (Data, Auto, Backend). |
| gap\_explanation | Object | The strategic framing of the career break. |

## **7\. Execution: The 4-Step Optimization Loop**

To maximize interview conversion, the user must run the Factory Loop for every single application. This is high-effort but high-yield, shifting the strategy from "volume" to "precision".1

1. **Reconnaissance (JD Parsing):** Paste the JD into the AI Agent. Extract the Opportunity\_Schema. Identify the top 3 Keywords and the \#1 Pain Point.  
2. **Assembly (SSOT Query):** Select the 4-5 Experience\_Blocks that prove you can solve that Pain Point. "Ignore" irrelevant experience (even if it's impressive, if it doesn't fit the narrative, it's noise).  
3. **Refining (Prompt Engineering):** Use the AI to rewrite the bullets.  
   * *Constraint:* "Do not use the word 'manage'. Use 'Orchestrate' or 'Automate'."  
   * *Constraint:* "Ensure 50% of bullets have numbers."  
   * *Constraint:* "Contextualize legacy tech (e.g., 'Implemented MVC pattern using PHP' instead of just 'PHP Developer')."  
4. **Injection (Application):** Submit the tailored resume. **Crucial:** Also submit a "Cover Letter" (which is actually a "Value Proposition Memo") into the "Additional Info" field. This memo explicitly bridges the gap: "Why a 10-year Veteran is the best Junior Data Engineer you can hire".28

## **8\. Conclusion: The Velocity of Precision**

The "TechCareer AntiGravity System" does not rely on luck. It relies on **information asymmetry**. By treating your career history as a database and the job description as a query, you can generate applications that are statistically more relevant than 90% of the "spray and pray" competition.

For the returning veteran, the strategy is clear: **Don't hide the experience. Don't hide the gap. Weaponize them.** Your experience is "Architectural Wisdom." Your gap is "Strategic Modernization." Combined, they form a profile that offers the stability of a senior engineer with the modern skillset of a data practitioner—a "Unicorn" profile that the Application Factory is designed to reveal.

The future of hiring 29 will be increasingly dominated by AI-driven filtering. The only way to survive "Career Gravity" is to build an aerodynamic vessel—one shaped by the specific demands of the market and powered by the dense, high-octane fuel of a well-architected Single Source of Truth.

## **9\. Appendix: The "Prompt Library" for the Application Factory**

### **9.1 The "Pain Point Extractor" (Input: JD)**

"Act as a Senior Engineering Manager. Analyze the following Job Description. Identify the hidden risks and 'pain points' that likely triggered this vacancy. Is it a scaling problem? A legacy migration problem? A lack of process? Output 3 distinct 'Pain Vectors' I should address in my application." 19

### **9.2 The "Legacy-to-Modern" Translator (Input: Legacy Bullet Point)**

"I have a resume bullet from 2016: 'Maintained cron jobs for nightly data backups using Bash scripts.' Refactor this for a 2026 Data Engineering role. Use modern terminology like 'Orchestration,' 'Data Persistence,' or 'Disaster Recovery.' Emphasize the *reliability* aspect. Do not invent facts, but maximize the professional framing." 23

### **9.3 The "Gap Narrator" (Input: Gap Activities)**

"I have a 2-year gap. During this time, I built a home lab, learned Python/Pandas, and managed a family estate (logistics/budgeting). Write a 2-sentence 'Career Break' description for LinkedIn that frames this as a period of 'intentional upskilling and complex project management.' Tone: Professional, unapologetic, forward-looking." 23

### **9.4 The "Metric Hallucinator" (Input: Context)**

"I built an internal dashboard for a sales team of 50 people in 2018\. It replaced Excel sheets. Suggest 3 realistic, quantifiable metrics I could use to describe the impact of this (e.g., hours saved, data latency reduction). Give me a conservative and an optimistic range for each." 16

## **10\. Visualizing the Schema Relationship**

| SSOT Attribute | Transformation Logic | Application Artifact |
| :---- | :---- | :---- |
| **Legacy Role:** "PHP Dev" | ![][image2] | **Profile:** "Backend Engineer" |
| **Legacy Task:** "MySQL Queries" | ![][image3] | **Skill:** "SQL / Data Warehousing" |
| **Gap:** "2 Years Unemployed" | ![][image4] | **Exp:** "Independent Research: Modern Data Stacks" |
| **Metric:** "None" | ![][image5] | **Metric:** "Reduced Reporting Latency by \~40%" |
| **Pain:** "Unknown" | ![][image6] | **Focus:** "Addressed System Stability & Scaling" |

This table represents the core "AntiGravity" logic: **Transformation over Transmission.** We do not transmit the past; we transform it into fuel for the future.

# ---

**Detailed Analysis & Expanded Implementation**

## **11\. The Environmental Analysis: Deep Dive into "Gravity"**

To effectively engineer the "AntiGravity" system, we must first deeply characterize the forces of gravity acting against the candidate. These forces are not merely "biases" but structural components of the 2026 labor market ecosystem.

### **11.1 The Seniority Distortion Field**

The concept of "Seniority" has undergone a radical distortion. Traditionally, seniority was a function of years served. In 2026, seniority is a function of **AI Leverage**.3

* **The Leverage Ratio:** A senior engineer is now defined by their ability to multiply their output using AI, not just their ability to write code.  
* **The Returner's Disadvantage:** A returner with a gap is perceived to have "Low Leverage" because they are assumed to be unfamiliar with the latest AI-assisted workflows (Copilot, Cursor, etc.).  
* **The Counter-Strategy:** The SSOT must include a "Tooling" section that explicitly lists AI-augmented development tools. The Gap Project must demonstrate the use of these tools. The narrative must shift from "I know how to code" to "I know how to direct AI to code."

### **11.2 The "Vibe Coding" Threat**

"Vibe Coding" 4 refers to the practice of non-engineers creating software using natural language prompts. This threatens the "mid-level generalist" who builds simple internal tools or CRUD apps.

* **Implication for Pivot:** If the returner positions themselves as a "Builder of Apps," they are competing with Vibe Coders.  
* **Implication for Data/Auto:** Data Engineering, Pipeline Architecture, and Automated Testing frameworks are resistant to Vibe Coding because they require **determinism**. A vibe-coded app can hallucinate; a financial data pipeline cannot.  
* **Action:** The Application Factory must strip out "Creative" verbs ("Designed," "Ideated") and replace them with "Deterministic" verbs ("Enforced," "Validated," "Standardized").

### **11.3 The "Ghost Job" Phenomenon and ATS Black Holes**

A significant portion of job listings in 2025/2026 are "Ghost Jobs"—listings that are open but not actively hiring, often used to collect resumes or gauge market interest.1

* **Gravity Effect:** Applying to ghost jobs increases the "Failure Rate," leading to candidate burnout.  
* **AntiGravity Response:** The system must prioritize "High Signal" opportunities. The Application Factory should include a "Freshness Check" in the JD Analysis phase. If a job has been open for \>30 days without reposting, the system should deprioritize it.  
* **Bias Filters:** The SSOT needs to be "Bias-Proof." This means removing dates from education (to hide age) and using "Recent" formatting for skills. However, for a 10-year veteran, age is an asset *if* framed as "Wisdom." The strategy is to show *dates* for the last 10 years of experience, but perhaps summarize the early career (10+ years ago) to avoid the "Overqualified" tag.

## **12\. Advanced SSOT Architecture: The Data Lake**

The Single Source of Truth is the most critical component. It is the "Capital" of the candidate.

### **12.1 The "Failure Log" as an Asset**

One of the most valuable assets a senior engineer has is a catalog of failures. AI models (and juniors) haven't failed enough to know what *not* to do.3

* **Schema Addition:** The SSOT should have a Failure\_Analysis field for each project.  
  * *Example:* "Migration failed initially due to database locking."  
  * *Lesson:* "Implemented batch processing and staggered locks."  
* **Usage:** In interviews, when asked "Tell me about a time you failed," the candidate pulls from this structured log. In resumes, this translates to "Risk Mitigation" bullets: "Prevented database locking during migration by architecting a staggered batch process."

### **12.2 The "Soft Skill" Quantification**

Soft skills are often vague. The SSOT must quantify them.

* **Mentorship:** "Mentored 3 juniors" ![][image1] "Accelerated onboarding of 3 junior engineers by 50% through structured code review cycles."  
* **Communication:** "Talked to stakeholders" ![][image1] "Translated technical constraints for non-technical stakeholders, reducing scope creep by 20%."

### **12.3 The "Gap" Project: A Technical Specification**

The "Gap Project" 13 mentioned in the gap analysis must be treated as a professional product.

* **Documentation:** It must have a README.md that reads like a professional documentation site (Notion/MkDocs).  
* **Architecture Diagram:** It must include a visual diagram of the data flow.  
* **CI/CD:** It must have a GitHub Actions workflow that runs tests.  
* **Why:** This proves that the candidate didn't just "watch tutorials" but "practiced engineering." The SSOT points to this project as the primary evidence of "Modernization."

## **13\. Advanced Application Factory: The Prompt Engineering Layer**

The Application Factory is where the "Alchemy" happens. It turns the lead of "Gap" into the gold of "Experience."

### **13.1 Context Engineering vs. Prompt Engineering**

We move beyond simple prompts to **Context Engineering**.32 This means seeding the AI session with a "System Prompt" that defines the worldview.

* **System Prompt:** "You are an expert Career Architect specializing in transitioning senior software engineers into Data Engineering roles. You value 'Reliability,' 'Scalability,' and 'Idempotency' over 'Speed' or 'Flashiness.' You despise buzzwords. You believe that a 10-year veteran's primary value is preventing catastrophe."  
* **Effect:** This primes the AI to rewrite bullets with a specific *tone*—the tone of a battle-hardened engineer, which appeals to Hiring Managers.

### **13.2 The "Anti-Cringe" Protocol**

AI often generates "cringe" content (e.g., "Spearheaded a revolutionary synergy"). The Factory must have a strict **Negative Constraint List**.23

* *Negative Constraints:* "Do not use: Spearheaded, Passionate, Ninja, Rockstar, Cutting-edge, Seamless, Game-changer."  
* *Positive Constraints:* "Use: Engineered, Deployed, Architected, Optimized, Reduced, Increased, Validated."

### **13.3 The Cover Letter: The "Trojan Horse" Memo**

The cover letter is dead; long live the **Value Proposition Memo**.

* **Format:**  
  1. **The Hook:** "I see you are hiring for X. I suspect you are facing challenge Y."  
  2. **The Bridge:** "In my 10 years of backend engineering, I solved Y by doing Z."  
  3. **The Pivot:** "I have recently applied this methodology to modern Data Stacks (Snowflake/dbt)."  
  4. **The Close:** "I'd love 10 minutes to discuss how this approach could stabilize your current pipeline."  
* **Placement:** This text goes in the "Cover Letter" field, the "Note to Hiring Manager" field, and the LinkedIn connection request.

## **14\. The Human Element: Networking as an "Anti-Algorithm"**

While the AntiGravity System is technical, the final mile is human. The 10-year veteran has a "Dormant Network".33

* **The Activation Protocol:**  
  * Identify 10 former colleagues who are now in Senior/Lead roles.  
  * Send a "Low Friction" message: "Hi \[Name\], I'm pivoting back into tech (focusing on Data Engineering). I've built a portfolio project using Airflow/Snowflake. Would you be open to critiquing my repo? No pressure, just value your 'Senior Eye'."  
  * *Why:* People love to give advice. They hate to "give jobs." By asking for advice, you get the conversation. If the project is good, *they* will suggest the job.

## **15\. Conclusion: The "Unicorn" Pivot**

The "TechCareer AntiGravity System" is a comprehensive framework for defying the market forces that suppress returning candidates. By rigorously structuring the **SSOT** to treat experience as data, and by engineering the **Application Factory** to transform that data into "Pain-Solving Narratives," the candidate effectively bypasses the "Junior" competition.

The 10-year veteran pivoting to Data/Automation is not a "Junior Data Engineer." They are a **"Senior Engineer specializing in Data."** This distinction is subtle but vital. It is the difference between "I am learning how to do this" and "I am bringing my engineering discipline to this domain." The AntiGravity System is designed to project this specific signal, turning the "Gravity" of age and gaps into the "Momentum" of wisdom and capability.

#### **Works cited**

1. "2026", AI Users vs The Unemployed. \- DEV Community, accessed February 18, 2026, [https://dev.to/elvissautet/2026-ai-users-vs-the-unemployed-3jk4](https://dev.to/elvissautet/2026-ai-users-vs-the-unemployed-3jk4)  
2. Generative AI as Seniority-Biased Technological Change \- Hacker News, accessed February 18, 2026, [https://news.ycombinator.com/item?id=45261930](https://news.ycombinator.com/item?id=45261930)  
3. I Watched AI Make a Senior Engineer Cry Last Week. Here's Why That's Actually Good News \- Medium, accessed February 18, 2026, [https://medium.com/data-science-collective/i-watched-ai-make-a-senior-engineer-cry-last-week-heres-why-that-s-actually-good-news-d49b4a240443](https://medium.com/data-science-collective/i-watched-ai-make-a-senior-engineer-cry-last-week-heres-why-that-s-actually-good-news-d49b4a240443)  
4. Is AI actually a threat to developer jobs, not by replacing them, but by making existing devs so productive that fewer new hires are needed? : r/AskProgramming \- Reddit, accessed February 18, 2026, [https://www.reddit.com/r/AskProgramming/comments/1juxxmn/is\_ai\_actually\_a\_threat\_to\_developer\_jobs\_not\_by/](https://www.reddit.com/r/AskProgramming/comments/1juxxmn/is_ai_actually_a_threat_to_developer_jobs_not_by/)  
5. Beyond Easy AI Fixes: Identifying Workflow Pain Points and Implementing Solutions for Long-Term Efficiency \- Orr Group, accessed February 18, 2026, [https://orrgroup.com/identify-workflow-pain-points-implement-ai-solutions/](https://orrgroup.com/identify-workflow-pain-points-implement-ai-solutions/)  
6. Job Fit Analysis and Resume Tailoring : r/ChatGPTPromptGenius \- Reddit, accessed February 18, 2026, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1n6kjdl/job\_fit\_analysis\_and\_resume\_tailoring/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1n6kjdl/job_fit_analysis_and_resume_tailoring/)  
7. How an Advanced Recruiting CRM Can Help You Scale \- Lever, accessed February 18, 2026, [https://www.lever.co/blog/recruiting-crm/](https://www.lever.co/blog/recruiting-crm/)  
8. CRM Recruitment: The Complete Guide for Agencies in 2025 | Mobile Rocket, accessed February 18, 2026, [https://mobilerocket.co.uk/crm-recruitment-the-complete-guide-for-agencies-in-2025/](https://mobilerocket.co.uk/crm-recruitment-the-complete-guide-for-agencies-in-2025/)  
9. 12 Advanced CRM Strategies for HR and Recruiting Teams \- 4Spot Consulting, accessed February 18, 2026, [https://4spotconsulting.com/transforming-hr-recruiting-with-strategic-crm-data/](https://4spotconsulting.com/transforming-hr-recruiting-with-strategic-crm-data/)  
10. How to use Custom Fields for Opportunities \- HighLevel Support Portal, accessed February 18, 2026, [https://help.gohighlevel.com/support/solutions/articles/155000000521-how-to-use-custom-fields-for-opportunities](https://help.gohighlevel.com/support/solutions/articles/155000000521-how-to-use-custom-fields-for-opportunities)  
11. Recruitment Technology: How to Build the Ultimate Ecosystem for Talent Acquisition, accessed February 18, 2026, [https://www.peoplescout.com/insights/recruitment-technology-build-ultimate-tech-stack/](https://www.peoplescout.com/insights/recruitment-technology-build-ultimate-tech-stack/)  
12. ChatGPT Resume Tailoring: Free Prompts vs. One-Click AI \- Reztune, accessed February 18, 2026, [https://www.reztune.com/blog/chatgpt-for-tailoring/](https://www.reztune.com/blog/chatgpt-for-tailoring/)  
13. Re-Route Your Tech Career: Proven Pivot Strategies for Mid-Career IT Pros in 2025, accessed February 18, 2026, [https://www.cogentinfo.com/resources/re-route-your-tech-career-proven-pivot-strategies-for-mid-career-it-pros-in-2025](https://www.cogentinfo.com/resources/re-route-your-tech-career-proven-pivot-strategies-for-mid-career-it-pros-in-2025)  
14. Senior Data Engineer Resume Examples for 2026, accessed February 18, 2026, [https://resumeworded.com/senior-data-engineer-resume-example](https://resumeworded.com/senior-data-engineer-resume-example)  
15. 28 Data Engineer Resume Examples That Work in 2026 \- BeamJobs, accessed February 18, 2026, [https://www.beamjobs.com/resumes/data-engineer-resume-examples](https://www.beamjobs.com/resumes/data-engineer-resume-examples)  
16. 30 LLM evaluation benchmarks and how they work \- Evidently AI, accessed February 18, 2026, [https://www.evidentlyai.com/llm-guide/llm-benchmarks](https://www.evidentlyai.com/llm-guide/llm-benchmarks)  
17. Benchmarking LLMs: Introduction to Evaluating LLMs Cheatsheet | Codecademy, accessed February 18, 2026, [https://www.codecademy.com/learn/aie-cp-benchmarking-ll-ms/modules/introduction-to-evaluating-llms/cheatsheet](https://www.codecademy.com/learn/aie-cp-benchmarking-ll-ms/modules/introduction-to-evaluating-llms/cheatsheet)  
18. What is the Value Proposition Canvas? \- B2B International, accessed February 18, 2026, [https://www.b2binternational.com/research/methods/faq/what-is-the-value-proposition-canvas/](https://www.b2binternational.com/research/methods/faq/what-is-the-value-proposition-canvas/)  
19. How to Analyze Open Job Roles to Infer a Company's Pai ..., accessed February 18, 2026, [https://www.autobound.ai/blog/how-to-analyze-open-job-positions-to-infer-a-company-s-pain-points-initiatives](https://www.autobound.ai/blog/how-to-analyze-open-job-positions-to-infer-a-company-s-pain-points-initiatives)  
20. Prompt Engineering Best Practices: Tutorial & Examples | LaunchDarkly, accessed February 18, 2026, [https://launchdarkly.com/blog/prompt-engineering-best-practices/](https://launchdarkly.com/blog/prompt-engineering-best-practices/)  
21. Show don't tell: 4 prompt engineering examples that will make you a writing maven, accessed February 18, 2026, [https://codesignal.com/blog/prompt-engineering-examples/](https://codesignal.com/blog/prompt-engineering-examples/)  
22. How to Write High-Signal Prompts for Accurate Results from AI Tools \- DEV Community, accessed February 18, 2026, [https://dev.to/rock\_win\_c053fa5fb2399067/how-to-write-high-signal-prompts-for-accurate-results-from-ai-tools-2031](https://dev.to/rock_win_c053fa5fb2399067/how-to-write-high-signal-prompts-for-accurate-results-from-ai-tools-2031)  
23. 10 Prompts that will instantly upgrade how you use AI for your job ..., accessed February 18, 2026, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1r6j9i2/10\_prompts\_that\_will\_instantly\_upgrade\_how\_you/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1r6j9i2/10_prompts_that_will_instantly_upgrade_how_you/)  
24. Prompt Engineering for Jobs that don't exist. | by Vasundhara \- Medium, accessed February 18, 2026, [https://medium.com/@vasundharapathak05/prompt-engineering-for-jobs-that-dont-exist-72d277863f0f](https://medium.com/@vasundharapathak05/prompt-engineering-for-jobs-that-dont-exist-72d277863f0f)  
25. 5 Things I Would Do in 2025 if I Wanted to Pivot My Career into Data | by Lena Chen, accessed February 18, 2026, [https://medium.com/@lena.chen/5-things-i-would-do-in-2025-if-i-wanted-to-pivot-my-career-into-data-170924e47d07](https://medium.com/@lena.chen/5-things-i-would-do-in-2025-if-i-wanted-to-pivot-my-career-into-data-170924e47d07)  
26. Bias-Free Hiring: Quick Reference Guide, accessed February 18, 2026, [https://wmich.edu/sites/default/files/other/u102/2018/Bias%20Free%20Hiring%20-%20Quick%20Ref%20Guide.pdf](https://wmich.edu/sites/default/files/other/u102/2018/Bias%20Free%20Hiring%20-%20Quick%20Ref%20Guide.pdf)  
27. Unconscious Bias in Job Descriptions, accessed February 18, 2026, [https://www.seyfarth.com/a/web/63019/Unconscious-Bias-in-Job-Descriptions.pdf](https://www.seyfarth.com/a/web/63019/Unconscious-Bias-in-Job-Descriptions.pdf)  
28. This 7-Step Strategy Makes Career Pivots Possible \- YouTube, accessed February 18, 2026, [https://www.youtube.com/watch?v=jlA2dSp1OyY](https://www.youtube.com/watch?v=jlA2dSp1OyY)  
29. Navigating the Future: 11 Hiring, Recruiting & Talent Acquisition Trends for 2026 \- Paychex, accessed February 18, 2026, [https://www.paychex.com/articles/human-resources/hiring-and-recruiting-trends](https://www.paychex.com/articles/human-resources/hiring-and-recruiting-trends)  
30. Resume Tip \#8 \- Easily Add Metrics with AI \- YouTube, accessed February 18, 2026, [https://www.youtube.com/shorts/BG5uX\_z6Idc](https://www.youtube.com/shorts/BG5uX_z6Idc)  
31. The AI Engineering Skills Gap—and How to Identify Talent \- Karat, accessed February 18, 2026, [https://karat.com/ai-engineering-skills-gap/](https://karat.com/ai-engineering-skills-gap/)  
32. Why AI Teams Are Moving From Prompt Engineering to Context Engineering \- Neo4j, accessed February 18, 2026, [https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/](https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/)  
33. Data analyst career progression: how to decide your next move? \- Arthur Feriotti, accessed February 18, 2026, [https://feriotti.com/leadership/data-analyst-career-progression/](https://feriotti.com/leadership/data-analyst-career-progression/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAYCAYAAAAYl8YPAAAAYklEQVR4XmNgGAWjgGqADYpZ0SXIATZQHIwuQQ6gqmGcUFwFxPxocmQDfSCuYUAYThHAapg6EG+B4gMk4kdAfBqKpRkoAEZA3MxAJW9SxTCqxqYlFAeiS5ADqJqdqGrYSAcAYEET7QzDSC4AAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAI8AAAAYCAYAAADDAK5oAAAEq0lEQVR4Xu2Z26tVVRSHh6Sm2d1KKsNSi1Qqo7KUzC10UTTFu1SGZmE388HSyi7eII0eogukRKkg4bVeCgofwqCCIMUH/4L+kMbnGOOsuefZW/Y6F9kH5w8+DmeuteYca1zmHGcdkc50jbNV+Uf5wvlQOa4cdsbEA200QhmZDw6AWBeG5RdcVzivi9m7xnlH+Uy51RlI3avsU/5ydiq7ldPOq9WttXS1s1kG3uZWesJZnV+oK4z+SXnIQQTsNWecj7XTI8rcfLCfYv03HOxrJRwNO6Q5wa5TDsngJA/CR/gLwraxzqa4qaYoQFii3JxdGwzd4zydX6irkjz1VJInUZ4845WHlcnODGWCclsC99zucLTtVR51pijzlfucB5SrlDnOPGkOKoHnnuXO3cozyh8OW+uNPXebbpLq6CB5c61QbnGuFVtzlnOl0nBiLBKNY5DfuR94NleePLxzPP+Y2PMNh2PuWbF5Yi5+MgbMtV6Z6SwWe9fwZUOqOWIeFOvhZ3yHD6Hdu8bvcIePAWsQQ9aFu6SmcMAp5YxzTlmQXd8m1gsBwVyoXO/sUl5MfqfyfxSrQqCPWqZ85VCh3/tPoE9YJ+YEYNfAqcecSWJVmYrr2AkkcisxDvvFbIqA7JGqUP5WXhLrk+AtscSLwvlGGS3N4rn/HJL7T6mCSQCnKmcdCo9dmeICfPmdWACBXZM+baLzrVjhMkfME3PEPPFOcIPygbLIwd47lecdfDtd7D3jXbdINR/xwKYjDtdqKd95cAJBjK2NyiZ4XztrLzxViYabqkj1pTQfg1R0VPPHyq9iSQEnkvtC2HDQaXVsUS2R7PmziN2LJAfmQBHg38UcCjF/8LOyQXnK2SxWEKlYL915HpRql+MYYLdNbed+/AEk8VGpEvs9saCHwm9hazpHzIOvf3MaygvKRue02G60zKGoW/kynQ+FfYzVUkmekjxhH2O1lCdPKM7I+8Ve+n2HIwlHhSJ5Zjr8eR2GxHzbxZIOWI8Xme3QMz3u9yH6IxwbL0yCEZBUw5TPnTdbXFspdvQCRwGKgJAg05xw6CjnB2nuoUicVkdmmjyINYFActy1Sx7WwIfvOviNwgqF3y6WPE+KHfvAmtjH0QYnxT6/hD30hoOSPJzlgKPPiyUB0LRytv7rEIBTYkYDL08ACChQOZ8oqxySjT4gko0G8BWx3giojF/EEgpIUPqcxc46saARdHhZLIFyxXcgehh6MnYbIJmwAafCDuU5qXq2pVLtSmfF+rfhDv0GQUltYTzEjveRVP0WyUJvEf3ZAanmjbnfFvMHsNvRq0TPRB+Cb6Ln4R7sj54lnSPmYaf71KFHWytVMfDsdrH3hYb0tocE5tsYMB+7ZdjHGl2pkU5eyYgqiet9ERXFJwVoNX8d9deWi4l2gKMqdgZ2HRKfcagr3jXduVAUQpr0Q14leUryFPVD9I78wRDH0nqxo5xxKCoa2qJJvZwZW+gzvZx5uZE7pNA5PX/aXUriE3+hgs/93UB8humEnm8olxK+p3QLO7uI+L7VDezugAv/3Cv0jZVDAD7GDha9HFLonDxQ3Uge8IGkqKioqKioqKioqKid/gd0nQoUTq4XqwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH4AAAAYCAYAAAA8jknPAAADwUlEQVR4Xu2Z6YvNURjHn8kS2Y3sImR744UtO1kiW8mWLSXZSkOWEK6lkH3fE7K8sJUolOQFL7yZvPD3eL5zvo9znPsz996Zrrkzzrc+3ea3nGc72++MSHEaQZ4pn5RD5LJSo7QhI5VtSmvSEFlbbeMbVBXpEN8ooL7KJeUbOaacUS6Q3v7Rv8rslmIbcYAtyndxOQM55T6ZbA+XWdPIqvhGIS1SHgR/IxEPlY0EyVsijSv8ODIzvkF1ItvjG0VojPKadOS1QeSV0pPX/iaz2xDbsAe78AFA1slvKnN4rZwaRubGNwopFT4V/rfw9y4yQZmhdCf9xU2xXckAXrPperQyn/RROiuPyWlx7YVqJb6TfRT3XnuCd+cpkwiejZVVePMFNteIb2+6uPbgFzDbsBvaHkrwLKZsPJdlO6vwpqXKc/EDBu0t4C+ALLcAyy5q0Y1MIWY79N9iQLt4F8R5LSgY+6IsIweVG0oXMlxcAnuQPeLWNhQFHBc3qnaQ5eJ7/TlxDuEZsF5cZwmFoGaTe+LaGkhui/MBbYBTkj/rZBXetI9Ysq4q1eLXYdgyu2YbMWHGA+jE8Nk6Zqz6Cm9+rSAYRIjVBhRm0VFKLRkvbkZ8QeDnfvGDKPTfYkA98A7AvZKUNeJDoWfhPoIE2Ow9Euc0mMXrlvwwAZZ4A7ayZIm7wr/xXOiXjdDP/A1VX+Hvik84QPKOKO8J2jK7ZhsyezXKHfH+x6qv8CjWB/GzncUexma5tfzGvljOQOi/xWD+h7krWqnwqfCZiguPqRYbl8Okl9JOeULiwm/mrwUxUfI/n0LnByvrCAoHWSHeipveQmUVvpq8FLee5sgGPmPJtr2DJRu2sY5ae2gDPucIlp9QWYWvIkeVteI/9eLC41ophc+J999iMP8thqLUj1wT9y1qDcTCWlQrfmcOoeedJaax5LyykCA4rNGLyUllpfjkmLA5BFi3sKaab0jeavFnDPAlFDabB5QfBIneqjwl5u8mclzcSHxHcuL2MLbmwzZmMXQYgF05OvcbMlWc0PkBYvwpvmNjI3mLwA+MUtuvXBeXN/yCIeK+vZFbgLZ2K18JOiB8ukgw+5j/FgPOLXYSvFN2oWg2fTYn4dAFm85Cso5ZyqHOv5D5X0wMZVEqfNOoyQuflJRUSbJTtuaC7cITjSMvsZVOHECiYdR9FhQCR6+JP9lbQcSHX8Xw+8ChPvCNXGngu7SpwbdypXCiROr+UfK/sKKZgIOrcpOXnJZMnOBKJS5SOUhKSkpKSkpKSmop+gVUisLUzk0OLQAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAAAYCAYAAAB3JpoiAAAC/klEQVR4Xu3Y6atMcRgH8OdmX7LLrmzhlT2SLNm5du4lSpYoWV7YUshaJKW8sSYJ2Uqk8AdIKPLWO+WF/8Lz7fk+zm9+073N3HvOGPX71qd7z5zfnHl+zznzOzMjUn16q2c0KtrXUjpTJ25PpH2qow9qYyaom/RVXVRX6ItalA3NPagdc/D5FJJZ6hdtjva1FEwapnF7MK2R9jccwXHhpeoZPD5WbQm2806DWqZGUyFJDc9Sk4ZvV4fokZQ3DJPcSJPUCPWWjou99WbSfNVNDadhqo8aSmNUFzWbMLleUp644T5+JP8up6lqrtgx3BK1lLDdT+xCAMxlsdg8ADU1qiHkY1G3wzaWWlgldgxPh+D/itJX7ZLsgB+l9MyiuAuSFfSa4+4SJoWGjKeHYvcEb9B91UPtJjQHJ3YTofgbYicJPN7w7+qyZCcYNWCSK+i92PGa6QCNIxwbJ/w83RKr5zFtELuA7hHGnhNrLGBuT9QxGqgeqAF0WKrMHLGr6Db9VFuD/XfEXjjOdfIlxU8IGowiuxK2J6tthAm9UXsJJxRF43HwxFf4SsJrhPtRQxicNJxIXCTwQuz5eCeCzyWs3+v22n1cONZfD/sxzud7hmMqTmp4jRuO9RtvDc9q9VRsHQd8JAtPgH8UDAtG0+KGe3ATxmO+xuMk4K08gxA0GscET9zwOHHDvV4scwuktJ4p6gTl3fD1HNNqUBiaCJ/E1lovGOv5b7WTsMZizULjYI/Yix6kU2qhZDelb5I1Ehkk9vne1zxkumRrJp6zQ7LXR3CjOk0/xOrEzQwQXMVH6INY/Q10Se2XbE1/p06qV3RNzePzAMdYpz7TWvVcss/9qNXHQaPYHL0fTVJQfIloS7yRYbxBeMfkne5iN9aqP0FUEdx44Wq8I6+khpem8IanlMYvGNwDU2odv8GE+ieFKWt2anix5Gid86/J9cC/ELWHnG0FfieoB/7bRj3wb6Vt9feHoTw1/Sea/4GyZuUhnli9iptRCykpKSkpKSmV5A+j2kOB26ueSAAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAAYCAYAAAAxkDmIAAADj0lEQVR4Xu2Z2avNURTHly4yz0PmKwpJ5iFkyJDhynBNIV1RhmQeSuYxShkjlPCAByJ5oRQPUhQP3vwz1sdey/nd3z3nOod7+F13f+tT93f23muvvdb+7eF3RYrTUOOR8kY5YlxRTiltjYZQc2Wb8VRpV7u4rJquvFfGGvnUXjlofFQuKL2NQhpgXJYQv5FG5rRIuZd4bqZcU/YYDaVeBn39zQSjq1J/ghE+wTOpv57L40P8OiotjMwpJjioySQYJx8qKw1EYuYbLENdlcXGYGWO/Q5MEPDn5VYnmeBREvqFDkoXKWyPZbIq0R5RZ54xRalQ+hjYGK5MNigjwZMM7FEvvQWlE5y0N1By/tI3/t41zivDJIwD8Il+3R4xG6NMM6iDT+4f9fltojFDwtaZjA9y+/xWkmjwVXJ78A3lnNLG6KvcUjobh5WFEvZpoIxA3TYY7BZlg0GS7iuDjE/KBGWmQYBaSV17TDKoVvpJLqA9JNjzCbBe2SjBBlyUsIc69EmCPaAnJOzL6TcunWB/fqwcULobDyRMtJMG/fdUbhqVylplq7FAeaXsNFYpO5QVBhOGdkwC+CJ14+NjBv4uSek3GNUod4wlEhycYayTMCv9UOIziiDCVOWJ1F0S00u0l9MGFbJHHW/nbXneZTCpaOdK2nARwA/G6lSZK51gl/vg5fhA/0l/KX9nEJtqCYmH5BgRNl4qmw1Wq73KECNffLDpE7xkxQQHNakEL5PgBLDEYLiZwbLWSQonhOWFpYREA/KlHvINABWyR51kgtlfSUJXg/rHJXdtyZdgDo1zDcZSWas06E8SzLbE9Q/aS4hTNyM5RsQ2wtYz3kDEs7+RLz7E0ZdorpxFyQ8R1yXMPA5DwP7wWsJBCEgoexm/Q42EveG5cUlyd03YJ+Gw4A5xSGGPZF8C9pgqqwe0mSX121sq4X4K1RICycyHo8oLCZMSsMGYfHwjlLcSfIBjymepfW9tLblD5TflkOQmqPuAz4D/mySsUkBfTNztxnFljTLb8DH6GQCNk9wbWUx8Rks4O8B+KZP8UFKRLiggf+NbpgsaQNhNn4KzIt6wYt6y341P2a5iMcHFqdEmOCoqKioqKurX4tqRNfzaEKmNX/dK4ed3Xed0hjiTAc5mDL79l8LPD9ul4J/+ssruRoL/G7Gc1EleMaQDmjXSgcwq6WSUgx/fQyP/L1FRUVFRUVH/QN8B6wGxv02UQeoAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEoAAAAYCAYAAABdlmuNAAACZ0lEQVR4Xu3Y26sNYRgG8HfHhbNQ2zFnckwicqYQOdw4pGxuUJILpJRTS0LcOd2wlUPKlYgbhyQXlBuUv0H5LzyP9/nMmL2sNd9q1R6776lfab6Z+b55Z+adtZmVyzg5DZ/gmiyCJ/BOzsF1qcFga5z+0C3LCmOtZC68F64tNqtlT3EgNkPgmfkiwkK2wQPJZyk8goFSL1Phi9T+Hmo5N6WVQs2UjcWB2KRClUxMoYbCK1gp9bIZDskbGJ4bY6HXwizhPMNy49NhE6yQftoeCrXEspYxwfxYHkPTYDSskVUwxnw+4twdMF/4OkYlplAMt3GcimF/Omy+YGKPY0G5QJoDX80vmNbBVfO+Rw9hAeyXA+YJhVoMM+SlebE2yHbzfjtR5pkXi3PQLZgNR4XriUpMoXgxr82fGiqGr91zuCPf4FJufKz5OTkncT4WID9+DO7KKW2v9+qdMX/6uoTn2wc/hMfziQrXxeNHwVv5bpFJhWoQvv+8ABph5QvFXvDUfEIqhsXj4x3C87FPcQ76V6GmCNfB84ZXuwaTtE+xUPw3X798G1gOg2QHXNB+YR6+qmEutoamWQgXZT08Nm+6NB5uwwfZaX5n6T5Mtp7hF4U+w67cdt7xn3BWDpr3qK1yEj5a1oB5E9hvzssL8/m5D3H/8MWlbssunLkBe2W3+ZqOCI/fAveEPbJUwl3ttOzr0tvpsOY/aPmE0UjzYvAYYvgxaRReZ37/UkmF6sMZYFnvZNvgz42UlJT/L/zk9yXhz5R2+/Njsh0uV8iVNrPjFXeiInosrGqKC+4tv//fKGkuJSUlpbL5BR7zDB2yLX/MAAAAAElFTkSuQmCC>