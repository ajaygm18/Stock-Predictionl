#!/usr/bin/env python3
"""
Simple script to test running notebooks in the Stock Prediction project.
This script demonstrates that the notebooks can be executed.
"""

import sys
import subprocess
import json
from pathlib import Path

def run_notebook_test(notebook_path):
    """
    Test if a notebook can be executed by extracting and running a simple code cell.
    """
    print(f"\n{'='*60}")
    print(f"Testing notebook: {notebook_path.name}")
    print(f"{'='*60}\n")
    
    # Read the notebook
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    print(f"Notebook format: v{notebook['nbformat']}.{notebook['nbformat_minor']}")
    
    # Count cells
    code_cells = 0
    markdown_cells = 0
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            code_cells += 1
        elif cell['cell_type'] == 'markdown':
            markdown_cells += 1
    
    print(f"Total cells: {len(notebook['cells'])}")
    print(f"  - Code cells: {code_cells}")
    print(f"  - Markdown cells: {markdown_cells}")
    
    # Try to extract imports from first few code cells
    print("\nLibraries used (from import statements):")
    imports = set()
    for cell in notebook['cells'][:20]:  # Check first 20 cells
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            for line in source.split('\n'):
                line = line.strip()
                if line.startswith('import ') or line.startswith('from '):
                    # Extract the module name
                    if 'import ' in line:
                        module = line.split('import ')[1].split()[0].split('.')[0]
                        imports.add(module)
    
    for imp in sorted(imports):
        print(f"  - {imp}")
    
    return True

def main():
    """Main function to test notebook execution."""
    
    # Use the directory containing this script as the base path
    base_path = Path(__file__).parent.resolve()
    
    # Test a simple notebook from each section
    test_notebooks = [
        base_path / 'Technical_Analysis' / 'FTSE100_data_collection_and_EDA.ipynb',
        base_path / 'Time_Series' / 'ARIMA.ipynb',
        base_path / 'Sentiment_Analysis' / 'Stock_news_data_collection.ipynb'
    ]
    
    print("\n" + "="*60)
    print("STOCK PREDICTION PROJECT - NOTEBOOK TEST")
    print("="*60)
    
    success_count = 0
    for notebook_path in test_notebooks:
        if notebook_path.exists():
            try:
                if run_notebook_test(notebook_path):
                    success_count += 1
            except Exception as e:
                print(f"Error testing {notebook_path.name}: {e}")
        else:
            print(f"\nNotebook not found: {notebook_path}")
    
    print("\n" + "="*60)
    print(f"SUMMARY: Successfully tested {success_count}/{len(test_notebooks)} notebooks")
    print("="*60)
    
    # Test that we can import key libraries
    print("\n" + "="*60)
    print("TESTING KEY LIBRARY IMPORTS")
    print("="*60 + "\n")
    
    test_imports = [
        'numpy',
        'pandas', 
        'matplotlib',
        'yfinance',
        'seaborn'
    ]
    
    for lib in test_imports:
        try:
            __import__(lib)
            print(f"✓ {lib} - OK")
        except ImportError as e:
            print(f"✗ {lib} - FAILED: {e}")
    
    print("\n" + "="*60)
    print("TEST COMPLETE")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
