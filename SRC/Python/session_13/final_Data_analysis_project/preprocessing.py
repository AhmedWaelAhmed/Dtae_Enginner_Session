
# Purpose: Clean and inspect data (Steps A & B)
# ---------------------------------------------------------
import pandas as pd
import numpy as np

def check_data_types(df):
    """
    (Step A) Separates numerical and categorical columns.
    """
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    print(f"🔢 Numerical Columns ({len(num_cols)}): {num_cols}")
    print(f"📝 Categorical Columns ({len(cat_cols)}): {cat_cols}")
    return num_cols, cat_cols

def handle_hidden_nulls(df):
    """
    (Step B - Trick) Converts 'unknown' string to real NaN
    so Python can count them as missing values.
    """
    df = df.replace('unknown', np.nan)
    print("✅ All 'unknown' values converted to NaN.")
    return df

def get_missing_report(df):
    """
    (Step B - Analysis) Calculates missing ratio to decide strategy.
    """
    null_count = df.isnull().sum()
    null_ratio = (null_count / len(df)) * 100
    
    report = pd.DataFrame({
        'Missing Count': null_count,
        'Ratio (%)': null_ratio
    })
    
    # Return only columns with missing values, sorted
    return report[report['Missing Count'] > 0].sort_values('Ratio (%)', ascending=False)