"""
Data Cleaning Script for Global Happiness and Economic Development Project
Author: Gregorius Aviantoro
Date: November 2025
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime
import hashlib
import json

def calculate_file_hash(filepath):
    """Calculate SHA-256 hash of a file"""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_happiness_data(filepath):
    """Load and perform initial inspection of happiness data"""
    print("Loading World Happiness Report 2018...")
    df = pd.read_csv(filepath)
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    return df

def load_gapminder_data(filepath):
    """Load and filter Gapminder data for 2018"""
    print("\nLoading Gapminder data...")
    df = pd.read_csv(filepath)
    print(f"Original shape: {df.shape}")
    
    df_2018 = df[df['year'] == 2018].copy()
    print(f"Filtered to 2018 - Shape: {df_2018.shape}")
    print(f"Columns: {df_2018.columns.tolist()}")
    return df_2018

def standardize_country_names(df, country_col):
    """Standardize country names to ensure consistent merging"""
    country_mappings = {
        'United States': 'United States',
        'United Kingdom': 'United Kingdom',
        'South Korea': 'South Korea',
        'North Korea': 'North Korea',
        'Czech Republic': 'Czech Republic',
        'Hong Kong': 'Hong Kong',
        'Taiwan': 'Taiwan',
        'Palestinian Territories': 'Palestine',
        'Congo (Brazzaville)': 'Congo, Rep.',
        'Congo (Kinshasa)': 'Congo, Dem. Rep.',
        'Trinidad & Tobago': 'Trinidad and Tobago',
        'Northern Cyprus': 'Cyprus',
        'Ivory Coast': "Cote d'Ivoire",
    }
    
    df[country_col] = df[country_col].replace(country_mappings)
    df[country_col] = df[country_col].str.strip()
    
    return df

def clean_happiness_data(df):
    """Clean World Happiness Report data"""
    print("\nCleaning Happiness data...")
    
    column_mapping = {
        'Overall rank': 'happiness_rank',
        'Country or region': 'country',
        'Score': 'happiness_score',
        'GDP per capita': 'happiness_gdp_contribution',
        'Social support': 'social_support',
        'Healthy life expectancy': 'happiness_life_exp_contribution',
        'Freedom to make life choices': 'freedom',
        'Generosity': 'generosity',
        'Perceptions of corruption': 'corruption_perception'
    }
    
    df = df.rename(columns=column_mapping)
    df = standardize_country_names(df, 'country')
    
    print(f"\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    df = df.dropna(subset=['happiness_score'])
    
    print(f"\nMissing values after removing incomplete happiness scores:")
    print(df.isnull().sum())
    print(f"Final cleaned happiness data shape: {df.shape}")
    
    return df

def clean_gapminder_data(df):
    """Clean Gapminder data filtered to 2018"""
    print("\nCleaning Gapminder data...")
    
    column_mapping = {
        'country': 'country',
        'continent': 'continent',
        'year': 'year',
        'life_exp': 'life_expectancy',
        'hdi_index': 'hdi',
        'co2_consump': 'co2_per_capita',
        'gdp': 'gdp_per_capita',
        'services': 'service_workers_pct'
    }
    
    df = df.rename(columns=column_mapping)
    df = standardize_country_names(df, 'country')
    
    print(f"\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    missing_summary = df.isnull().sum()
    print(f"\nPercentage of missing values:")
    print((missing_summary / len(df) * 100).round(2))
    print(f"Final cleaned Gapminder data shape: {df.shape}")
    
    return df

def save_provenance_info(happiness_path, gapminder_path, output_dir):
    """Save provenance information"""
    provenance = {
        'timestamp': datetime.now().isoformat(),
        'datasets': {
            'happiness_2018': {
                'source_path': happiness_path,
                'source_url': 'https://www.kaggle.com/datasets/unsdsn/world-happiness',
                'file_hash': calculate_file_hash(happiness_path),
                'description': 'World Happiness Report 2018'
            },
            'gapminder': {
                'source_path': gapminder_path,
                'source_url': 'https://www.kaggle.com/datasets/albertovidalrod/gapminder-dataset',
                'file_hash': calculate_file_hash(gapminder_path),
                'description': 'Gapminder Global Development Data (filtered to 2018)'
            }
        },
        'python_version': pd.__version__,
        'pandas_version': pd.__version__,
        'numpy_version': np.__version__,
        'cleaning_steps': [
            'Standardized country names for consistent merging',
            'Renamed columns for clarity and consistency',
            'Filtered Gapminder data to year 2018',
            'Removed rows with missing happiness scores',
            'Documented all missing value patterns'
        ]
    }
    
    provenance_path = os.path.join(output_dir, 'cleaning_provenance.json')
    with open(provenance_path, 'w') as f:
        json.dump(provenance, f, indent=2)
    
    print(f"\nProvenance information saved to: {provenance_path}")

def main():
    """Main execution function"""
    raw_data_dir = 'data/raw'
    processed_data_dir = 'data/processed'
    
    happiness_path = os.path.join(raw_data_dir, '2018.csv')
    gapminder_path = os.path.join(raw_data_dir, 'gapminder_data_graphs.csv')
    
    os.makedirs(processed_data_dir, exist_ok=True)
    
    happiness_df = load_happiness_data(happiness_path)
    gapminder_df = load_gapminder_data(gapminder_path)
    
    happiness_clean = clean_happiness_data(happiness_df)
    gapminder_clean = clean_gapminder_data(gapminder_df)
    
    happiness_output = os.path.join(processed_data_dir, 'happiness_2018_cleaned.csv')
    gapminder_output = os.path.join(processed_data_dir, 'gapminder_2018_cleaned.csv')
    
    happiness_clean.to_csv(happiness_output, index=False)
    gapminder_clean.to_csv(gapminder_output, index=False)
    
    print(f"\nCleaned happiness data saved to: {happiness_output}")
    print(f"Cleaned gapminder data saved to: {gapminder_output}")
    
    save_provenance_info(happiness_path, gapminder_path, processed_data_dir)
    
    print("\n" + "="*60)
    print("CLEANING SUMMARY")
    print("="*60)
    print(f"\nHappiness Dataset:")
    print(f"  - Countries: {len(happiness_clean)}")
    print(f"  - Variables: {len(happiness_clean.columns)}")
    print(f"  - Average happiness score: {happiness_clean['happiness_score'].mean():.2f}")
    
    print(f"\nGapminder Dataset:")
    print(f"  - Countries: {len(gapminder_clean)}")
    print(f"  - Variables: {len(gapminder_clean.columns)}")
    print(f"  - Continents represented: {gapminder_clean['continent'].nunique()}")
    
    print("\nData cleaning complete!")

if __name__ == "__main__":
    main()