# Diabetic Patient Readmission Risk Analysis

A pandas-driven analysis of 30-day hospital readmission patterns in diabetic patients using real-world EHR data. The project investigates which patient, utilization, and clinical factors are most strongly associated with 30-day readmission and uses these findings to develop an exploratory, transparent, rule-based risk-scoring system — without machine learning.

## Problem

Hospital readmissions within 30 days are an important healthcare quality and cost concern in the United States and are addressed through programs such as the CMS Hospital Readmissions Reduction Program.

This project asks:

* Which patient, utilization, and clinical factors are associated with higher 30-day readmission rates among diabetic patients?
* How do combinations of factors affect observed readmission rates?
* Can descriptive analysis be used to identify patient segments with comparatively higher observed readmission rates?
* Can these findings be translated into a transparent, rule-based risk score?

The analysis is designed to demonstrate practical healthcare data analysis using Python and pandas rather than machine-learning prediction.

## Dataset

* **Source:** [Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) — UCI Machine Learning Repository
* **Size:** Approximately 101,766 hospital encounters
* **Features:** 50 variables
* **Data type:** Hospital encounter-level EHR data
* **Time period:** 1999–2008

The dataset contains information including:

* Demographics
* Admission and discharge details
* Previous inpatient and emergency visits
* Length of hospital stay
* Diagnoses using ICD-9 codes
* Laboratory procedures
* Medications
* Number of medications
* Diabetes-related information
* Readmission outcome

The raw dataset is **not included in this repository**. Download `diabetic_data.csv` from the UCI link above and place it in the `data/` folder before running the analysis.

### 30-Day Readmission Definition

The dataset contains three values for the `readmitted` variable:

* `<30` — readmitted within 30 days
* `>30` — readmitted after 30 days
* `NO` — not readmitted

For the primary analysis, an encounter is classified as a **30-day readmission** when:

```text
readmitted == "<30"
```

Encounters with `>30` or `NO` are treated as **not readmitted within 30 days** for this specific analysis.

## Tech Stack

* **Python 3.x**
* **pandas** — data cleaning, transformation, grouping and analysis
* **NumPy** — numerical operations
* **Matplotlib** — data visualization
* **Seaborn** — statistical visualization
* **openpyxl** — Excel report generation
* **Jupyter Notebook** — exploratory analysis

## Repository Structure

```text
diabetic-readmission-analysis/
│
├── data/
│   └── diabetic_data.csv        # Download separately from UCI
│
├── notebooks/
│   └── analysis.ipynb           # Main analysis notebook
│
├── outputs/
│   ├── readmission_summary.xlsx # Excel summary tables
│   └── figures/                 # Generated visualizations
│
├── requirements.txt
└── README.md
```

## Methodology

### 1. Data Profiling and Cleaning

The dataset is first examined for:

* Missing values
* `?` placeholders
* Duplicate records
* Inconsistent categorical values
* Data types and column structure
* Distribution of important variables

Missing-value indicators such as `?` are converted into appropriate missing-value representations before analysis.

Duplicate records are checked rather than automatically removing repeated patient encounters, since the dataset contains legitimate multiple hospital encounters for the same patient.

### 2. Readmission Outcome Construction

A binary 30-day readmission variable is created:

```text
1 → readmitted within 30 days
0 → not readmitted within 30 days
```

This allows readmission rates to be calculated consistently across different patient and encounter groups.

### 3. Clinical Diagnosis Recoding

The raw ICD-9 diagnosis codes are grouped into broader clinical categories to make the analysis easier to interpret.

Example categories include:

* Circulatory
* Respiratory
* Digestive
* Diabetes
* Genitourinary
* Injury
* Musculoskeletal
* Neoplasms
* Other

The analysis documents the coding rules used to convert diagnosis codes into these broader categories.

### 4. Readmission Rate Analysis

Pandas `groupby()` operations are used to compare 30-day readmission rates across variables such as:

* Age group
* Number of previous inpatient visits
* Number of emergency visits
* Number of outpatient visits
* Length of stay
* Number of medications
* Primary diagnosis category
* Other relevant encounter characteristics

The primary metric is:

```text
30-Day Readmission Rate =
Number of encounters readmitted within 30 days
------------------------------------------------
Total encounters in the group
```

### 5. Multi-Variable Analysis

Cross-tabulations and grouped analyses are used to examine how combinations of variables relate to observed readmission rates.

Examples include:

* Age × medication count
* Age × previous inpatient visits
* Diagnosis category × previous inpatient visits
* Length of stay × previous admission history

This helps identify whether certain combinations of characteristics are associated with particularly high observed readmission rates.

### 6. Exploratory Rule-Based Risk Score

An exploratory rule-based scoring system is developed from factors that show relatively higher observed 30-day readmission rates in the analysis.

Each selected factor contributes a predefined number of points according to the observed pattern.

The resulting score is used to categorize encounters into exploratory groups such as:

* Lower observed risk
* Moderate observed risk
* Higher observed risk

The scoring system is intended to demonstrate how descriptive findings can be translated into a simple and interpretable analytical framework.

**Important:** This score is an exploratory analytical tool derived from associations observed in this dataset. It is **not a clinically validated risk prediction model** and should not be used for real-world clinical decision-making.

## Key Findings

*This section will be updated after the analysis is completed.*

* **Finding 1:** TBD
* **Finding 2:** TBD
* **Finding 3:** TBD

### Risk Segments Identified

*To be completed after the rule-based scoring analysis.*

The final analysis will describe the patient/encounter segments with the highest observed 30-day readmission rates and explain which factors contributed to their classification.

## Visualizations

The analysis will include visualizations such as:

* 30-day readmission rate by age group
* Readmission rate by previous inpatient visits
* Readmission rate by length of stay
* Readmission rate by medication count
* Readmission rate by diagnosis category
* Heatmaps showing combinations of important factors
* Comparison of readmission rates across exploratory risk groups

Generated figures will be stored in:

```text
outputs/figures/
```

## Excel Report

Key analysis results will be exported to a formatted Excel workbook for easier interpretation by non-technical users.

The workbook will contain summary tables such as:

* Overall readmission rate
* Readmission rate by age
* Readmission rate by prior admission history
* Readmission rate by diagnosis category
* Multi-variable comparison tables
* Exploratory risk-segment summary

The final report will be saved as:

```text
outputs/readmission_summary.xlsx
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/diabetic-readmission-analysis.git
cd diabetic-readmission-analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the dataset

Download the dataset from the UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008

Place the downloaded file here:

```text
data/diabetic_data.csv
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/analysis.ipynb
```

and run the notebook from beginning to end.

## Limitations

* The dataset covers hospital encounters from **1999–2008**, so the findings may not reflect current clinical practices, medications, healthcare systems, or patient populations.
* The analysis is **descriptive and rule-based**, not a machine-learning prediction model.
* Observed associations do not establish causation.
* The dataset contains multiple encounters for some patients. Therefore, the primary analysis is **encounter-level rather than patient-level**.
* The exploratory risk score has not been clinically validated or externally tested.
* ICD-9 diagnosis codes are grouped into broad categories, which may hide differences between individual diagnoses.
* Missing values and unknown categories may affect some analyses.
* Results from this dataset should not be interpreted as clinical recommendations or used for patient-level medical decision-making.

## Project Goal

The main goal of this project is to demonstrate how healthcare EHR data can be cleaned, analyzed, visualized, and translated into interpretable insights using Python and pandas.

Rather than relying on a black-box machine-learning model, the project focuses on understanding the underlying data and building an analytical workflow that can be explained step by step.

**Tools:** Python · pandas · NumPy · Matplotlib · Seaborn · openpyxl · Jupyter Notebook

