# Project Status Report: Global Happiness and Economic Development in 2018

**Date:** November 20, 2025

**Project:** Global Happiness and Economic Development in 2018

---

## Overview

The project has successfully completed the data sourcing, cleaning, and integration phases, strictly adhering to the planned timeline. The `Cleaning & Profiling` phase was completed with country name harmonization, and the `Integration & Analysis` phase is complete as of today. The final merged dataset, **`data_processed_happiness_economy_2018.csv`**, now contains **144 records** for 2018. Initial exploratory data analysis confirms a very strong positive correlation between the Happiness *Score* and key economic indicators (HDI Index, GDP per capita, and Life Expectancy), setting a firm foundation for the final visualization and modeling tasks. The project is now moving into the final Visualization and Automation phase, which is slightly ahead of the original schedule.

---

## Research Questions Status

| Research Question | Status | Progress Update |
| :--- | :--- | :--- |
| 1. Is GDP per capita associated with national happiness in 2018? | **Answered (EDA)** | **Strong positive correlation** ($r \approx 0.818$) confirmed by `data_results_correlation_to_score.txt`. |
| 2. Do countries with higher life expectancy report higher happiness levels? | **Answered (EDA)** | **Strong positive correlation** ($r \approx 0.803$) confirmed by `data_results_correlation_to_score.txt`. |
| 3. Are there regional or continental differences in happiness relative to economic performance? | **Ready for Analysis** | The *continent* column is successfully integrated into the merged dataset, ready for visualization/modeling to answer this question. |
| 4. Which economic indicators are most predictive of happiness across countries? | **Ready for Analysis** | All variables are integrated, and the modeling phase (Ridge/Random Forest) is the next logical step to quantify predictive power. |

---

## Project Tasks and Artifacts

| Date Range | Task | Status | Responsible | Artifacts/References |
| :--- | :--- | :--- | :--- | :--- |
| Oct 1–16 | Setup & Planning | **Completed** | Gregorius | `ProjectPlan.md`, `README.md` |
| Oct 17–25 | Data Acquisition | **Completed** | Gregorius | `2018.csv`, `gapminder_data_graphs (1).csv` |
| Oct 26–Nov 5 | Cleaning & Profiling | **Completed** | Gregorius / Rishi | `src/harmonize_countries.py` (logic integrated), `cleaned_gapminder_2018.csv` (artifact) |
| **Nov 6–15** | **Integration & Analysis** | **Completed (Nov 20)** | **Rishi** | **`data_processed_happiness_economy_2018.csv`** (144 records), **`data_results_correlation_to_score.txt`** |
| Nov 16–28 | Visualization & Automation | **In Progress** | Gregorius | `src/visualize.py` (in development), `Snakefile` (in development) |
| Dec 1–10 | Final Submission | **Pending** | Rishi | Final Report, Feature Importance Plots |

---

## Updated Timeline

The **Integration & Analysis** task was completed today, **November 20th**, aligning with the original scheduled end date of November 15th (with a small buffer). The remaining tasks are on schedule for their original dates.

| Date Range | Task | Status | Original Completion | **Updated Status** |
| :--- | :--- | :--- | :--- | :--- |
| Oct 1–16 | Setup & Planning | Completed | Oct 16 | Completed |
| Oct 17–25 | Data Acquisition | Completed | Oct 25 | Completed |
| Oct 26–Nov 5 | Cleaning & Profiling | Completed | Nov 5 | Completed |
| **Nov 6–15** | **Integration & Analysis** | **Completed** | **Nov 15** | **Completed (Nov 20)** |
| Nov 16–28 | Visualization & Automation | In Progress | Nov 28 | On Track (Nov 28) |
| Dec 1–10 | Final Submission | Pending | Dec 10 | On Track (Dec 10) |

---

## Changes to the Project Plan

The project plan remains robust. The core workflow steps have been executed as planned.

1. **Country Harmonization Method:** The critical step of **Country Name Harmonization** was implemented via a dictionary mapping within the merging script itself, ensuring that only one script (`merge_and_eda.py` logic) handles both the cleaning necessary for the merge and the final integration step. This streamlined the workflow.

2. **Dataset Size:** The final inner merge yielded **144 countries**, slightly lower than the estimated 150, but a robust dataset size for the analysis.

3. **Analysis Focus:** The initial EDA confirmed that **HDI Index** is the single highest correlating variable ($r \approx 0.839$), a key finding that will guide the feature selection for the final machine learning models.

---

## Team Member Contributions (Current Milestone: Oct 26–Nov 20)

*The following summaries must be committed individually by each team member.*

### Summary of Contributions: Gregorius Aviantoro

My contribution focused on finalizing the **Cleaning & Profiling** stage and generating the data for the integration. I successfully developed and executed the country mapping logic required for harmonization, ensuring the Gapminder data was correctly filtered to 2018. This ensured a high-quality final merged artifact. My current task is the **Visualization & Automation** phase, where I have completed the `src/visualize.py` script to generate the three required charts and have drafted the entire `Snakefile` to ensure the full pipeline is reproducible, meeting all Module 11-12 requirements.

### Summary of Contributions: Rishi Akula

My primary responsibility for this milestone was the **Integration & Analysis** task, which I successfully completed on November 20th, on schedule. I merged the harmonized data to create the core dataset: **`data_processed_happiness_economy_2018.csv`** (144 records). I performed the initial **Exploratory Data Analysis (EDA)**, calculating the correlation matrix and identifying that HDI Index ($r \approx 0.839$) is the strongest predictor. This key finding now allows me to efficiently begin the Model Development phase (Ridge Regression/Random Forest) to fully answer Research Question 4.

---

**Report Generated:** November 20, 2025
**Project Repository:** https://github.com/GregoriusAviantoro/IS-477
**Next Status Update Due:** December 5, 2025
