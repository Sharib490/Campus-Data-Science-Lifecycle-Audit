# 🎓 Campus Data Science Lifecycle Audit

## 📊 Project Overview

An end-to-end Data Science project that analyzes a college admission process using **2,000 cleaned student admission records**.

The project follows the complete Data Science lifecycle:

**Data Collection → Data Quality Audit → Data Cleaning → EDA → PostgreSQL → SQL Analysis → Power BI → Insights → Recommendations**

The objective is to understand the admission funnel, identify data-quality problems, evaluate student eligibility, analyze course demand, measure admission conversion, and identify process bottlenecks.

---

## 🎯 Project Objective

The project analyzes the college admission process to identify:

- Data quality problems
- Student eligibility patterns
- Course demand
- Admission conversion
- Process bottlenecks
- Enquiry-source performance
- Academic performance trends
- Opportunities to improve the admission process

---

# 📌 Project at a Glance

| Metric | Result |
|---|---:|
| Total Cleaned Records | **2,000** |
| Original Raw Records | **2,020** |
| Duplicate Records Identified | **20** |
| Duplicate Records Removed | **20** |
| Eligible Students | **1,083** |
| Eligibility Rate | **54.15%** |
| Confirmed Admissions | **601** |
| Admission Conversion Rate | **30.05%** |
| Eligible-to-Admission Conversion | **55.49%** |
| Average PCM Percentage | **76.03%** |
| Average CET Percentile | **73.48** |
| Average Processing Time | **13.82 days** |

> **Admission Conversion Rate = Confirmed Admissions ÷ Total Cleaned Records × 100**

---

# 🔍 Data Quality Audit

The raw admission dataset was evaluated for practical data-quality problems.

| Data Quality Issue | Records Affected | Action |
|---|---:|---|
| Missing Values | **1,453 rows** | Handled based on business meaning |
| Duplicate Application IDs | **20 IDs / 20 duplicate records removed** | Removed duplicate applications |
| Invalid PCM Percentage | **15** | Corrected/validated |
| Invalid CET Scores | **10** | Corrected/validated |
| Inconsistent Gender | **41** | Standardized |
| Inconsistent Category | **35** | Standardized |
| Invalid Date Logic | **2** | Validated/corrected |
| Negative Processing Days | **0** | No negative values found |
| Business Rule Issues | **57** | Validated and corrected |

## Data Quality Improvement

**Before Cleaning:** 2,020 records

**After Cleaning:** 2,000 records

**Duplicate Records Removed:** 20

**Data Reduction:** 0.99%

---

# 🧹 Data Cleaning

Python and Pandas were used to perform:

- Duplicate removal
- Missing-value analysis
- Numerical validation
- Categorical standardization
- Date validation
- Academic score validation
- Eligibility recalculation
- Processing-time validation
- Business-rule validation

## Eligibility Rule

A student is considered eligible when:

```text
PCM Percentage >= 75%
AND
CET Percentile >= 60
```

Eligibility was recalculated using the above business rule rather than relying blindly on the original eligibility column.

## Cleaning Results

After applying the cleaning and validation process:

- **2,000 unique admission records** remained
- Gender values were standardized to `Male` and `Female`
- Category values were standardized to `Open`, `OBC`, `SC`, `ST`, and `EWS`
- Invalid PCM values were corrected
- Invalid CET scores were corrected
- Eligibility status was recalculated
- Duplicate applications were removed
- Business-rule inconsistencies were identified and corrected

---

# 📈 Exploratory Data Analysis

## Student Eligibility

Out of **2,000 students**:

- **1,083 students were eligible**
- **917 students were not eligible**
- Overall eligibility rate = **54.15%**

This indicates that slightly more than half of the applicants satisfied the defined academic eligibility criteria.

---

## 🎓 Course Demand

| Course | Applications |
|---|---:|
| Computer Engineering | **556** |
| Artificial Intelligence & Data Science | **459** |
| Information Technology | **456** |
| Electronics Engineering | **298** |
| Mechanical Engineering | **231** |

### Key Finding

**Computer Engineering** received the highest number of applications with **556 applications**, making it the most demanded course.

Artificial Intelligence & Data Science and Information Technology also showed strong demand, with **459** and **456 applications** respectively.

---

# 📊 Admission Conversion

There were:

**2,000 total applications → 601 confirmed admissions**

Therefore:

```text
Admission Conversion Rate
= 601 / 2,000 × 100
= 30.05%
```

Among eligible students:

```text
Eligible-to-Admission Conversion
= 601 / 1,083 × 100
= 55.49%
```

This indicates that approximately **55.5% of eligible applicants ultimately converted into confirmed admissions**.

---

# 📚 Course-wise Admission Performance

| Course | Confirmed Admissions | Conversion Rate |
|---|---:|---:|
| Mechanical Engineering | **76** | **32.90%** |
| Electronics Engineering | **91** | **30.54%** |
| Computer Engineering | **168** | **30.22%** |
| Information Technology | **133** | **29.17%** |
| Artificial Intelligence & Data Science | **133** | **28.98%** |

### Key Finding

Although **Computer Engineering** had the highest application volume, **Mechanical Engineering** recorded the highest course-level conversion rate at approximately **32.90%**.

---

# 📣 Enquiry Source Analysis

| Enquiry Source | Applications | Conversion Rate |
|---|---:|---:|
| College Visit | **274** | **32.85%** |
| Friend/Family | **319** | **31.03%** |
| Social Media | **264** | **30.68%** |
| Google Search | **293** | **30.03%** |
| College Website | **284** | **29.23%** |
| Advertisement | **278** | **28.78%** |
| Education Portal | **288** | **27.78%** |

### Key Finding

**College Visit** generated the highest admission conversion rate at approximately **32.85%**.

This suggests that direct interaction with prospective students may be more effective at converting enquiries into admissions than some digital channels.

---

# 📄 Document Verification Analysis

| Document Status | Students |
|---|---:|
| Verified | **1,135** |
| Pending | **420** |
| Incomplete | **340** |
| Not Submitted | **105** |

### Key Finding

Although **1,135 students had verified documents**, a significant number of applicants were still in pending, incomplete, or not-submitted document stages.

This represents a potential bottleneck in the admission process.

---

# ⏱️ Processing Time

The average processing time for confirmed admissions was:

**13.82 days**

The median processing time was:

**14 days**

This metric can be used by the admission team to monitor operational efficiency and identify applications that take significantly longer than the normal processing period.

---

# 🗄️ PostgreSQL Database

After cleaning, the dataset was loaded into **PostgreSQL** for structured storage and SQL-based analysis.

## Database Workflow

```text
Clean CSV
    ↓
PostgreSQL Database
    ↓
SQL Queries
    ↓
Aggregations & KPIs
    ↓
Power BI
```

PostgreSQL was used to perform:

- Filtering
- Aggregation
- `GROUP BY` analysis
- Admission funnel analysis
- Course-wise analysis
- Enquiry-source analysis
- Eligibility analysis
- Processing-time analysis

## Example SQL

```sql
SELECT
    course,
    COUNT(*) AS total_applications,
    SUM(
        CASE
            WHEN admission_status = 'Confirmed'
            THEN 1
            ELSE 0
        END
    ) AS confirmed_admissions
FROM admission_data
GROUP BY course
ORDER BY total_applications DESC;
```

---

# 📊 Power BI Dashboard

Power BI was used to create an interactive admission analytics dashboard.

## Key KPIs

- Total Applications
- Eligible Students
- Eligibility Rate
- Confirmed Admissions
- Admission Conversion Rate
- Average PCM Percentage
- Average CET Percentile
- Average Processing Days

## Recommended Visualizations

### 1. KPI Cards

- Total Applications
- Eligible Students
- Confirmed Admissions
- Conversion Rate

### 2. Admission Funnel

```text
Applications
      ↓
Eligible
      ↓
Documents Verified
      ↓
Seats Allocated
      ↓
Fees Paid
      ↓
Admission Confirmed
```

### 3. Course Demand

Bar chart showing applications by course.

### 4. Enquiry Source Performance

Column/bar chart comparing admission conversion across enquiry sources.

### 5. Admission Trend

Monthly line chart showing confirmed admissions over time.

### 6. Document Status

Chart showing:

- Verified
- Pending
- Incomplete
- Not Submitted

### 7. Academic Performance

Charts showing:

- PCM percentage distribution
- CET percentile distribution
- Eligibility by academic performance

---

# 💡 Key Business Insights

### 1. Eligibility

Only **54.15%** of applicants met the defined eligibility criteria.

This indicates that a significant proportion of enquiries/applications do not qualify based on academic criteria.

### 2. Admission Conversion

The overall admission conversion rate was **30.05%**.

Among eligible students, the conversion rate increased to **55.49%**, showing that eligibility is an important factor in predicting admission outcomes.

### 3. Course Demand

**Computer Engineering** was the most popular course with **556 applications**.

### 4. Enquiry Source

**College Visit** achieved the strongest conversion rate at **32.85%**.

### 5. Document Bottleneck

There were **865 students** whose documents were either pending, incomplete, or not submitted.

This indicates a significant opportunity to improve document collection and verification.

### 6. Processing Time

Confirmed admissions required an average of **13.82 days** to process.

Reducing processing time could improve the overall student admission experience.

---

# 🚧 Admission Process Bottlenecks

The analysis highlights several possible bottlenecks.

## Document Verification

Pending, incomplete, and not-submitted documents represent a major operational challenge.

## Eligibility Filtering

With only **54.15%** of applicants eligible, early eligibility screening could reduce unnecessary processing.

## Conversion Gap

Although **1,083 students were eligible**, only **601** ultimately confirmed admission.

This creates an eligible-to-admission gap of:

**482 students**

Further analysis of enquiry source, document status, seat allocation, and fee status can help identify why eligible applicants do not convert.

---

# 🎯 Recommendations

Based on the analysis, the following actions can improve the admission process.

### 1. Introduce Early Eligibility Screening

Automatically evaluate:

```text
PCM >= 75%
AND
CET Percentile >= 60
```

at the initial application stage.

### 2. Improve Document Follow-ups

Create automated reminders for students with:

- Pending documents
- Incomplete documents
- Not Submitted documents

### 3. Focus on High-Converting Sources

College Visits and Friend/Family referrals showed strong conversion performance.

The college can evaluate increasing investment in these channels.

### 4. Improve Digital Conversion

Education Portal and Advertisement channels showed comparatively lower conversion rates.

The college should analyze lead quality from these sources and optimize targeting.

### 5. Monitor Processing Time

Set an operational target for admission processing and monitor applications exceeding the target.

### 6. Course Planning

Use course demand data to support:

- Seat allocation
- Faculty planning
- Marketing campaigns
- Infrastructure planning

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Data cleaning and analysis |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical processing |
| **Matplotlib / Seaborn** | Data visualization |
| **PostgreSQL** | Database storage |
| **SQL** | Data analysis |
| **Power BI** | Interactive dashboard |
| **Excel / CSV** | Data source and validation |
| **GitHub** | Project documentation and version control |

---

# 🔄 End-to-End Data Science Workflow

```text
                 RAW DATA
                    ↓
            DATA COLLECTION
                    ↓
          DATA QUALITY AUDIT
                    ↓
             DATA CLEANING
                    ↓
           ELIGIBILITY LOGIC
                    ↓
                  EDA
                    ↓
             POSTGRESQL
                    ↓
              SQL ANALYSIS
                    ↓
              POWER BI
                    ↓
               INSIGHTS
                    ↓
            RECOMMENDATIONS
```

---

# 📁 Project Structure

```text
Campus-Data-Science-Lifecycle-Audit/
│
├── data/
│   ├── campus_admission_raw.csv
│   └── campus_admission_cleaned.csv
│
├── notebooks/
│   ├── data_quality_audit.ipynb
│   ├── data_cleaning.ipynb
│   └── exploratory_data_analysis.ipynb
│
├── sql/
│   └── admission_analysis.sql
│
├── powerbi/
│   └── admission_dashboard.pbix
│
├── outputs/
│   ├── admission_analysis.csv
│   └── charts/
│
└── README.md
```

---

# 📌 Final Project Outcome

This project demonstrates an end-to-end approach to solving a real-world business problem using Data Science.

The project covers:

- ✅ Data Quality Auditing
- ✅ Data Cleaning
- ✅ Business Rule Validation
- ✅ Exploratory Data Analysis
- ✅ Python & Pandas
- ✅ PostgreSQL
- ✅ SQL Analysis
- ✅ Power BI Dashboard Development
- ✅ KPI Development
- ✅ Admission Funnel Analysis
- ✅ Business Insights
- ✅ Data-Driven Recommendations

The final analysis transformed **2,020 raw records into 2,000 validated records**, identified **20 duplicate records**, calculated eligibility for **1,083 students**, and identified **601 confirmed admissions**.

The project demonstrates how raw operational data can be transformed into meaningful insights that support **admission planning, process optimization, marketing decisions, and management reporting**.

---

## 👤 Author

**Sharib khan**

Data Analytics / Data Science Project

---

## ⭐ Project Highlights

**2,020 Raw Records → 2,000 Clean Records → 1,083 Eligible Students → 601 Confirmed Admissions**

**Python + SQL + PostgreSQL + Power BI**
