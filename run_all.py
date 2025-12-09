"""
Complete Workflow Automation Script
Global Happiness and Economic Development Project 2018

This script runs the entire analysis pipeline from data cleaning through visualization.

Author: Gregorius Aviantoro, Rishi Akula
Date: December 2024
"""

import subprocess
import sys
import os
from datetime import datetime

def print_header(message):
    """Print a formatted header message"""
    print("\n" + "="*70)
    print(message)
    print("="*70 + "\n")

def run_script(script_path, script_name):
    """Run a Python script and handle errors"""
    print(f"Running {script_name}...")
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        if result.stderr:
            print("Warnings:", result.stderr)
        print(f"✓ {script_name} completed successfully\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error running {script_name}:")
        print(e.stdout)
        print(e.stderr)
        return False
    except FileNotFoundError:
        print(f"✗ Error: {script_path} not found")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print_header("CHECKING DEPENDENCIES")
    required_packages = ['pandas', 'numpy', 'matplotlib', 'seaborn']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is NOT installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    print("\n✓ All dependencies are installed")
    return True

def check_input_data():
    """Check if required input data files exist"""
    print_header("CHECKING INPUT DATA")
    required_files = [
        'data/raw/2018.csv',
        'data/raw/gapminder_data_graphs.csv'
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            print(f"✓ {file_path} exists ({file_size:,} bytes)")
        else:
            print(f"✗ {file_path} NOT FOUND")
            all_exist = False
    
    if not all_exist:
        print("\nPlease download the data files from Box and place them in data/raw/")
        return False
    
    print("\n✓ All input data files are present")
    return True

def verify_outputs():
    """Verify that expected output files were created"""
    print_header("VERIFYING OUTPUTS")
    
    expected_files = {
        'Processed Data': [
            'data/processed/happiness_2018_cleaned.csv',
            'data/processed/gapminder_2018_cleaned.csv',
            'data/processed/happiness_economy_2018.csv',
            'data/processed/cleaning_provenance.json',
            'data/processed/data_profile_report.json',
            'data/processed/merge_report.json'
        ],
        'Visualizations': [
            'results/gdp_happiness_scatter.png',
            'results/life_exp_happiness_scatter.png',
            'results/correlation_heatmap.png'
        ]
    }
    
    all_created = True
    for category, files in expected_files.items():
        print(f"\n{category}:")
        for file_path in files:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"  ✓ {file_path} ({file_size:,} bytes)")
            else:
                print(f"  ✗ {file_path} NOT CREATED")
                all_created = False
    
    return all_created

def main():
    """Main execution function"""
    start_time = datetime.now()
    
    print_header("GLOBAL HAPPINESS AND ECONOMIC DEVELOPMENT PROJECT")
    print("Complete Workflow Automation")
    print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Check dependencies
    if not check_dependencies():
        print("\n✗ Dependency check failed. Exiting.")
        sys.exit(1)
    
    # Check input data
    if not check_input_data():
        print("\n✗ Input data check failed. Exiting.")
        sys.exit(1)
    
    # Define workflow steps
    workflow_steps = [
        ('src/clean_data.py', 'Data Cleaning'),
        ('src/profile_data.py', 'Data Profiling'),
        ('src/merge_data.py', 'Data Integration'),
        ('src/visualize.py', 'Visualization Generation')
    ]
    
    # Execute workflow
    print_header("EXECUTING WORKFLOW")
    
    success = True
    for script_path, script_name in workflow_steps:
        if not run_script(script_path, script_name):
            success = False
            print(f"\n✗ Workflow failed at: {script_name}")
            break
    
    if success:
        print_header("WORKFLOW COMPLETED SUCCESSFULLY")
        
        # Verify outputs
        if verify_outputs():
            print("\n✓ All expected output files were created")
        else:
            print("\n⚠ Some output files may be missing")
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print(f"\nCompleted at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total runtime: {duration:.1f} seconds")
        print("\nYou can now view the results:")
        print("  - Processed data: data/processed/")
        print("  - Visualizations: results/")
        print("\nTo reproduce these results, run: python run_all.py")
    else:
        print_header("WORKFLOW FAILED")
        print("Please check the error messages above and fix any issues.")
        sys.exit(1)

if __name__ == "__main__":
    main()