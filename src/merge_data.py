"""
Data Integration Script for Global Happiness and Economic Development Project
Author: Gregorius Aviantoro
Date: November 2025
"""

import pandas as pd
import os
from datetime import datetime
import json

def load_cleaned_datasets():
    """Load the cleaned datasets"""
    print("Loading cleaned datasets...")
    processed_dir = 'data/processed'
    
    happiness_path = os.path.join(processed_dir, 'happiness_2018_cleaned.csv')
    gapminder_path = os.path.join(processed_dir, 'gapminder_2018_cleaned.csv')
    
    happiness_df = pd.read_csv(happiness_path)
    gapminder_df = pd.read_csv(gapminder_path)
    
    print(f"Happiness dataset: {len(happiness_df)} countries")
    print(f"Gapminder dataset: {len(gapminder_df)} countries")
    
    return happiness_df, gapminder_df

def merge_datasets(happiness_df, gapminder_df):
    """Merge the two datasets on country name"""
    print("\nMerging datasets on 'country' column...")
    
    merged_df = pd.merge(
        happiness_df,
        gapminder_df,
        on='country',
        how='inner'
    )
    
    print(f"Merged dataset: {len(merged_df)} countries successfully matched")
    
    return merged_df

def analyze_merge_quality(happiness_df, gapminder_df, merged_df):
    """Analyze the quality of the merge"""
    print("\n" + "="*60)
    print("MERGE QUALITY ANALYSIS")
    print("="*60)
    
    happiness_only = set(happiness_df['country']) - set(gapminder_df['country'])
    print(f"\nCountries in Happiness dataset only: {len(happiness_only)}")
    if len(happiness_only) > 0 and len(happiness_only) <= 10:
        print("  " + ", ".join(sorted(list(happiness_only))))
    
    gapminder_only = set(gapminder_df['country']) - set(happiness_df['country'])
    print(f"\nCountries in Gapminder dataset only: {len(gapminder_only)}")
    if len(gapminder_only) > 0 and len(gapminder_only) <= 10:
        print("  " + ", ".join(sorted(list(gapminder_only))))
    
    success_rate = (len(merged_df) / len(happiness_df)) * 100
    print(f"\nMerge success rate: {success_rate:.1f}%")
    
    print(f"\nMissing values in merged dataset:")
    missing_counts = merged_df.isnull().sum()
    missing_counts = missing_counts[missing_counts > 0]
    if len(missing_counts) > 0:
        print(missing_counts)
    else:
        print("  No missing values!")
    
    return {
        'happiness_only': list(happiness_only),
        'gapminder_only': list(gapminder_only),
        'merge_success_rate': success_rate,
        'merged_country_count': len(merged_df)
    }

def save_merged_dataset(merged_df, output_dir):
    """Save the merged dataset"""
    output_path = os.path.join(output_dir, 'happiness_economy_2018.csv')
    merged_df.to_csv(output_path, index=False)
    print(f"\nMerged dataset saved to: {output_path}")
    return output_path

def save_merge_report(merge_quality, output_dir):
    """Save a report about the merge"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'merge_statistics': merge_quality
    }
    
    report_path = os.path.join(output_dir, 'merge_report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Merge report saved to: {report_path}")

def generate_summary_statistics(merged_df):
    """Generate summary statistics for the merged dataset"""
    print("\n" + "="*60)
    print("MERGED DATASET SUMMARY")
    print("="*60)
    
    print(f"\nTotal countries: {len(merged_df)}")
    print(f"Total variables: {len(merged_df.columns)}")
    
    print(f"\nContinents represented:")
    print(merged_df['continent'].value_counts())
    
    print(f"\nKey statistics:")
    print(f"  Average happiness score: {merged_df['happiness_score'].mean():.2f}")
    print(f"  Average GDP per capita: ${merged_df['gdp_per_capita'].mean():.2f}")
    print(f"  Average life expectancy: {merged_df['life_expectancy'].mean():.1f} years")
    if 'hdi' in merged_df.columns:
        print(f"  Average HDI: {merged_df['hdi'].mean():.3f}")

def main():
    """Main execution function"""
    processed_dir = 'data/processed'
    
    happiness_df, gapminder_df = load_cleaned_datasets()
    merged_df = merge_datasets(happiness_df, gapminder_df)
    merge_quality = analyze_merge_quality(happiness_df, gapminder_df, merged_df)
    save_merged_dataset(merged_df, processed_dir)
    save_merge_report(merge_quality, processed_dir)
    generate_summary_statistics(merged_df)
    
    print("\n" + "="*60)
    print("INTEGRATION COMPLETE")
    print("="*60)
    print("\nAll files have been successfully merged!")

if __name__ == "__main__":
    main()
    