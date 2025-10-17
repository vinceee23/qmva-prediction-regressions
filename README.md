# QMVA Regression Analysis — Project README

## Overview
This project analyzes **which features most strongly predict Qualified MVA (QMVA)** outcomes and produces:
- A trained multivariate model (LightGBM) with evaluation metrics
- Global and “zoomed” SHAP explainability artifacts
- Roll-up Excel summaries (by month and “Full” period) for bucket-level SHAP effects
- A formatted Word report compiling the key charts and tables

The workflow ties together three notebooks that build from **feature engineering → model training + explainability → month-by-month reporting**.

---

## Repository Structure (expected)
```
.
├── data_engineering.ipynb
├── multivariate_analysis.ipynb
├── Zoom_Consistency_ByMonth.ipynb
├── enhanced_engineered_data/
│   └── dataset_with_temporal_features.csv
├── enhanced_univariate_temporal_results/
│   └── selected_features.py  # provides TOP_50_FEATURES
├── multivariate_modeling_results/
│   ├── final_model.pkl
│   ├── cv_results.json
│   ├── multivariate_selected_features.py
│   ├── shap/
│   │   ├── Full_SHAP_Summary_Plot.png
│   │   └── Full_SHAP_Beeswarm.png (name may vary)
│   └── shap_zoom/
│       └── Full/  # per-feature “zoom” exports
├── Insights.xlsx
├── Insights - Zoom - Marketing.xlsx  # created/updated by notebooks
├── Zoom_Consistency_ByMonth.xlsx     # created by Zoom_Consistency_ByMonth.ipynb
└── QMVA_Regression_Findings_Marketing_QUANT_v7.docx  # created by Zoom_Consistency_ByMonth.ipynb
```

> **Primary target variable:** `MVA_Qualified` (binary; 1 = qualified).  
> **Primary purpose:** identify and document the strongest predictors/indicators of QMVA using regressions and SHAP-based interpretation.

---

## Notebook 1 — `data_engineering.ipynb` (Feature Engineering + Univariate Foundations)

**Purpose**
- Build robust features for QMVA prediction using a **composite target** (Qualified = “Yes” AND Law Type = “MVA”).
- Provide univariate diagnostics and a curated list of top predictive features.

**Key Capabilities**
- **Robust CSV loading** with multiple encodings and tolerant fallbacks.
- **Temporal feature engineering** (e.g., month extractors, lag-like transforms, calendar signals).
- **Categorical handling** (label encoding), optional scaling, composite features.
- **Univariate statistics**: frequency checks, **mutual information**, basic AUC checks, and sanitizer utilities.
- Tracks feature lineage/metadata via a simple **FeatureStore** helper.

**Typical Inputs / Dependencies**
- Raw exports (varies; loaded by the robust reader).
- Produces/updates: `enhanced_engineered_data/dataset_with_temporal_features.csv`
- Produces/updates (from your earlier pipeline): `enhanced_univariate_temporal_results/selected_features.py` (contains `TOP_50_FEATURES` for downstream use).

**Main Outputs**
- `enhanced_engineered_data/dataset_with_temporal_features.csv` (master table used by multivariate training)
- A ranked short list `TOP_50_FEATURES` (module file) used by `multivariate_analysis.ipynb`

---

## Notebook 2 — `multivariate_analysis.ipynb` (Model Training + SHAP Explainability)

**Purpose**
- Train a **LightGBM binary classifier** on your engineered dataset (optionally filtered by month).
- Quantify performance and **explain model behavior with SHAP**.
- Create **zoomed** per-feature SHAP analyses suitable for month-by-month and anchor-by-anchor inspection.

**How It Works**
1. **Parameters**
   - `month = 'Full'` by default. You can set `"January"` … `"December"` or numeric `1..12` to filter the dataset via the column `Call_Start_Date_Month`.
2. **Data + Features**
   - Loads `enhanced_engineered_data/dataset_with_temporal_features.csv`.
   - Imports `TOP_50_FEATURES` from `enhanced_univariate_temporal_results/selected_features.py`.
   - **Excludes** known leaky features (hard-coded list).
   - Encodes categoricals, applies basic variance filtering, and splits into train/validation.
3. **Modeling**
   - Trains `lgb.LGBMClassifier` (seeded; ~500 trees, LR 0.05; tweakable).
   - Evaluates on validation set and **prints AUC**, confusion matrix, and classification report.
   - Runs **Stratified K-Fold CV** and stores AUC distribution.
4. **Explainability**
   - Computes **SHAP values** (beeswarm + summary).
   - Handles SHAP/Numpy compatibility quirks (e.g., `np.bool` patch).
   - Builds a 2D SHAP matrix aligned to the same X used in SHAP to enable bucketed stats.
5. **Exports**
   - Saves artifacts under `multivariate_modeling_results/`:
     - `final_model.pkl` — serialized model
     - `cv_results.json` — mean/std + per-fold AUC
     - `multivariate_selected_features.py` — **final encoded column list** used in training
     - `shap/Full_SHAP_Summary_Plot.png` (+ any additional plots generated)
     - `shap_zoom/Full/…` — “zoomed” per-feature SHAP breakdowns
   - Writes/updates **`Insights - Zoom - Marketing.xlsx`** with the bucketed SHAP statistics (per zoom/feature).

**Primary Outputs**
- **Model**: `multivariate_modeling_results/final_model.pkl`
- **Metrics**: `multivariate_modeling_results/cv_results.json`
- **Explainability**: SHAP plots and “zoom” sheets (also used downstream)

---

## Notebook 3 — `Zoom_Consistency_ByMonth.ipynb` (Rollups + Word Report)

**Purpose**
- Take the per-feature **zoomed SHAP** exports and compile month-by-month **consistency tables**.
- Produce a **single Excel** file with one sheet per month and a polished **Word report** with centered visuals and section headers.

**How It Works**
1. **Parameters**
   - `src_path = Path('Insights - Zoom - Marketing.xlsx')`
   - `months = ['Full']` (use `[]` to include **all** month sheets)
   - `out_path = Path('Zoom_Consistency_ByMonth.xlsx')`
2. **Processing**
   - Loads each selected sheet and **combines all anchors** for the month into a “tall” table:
     - Columns include: `Zoomed In Feature`, `bucket`, `feature`, `direction`, `mean_shap`, `mean_abs_shap`, etc.
     - **Bucket order normalization** using numeric extraction (e.g., “0 days to 4.23” < “6.46 days+”).
   - Validates required columns and raises a helpful error if missing.
3. **Word Report**
   - Generates `QMVA_Regression_Findings_Marketing_QUANT_v7.docx` with:
     - **Centered image** sections (e.g., SHAP summary, zoom visuals)
     - Bolded section headers and consistent spacing

**Outputs**
- `Zoom_Consistency_ByMonth.xlsx` (one sheet per month, or all months)
- `QMVA_Regression_Findings_Marketing_QUANT_v7.docx` (visual narrative of findings)

---

## End-to-end: What the Project Produces

1. **A ranked, inspected feature set** for QMVA (from univariate + temporal engineering).
2. **A vetted multivariate model** with cross-validated AUC and validation diagnostics.
3. **Global SHAP** (summary/beeswarm) to understand overall drivers.
4. **Zoomed SHAP** per top feature, **bucketed** by interpretable ranges (days, counts, etc.).
5. **Excel artifacts** for analysts/stakeholders:
   - `Insights - Zoom - Marketing.xlsx` — per-feature zoom stats (by month or “Full”)
   - `Zoom_Consistency_ByMonth.xlsx` — **roll-up** by month (one sheet each)
6. **A Word report** to share or present findings: `QMVA_Regression_Findings_Marketing_QUANT_v7.docx`.

---

## How to Run (Quickstart)

### 1) Prepare Environment
- Python ≥ 3.10 recommended
- `pip install` the following (minimum set):
  ```bash
  pip install pandas numpy scikit-learn lightgbm shap matplotlib openpyxl python-docx joblib
  ```

### 2) Order of Execution
1. **Feature Engineering / Univariate**: run `data_engineering.ipynb`
   - Produces `enhanced_engineered_data/dataset_with_temporal_features.csv`
   - Produces `enhanced_univariate_temporal_results/selected_features.py` (contains `TOP_50_FEATURES`)
2. **Multivariate + SHAP**: run `multivariate_analysis.ipynb`
   - Set `month = 'Full'` (or a month name/number)
   - Confirms **AUC** and writes **SHAP** plots + **zoom** exports to Excel
3. **Consistency + Report**: run `Zoom_Consistency_ByMonth.ipynb`
   - Set `months = ['Full']` or `[]` to include **all**
   - Produces `Zoom_Consistency_ByMonth.xlsx` and the Word report

---

## Configuration & Parameters

- **Target**: `TARGET_VARIABLE = "MVA_Qualified"`
- **Month filter** (in `multivariate_analysis.ipynb`): `month = 'Full' | 'January'..'December' | 1..12`
- **Workbook paths**:
  - `Insights.xlsx` (base)
  - `Insights - Zoom - Marketing.xlsx` (bucketed zoom stats; created/updated by notebooks)
- **Outputs**:
  - `multivariate_modeling_results/*` (model + explainability)
  - `Zoom_Consistency_ByMonth.xlsx`
  - `QMVA_Regression_Findings_Marketing_QUANT_v7.docx`

---

## Expected Columns & Assumptions

- The engineered dataset includes at least:
  - `MVA_Qualified` (binary target)
  - `Call_Start_Date_Month` (1–12, used for filtering in multivariate notebook)
  - All features listed in `TOP_50_FEATURES` (post-exclusion of leaky columns)
- Zoom/Insights workbooks contain columns like:
  - `Zoomed In Feature`, `bucket`, `feature`, `direction`, `mean_shap`, `mean_abs_shap`

If these columns are missing, the Zoom rollup notebook will raise a helpful error indicating which columns to add/regenerate.

---

## Troubleshooting

- **`np.bool` or SHAP compatibility errors**: the notebooks include a protective patch for NumPy≥1.24.
- **`BadZipFile` when appending to Excel**: the exporter backs up the invalid file (adds `.bak`) and recreates the workbook cleanly.
- **Missing columns in Zoom rollup**: re-run `multivariate_analysis.ipynb` to regenerate zoom sheets with the required columns.
- **Class imbalance**: review AUC alongside precision/recall; consider threshold tuning if needed.
- **Feature leakage**: an explicit **exclusion list** removes known leaky features before modeling; update as necessary.

---

## Interpretation Notes (QMVA Context)

- **SHAP** values quantify each feature’s contribution to the probability of being QMVA-qualified.
- The **bucketed zooms** turn raw feature values into interpretable ranges (e.g., *0–4.23 days*, *6.46+ days*), making it easy to spot monotonic or U-shaped relationships.
- Month-level filtering lets you compare **seasonality** or operational shifts in the drivers.
- The `Zoom_Consistency_ByMonth.xlsx` consolidates anchors and features for each month so you can quickly check **directional consistency** (positive/negative SHAP) and **magnitude** across time.

---

## Change Log Hints (what to update when notebooks evolve)
- Update `selected_features.py` whenever univariate criteria change.
- If engineered dataset columns move or are renamed, refresh `multivariate_selected_features.py` by re-running the multivariate notebook.
- When adding new zoom visuals, the Word report template section (in `Zoom_Consistency_ByMonth.ipynb`) can be extended with a new, centered image block.

---

## Glossary
- **QMVA** — Qualified Motor Vehicle Accident (qualified inquiry/case status).
- **Zoom** — Focused SHAP analysis on a single feature with bucketed ranges.
- **Anchor** — The feature currently zoomed-in on; “anchors + features” tables list interactions/relationships.
- **SHAP** — Model-agnostic method to explain individual predictions and global feature importance.
- **AUC** — Area Under the ROC Curve; a threshold-independent measure of ranking quality.

---

*Maintainer: Vince (Data Analyst)*
