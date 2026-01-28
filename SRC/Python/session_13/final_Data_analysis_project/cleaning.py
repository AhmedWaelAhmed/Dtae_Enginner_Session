# ---------------------------------------------------------
# File Name: cleaning.py
# Purpose: Apply specific cleaning actions (Drop, Fill, etc.)
# ---------------------------------------------------------
import pandas as pd

def drop_useless_columns(df, columns):
    """
    Removes columns that are too corrupted (like 'poutcome').
    """
    df_clean = df.drop(columns=columns, errors='ignore')
    print(f"🗑️ Successfully dropped columns: {columns}")
    return df_clean

def fill_with_mode(df, columns):
    """
    Fills null values with the most frequent value (Mode).
    Great for categorical columns like 'contact'.
    """
    for col in columns:
        if col in df.columns:
            mode_value = df[col].mode()[0]
            df[col] = df[col].fillna(mode_value)
            print(f"🔧 Filled nulls in '{col}' with mode: '{mode_value}'")
    return df

def drop_rows(df, columns):
    """
    Drops rows if they have a missing value in specific columns.
    Great for small missing errors like 'job'.
    """
    initial_count = len(df)
    df_clean = df.dropna(subset=columns)
    dropped_count = initial_count - len(df_clean)
    print(f"✂️ Dropped {dropped_count} rows due to missing values in {columns}")
    return df_clean