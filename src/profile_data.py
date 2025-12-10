"""
Data Profiling Script for Global Happiness and Economic Development Project
Author: Gregorius Aviantoro
Date: November 2025
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime
import json

def load_cleaned_data():
    """Load the cleaned datasets"""
    processed_dir = 'data/processed'
    
    happiness_path = os.path.join(processed_dir, 'happiness_2018_cleaned.csv')
    gapminder_path = os.path.join(processed_dir, 'gapminder_2018_cleaned.csv')
    
    happiness_df = pd.read_csv(happiness_path)
    gapminder_df = pd.read_csv(gapminder_path)
    
    return happiness_df, gapminder_df

def generate_descriptive_stats(df, dataset_name):
    """Generate descriptive statistics for numeric columns"""
    print(f"\n{'='*60}")
    print(f"DESCRIPTIVE STATISTICS: {dataset_name}")
    print('='*60)
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    stats = df[numeric_cols].describe()
    print(stats)
    
    return stats

def analyze_missing_values(df, dataset_name):
    """Analyze patterns in missing values"""
    print(f"\n{'='*60}")
    print(f"MISSING VALUE ANALYSIS: {dataset_name}")
    print('='*60)
    
    missing_count = df.isnull().sum()
    missing_pct = (missing_count / len(df) * 100).round(2)
    
    missing_df = pd.DataFrame({
        'Missing_Count': missing_count,
        'Missing_Percentage': missing_pct
    })
    
    missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values(
        'Missing_Count', ascending=False
    )
    
    if len(missing_df) > 0:
        print(missing_df)
    else:
        print("No missing values detected!")
    
    return missing_df

def analyze_data_types(df, dataset_name):
    """Analyze data types and structure"""
    print(f"\n{'='*60}")
    print(f"DATA TYPE ANALYSIS: {dataset_name}")
    print('='*60)
    
    dtype_summary = pd.DataFrame({
        'Column': df.columns,
        'Data_Type': df.dtypes.values,
        'Non_Null_Count': df.count().values,
        'Unique_Values': [df[col].nunique() for col in df.columns]
    })
    
    print(dtype_summary)
    return dtype_summary

def analyze_distributions(df, dataset_name):
    """Analyze distributions of key numeric variables"""
    print(f"\n{'='*60}")
    print(f"DISTRIBUTION ANALYSIS: {dataset_name}")
    print('='*60)
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    distribution_info = {}
    
    for col in numeric_cols:
        data = df[col].dropna()
        if len(data) > 0:
            distribution_info[col] = {
                'mean': float(data.mean()),
                'median': float(data.median()),
                'std': float(data.std()),
                'min': float(data.min()),
                'max': float(data.max()),
                'skewness': float(data.skew()),
                'kurtosis': float(data.kurtosis())
            }
            
            print(f"\n{col}:")
            print(f"  Mean: {distribution_info[col]['mean']:.2f}")
            print(f"  Median: {distribution_info[col]['median']:.2f}")
            print(f"  Std Dev: {distribution_info[col]['std']:.2f}")
            print(f"  Range: [{distribution_info[col]['min']:.2f}, {distribution_info[col]['max']:.2f}]")
            print(f"  Skewness: {distribution_info[col]['skewness']:.2f}")
    
    return distribution_info

def check_data_quality(df, dataset_name):
    """Perform data quality checks"""
    print(f"\n{'='*60}")
    print(f"DATA QUALITY CHECKS: {dataset_name}")
    print('='*60)
    
    quality_report = {}
    
    duplicates = df.duplicated().sum()
    quality_report['duplicate_rows'] = int(duplicates)
    print(f"Duplicate rows: {duplicates}")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    negative_checks = {}
    
    for col in numeric_cols:
        negative_count = (df[col] < 0).sum()
        if negative_count > 0:
            negative_checks[col] = int(negative_count)
            print(f"Negative values in {col}: {negative_count}")
    
    quality_report['negative_values'] = negative_checks
    
    outlier_info = {}
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
        if outliers > 0:
            outlier_info[col] = int(outliers)
    
    quality_report['potential_outliers'] = outlier_info
    
    if outlier_info:
        print(f"\nPotential outliers (IQR method):")
        for col, count in outlier_info.items():
            print(f"  {col}: {count} outliers")
    
    return quality_report

def analyze_categorical_variables(df, dataset_name):
    """Analyze categorical variables"""
    print(f"\n{'='*60}")
    print(f"CATEGORICAL VARIABLE ANALYSIS: {dataset_name}")
    print('='*60)
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    cat_summary = {}
    
    for col in categorical_cols:
        unique_count = df[col].nunique()
        cat_summary[col] = {
            'unique_values': int(unique_count),
            'top_values': df[col].value_counts().head(5).to_dict()
        }
        
        print(f"\n{col}:")
        print(f"  Unique values: {unique_count}")
        print(f"  Top 5 values:")
        for val, count in list(cat_summary[col]['top_values'].items())[:5]:
            print(f"    {val}: {count}")
    
    return cat_summary

def generate_profile_report(happiness_df, gapminder_df, output_dir):
    """Generate comprehensive profile report"""
    
    report = {
        'generation_timestamp': datetime.now().isoformat(),
        'happiness_dataset': {},
        'gapminder_dataset': {}
    }
    
    print("\n" + "="*60)
    print("GENERATING COMPREHENSIVE DATA PROFILES")
    print("="*60)
    
    print("\n\n### HAPPINESS DATASET ###\n")
    report['happiness_dataset']['descriptive_stats'] = generate_descriptive_stats(
        happiness_df, "Happiness 2018"
    ).to_dict()
    missing_result = analyze_missing_values(happiness_df, "Happiness 2018")
    report['happiness_dataset']['missing_values'] = missing_result.to_dict() if not missing_result.empty else {}
    report['happiness_dataset']['data_types'] = analyze_data_types(
        happiness_df, "Happiness 2018"
    ).to_dict()
    report['happiness_dataset']['distributions'] = analyze_distributions(
        happiness_df, "Happiness 2018"
    )
    report['happiness_dataset']['quality_checks'] = check_data_quality(
        happiness_df, "Happiness 2018"
    )
    report['happiness_dataset']['categorical_analysis'] = analyze_categorical_variables(
        happiness_df, "Happiness 2018"
    )
    
    print("\n\n### GAPMINDER DATASET ###\n")
    report['gapminder_dataset']['descriptive_stats'] = generate_descriptive_stats(
        gapminder_df, "Gapminder 2018"
    ).to_dict()
    missing_result = analyze_missing_values(gapminder_df, "Gapminder 2018")
    report['gapminder_dataset']['missing_values'] = missing_result.to_dict() if not missing_result.empty else {}
    report['gapminder_dataset']['data_types'] = analyze_data_types(
        gapminder_df, "Gapminder 2018"
    ).to_dict()
    report['gapminder_dataset']['distributions'] = analyze_distributions(
        gapminder_df, "Gapminder 2018"
    )
    report['gapminder_dataset']['quality_checks'] = check_data_quality(
        gapminder_df, "Gapminder 2018"
    )
    report['gapminder_dataset']['categorical_analysis'] = analyze_categorical_variables(
        gapminder_df, "Gapminder 2018"
    )
    
    report_path = os.path.join(output_dir, 'data_profile_report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"\nComplete profile report saved to: {report_path}")
    return report

def main():
    """Main execution function"""
    print("Loading cleaned datasets...")
    happiness_df, gapminder_df = load_cleaned_data()
    
    processed_dir = 'data/processed'
    report = generate_profile_report(happiness_df, gapminder_df, processed_dir)
    
    print("\n" + "="*60)
    print("PROFILING COMPLETE")
    print("="*60)
    print(f"\nHappiness Dataset: {len(happiness_df)} countries, {len(happiness_df.columns)} variables")
    print(f"Gapminder Dataset: {len(gapminder_df)} countries, {len(gapminder_df.columns)} variables")
    print("\nAll profiling tasks completed successfully!")

if __name__ == "__main__":
    main()