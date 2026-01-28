# ---------------------------------------------------------
# File Name: outliers.py
# Purpose: Detect and Handle Outliers (Phase C)
# ---------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def detect_outliers_iqr(df, col_name):
    """
    Calculates the IQR fences and counts outliers.
    Returns the lower and upper fences.
    """
    Q1 = df[col_name].quantile(0.25)
    Q3 = df[col_name].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    
    # Count outliers for reporting
    outliers_count = df[(df[col_name] < lower_fence) | (df[col_name] > upper_fence)].shape[0]
    
    print(f"📊 Column: {col_name}")
    print(f"   - Fences: {lower_fence:.2f} to {upper_fence:.2f}")
    print(f"   - Outliers Detected: {outliers_count}")
    
    return lower_fence, upper_fence

def visualize_boxplots(df, num_cols):
    """
    Plots boxplots for numerical columns to visualize outliers.
    """
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(num_cols):
        plt.subplot(1, len(num_cols), i+1)
        sns.boxplot(x=df[col], color='orange')
        plt.title(f'Boxplot: {col}')
    plt.tight_layout()
    plt.show()

def cap_outliers(df, col_name):
    """
    Caps (clips) outliers to the lower and upper fences.
    This preserves the data but reduces the impact of extreme values.
    """
    lower, upper = detect_outliers_iqr(df, col_name)
    
    # Apply Capping: 
    # Values < lower become lower_fence
    # Values > upper become upper_fence
    df[col_name] = df[col_name].clip(lower=lower, upper=upper)
    print(f"✅ Capped outliers in '{col_name}' successfully.\n")
    return df