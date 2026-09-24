# Project Assumptions, Dependencies, Constraints & Limitations

> **Document Reference:** ATS-REF-002  
> **Project:** Enterprise Recruitment & Applicant Tracking Information System Proposal  
> **Author:** Lead Business Systems Analyst  
> **Status:** Approved Baseline Reference  

---

## 1. Executive Purpose

To maintain architectural rigor, risk transparency, and clear operational boundaries, this document records all **foundational assumptions, enterprise dependencies, operational constraints, and technical limitations** underpinning the Recruitment & Applicant Tracking System (ATS) proposal.

---

## 2. Business & Operational Assumptions

1. **Hiring Velocity & Scale:**
   * The enterprise projects an annual hiring volume of **450 to 600 full-time equivalents (FTEs)** across Engineering, Product, Sales, and Corporate Operations over the next 36 months.
   * Total inbound application volume is estimated at **35,000 to 50,000 candidates annually**.
2. **Talent Acquisition Staffing:**
   * The Talent Acquisition team consists of **8 full-time recruiters**, **2 recruiting coordinators**, and **1 talent operations manager**.
   * Recruiter fully loaded labor cost is assumed at **$55.00 / hour** ($114,400 annually).
3. **Current Contingency Agency Reliance:**
   * In the AS-IS baseline, **35% of technical and sales positions** are filled through external contingency recruitment agencies charging an average fee of **20% of first-year base salary**.
   * The proposal assumes an agency reduction target from 35% down to **10%**, achieved through active talent rediscovery and improved inbound career portal conversion.
4. **Stakeholder Adoption & Change Enablement:**
   * Hiring managers will complete mandatory 30-minute training on calibrated rubric evaluation.
   * Executive leadership will enforce an operational policy mandating scorecard submission within **24 hours** of interview completion.

---

## 3. Technical & Architectural Assumptions

1. **Cloud Hosting Environment:**
   * The target production deployment resides within **AWS (us-east-1)** utilizing containerized microservices orchestrated via **AWS ECS with AWS Fargate** (serverless containers).
   * Primary relational storage is hosted on **AWS Aurora PostgreSQL** (multi-AZ replication).
2. **HRIS System of Record:**
   * **Workday HCM** remains the authoritative single source of truth (SSOT) for employee master records, cost center hierarchies, and approved headcount requisitions.
   * The ATS will consume approved requisitions from Workday via bi-directional REST APIs and publish newly hired candidate records upon offer acceptance.
3. **Identity & Access Management:**
   * Enterprise single sign-on (SSO) is federated through **Okta / Microsoft Entra ID** utilizing **SAML 2.0 / OAuth 2.0**.
   * Role-Based Access Control (RBAC) enforces strict least-privilege access across 5 permission tiers (Candidate, Interviewer, Recruiter, Talent Admin, System Admin).
4. **Email & Calendar Infrastructure:**
   * The organization utilizes dual enterprise productivity suites (**Google Workspace** and **Microsoft 365**). The scheduling microservice must support two-way availability checks across both Google Calendar and Microsoft Graph APIs.

---

## 4. Synthetic Data Modeling Assumptions

1. **Dataset Nature:**
   * The operational dataset (`data/recruitment_sample_dataset_anonymized.csv`) consists of **1,250 records** created strictly for demonstration, validation, and analytics telemetry.
   * All names, emails, and identifiers are **100% synthetic and anonymized** to ensure zero Personally Identifiable Information (PII) exposure.
2. **Statistical Distribution Parameters:**
   * Pipeline progression stages are modeled using empirical recruitment funnel conversion rates:
     * *Screening Pass Rate:* 52.0% (simulating automated knockout qualification filtering).
     * *Shortlist Rate:* 28.5% (recruiter curation bar for panel review).
     * *Interview-to-Offer Conversion:* 29.2% (calibrated competency panel selection).
     * *Offer Acceptance Rate:* 75.0% (competitive compensation benchmark).
   * Time-to-Hire values follow a truncated log-normal distribution centered around **23.0 calendar days** (Standard Deviation: 2.1 days).

---

## 5. Compliance & Regulatory Assumptions

1. **Equal Employment Opportunity (EEO-1) & OFCCP Compliance:**
   * Candidate voluntary demographic self-identification data (race, gender, veteran, disability status) is stored in a segregated schema accessible **only** to HR Compliance Officers.
   * Hiring managers and recruiters have zero visibility into EEO demographic data during screening and interview stages to prevent cognitive bias.
2. **Data Privacy (GDPR & CCPA):**
   * Data storage must adhere to GDPR Article 5 principles (data minimization, purpose limitation, storage limitation).
   * The architecture includes automated data retention policies executing automated profile anonymization or erasure after **24 months of candidate inactivity**, unless consent is explicitly renewed.
   * Candidate self-service data export ("Right of Access") and erasure ("Right to be Forgotten") workflows are implemented natively.

---

## 6. Financial & ROI Assumptions

1. **Implementation Capital Expenditure (Capex):**
   * Estimated one-time implementation investment: **$210,000**.
   * Breakdown: Software licenses & cloud provisioning ($65,000), systems integration & API development ($95,000), change management, training & contingency ($50,000).
2. **Ongoing Operational Expenditure (Opex):**
   * Annual recurring cloud hosting, database licensing, and vendor API fees (DocuSign, Twilio, Workday connector maintenance): **$45,000 / year**.
3. **Net Financial Valuation:**
   * Gross annual operational savings: **$570,000**.
   * Net annual recurring benefit (Gross minus Opex): **$525,000 / year**.
   * Payback Period: **7.2 Months** ($\frac{\$210,000}{\$525,000} \times 12$).
   * 3-Year Expected Return on Investment (ROI): **3.4x (340%)**.

---

## 7. Project Scope Boundaries & System Limitations

### Out-of-Scope Boundaries (What the ATS Does NOT Do):
* **Payroll Execution:** The ATS does not manage payroll deductions, direct deposits, or tax withholdings (handled downstream by Workday HCM / ADP).
* **Direct Background Checks:** The system does not conduct criminal or credit background checks natively; it integrates via webhooks with third-party background screening vendors (e.g., Checkr / HireRight).
* **Post-Hire Performance Management:** Probationary tracking, performance reviews, and promotions are out of scope (handled in Workday).
* **IT Asset Provisioning:** Automated laptop imaging and security badge creation are handled downstream via ServiceNow ticketing webhooks triggered on hire event.

### Technical & System Limitations:
* **Resume Parsing OCR Accuracy:** Automated resume parsing assumes standard PDF, DOCX, or RTF formats. Complex multi-column graphic design resumes or image-only scans may exhibit up to a 12% parsing degradation, necessitating manual recruiter review.
* **Multilingual Candidate Submissions:** The Phase 1 MVP is localized for English-language job postings and resumes. Multi-language localization (Spanish, French, German, Japanese) is deferred to Phase 3.
* **High-Concurrency Scale Threshold:** The proposed database architecture supports up to **50,000 active candidates per year** and **500 concurrent recruiter sessions**. Scaling beyond this volume will require database read-replica sharding and ElasticSearch cluster clustering.
