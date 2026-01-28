# ---------------------------------------------------------
# File Name: visualization.py
# Purpose: Bivariate Analysis (Phase 2 - Right Side)
# ---------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(df):
    """
    (Num vs Num)
    Calculates and plots the correlation matrix for numerical columns.
    Goal: Find if variables are related (e.g., duration vs campaign).
    """
    # Select only numerical columns
    num_df = df.select_dtypes(include=['number'])
    
    plt.figure(figsize=(6, 4))
    correlation = num_df.corr()
    
    # Draw heatmap
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap (Numerical Variables)')
    plt.show()

def plot_cat_vs_cat(df, col_x, col_target):
    """
    (Cat vs Cat)
    Creates a Stacked Bar Chart to compare distributions.
    Goal: See if 'Job' affects 'Deposit' (Yes/No).
    """
    plt.figure(figsize=(12, 6))
    
    # Create a cross-tabulation (contingency table)
    cross_tab = pd.crosstab(df[col_x], df[col_target])
    
    # Plot stacked bar
    cross_tab.plot(kind='bar', stacked=True, color=['#ff9999','#66b3ff'], figsize=(12,6))
    plt.title(f'Relationship: {col_x} vs {col_target}')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title=col_target)
    plt.tight_layout()
    plt.show()

def plot_num_vs_cat(df, col_num, col_cat):
    """
    (Num vs Cat)
    Uses Boxplots to compare statistics across groups.
    Goal: Do people with higher 'Balance' subscribe more?
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col_cat, y=col_num, data=df, palette='Set2')
    plt.title(f'Distribution of {col_num} by {col_cat}')
    plt.show()