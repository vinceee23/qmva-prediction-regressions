# Temporal Feature Analysis Summary

**Generated on:** 2025-10-03 00:37:44
**Total temporal features analyzed:** 107

## Top 20 Temporal Features by Predictiveness

| Rank | Feature | Score | Type | AUC | Correlation | Key Pattern |
|------|---------|-------|------|-----|-------------|-------------|
| 1 | Incident_Date_TimeOfDay | 0.832 | Categorical | nan | nan | Other |
| 2 | Incident_Recency_Detailed | 0.784 | Categorical | nan | nan | Other |
| 4 | Incident_Season | 0.730 | Categorical | nan | nan | Seasonal |
| 5 | Inquiry_Start_Date_TimeOfDay | 0.713 | Categorical | nan | nan | Other |
| 6 | Call_Start_Date_TimeOfDay | 0.710 | Categorical | nan | nan | Other |
| 8 | Incident_Recency_Detailed_Unknown | 0.659 | Numeric | 0.948 | 0.522 | Other |
| 9 | Incident_Date_TimeOfDay_Unknown | 0.659 | Numeric | 0.948 | 0.522 | Other |
| 10 | Delayed_Treatment_Risk | 0.659 | Numeric | 0.948 | 0.522 | Risk Score |
| 11 | Incident_Date_TimeOfDay_Night | 0.659 | Numeric | 0.948 | 0.522 | Other |
| 12 | Incident_Within_730_Days | 0.658 | Numeric | 0.943 | 0.543 | Time Window |
| 14 | Call_Season | 0.641 | Categorical | nan | nan | Seasonal |
| 15 | Incident_Within_365_Days | 0.621 | Numeric | 0.902 | 0.530 | Time Window |
| 17 | Case_Urgency_Score | 0.579 | Numeric | 0.739 | 0.425 | Risk Score |
| 19 | Incident_to_Inquiry_Within_30d | 0.550 | Numeric | 0.821 | 0.511 | Time Difference |
| 20 | Incident_to_Call_Within_30d | 0.543 | Numeric | 0.814 | 0.506 | Time Difference |
| 23 | Incident_to_Inquiry_Within_14d | 0.514 | Numeric | 0.781 | 0.497 | Time Difference |
| 24 | Incident_to_Call_Within_14d | 0.508 | Numeric | 0.775 | 0.492 | Time Difference |
| 25 | Incident_to_Inquiry_Within_7d | 0.478 | Numeric | 0.743 | 0.479 | Time Difference |
| 26 | Incident_to_Call_Within_7d | 0.473 | Numeric | 0.738 | 0.475 | Time Difference |
| 27 | Inquiry_Start_Date_TimeOfDay_Unknown | 0.469 | Numeric | 0.823 | 0.272 | Other |

## Temporal Pattern Analysis


### Recency Features (9 features)

- **Average Predictiveness Score:** 0.196
- **Average AUC:** 0.577
- **Top Feature:** Days_Incident_to_Call

**Top 5 Recency Features:**
- Days_Incident_to_Call (Score: 0.342)
- Days_Incident_to_Inquiry (Score: 0.341)
- Log_Days_Since_Incident (Score: 0.316)
- Days_Since_Incident_Date (Score: 0.290)
- Days_Since_Call_Start_Date (Score: 0.142)

### Cyclical Features (37 features)

- **Average Predictiveness Score:** 0.097
- **Average AUC:** 0.517
- **Top Feature:** Hours_Incident_to_Call

**Top 5 Cyclical Features:**
- Hours_Incident_to_Call (Score: 0.342)
- Hours_Incident_to_Inquiry (Score: 0.341)
- Incident_Date_Quarter (Score: 0.187)
- Incident_Date_DayOfMonth (Score: 0.187)
- Incident_Date_Month (Score: 0.186)

### Binary Time Windows (20 features)

- **Average Predictiveness Score:** 0.380
- **Average AUC:** 0.685
- **Top Feature:** Incident_Within_730_Days

**Top 5 Binary Time Windows:**
- Incident_Within_730_Days (Score: 0.658)
- Incident_Within_365_Days (Score: 0.621)
- Incident_to_Inquiry_Within_30d (Score: 0.550)
- Incident_to_Call_Within_30d (Score: 0.543)
- Incident_to_Inquiry_Within_14d (Score: 0.514)

### MVA Specific (5 features)

- **Average Predictiveness Score:** 0.405
- **Average AUC:** 0.723
- **Top Feature:** Delayed_Treatment_Risk

**Top 5 MVA Specific:**
- Delayed_Treatment_Risk (Score: 0.659)
- Case_Urgency_Score (Score: 0.579)
- In_Optimal_Window (Score: 0.437)
- Statute_Risk_Score (Score: 0.300)
- Emergency_Treatment_Window (Score: 0.050)

### Time Differences (16 features)

- **Average Predictiveness Score:** 0.408
- **Average AUC:** 0.702
- **Top Feature:** Incident_to_Inquiry_Within_30d

**Top 5 Time Differences:**
- Incident_to_Inquiry_Within_30d (Score: 0.550)
- Incident_to_Call_Within_30d (Score: 0.543)
- Incident_to_Inquiry_Within_14d (Score: 0.514)
- Incident_to_Call_Within_14d (Score: 0.508)
- Incident_to_Inquiry_Within_7d (Score: 0.478)

## Recommendations for Temporal Features

1. **High-value recency features:**
   - Log_Days_Since_Incident: Indicates strong time-dependency
   - Days_Since_Incident_Date: Indicates strong time-dependency
   - Days_Since_Call_Start_Date: Indicates strong time-dependency

2. **Important time windows:**
   - Incident_Within_730_Days: Critical threshold identified
   - Incident_Within_365_Days: Critical threshold identified
   - Incident_to_Inquiry_Within_30d: Critical threshold identified

3. **Cyclical patterns:**
   - Hours_Incident_to_Call: Shows periodic behavior
   - Hours_Incident_to_Inquiry: Shows periodic behavior
   - Shared_Date_DayOfWeek: Shows periodic behavior

4. **Model considerations:**
   - Consider interaction terms between temporal and non-temporal features
   - Use time-based cross-validation for model evaluation
   - Monitor for temporal drift in production
   - Consider separate models for different time periods if patterns change
