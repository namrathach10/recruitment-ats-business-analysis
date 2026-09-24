# Synthetic Recruitment Dataset Documentation

**File Name:** `recruitment_sample_dataset_anonymized.csv`  
**Record Count:** 1,250 Historical Application Records  
**Data Class:** Synthetic Portfolio Benchmark Data (Anonymized)  
**Schema Compliance:** ANSI SQL & ISO 8601 Date Formatting  

---

## 🔒 Data Anonymization & Privacy Notice

> **Important Disclosure:**  
> To protect personal privacy and adhere to data protection best practices (GDPR / CCPA), this dataset is entirely **synthetic and fully anonymized**.
> 
> * **No Personally Identifiable Information (PII):** Candidate names have been replaced with standardized identifiers (`Candidate_0001` through `Candidate_1250`).
> * **Synthetic Email Addresses:** All email fields follow the format `candidate_xxxx@example.com` (using the RFC 2606 reserved `.example.com` domain).
> * **Empirical Modeling Purpose:** The operational metrics (application stages, knockout results, stage progression dates, interview scores, and salary distributions) were generated using statistical distributions modeled on enterprise recruitment benchmarks to validate the ATS proposal's business case and Power BI analytics models.

---

## 📊 Dataset Schema & Column Definitions

| Column Name | Data Type | Description | Domain / Sample Values |
| :--- | :--- | :--- | :--- |
| `application_id` | String | Unique tracking code for application instance | `APP-2026-1001` to `APP-2026-2250` |
| `candidate_id` | String | Unique master identifier for candidate | `CAND-0001` to `CAND-1250` |
| `candidate_name` | String | Anonymized candidate reference label | `Candidate_0001` to `Candidate_1250` |
| `email` | String | Anonymized contact email | `candidate_0001@example.com` |
| `department` | String | Hiring business unit | `Engineering`, `Product`, `Sales & Marketing`, `Operations`, `Finance & HR` |
| `job_title` | String | Formal role title applied for | `Senior Systems Software Engineer`, `Product Operations Associate`, etc. |
| `job_id` | String | Requisition identifier reference | `JOB-ENG-104`, `JOB-SAL-102`, etc. |
| `recruiter_name` | String | Assigned talent acquisition specialist | `Sarah Jenkins`, `Michael Chang`, `Elena Rostova`, `Marcus Brody` |
| `hiring_manager` | String | Functional department hiring lead | `David Vance`, `Rachel Adams`, `Julian Hayes`, `Karen Patel`, `Simon Sterling` |
| `source_channel` | String | Attribution acquisition source | `LinkedIn`, `Indeed`, `Career Portal`, `Employee Referral`, `Recruitment Agency` |
| `applied_date` | Date | Initial application submission timestamp | `2026-01-05` to `2026-05-25` |
| `knockout_passed` | Boolean | Pre-screening qualification filter result | `True`, `False` |
| `screened_date` | Date | Resume triage completion date | ISO 8601 Date |
| `shortlisted_date`| Date | Hiring manager shortlist approval date | ISO 8601 Date |
| `interview_date` | Date | Panel interview completion date | ISO 8601 Date |
| `interview_score`| Float | Consolidated rubric evaluation score | `1.0` to `5.0` (Avg: `4.5` for hires) |
| `offer_date` | Date | Formal employment offer extended date | ISO 8601 Date |
| `offer_status` | String | Final disposition of employment offer | `ACCEPTED`, `DECLINED`, `N/A` |
| `hired_date` | Date | Candidate e-signature execution date | ISO 8601 Date |
| `current_stage` | String | Final recruitment pipeline stage reached | `APPLIED`, `SCREENED`, `SHORTLISTED`, `INTERVIEW`, `OFFER`, `HIRED` |
| `application_status`| String | Final application status flag | `HIRED`, `REJECTED`, `DISQUALIFIED`, `DECLINED` |
| `time_to_hire_days` | Integer | Elapsed days from application to hire | `20` to `28` days (Average: `23.0` days) |
| `salary_offered` | Integer | Approved base salary in USD | `$95,000` to `$185,000` |

---

## 📈 Cohort Benchmark Summary

* **Total Applications:** 1,250
* **Applications Screened:** 650 (52.0%)
* **Candidates Shortlisted:** 185 (14.8%)
* **Interviews Conducted:** 96 (7.68%)
* **Formal Offers Extended:** 28 (2.24%)
* **Confirmed Hires:** 21 (75.0% Offer Acceptance Rate)
* **Average Time-to-Hire:** **23.0 Calendar Days** (Legacy baseline: 46.5 days)
