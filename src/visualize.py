"""
Visualization Script for Global Happiness and Economic Development Project
Author: Gregorius Aviantoro
Date: November 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_merged_data():
    """Load the merged dataset"""
    print("Loading merged dataset...")
    processed_dir = 'data/processed'
    merged_path = os.path.join(processed_dir, 'happiness_economy_2018.csv')
    df = pd.read_csv(merged_path)
    print(f"Loaded {len(df)} countries")
    return df

def create_gdp_happiness_scatter(df, output_dir):
    """Create scatterplot: GDP per capita vs Happiness Score"""
    print("\nCreating GDP vs Happiness scatterplot...")
    
    plt.figure(figsize=(12, 8))
    
    continents = df['continent'].unique()
    colors = {'Africa': 'red', 'Americas': 'blue', 'Asia': 'green', 
              'Europe': 'purple', 'Oceania': 'orange'}
    
    for continent in continents:
        data = df[df['continent'] == continent]
        plt.scatter(data['gdp_per_capita'], data['happiness_score'], 
                   label=continent, alpha=0.6, s=100, 
                   color=colors.get(continent, 'gray'))
    
    plt.xlabel('GDP per Capita (USD)', fontsize=12)
    plt.ylabel('Happiness Score', fontsize=12)
    plt.title('GDP per Capita vs Happiness Score by Continent (2018)', fontsize=14)
    plt.legend(title='Continent')
    plt.grid(True, alpha=0.3)
    
    output_path = os.path.join(output_dir, 'gdp_happiness_scatter.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved to: {output_path}")
    plt.close()

def create_life_exp_happiness_scatter(df, output_dir):
    """Create scatterplot: Life Expectancy vs Happiness Score"""
    print("\nCreating Life Expectancy vs Happiness scatterplot...")
    
    plt.figure(figsize=(12, 8))
    
    continents = df['continent'].unique()
    colors = {'Africa': 'red', 'Americas': 'blue', 'Asia': 'green', 
              'Europe': 'purple', 'Oceania': 'orange'}
    
    for continent in continents:
        data = df[df['continent'] == continent]
        plt.scatter(data['life_expectancy'], data['happiness_score'], 
                   label=continent, alpha=0.6, s=100, 
                   color=colors.get(continent, 'gray'))
    
    plt.xlabel('Life Expectancy (years)', fontsize=12)
    plt.ylabel('Happiness Score', fontsize=12)
    plt.title('Life Expectancy vs Happiness Score by Continent (2018)', fontsize=14)
    plt.legend(title='Continent')
    plt.grid(True, alpha=0.3)
    
    output_path = os.path.join(output_dir, 'life_exp_happiness_scatter.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved to: {output_path}")
    plt.close()

def create_correlation_heatmap(df, output_dir):
    """Create correlation heatmap for numeric variables"""
    print("\nCreating correlation heatmap...")
    
    numeric_cols = ['happiness_score', 'gdp_per_capita', 'life_expectancy', 
                   'hdi', 'social_support', 'freedom', 'generosity']
    
    correlation_matrix = df[numeric_cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                fmt='.2f', square=True, linewidths=1)
    plt.title('Correlation Matrix: Happiness and Economic Indicators (2018)', fontsize=14)
    plt.tight_layout()
    
    output_path = os.path.join(output_dir, 'correlation_heatmap.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved to: {output_path}")
    plt.close()

def main():
    """Main execution function"""
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)
    
    df = load_merged_data()
    
    create_gdp_happiness_scatter(df, results_dir)
    create_life_exp_happiness_scatter(df, results_dir)
    create_correlation_heatmap(df, results_dir)
    
    print("\n" + "="*60)
    print("VISUALIZATION COMPLETE")
    print("="*60)
    print(f"\nAll visualizations saved to: {results_dir}/")
    print("Files created:")
    print("  - gdp_happiness_scatter.png")
    print("  - life_exp_happiness_scatter.png")
    print("  - correlation_heatmap.png")

if __name__ == "__main__":
    main()