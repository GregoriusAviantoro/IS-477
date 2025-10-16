# Project Plan — Global Happiness and Economic Development (2019)

## Overview

This project examines the relationship between economic development and national happiness across countries in 2019. Using two trusted, openly available datasets — the World Happiness Report 2019 and the Gapminder Global Development Data — it investigates how economic and demographic factors such as GDP per capita and life expectancy relate to citizens' reported happiness.

The project focuses on a single year (2019) for consistency, as the Happiness dataset does not extend beyond that year. This also simplifies integration and avoids temporal mismatches. The final analysis will involve merging, cleaning, profiling, and visualizing the combined dataset to reveal how economic prosperity and quality of life correlate with happiness levels worldwide.

## Research Questions

1. Is GDP per capita associated with national happiness in 2019?
2. Do countries with higher life expectancy report higher happiness levels?
3. Are there regional or continental differences in happiness relative to economic performance?
4. Which economic indicators are most predictive of happiness across countries?

## Team

- **Student:** Greg A.
- **Role:** Working individually (with instructor approval)
- **Responsibilities:**
  - Data acquisition, cleaning, and documentation.
  - Integration and quality assessment.
  - Exploratory data analysis and visualization.
  - Workflow automation for reproducibility.
  - Preparation of Markdown documentation and GitHub deliverables.

## Datasets

### Dataset 1: World Happiness Report 2019

- **Source:** [Kaggle: World Happiness Report Dataset]()
- **Direct CSV:** [https://github.com/unsdsn/world-happiness/blob/master/2019.csv]()
- **Coverage:** 158 countries (2019)
- **Variables:**
  - Country or region
  - Score — overall happiness score (0–10)
  - GDP per capita — national income (log scale)
  - Social support
  - Healthy life expectancy
  - Freedom to make life choices
  - Generosity
  - Perceptions of corruption
- **Format:** CSV
- **License:** CC BY 4.0
- **Notes:** Represents subjective well-being data compiled from Gallup World Poll responses.
- **Use in project:** Provides the dependent variable (Score) and several social indicators.

### Dataset 2: Gapminder Global Development Data

- **Source:** [Gapminder Data Portal](https://www.gapminder.org/data/?utm_source=chatgpt.com)
- **Direct CSV:** [https://github.com/syntagmatic/gapminder-csv/raw/master/data/gapminder.csv](https://github.com/syntagmatic/gapminder-csv/raw/master/data/gapminder.csv)
- **Coverage:** 175 countries (1950–2021)
- **Variables (used):**
  - country
  - year
  - lifeExp — life expectancy at birth (years)
  - pop — population
  - gdpPercap — GDP per capita (constant international dollars)
- **Format:** CSV
- **License:** CC BY 4.0
- **Use in project:** Provides economic and demographic indicators for analysis.

## Integration Plan

1. Filter both datasets for 2019 to align temporal coverage.
2. Standardize country names (e.g., "United States" vs. "United States of America").
3. Merge datasets using `pandas.merge()` on the country column (inner join).
4. Clean and normalize data:
   - Convert GDP per capita values to comparable units.
   - Handle missing or unmatched countries.
5. Perform exploratory analysis:
   - Compute summary statistics and correlation coefficients.
   - Visualize relationships using scatterplots and heatmaps.
6. Automate workflow with a `run_all.py` or Snakemake pipeline for reproducibility.

## Timeline

| Date Range | Task | Description | Responsible |
|------------|------|-------------|-------------|
| Oct 16–20 | Setup & Planning | Create GitHub repo and initialize documentation | Greg |
| Oct 21–31 | Data Acquisition | Download both CSVs and store in /data/raw/ | Greg |
| Nov 1–10 | Cleaning & Profiling | Inspect missing values, harmonize country names, convert data types | Greg |
| Nov 11–20 | Integration & Analysis | Merge datasets, compute descriptive statistics and correlations | Greg |
| Nov 21–Dec 5 | Visualization & Automation | Generate charts, finalize pipeline, document workflow | Greg |
| Dec 6–10 | Final Submission | Complete report and reproducibility materials | Greg |

## Constraints

- **Non-matching countries:** Happiness (158) vs. Gapminder (175); the merge may yield ~150 records.
- **Year limitation:** Happiness data only extends to 2019; project will be limited to that year.
- **Country naming inconsistencies:** Will require minor cleaning (e.g., "Côte d'Ivoire" vs. "Ivory Coast").
- **Different GDP units:** Happiness dataset uses log GDP; Gapminder uses absolute GDP — normalization will be needed before correlation.
- **Interpretation limits:** Correlation ≠ causation; the report will clearly state this.

## Gaps / Next Steps

- Confirm which subset of Gapminder indicators provides the strongest predictive power for happiness.
- Investigate the effect of regional grouping (continents) for visualization.
- Create a reproducibility checklist to document all analysis steps.
- Write metadata and data dictionary for both datasets.
- Ensure that file paths and workflow scripts are compatible with GitHub release packaging.

## Relation to Course Requirements

| Requirement | How It's Addressed |
|-------------|--------------------|
| Data lifecycle | End-to-end process: acquisition → cleaning → integration → analysis → documentation. |
| Ethical data handling | Both datasets are open-access under CC BY 4.0; no privacy issues. |
| Data collection | Static CSV downloads from reputable sources. |
| Storage & organization | Versioned storage with raw/processed separation and descriptive naming. |
| Extraction & enrichment | Economic data enriches happiness data for deeper insights. |
| Integration | Performed in Python (pandas) on country after standardization. |
| Data quality | Assess missingness, outliers, and merge completeness. |
| Cleaning | Harmonize names, handle NaNs, normalize GDP variables. |
| Workflow automation | Create a single-run script (run_all.py) or Snakemake pipeline. |
| Reproducibility | All data, code, and documentation published in GitHub. |
| Metadata & documentation | Markdown documentation and data dictionaries for reuse. |

## Planned Outputs

- **Integrated dataset:** `/data/processed/happiness_economy_2019.csv`
- **Python scripts:** for data cleaning, integration, and visualization.
- **Visualizations:**
  - GDP per capita vs. Happiness scatterplot
  - Life expectancy vs. Happiness scatterplot
  - Correlation heatmap
- **Reproducible workflow:** Python or Snakemake script to reproduce results.
- **Documentation:**
  - README.md (project overview & reproducibility steps)
  - data_dictionary.md (metadata)
  - requirements.txt (Python dependencies)

## Recommended GitHub Repository Structure

```
IS477-Project/
│
├── data/
│   ├── raw/
│   │   ├── world_happiness_2019.csv
│   │   └── gapminder.csv
│   └── processed/
│       └── happiness_economy_2019.csv
│
├── scripts/
│   ├── clean_merge.py
│   ├── visualize.py
│   └── run_all.py
│
├── docs/
│   ├── data_dictionary.md
│   └── metadata.md
│
├── ProjectPlan.md
├── README.md
├── requirements.txt
└── LICENSE
```

## Conclusion

This project will explore how economic indicators such as GDP per capita and life expectancy correlate with national happiness levels using two reputable, open datasets: World Happiness Report 2019 and Gapminder. By focusing on 2019, it ensures consistent temporal coverage and straightforward data integration.

The final deliverable will include a fully reproducible workflow, a cleaned and merged dataset, and visualizations illustrating the connections between economic prosperity and happiness — aligning with the IS477 course objectives of ethical, transparent, and reproducible data curation.
