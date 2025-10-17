✅ Ready for Unicode!# Enhanced Feature Analysis Summary

**Generated on:** 2025-10-18 04:38:41
**Version:** Enhanced with Aggressive Risk Detection and Composite Target

## Target Variable Definition

**Target Name:** `MVA_Qualified`

**Definition:** A record is positive (1) if:
- Inquiry Call Type Qualified Flag = 'Yes' AND
- Inquiry Call Type Law Type (Broad) = 'MVA'

## Dataset Overview

- **Total records:** 1,000
- **Total features:** 236
- **Target variable:** MVA_Qualified
- **Positive cases (MVA Qualified):** 20 (2.00%)
- **Negative cases:** 980 (98.00%)

## Data Composition

### Law Type Distribution

| Law Type | Count | Percentage |
|----------|-------|------------|
| MVA | 188 | 18.8% |
| Misc | 156 | 15.6% |
| Call Back | 151 | 15.1% |
| WC | 18 | 1.8% |
| Premise | 13 | 1.3% |
| L&E | 9 | 0.9% |

## Tiered Risk Distribution

| Tier | Risk Score | Count | Percentage | Action |
|------|------------|-------|------------|--------|
| Tier 1 | ≥8 | 87 | 36.9% | Auto-exclude |
| Tier 2 | 5-7 | 47 | 19.9% | Strong review |
| Tier 3 | 3-4 | 2 | 0.8% | Consider carefully |
| Tier 4 | <3 | 100 | 42.4% | Likely safe |

## Risk Factor Analysis

| Risk Factor | Feature Count |
|------------|---------------|
| Temporal Leakage | 0 |
| Unstable Features | 0 |
| PII Patterns | 50 |
| System Patterns | 67 |
| High Cardinality (>50%) | 30 |
| Very High Correlation (>0.8) | 18 |

## Top 15 Highest Risk Features

| Feature | Risk Score | Unique Ratio | Key Reasons |
|---------|------------|--------------|-------------|
| Incident State | 34 | 95.6% | very_high_cardinality(95.6%), medium_unique_count(956), PII_pattern |
| Consumer Phone (Caller ID) Geo State | 33 | 94.0% | very_high_cardinality(94.0%), medium_unique_count(940), PII_pattern |
| First Log Entry Timestamp | 29 | 39.3% | high_cardinality(39.3%), PII_pattern, system_pattern |
| Consumer Name (First) | 28 | 93.4% | very_high_cardinality(93.4%), medium_unique_count(934), PII_pattern |
| Consumer State | 28 | 95.9% | very_high_cardinality(95.9%), medium_unique_count(959), PII_pattern |
| Consumer City | 27 | 79.5% | very_high_cardinality(79.5%), medium_unique_count(795), PII_pattern |
| Consumer Name (Last) | 27 | 93.5% | very_high_cardinality(93.5%), medium_unique_count(935), PII_pattern |
| Consumer Phone (Caller ID) | 27 | 89.7% | very_high_cardinality(89.7%), medium_unique_count(897), PII_pattern |
| Consumer Email | 27 | 76.9% | very_high_cardinality(76.9%), medium_unique_count(769), PII_pattern |
| Inquiry DMA State | 27 | 80.6% | very_high_cardinality(80.6%), medium_unique_count(806), PII_pattern |
| Phone Area Code (ID) | 27 | 53.5% | very_high_cardinality(53.5%), medium_unique_count(535), PII_pattern |
| Consumer Phone (Caller ID) Area Code | 26 | 51.0% | very_high_cardinality(51.0%), medium_unique_count(510), PII_pattern |
| Inquiry Most Recent Timestamp | 26 | 99.5% | very_high_cardinality(99.5%), medium_unique_count(995), system_pattern |
| Inquiry Start Timestamp | 26 | 99.3% | very_high_cardinality(99.3%), medium_unique_count(993), system_pattern |
| Consumer Walker Geo (Code) | 25 | 81.6% | very_high_cardinality(81.6%), medium_unique_count(816), system_pattern |

## Recommendations

### Immediate Actions

1. **Exclude 87 Tier 1 features** - These have clear data leakage or PII risks
2. **Review 47 Tier 2 features** - Domain expert review required
3. **Start modeling with 50 Tier 4 features** - These appear safest

### Feature Selection Strategy

1. Begin with Tier 4 features only for baseline model
2. Gradually add reviewed Tier 3 features if needed
3. Only include Tier 2 features after thorough validation
4. Never include Tier 1 features

### Model Development Considerations

- The composite target captures MVA-specific qualification patterns
- Consider building separate models for other law types if needed
- Monitor for class imbalance given the low positive rate
- Use stratified sampling to maintain target distribution

### Risk Mitigation

- Validate temporal integrity (no future information)
- Check for indirect target leakage
- Consider feature engineering from safe features only
- Monitor model performance for signs of overfitting
- Implement cross-validation to ensure generalization
