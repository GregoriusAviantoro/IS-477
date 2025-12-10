# Global Happiness and Economic Development in 2018

**A Data Curation and Analysis Project**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)

---

## Contributors

- **Gregorius Aviantoro** - Data Curator, Primary Developer
  - University of Illinois Urbana-Champaign
  - Email: [ga22@illinois.edu]
  
- **Rishi Akula** - Data Analyst, Documentation Lead
  - University of Illinois Urbana-Champaign
  - Email: [@illinois.edu]

---

## Summary

### Project Overview

This project examines the relationship between economic development and national happiness across countries in 2018. Using two trusted openly available datasets—the World Happiness Report 2018 and the Gapminder Global Development Data—we investigate how economic and demographic factors such as GDP per capita, life expectancy, and Human Development Index (HDI) correlate with citizens' reported happiness levels.

### Motivation

Understanding the factors that contribute to national happiness is crucial for policymakers and researchers alike. While economic prosperity is often assumed to correlate with well-being, the relationship is complex and multifaceted. This project aims to quantify these relationships using rigorous data curation practices and transparent analytical methods.

### Research Questions

1. **Is GDP per capita associated with national happiness in 2018?**
2. **Do countries with higher life expectancy report higher happiness levels?**
3. **Are there regional or continental differences in happiness relative to economic performance?**
4. **Which economic indicators are most predictive of happiness across countries?**

### Methodology

Our approach followed the complete data lifecycle:

1. **Data Acquisition**: Downloaded World Happiness Report 2018 (156 countries) and Gapminder Global Development Data from Kaggle
2. **Data Cleaning**: Standardized country names, renamed columns for consistency, filtered Gapminder to 2018
3. **Data Profiling**: Assessed data quality, missing values, distributions, and outliers
4. **Data Integration**: Merged datasets using country name as key, achieving 144 matched countries
5. **Data Analysis**: Generated visualizations and correlation analyses
6. **Workflow Automation**: Created reproducible pipeline with provenance tracking

### Key Findings

Our analysis revealed several important patterns:

**Strong Positive Correlations with Happiness:**
- **GDP per capita**: Countries with higher GDP per capita consistently report higher happiness scores
- **Life expectancy**: Strong positive correlation between life expectancy and happiness
- **Human Development Index (HDI)**: The strongest single predictor of national happiness among economic indicators

**Continental Differences:**
- European countries cluster in the high happiness, high GDP region
- African countries show more variation in the happiness-economic performance relationship
- Asian countries demonstrate diverse patterns reflecting their economic heterogeneity
- Americas show moderate to high happiness levels with corresponding economic indicators
- Oceania countries (limited sample) show high happiness and economic development

**Correlation Matrix Results:**
The correlation analysis revealed:
- happiness_score ↔ HDI: r ≈ 0.84 (very strong)
- happiness_score ↔ GDP per capita: r ≈ 0.82 (very strong)
- happiness_score ↔ life_expectancy: r ≈ 0.80 (very strong)
- happiness_score ↔ social_support: r ≈ 0.78 (strong)
- happiness_score ↔ freedom: r ≈ 0.56 (moderate)

These findings suggest that while economic factors are strongly associated with happiness, the relationship is not deterministic. Some countries achieve relatively high happiness with moderate economic resources, suggesting the importance of other factors such as social support, freedom, and governance quality.

### Significance

This project demonstrates:
- The importance of rigorous data curation practices in social science research
- The value of integrating multiple data sources for comprehensive analysis
- The need for transparent, reproducible workflows in data science
- The complex, multifaceted nature of national well-being

---

## Data Profile

### Dataset 1: World Happiness Report 2018

**Source**: United Nations Sustainable Development Solutions Network  
**Acquisition**: Downloaded from Kaggle (https://www.kaggle.com/datasets/unsdsn/world-happiness)  
**File**: `data/raw/2018.csv`  
**Coverage**: 156 countries  
**Year**: 2018  
**License**: Open access, publicly available

**Description**:
The World Happiness Report is an annual publication that ranks countries by their happiness levels based on the Cantril Ladder life evaluation. Respondents rate their current life from 0 (worst possible) to 10 (best possible). The report also includes explanatory factors that contribute to the happiness score.

**Variables**:
- Overall rank: Ranking of countries (1-156)
- Country or region: Country name
- Score: Happiness score (0-10 scale)
- GDP per capita: GDP contribution to happiness score
- Social support: Social support contribution to happiness
- Healthy life expectancy: Life expectancy contribution
- Freedom to make life choices: Freedom contribution
- Generosity: Generosity contribution
- Perceptions of corruption: Corruption perception contribution

**Ethical/Legal Considerations**:
- No personal identifying information; aggregate country-level data only
- Publicly available dataset with open access
- Proper attribution to UN Sustainable Development Solutions Network required
- Survey methodology documented in original reports
- No restrictions on use for research or educational purposes

**Data Quality**:
- High completeness (minimal missing values)
- Standardized collection methodology across countries
- Annual publication ensures consistency
- Validated by reputable international organization (UN)

### Dataset 2: Gapminder Global Development Data

**Source**: Gapminder Foundation (compiled from World Bank, UN, OECD, and other sources)  
**Acquisition**: Downloaded from Kaggle (https://www.kaggle.com/datasets/albertovidalrod/gapminder-dataset)  
**File**: `data/raw/gapminder_data_graphs.csv`  
**Coverage**: 175 countries, 1998-2018 (filtered to 2018 for this project)  
**License**: CC BY 4.0  
**Attribution**: Gapminder Foundation, www.gapminder.org

**Description**:
Gapminder compiles data from multiple authoritative international sources to provide comprehensive development indicators. This dataset includes economic, demographic, and environmental metrics that complement the happiness data.

**Variables**:
- country: Country name
- continent: Geographic continent
- year: Year of observation (1998-2018)
- life_exp: Life expectancy at birth (years)
- hdi_index: Human Development Index (0-1 scale)
- co2_consump: CO2 emissions per capita (tonnes)
- gdp: GDP per capita (constant international dollars)
- services: Percentage of workforce in service sector

**Ethical/Legal Considerations**:
- CC BY 4.0 license requires attribution
- Aggregate country-level data, no individual privacy concerns
- Data compiled from reputable international sources
- Some missing values for smaller nations due to data availability
- No restrictions on redistribution with proper attribution

**Data Quality**:
- Some missing values, particularly for smaller or developing nations
- Multi-year coverage allows validation across time
- Compiled from multiple authoritative sources
- Regular updates and corrections by Gapminder Foundation
- Well-documented methodology and sources

### Integrated Dataset

**File**: `data/processed/happiness_economy_2018.csv`  
**Coverage**: 144 countries (92% merge success rate)  
**Variables**: 16 (combined from both sources)

The integrated dataset combines happiness indicators with economic and demographic data, enabling comprehensive analysis of factors associated with national well-being. The merge was performed using country names as keys after standardization to handle naming inconsistencies.

---

## Data Quality

### Quality Assessment Methodology

We performed comprehensive data quality assessment using automated profiling scripts that evaluated:
1. Completeness (missing values)
2. Accuracy (range validation, type checking)
3. Consistency (duplicate detection)
4. Validity (outlier detection using IQR method)

### Happiness Dataset Quality

**File**: `data/raw/2018.csv`

**Completeness**:
- Total records: 156 countries
- Missing happiness scores: 0 (100% complete)
- Missing values in other variables: Minimal (<2%)

**Quality Findings**:
- No duplicate records detected
- All numeric values within expected ranges (0-10 for happiness score)
- No negative values in variables where positivity is expected
- Outliers detected but retained as they represent legitimate country differences
- Country names required standardization for merging

**Quality Issues Identified**:
- Minor inconsistencies in country naming (e.g., "Palestinian Territories" needed standardization)
- No major data quality issues requiring correction

### Gapminder Dataset Quality

**File**: `data/raw/gapminder_data_graphs.csv` (filtered to 2018)

**Completeness**:
- Total records after filtering to 2018: 175 countries
- Missing values varied by indicator:
  - HDI: ~15% missing (primarily smaller nations)
  - GDP per capita: ~8% missing
  - Life expectancy: ~5% missing
  - CO2 per capita: ~12% missing
  - Service workers percentage: ~18% missing

**Quality Findings**:
- No duplicate records for year 2018
- Some outliers in CO2 emissions (oil-producing nations)
- GDP per capita outliers for very wealthy small nations (expected)
- Life expectancy values all within biologically plausible range (50-85 years)

**Quality Issues Identified and Addressed**:
1. **Multi-year data required filtering**: Successfully filtered to 2018 only
2. **Missing economic data**: Documented and retained (no imputation) for transparency
3. **Country naming inconsistencies**: Standardized using mapping dictionary (13+ mappings)
4. **Outliers in economic indicators**: Retained as legitimate variation, not errors

### Data Cleaning Actions Taken

**Country Name Standardization** (13+ mappings):
- "Palestinian Territories" → "Palestine"
- "Congo (Brazzaville)" → "Congo, Rep."
- "Congo (Kinshasa)" → "Congo, Dem. Rep."
- "Trinidad & Tobago" → "Trinidad and Tobago"
- "Northern Cyprus" → "Cyprus"
- "Ivory Coast" → "Cote d'Ivoire"
- And 7 additional mappings

**Column Renaming**:
- Standardized naming conventions across datasets
- Example: "Overall rank" → "happiness_rank", "life_exp" → "life_expectancy"

**Missing Value Handling**:
- Removed rows with missing happiness scores (0 rows affected)
- Retained missing values in economic indicators with documentation
- No imputation performed to maintain data integrity

**Data Type Validation**:
- Verified numeric columns contain valid numbers
- Validated categorical variables (continent) for consistency
- Confirmed year filtering produced correct subset

### Integration Quality

**Merge Statistics**:
- Countries in happiness dataset: 156
- Countries in Gapminder dataset: 175
- Successfully matched: 144 countries (92% merge rate)
- Countries in happiness only: 12
- Countries in Gapminder only: 31

**Merge Quality Assessment**:
- High merge success rate (92%) indicates good data quality
- Non-matches primarily due to naming differences or data availability
- All matched records have complete key variables (country, happiness_score, continent)
- Final dataset ready for analysis with no critical quality issues

### Provenance and Validation

All data processing steps documented with:
- SHA-256 checksums for raw data files
- Timestamps for all processing steps
- Python and package versions recorded
- Complete transformation history in JSON format
- Validation checks at each step

**Validation Results**:
- All processed files validated against raw sources
- Checksums match documented values
- Row counts confirmed at each processing stage
- No data loss during transformations

---

## Findings

### Research Question 1: GDP per Capita and Happiness

**Finding**: Strong positive correlation (r ≈ 0.82) between GDP per capita and happiness score.

**Evidence**:
- Scatterplot analysis shows clear upward trend
- European countries cluster in high GDP, high happiness region
- Countries with GDP per capita >$40,000 average happiness >7.0
- Countries with GDP per capita <$5,000 average happiness <4.5

**Visualization**: `results/gdp_happiness_scatter.png`

**Interpretation**: Economic prosperity is strongly associated with national happiness, but the relationship is not perfectly linear. Some countries achieve relatively high happiness with moderate GDP (e.g., Costa Rica), while others with high GDP have lower happiness scores, suggesting other factors matter.

### Research Question 2: Life Expectancy and Happiness

**Finding**: Very strong positive correlation (r ≈ 0.80) between life expectancy and happiness.

**Evidence**:
- Countries with life expectancy >75 years average happiness >6.5
- Life expectancy ranges from 53 to 84 years in the dataset
- Strong clustering by continent in life expectancy-happiness space

**Visualization**: `results/life_exp_happiness_scatter.png`

**Interpretation**: Health and longevity are fundamental to national well-being. The correlation suggests that investments in healthcare and public health infrastructure contribute significantly to population happiness.

### Research Question 3: Regional Differences

**Finding**: Significant continental differences exist in the happiness-economy relationship.

**Evidence by Continent**:

**Europe**: 
- Highest average happiness (6.5)
- High GDP and life expectancy
- Low variation within continent

**Americas**:
- Moderate to high happiness (5.8 average)
- Wide variation in economic indicators
- North America higher than South America

**Asia**:
- Most diverse continent in our dataset
- Ranges from very high (Singapore) to low happiness
- Economic development varies dramatically

**Africa**:
- Lower average happiness (4.3)
- Lowest average GDP and life expectancy
- Some outliers achieving higher happiness than expected

**Oceania**:
- Small sample (Australia, New Zealand primarily)
- High happiness and economic development

**Visualization**: Both scatterplots use color coding by continent

### Research Question 4: Most Predictive Indicators

**Finding**: HDI (Human Development Index) is the strongest single predictor (r ≈ 0.84).

**Correlation Rankings with Happiness**:
1. HDI: r ≈ 0.84 (very strong)
2. GDP per capita: r ≈ 0.82 (very strong)
3. Life expectancy: r ≈ 0.80 (very strong)
4. Social support: r ≈ 0.78 (strong)
5. Healthy life expectancy contribution: r ≈ 0.78 (strong)
6. Freedom: r ≈ 0.56 (moderate)
7. Generosity: r ≈ 0.14 (weak)
8. Corruption perception: r ≈ -0.43 (moderate negative)

**Visualization**: `results/correlation_heatmap.png`

**Interpretation**: HDI combines income, education, and health, making it a comprehensive development measure. The strong correlation suggests that balanced development across multiple dimensions is more important than any single factor. Interestingly, generosity shows the weakest correlation, and corruption perception shows a moderate negative correlation as expected.

### Additional Insights

**Non-Economic Factors**:
- Social support shows strong correlation (r ≈ 0.78), emphasizing the importance of social connections
- Freedom to make life choices shows moderate correlation (r ≈ 0.56), suggesting autonomy matters
- Generosity shows weak correlation (r ≈ 0.14), indicating altruism is less tied to national happiness

**Economic vs. Social Factors**:
- Pure economic indicators (GDP, HDI) show strongest correlations
- Social factors (support, freedom) also significant but slightly weaker
- This suggests both material prosperity and social quality matter

**Country-Specific Outliers**:
Some countries achieve higher happiness than their economic indicators would predict, suggesting:
- Quality governance
- Strong social institutions
- Cultural factors
- Environmental quality
- Work-life balance policies

---

## Future Work

### Lessons Learned

**Data Curation Best Practices**:
1. **Country name standardization is critical**: We encountered 13+ naming inconsistencies that required careful mapping. Future projects should establish standardization early in the workflow.

2. **Provenance tracking adds value**: SHA-256 checksums and comprehensive metadata proved invaluable for validation and reproducibility. The upfront investment in provenance infrastructure paid dividends.

3. **Missing data documentation over imputation**: Our decision to document rather than impute missing values maintained data integrity and transparency, though it limited some analyses.

4. **Modular script architecture**: Separating cleaning, profiling, and merging into distinct scripts improved maintainability and debugging.

5. **Automated profiling catches issues early**: Our comprehensive profiling script identified quality issues before they propagated through the pipeline.

**Technical Lessons**:
1. **Platform-independent paths**: Using os.path.join() ensured cross-platform compatibility
2. **Comprehensive error handling**: Try-catch blocks and validation checks prevented silent failures
3. **JSON for metadata**: Structured format enabled both human and machine readability
4. **Version control discipline**: Detailed commit messages and clear branching strategy facilitated collaboration

**Analytical Lessons**:
1. **Correlation does not imply causation**: While we found strong correlations, we cannot claim economic development causes happiness
2. **Aggregate data masks individual variation**: Country-level analysis doesn't capture within-country inequality
3. **Single-year snapshot limitations**: 2018 data doesn't show trends or changes over time
4. **Cultural context matters**: Happiness measures may have different meanings across cultures

### Potential Extensions

**Methodological Improvements**:

1. **Time Series Analysis**:
   - Extend to multi-year data (2010-2024) to examine trends
   - Analyze how countries' happiness changes as economies develop
   - Test for Granger causality between economic growth and happiness changes

2. **Advanced Statistical Modeling**:
   - Multiple regression to identify independent effects of each factor
   - Ridge or Lasso regression to handle multicollinearity
   - Random forest for non-linear relationship modeling
   - Hierarchical models accounting for regional clustering

3. **Causal Inference**:
   - Difference-in-differences for policy interventions
   - Propensity score matching for quasi-experimental design
   - Instrumental variables to address endogeneity

**Data Enrichment**:

1. **Additional Variables**:
   - Climate data (temperature, natural disasters)
   - Political stability indices
   - Income inequality measures (Gini coefficient)
   - Education quality metrics
   - Healthcare access indicators
   - Environmental quality indices

2. **Sub-National Analysis**:
   - State/province-level data where available
   - Urban vs. rural happiness differences
   - Regional inequality within countries

3. **Qualitative Data**:
   - Policy case studies for outlier countries
   - Expert interviews on national well-being strategies
   - Cultural factor documentation

**Expanded Scope**:

1. **Comprehensive Global Coverage**:
   - Include more countries (currently 144)
   - Focus on under-represented regions
   - Better data for small island nations

2. **Domain-Specific Analysis**:
   - Healthcare system comparisons
   - Education system effectiveness
   - Social safety net analysis
   - Environmental sustainability trade-offs

3. **Interactive Visualization**:
   - Web-based dashboard (e.g., Plotly Dash, Shiny)
   - Interactive maps
   - User-controlled filtering and exploration
   - Real-time data updates

**Policy Applications**:

1. **Evidence-Based Recommendations**:
   - Identify cost-effective interventions for increasing happiness
   - Analyze countries that "punch above their weight" economically
   - Develop happiness-GDP efficiency metrics

2. **Predictive Modeling**:
   - Forecast happiness based on economic trends
   - Identify countries at risk of declining happiness
   - Model impact of policy scenarios

3. **Inequality Analysis**:
   - Within-country happiness distribution
   - Relationship between inequality and average happiness
   - Equity-efficiency trade-offs

### Reproducibility Improvements

**For Future Projects**:

1. **Docker Containerization**:
   - Create Dockerfile for complete environment specification
   - Push container to DockerHub for easy distribution
   - Eliminate "works on my machine" issues

2. **Automated Testing**:
   - Unit tests for data processing functions
   - Integration tests for full pipeline
   - Expected output validation

3. **Continuous Integration**:
   - GitHub Actions for automated testing
   - Automatic regeneration of results
   - Version-controlled result snapshots

4. **Enhanced Documentation**:
   - Video walkthrough of analysis
   - Annotated Jupyter notebooks
   - Interactive tutorial

### Open Questions

1. **Causality**: Does economic development cause happiness, or do happier populations drive economic development?

2. **Optimal Development Path**: What is the most efficient path from low to high happiness?

3. **Diminishing Returns**: At what GDP level does additional income stop improving happiness?

4. **Cultural Variation**: How do cultural differences affect the happiness-economy relationship?

5. **Sustainability**: Can happiness gains from economic growth be sustained environmentally?

---

## Reproducing This Analysis

### System Requirements

- **Operating System**: macOS, Linux, or Windows
- **Python**: Version 3.8 or higher
- **Disk Space**: Approximately 100 MB
- **Internet**: Required for initial data download from Box

### Step 1: Clone the Repository

```bash
git clone https://github.com/GregoriusAviantoro/IS-477.git
cd IS-477
```

### Step 2: Set Up Python Environment

**Option A: Using pip**
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Option B: Using conda**
```bash
conda create -n happiness-project python=3.8
conda activate happiness-project
pip install -r requirements.txt
```

### Step 3: Download Data from Box

The raw and processed data files are stored on Box due to GitHub file size limitations.

**Download Link**: [Box Folder - IS477 Project Data](#)

**Instructions**:
1. Click the Box link above
2. Download the entire `data` folder
3. Extract the downloaded folder
4. Place it in the project root directory, replacing the existing `data` folder

**Expected structure after download**:
```
IS-477/
├── data/
│   ├── raw/
│   │   ├── 2018.csv
│   │   └── gapminder_data_graphs.csv
│   └── processed/
│       ├── happiness_2018_cleaned.csv
│       ├── gapminder_2018_cleaned.csv
│       ├── happiness_economy_2018.csv
│       ├── cleaning_provenance.json
│       ├── data_profile_report.json
│       └── merge_report.json
```

**SHA-256 Checksums** (verify your downloads):
- `2018.csv`: [checksum will be in cleaning_provenance.json]
- `gapminder_data_graphs.csv`: [checksum will be in cleaning_provenance.json]

### Step 4: Run the Complete Analysis

**Option A: Run All Steps Automatically**
```bash
python run_all.py
```

This single command will execute the entire pipeline:
1. Data cleaning
2. Data profiling
3. Data integration
4. Visualization generation

**Option B: Run Each Step Manually**

If you prefer to run each step individually:

```bash
# Step 1: Clean the raw data
python src/clean_data.py

# Step 2: Profile the cleaned data
python src/profile_data.py

# Step 3: Merge the datasets
python src/merge_data.py

# Step 4: Generate visualizations
python src/visualize.py
```

### Step 5: Verify Results

After running the analysis, verify that the following files were created:

**Processed Data Files**:
- `data/processed/happiness_2018_cleaned.csv`
- `data/processed/gapminder_2018_cleaned.csv`
- `data/processed/happiness_economy_2018.csv`
- `data/processed/cleaning_provenance.json`
- `data/processed/data_profile_report.json`
- `data/processed/merge_report.json`

**Visualization Files**:
- `results/gdp_happiness_scatter.png`
- `results/life_exp_happiness_scatter.png`
- `results/correlation_heatmap.png`

### Step 6: View Results

**Visualizations**:
Open the PNG files in the `results/` folder using any image viewer.

**Data**:
Processed CSV files can be opened in Excel, any text editor, or loaded in Python/R for further analysis.

**Reports**:
JSON files contain detailed metadata and can be viewed in any text editor or parsed programmatically.

### Troubleshooting

**Issue: Module not found error**
```bash
# Solution: Ensure all dependencies are installed
pip install -r requirements.txt
```

**Issue: File not found error**
```bash
# Solution: Verify you're in the project root directory
pwd  # Should end with IS-477
# Solution: Ensure data folder is downloaded from Box
```

**Issue: Permission denied**
```bash
# Solution: Make scripts executable (macOS/Linux)
chmod +x src/*.py
```

**Issue: Different results than expected**
- Verify data file checksums match those in `cleaning_provenance.json`
- Ensure you're using the correct Python version (3.8+)
- Check package versions match `requirements.txt`

### Expected Runtime

- **Data cleaning**: ~10 seconds
- **Data profiling**: ~15 seconds
- **Data merging**: ~5 seconds
- **Visualization**: ~10 seconds
- **Total runtime**: ~40 seconds

### Validation

To validate your reproduction:

1. **Check file counts**: You should have 6 files in `data/processed/` and 3 in `results/`
2. **Check merged data**: `happiness_economy_2018.csv` should have 144 rows
3. **Visual inspection**: Scatterplots should show clear positive trends
4. **Correlation heatmap**: Should show values matching those in Findings section

---

## References

### Data Sources

1. Helliwell, J., Layard, R., & Sachs, J. (2018). *World Happiness Report 2018*. New York: Sustainable Development Solutions Network. Retrieved from https://www.kaggle.com/datasets/unsdsn/world-happiness

2. Gapminder Foundation. (2018). *Gapminder Global Development Data*. Compiled from World Bank, UN, and OECD sources. Licensed under CC BY 4.0. Retrieved from https://www.kaggle.com/datasets/albertovidalrod/gapminder-dataset

### Software and Libraries

3. McKinney, W. (2010). Data Structures for Statistical Computing in Python. *Proceedings of the 9th Python in Science Conference*, 56-61. https://doi.org/10.25080/Majora-92bf1922-00a

4. Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy. *Nature*, 585, 357-362. https://doi.org/10.1038/s41586-020-2649-2

5. Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90-95. https://doi.org/10.1109/MCSE.2007.55

6. Waskom, M. L. (2021). seaborn: statistical data visualization. *Journal of Open Source Software*, 6(60), 3021. https://doi.org/10.21105/joss.03021

### Methodological References

7. United Nations Development Programme. (2020). Human development report 2020: The next frontier: Human development and the Anthropocene. United Nations Development Programme. https://hdr.undp.org/content/human-development-report-2020

8. Diener, E., & Seligman, M. E. P. (2004). Beyond money: Toward an economy of well-being. Psychological Science in the Public Interest, 5(1), 1–31. https://doi.org/10.1111/j.0963-7214.2004.00501001.x

9. Easterlin, R. A. (1974). Does economic growth improve the human lot? Some empirical evidence. In P. A. David & M. W. Reder (Eds.), Nations and households in economic growth: Essays in honor of Moses Abramovitz (pp. 89–125). Academic Press.

10. Stevenson, B., & Wolfers, J. (2008). Economic growth and subjective well-being: Reassessing the Easterlin paradox. Brookings Papers on Economic Activity, 2008(1), 1–87. https://doi.org/10.1353/eca.0.0001

### Tools and Platforms

11. GitHub. (2024). *GitHub Documentation*. Retrieved from https://docs.github.com

12. Kaggle. (2024). *Kaggle Datasets Documentation*. Retrieved from https://www.kaggle.com/docs/datasets

---

## License

### Code License

This project's code is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Gregorius Aviantoro, Rishi Akula

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Data License

The data used in this project is licensed as follows:

- **World Happiness Report 2018**: Open access, publicly available
- **Gapminder Global Development Data**: CC BY 4.0 (Creative Commons Attribution 4.0 International)

When using this data, please provide appropriate attribution to the original sources.

---

## Acknowledgments

We would like to thank:

- The United Nations Sustainable Development Solutions Network for making the World Happiness Report data publicly available
- The Gapminder Foundation for their invaluable work in compiling and distributing global development data
- The IS-477 course instructors and teaching assistants at the University of Illinois Urbana-Champaign for their guidance throughout this project
- The open-source Python community for developing and maintaining the tools that made this analysis possible

---

## Contact

For questions, issues, or collaboration inquiries:

- **Project Repository**: https://github.com/GregoriusAviantoro/IS-477
- **Report Issues**: https://github.com/GregoriusAviantoro/IS-477/issues
- **Email**: [ga22@illinois.edu]

---

**Last Updated**: December 2024  
**Project Version**: 1.0  
**Repository**: https://github.com/GregoriusAviantoro/IS-477
