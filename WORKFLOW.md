# Workflow Documentation


## Workflow Overview

This project uses an automated Python workflow (`run_all.py`) that orchestrates the complete data pipeline from raw data acquisition through final visualizations.

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     RAW DATA SOURCES                             │
├─────────────────────────────────────────────────────────────────┤
│  ┌────────────────────────┐    ┌─────────────────────────────┐  │
│  │ World Happiness 2018   │    │ Gapminder Development Data  │  │
│  │ (Kaggle/Box)           │    │ (Kaggle/Box)                │  │
│  │ 2018.csv               │    │ gapminder_data_graphs.csv   │  │
│  │ 156 countries          │    │ 175 countries (2018)        │  │
│  └────────────────────────┘    └─────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    STEP 1: DATA CLEANING                         │
│                   Script: src/clean_data.py                      │
├─────────────────────────────────────────────────────────────────┤
│  • Standardize country names (13+ mappings)                      │
│  • Rename columns for consistency                                │
│  • Filter Gapminder to 2018 only                                 │
│  • Handle missing values                                         │
│  • Calculate SHA-256 checksums                                   │
├─────────────────────────────────────────────────────────────────┤
│  Output:                                                         │
│  • data/processed/happiness_2018_cleaned.csv (156 countries)     │
│  • data/processed/gapminder_2018_cleaned.csv (175 countries)     │
│  • data/processed/cleaning_provenance.json                       │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                   STEP 2: DATA PROFILING                         │
│                  Script: src/profile_data.py                     │
├─────────────────────────────────────────────────────────────────┤
│  • Generate descriptive statistics                               │
│  • Analyze missing value patterns                                │
│  • Validate data types                                           │
│  • Calculate distributions (skewness, kurtosis)                  │
│  • Perform quality checks (duplicates, outliers)                 │
│  • Profile categorical variables                                 │
├─────────────────────────────────────────────────────────────────┤
│  Output:                                                         │
│  • data/processed/data_profile_report.json                       │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                   STEP 3: DATA INTEGRATION                       │
│                  Script: src/merge_data.py                       │
├─────────────────────────────────────────────────────────────────┤
│  • Merge datasets on standardized country names                  │
│  • Inner join (keep only matching countries)                     │
│  • Validate merge quality                                        │
│  • Document non-matching countries                               │
│  • Generate merge statistics                                     │
├─────────────────────────────────────────────────────────────────┤
│  Output:                                                         │
│  • data/processed/happiness_economy_2018.csv (144 countries)     │
│  • data/processed/merge_report.json                              │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                  STEP 4: VISUALIZATION                           │
│                 Script: src/visualize.py                         │
├─────────────────────────────────────────────────────────────────┤
│  • GDP per capita vs Happiness scatterplot (by continent)        │
│  • Life expectancy vs Happiness scatterplot (by continent)       │
│  • Correlation heatmap (all numeric variables)                   │
├─────────────────────────────────────────────────────────────────┤
│  Output:                                                         │
│  • results/gdp_happiness_scatter.png                             │
│  • results/life_exp_happiness_scatter.png                        │
│  • results/correlation_heatmap.png                               │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FINAL OUTPUTS                               │
├─────────────────────────────────────────────────────────────────┤
│  Processed Data (6 files):                                       │
│    • happiness_2018_cleaned.csv                                  │
│    • gapminder_2018_cleaned.csv                                  │
│    • happiness_economy_2018.csv                                  │
│    • cleaning_provenance.json                                    │
│    • data_profile_report.json                                    │
│    • merge_report.json                                           │
│                                                                  │
│  Visualizations (3 files):                                       │
│    • gdp_happiness_scatter.png                                   │
│    • life_exp_happiness_scatter.png                              │
│    • correlation_heatmap.png                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Execution Methods

### Method 1: Automated Complete Workflow (Recommended)

```bash
python run_all.py
```

**What it does**:
1. Checks all dependencies are installed
2. Verifies input data files exist
3. Runs all 4 processing scripts in sequence
4. Validates all output files were created
5. Reports runtime and success/failure

### Method 2: Manual Step-by-Step Execution

```bash
# Step 1: Clean data
python src/clean_data.py

# Step 2: Profile data
python src/profile_data.py

# Step 3: Merge datasets
python src/merge_data.py

# Step 4: Generate visualizations
python src/visualize.py
```

## Provenance Tracking

Each step in the workflow generates provenance metadata:

### Cleaning Provenance (`cleaning_provenance.json`)
```json
{
  "timestamp": "2025-12-09T16:45:00",
  "datasets": {
    "happiness_2018": {
      "source_path": "data/raw/2018.csv",
      "file_hash": "sha256_checksum_here",
      "description": "World Happiness Report 2018"
    },
    "gapminder": {
      "source_path": "data/raw/gapminder_data_graphs.csv",
      "file_hash": "sha256_checksum_here"
    }
  },
  "python_version": "3.8+",
  "pandas_version": "1.5.3",
  "cleaning_steps": [...]
}
```

### Profile Report (`data_profile_report.json`)
- Descriptive statistics for all numeric variables
- Missing value patterns and percentages
- Data type validation
- Distribution metrics (skewness, kurtosis)
- Quality checks (duplicates, outliers)

### Merge Report (`merge_report.json`)
- Countries matched: 144
- Countries in happiness only: 12
- Countries in Gapminder only: 31
- Merge success rate: 92%

---

## Error Handling

The workflow includes comprehensive error handling:

1. **Dependency Checking**: Verifies all required packages before execution
2. **Input Validation**: Checks that raw data files exist
3. **Script Execution**: Catches and reports errors from each script
4. **Output Verification**: Validates expected output files were created
5. **Detailed Logging**: Provides clear error messages for debugging

If any step fails, the workflow stops and reports the error location.

---

## Workflow Validation

### Expected File Counts

After successful execution:
- `data/processed/`: 6 files
- `results/`: 3 files
- Total: 9 output files

### Expected Data Characteristics

- **happiness_economy_2018.csv**: 144 rows, 16 columns
- **Visualizations**: 3 PNG files, each ~300-500 KB
- **JSON reports**: Human-readable metadata