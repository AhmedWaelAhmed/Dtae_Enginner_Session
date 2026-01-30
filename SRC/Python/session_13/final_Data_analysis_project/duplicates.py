
# Purpose: Check and Remove Duplicates (Phase D)
# ---------------------------------------------------------
import pandas as pd

def check_duplicates(df):
    """
    Checks for duplicated rows in the dataset.
    """
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        print(f"⚠️ Found {dup_count} duplicated rows.")
    else:
        print("✅ No duplicates found. Data is unique.")
    return dup_count

def drop_duplicates(df):
    """
    Removes duplicated rows to prevent model bias.
    """
    initial_rows = df.shape[0]
    df_clean = df.drop_duplicates()
    dropped_count = initial_rows - df_clean.shape[0]
    
    if dropped_count > 0:
        print(f"🗑️ Removed {dropped_count} duplicates successfully.")
    
    return df_clean