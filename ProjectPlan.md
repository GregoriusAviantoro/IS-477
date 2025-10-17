# Project Plan — Global Happiness and Economic Development (2018)

## Overview

This project examines the relationship between economic development and national happiness across countries in 2018. Using two trusted openly available datasets: the World Happiness Report 2018 and the Gapminder Global Development Data. It investigates how economic and demographic factors such as GDP per capita and life expectancy relate to citizens' reported happiness.

The project focuses on a single year (2018) for consistency, as the Happiness dataset does not extend beyond that year. This also simplifies integration and avoids temporal mismatches. The final analysis will involve merging, cleaning, profiling, and visualizing the combined dataset to reveal how economic prosperity and quality of life correlate with happiness levels worldwide.

## Research Questions

1. Is GDP per capita associated with national happiness in 2018?
2. Do countries with higher life expectancy report higher happiness levels?
3. Are there regional or continental differences in happiness relative to economic performance?
4. Which economic indicators are most predictive of happiness across countries?

## Team

- **Student:** Gregorius Aviantoro
- **Role:** Data Sourcing, Preprocessing, and Data Vizualisation.
- **Responsibilities:**
  - Data acquisition, cleaning, and documentation.
  - Integration and quality assessment.
  - Preparation of Markdown documentation and GitHub deliverables.
- **Student:** Rishi Akul
- **Role:** 
- **Responsibilities:**
  - X

## Datasets

### Dataset 1: World Happiness Report 2018

- **Source:** (https://www.kaggle.com/datasets/unsdsn/world-happiness?resource=download)
- **Coverage:** 156 countries (2018)
- **Variables:**
  - Overall Rank: Rank of countries based on happiness score
  - Country or region: Describes the country name
  - Score: Overall happiness score (0–10)
  - GDP per capita: The Gross Domestic Product of each country divided by population
  - Social support: Social Support score contribution to the happiness score
  - Healthy life expectancy: Healthy life expectancy score contribution to the happiness score
  - Freedom to make life choices: Freedom to ake life choices score contribution to the happiness score
  - Generosity: Generosity score contribution to the happiness score
  - Perceptions of corruption: Corruption perception score contribution to the happiness score
- **Format:** CSV
- **Use in project:** Provides the dependent variable (Score) and several social indicators.

### Dataset 2: Gapminder Global Development Data

- **Source:** https://www.kaggle.com/datasets/albertovidalrod/gapminder-dataset?
- **Coverage:** 175 countries (1998–2018)
- **Variables (used):**
- Country (country): Describes the country name
- Continent (continent): Describes the continent to which the country belongs
- Year (year): Describes the year to which the data belongs
- Life expectancy (life_exp): Describes the life expectancy for a given country in a given year
- Human Development Index (hdi_index): Describes the HDI index value for a given country in a given year
- CO2 emissions per person(co2_consump): Describes the CO2 emissions in tonnes per person for a given country in a given year
- Gross Domestic Product per capita (gdp): Describes the GDP per capita in dollars for a given country in a given year
- % Service workers (services): Describes the the % of service workers for a given country in a given year
- **Format:** CSV
- **License:** CC BY 4.0
- **Use in project:** Provides economic and demographic indicators for analysis.

## Integration Plan

1. Use the 2018 csv file from the World Happiness Report and filter the gapminder dataset for 2018.
2. Standardize country names (example: "Hong Kong" vs. "Hong Kong, China").
3. Merge datasets using `pandas.merge()` on the country column.
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
| Oct 1–16 | Setup & Planning | Create GitHub repo and initialize documentation | Gregorius |
| Oct 17–25 | Data Acquisition | Download both CSVs and store in /data/raw/ | Gregorius |
| Oct 26–Nov 5 | Cleaning & Profiling | Inspect missing values, harmonize country names, convert data types | Gregorius |
| Nov 6–15 | Integration & Analysis | Merge datasets, compute descriptive statistics and correlations | Rishi |
| Nov 16–28 | Visualization & Automation | Generate charts, finalize pipeline, document workflow | Gregorius |
| Dec 1–10 | Final Submission | Complete report and reproducibility materials | Rishi |

## Constraints

- **Non-matching countries:** Happiness (158) vs. Gapminder (175); the merge may yield ~150 records.
- **Year limitation:** Happiness data only extends to 2018; project will be limited to that year.
- **Country naming inconsistencies:** Will require minor cleaning (example: "Côte d'Ivoire" vs. "Ivory Coast").

## Gaps / Next Steps

- Confirm which subset of Gapminder indicators provides the strongest predictive power for happiness.
- Investigate the effect of regional grouping (continents) for visualization.
- Create a reproducibility checklist to document all analysis steps.

## Relation to Course Requirements

| Requirement | How It's Addressed |
|-------------|--------------------|
| Data lifecycle | End-to-end process: acquisition to cleaning to integration to analysis to documentation. |
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

- **Integrated dataset:** `/data/processed/happiness_economy_2018.csv`
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

## Conclusion

This project will explore how economic indicators such as GDP per capita and life expectancy correlate with national happiness levels using two reputable, open datasets: World Happiness Report 2018 and Gapminder. By focusing on 2018, it ensures consistent temporal coverage and straightforward data integration. The final deliverable will include a fully reproducible workflow, a cleaned and merged dataset, and visualizations illustrating the connections between economic prosperity and happiness, aligning with the IS477 course objectives of ethical, transparent, and reproducible data curation.
