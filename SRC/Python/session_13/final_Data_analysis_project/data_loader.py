
# Purpose: Load the dataset
# ---------------------------------------------------------
import pandas as pd

def load_dataset(file_path):
    """
    Reads a CSV file and returns a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ File loaded successfully! Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
        return None