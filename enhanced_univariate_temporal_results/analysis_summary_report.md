# Enhanced Univariate Feature Analysis Report (With Temporal Features)

**Generated on:** 2025-10-03 00:37:44
**Target Variable:** MVA_Qualified

## Dataset Overview

- **Total records:** 1,840,739
- **Total features analyzed:** 194
- **Numeric features:** 125
- **Categorical features:** 69
- **Temporal features:** 107
- **Non-temporal features:** 87
- **Engineered features:** 17
- **Original features:** 177
- **Target positive rate:** 4.37%

## Statistical Significance Summary

- **Numeric features with p < 0.05:** 100 / 125 (80.0%)
- **Categorical features with p < 0.05:** 48 / 69 (69.6%)

## Top 15 Temporal Features

| Rank | Feature | Score | Type | AUC | Pattern |
|------|---------|-------|------|-----|----------|
| 1 | Incident_Date_TimeOfDay | 0.832 | Categorical | nan | Other |
| 2 | Incident_Recency_Detailed | 0.784 | Categorical | nan | Other |
| 4 | Incident_Season | 0.730 | Categorical | nan | Seasonal |
| 5 | Inquiry_Start_Date_TimeOfDay | 0.713 | Categorical | nan | Other |
| 6 | Call_Start_Date_TimeOfDay | 0.710 | Categorical | nan | Other |
| 8 | Incident_Recency_Detailed_Unknown | 0.659 | Numeric | 0.948 | Other |
| 9 | Incident_Date_TimeOfDay_Unknown | 0.659 | Numeric | 0.948 | Other |
| 10 | Delayed_Treatment_Risk | 0.659 | Numeric | 0.948 | Risk Score |
| 11 | Incident_Date_TimeOfDay_Night | 0.659 | Numeric | 0.948 | Other |
| 12 | Incident_Within_730_Days | 0.658 | Numeric | 0.943 | Time Window |
| 14 | Call_Season | 0.641 | Categorical | nan | Seasonal |
| 15 | Incident_Within_365_Days | 0.621 | Numeric | 0.902 | Time Window |
| 17 | Case_Urgency_Score | 0.579 | Numeric | 0.739 | Risk Score |
| 19 | Incident_to_Inquiry_Within_30d | 0.550 | Numeric | 0.821 | Time Difference |
| 20 | Incident_to_Call_Within_30d | 0.543 | Numeric | 0.814 | Time Difference |

## Top 20 Non-Temporal Features

### Numeric Features

| Rank | Feature | Score | AUC | KS | Cohen's D | Correlation |
|------|---------|-------|-----|----|-----------|--------------|
| 18 | Multi_Touch_Engagement_Score | 0.576 | 0.857 | 0.694 | -1.497 | -0.427 |
| 36 | Has_Sms_Channel | 0.420 | 0.824 | 0.648 | 1.387 | 0.273 |
| 37 | Channel_Diversity_Index | 0.420 | 0.824 | 0.648 | 1.387 | 0.273 |
| 38 | Has_Web_Channel | 0.419 | 0.823 | 0.647 | 1.383 | 0.272 |
| 39 | Quick_Response | 0.412 | 0.817 | 0.634 | 1.362 | 0.268 |
| 44 | Web Lead Attempt Count | 0.359 | 0.720 | 0.416 | -0.615 | -0.191 |
| 49 | Engagement_Distance_From_LawType_Mean | 0.325 | 0.651 | 0.438 | -0.517 | -0.163 |
| 53 | Law_Type_Frequency | 0.312 | 0.663 | 0.329 | 0.688 | 0.143 |
| 60 | Response_Time_Hours | 0.260 | 0.577 | 0.293 | -0.545 | -0.171 |
| 70 | Is_MVA_Case | 0.239 | 0.685 | 0.370 | 0.775 | 0.156 |

### Categorical Features

| Rank | Feature | Score | IV | Cramér's V | Categories |
|------|---------|-------|----|------------|------------|
| 3 | Consumer At-Fault Flag (Agent) | 0.778 | 2.394 | 0.692 | 3 |
| 7 | Walker Campaign Group | 0.681 | 9.622 | 0.347 | 8 |
| 13 | Data Source | 0.644 | 6.153 | 0.272 | 6 |
| 16 | Consumer Gender | 0.620 | 2.024 | 0.289 | 3 |
| 21 | Retention by Atty | 0.533 | 0.732 | 0.346 | 10 |
| 22 | Shared Law Type | 0.517 | 2.070 | 0.147 | 8 |
| 29 | Uninsured Motorist (UM) Coverage | 0.466 | 0.518 | 0.331 | 3 |
| 40 | Walker Geo Group | 0.401 | 0.527 | 0.158 | 34 |
| 56 | XTM Offer | 0.290 | 0.186 | 0.158 | 87 |
| 61 | Walker Brand | 0.258 | 0.179 | 0.072 | 13 |

## Feature Origin Analysis

| Origin | Count | Mean Score | Std Dev | Median Score |
|--------|-------|------------|---------|-------------|
| Engineered | 17 | 0.251 | 0.168 | 0.239 |
| Original | 55 | 0.218 | 0.178 | 0.184 |
| Temporal | 107 | 0.250 | 0.219 | 0.152 |

## Temporal Patterns Discovered

### Recency Effects

- **Log_Days_Since_Incident**: Score = 0.316
- **Days_Since_Incident_Date**: Score = 0.290
- **Days_Since_Call_Start_Date**: Score = 0.142
- **Days_Since_Inquiry_Start_Date**: Score = 0.139
- **Days_Since_Month_Start_Date**: Score = 0.067

### Cyclical Patterns

- **Hours_Incident_to_Call**: Score = 0.342
- **Hours_Incident_to_Inquiry**: Score = 0.341
- **Incident_Date_DayOfMonth**: Score = 0.187
- **Incident_Date_Month**: Score = 0.186
- **Month_Start_Date_Year**: Score = 0.158

## Recommendations

### Feature Selection

1. **Start with top 50-100 features** based on predictiveness score
2. **Include key temporal features** for time-dependent patterns
3. **Consider temporal interactions** (e.g., recency × injury severity)
4. **Monitor temporal stability** of features over time

### Temporal Considerations

1. **Use time-based validation** to account for temporal dependencies
2. **Create cohort-based features** for different time periods
3. **Monitor for concept drift** in temporal patterns
4. **Consider seasonal adjustments** for cyclical features

### Model Development

1. **Baseline model:** Logistic regression with top features
2. **Time-aware models:** Consider LSTM or temporal transformers
3. **Feature engineering:** Focus on temporal interactions
4. **Validation strategy:** Time-based splits for realistic evaluation
