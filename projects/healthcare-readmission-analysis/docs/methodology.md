# Methodology

Full documentation of analytical decisions, statistical methods, risk-score construction, assumptions, and limitations for the Diabetic Patient Readmission Risk Analysis. This document is meant to let someone reproduce or critique every decision made in `analysis.ipynb` without re-deriving it themselves.

## 1. Data Cleaning Decisions

The dataset uses `"?"` as a placeholder for missing values rather than true nulls, so missingness was assessed with `(df == '?').sum()` rather than `df.isnull().sum()`.

| Column | Missing | % of rows | Decision | Rationale |
|---|---|---|---|---|
| `weight` | 98,569 | 96.9% | Dropped | Too sparse to be usable |
| `payer_code` | 40,256 | 39.6% | Dropped | Insurance billing code, not clinically relevant to readmission risk |
| `medical_specialty` | 49,949 | 49.1% | Filled as "Unknown" | Still informative even with ~50% missing |
| `race` | 2,273 | 2.2% | Filled as "Unknown" | Small gap; dropping rows would lose data unnecessarily |
| `diag_1` | 21 | 0.02% | Filled as "Unknown" | Negligible |
| `diag_2` | 358 | 0.35% | Filled as "Unknown" | Negligible |
| `diag_3` | 1,423 | 1.4% | Filled as "Unknown" | Small |

**Rule applied:** columns missing ~70%+ of values were dropped (imputation would be mostly guessing); columns below that threshold were filled with "Unknown" to preserve rows rather than dropping them.

**Encounter vs. patient level:** 101,766 total encounters, 71,518 unique patients (`patient_nbr`) — roughly 30,000 patients had more than one hospital visit. Analysis is conducted at the **encounter level** (each hospital stay is an independent row), matching how CMS and hospitals actually track and penalize readmissions. No deduplication was performed.

## 2. Target Variable Construction

The original `readmitted` column has three values: `NO`, `>30`, `<30`. A binary column `readmitted_30d` was derived: `1` if `<30`, else `0` (covering both `>30` and `NO`).

**Class balance:** 11,357 readmitted within 30 days (11.2%) vs. 90,409 not (88.8%). This is an imbalanced target — kept in mind throughout, since a "2x" rate difference means 2x of an ~11% baseline, not 2x of 50%.

## 3. Diagnosis Recoding

`diag_1`, `diag_2`, `diag_3` contain raw ICD-9 codes, mapped into broad clinical categories (Circulatory, Respiratory, Digestive, Diabetes, Genitourinary, Injury, Musculoskeletal, Neoplasms, Supplemental, External causes, Other) using standard ICD-9 range groupings (e.g., 390–459 → Circulatory). Codes starting with `V` or `E` are handled separately (Supplemental / External causes respectively), matching how ICD-9 itself distinguishes them from numeric disease codes.

**Limitation:** collapsing hundreds of specific codes into ~10 categories necessarily hides variation between individual diagnoses within a category (e.g., a minor arrhythmia and severe heart failure both fall under "Circulatory").

## 4. Confidence Interval Methodology

All 95% confidence intervals in this project use the **normal (Wald) approximation to the binomial proportion**:

```
CI = p ± 1.96 × sqrt(p(1-p) / n)
```

where `p` is the observed readmission rate and `n` is the number of encounters in that group. This is the standard, widely-used approximation and is appropriate here because sample sizes are large for most groups (n > 1,000). For the two smallest groups (risk scores 6 and 7, n=369 and n=237), the Wald approximation is less precise than alternatives like the Wilson score interval, and the resulting intervals should be read as directionally correct but approximate — they are wide enough (24.4–33.6% and 29.8–42.0% respectively) that the point estimate alone should not be over-trusted at that sample size.

**Age × prior-visits interaction cells:** unlike the single-variable groupbys above, this cross-tab required pulling cell-level counts separately (they aren't shown in a `pivot_table` built with `aggfunc='mean'` alone). The two cells behind the age-interaction finding:

- Ages 20–30, 3+ prior visits: 41.57% (95% CI: 35.52–47.62%, n=255)
- Ages 90–100, 3+ prior visits: 17.86% (95% CI: 11.52–24.20%, n=140)

Both are among the smallest cells in the analysis, so the intervals are wide — but they do not overlap (20–30's lower bound of 35.5% is still above 90–100's upper bound of 24.2%), so the interaction effect holds even accounting for that uncertainty. Code used to extract the counts:

```python
cross_tab_counts = df_clean.groupby(['age', 'prior_visits_bucket'], observed=True)['readmitted_30d'].agg(['mean', 'count'])
cross_tab_counts['mean'] = (cross_tab_counts['mean'] * 100).round(2)
print(cross_tab_counts)
```

## 5. Risk Score Construction

The 0–7 point risk score was built by hand from the groupby/pivot findings in Sections 4–5 of the notebook — it is **not a fitted or trained model**. Every threshold was chosen because it was visibly where the observed readmission rate stepped up in the underlying tables.

| Factor | Condition | Points |
|---|---|---|
| Prior inpatient visits | 3+ prior | +3 |
| | 2 prior | +2 |
| | 1 prior | +1 |
| | 0 prior | +0 |
| Medication count | 16–20 or 21+ | +2 |
| | 11–15 | +1 |
| | 0–5 or 6–10 | +0 |
| Age × prior visits interaction | Age 20–30 or 30–40 **and** 2+ or 3+ prior visits | +2 |
| | Otherwise | +0 |

**Why these specific weights:**
- Prior-visits weights (0/1/2/3) mirror the four groupby buckets directly, since that variable had the largest observed rate spread (8.44% → 25.66%).
- Medication weights collapse five buckets into three tiers, breaking at 11 and 16 medications — the two points where the groupby table showed a visible step up in rate.
- The age-interaction bonus applies only to the two age brackets (20–30, 30–40) where the interaction with prior visits was strongest in the cross-tab, so as not to overstate an effect that was much weaker at other ages.

**Why validation is exploratory, not confirmatory:** the score was checked by grouping encounters by score and confirming readmission rate rose monotonically (6.88% → 35.86%). This is **not out-of-sample validation**. The rules were derived from patterns in this dataset, then checked against that same dataset — a rule built to track an observed pattern will, unsurprisingly, track it. This confirms *internal consistency*, not that the score would generalize to new patients, a different hospital system, or a different time period. Genuine validation would require a held-out test set or an external dataset, which was intentionally out of scope for this project.

## 6. Assumptions

- Encounter-level analysis (not patient-level) is the appropriate unit for readmission tracking, matching CMS methodology.
- The `readmitted == '<30'` flag is a reliable ground-truth label for 30-day readmission (as provided by the original dataset curators).
- ICD-9 category groupings using standard clinical range definitions are a reasonable simplification for exploratory analysis, despite hiding within-category variation.
- Observed associations in this dataset (1999–2008, US hospitals) are treated as descriptive findings about *this population*, not causal claims or generalizable predictions.

## 7. Limitations

- Data spans **1999–2008** and may not reflect current clinical practice, medications, or patient populations.
- Analysis is **descriptive and rule-based**, not predictive modeling — associations shown do not establish causation.
- The risk score has **not been validated on held-out or external data** (see Section 5).
- ICD-9 codes are grouped into broad categories, hiding differences between individual diagnoses.
- The age × prior-visits interaction (41.57% vs 17.86%) is based on small cells (n=255 and n=140), giving wide confidence intervals; the finding holds since the intervals don't overlap, but should be treated as less precise than the larger single-variable findings.
- Smaller segments (age 20–30, n=1,657; risk scores 6–7, n=369/237) carry wider uncertainty and should be read with appropriate caution, as reflected in their wider confidence intervals.