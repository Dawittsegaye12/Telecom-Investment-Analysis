import numpy as np
import pandas as pd
from scipy.stats import zscore

# Winsorization Function
def winsorize_column(column, lower_quantile=0.01, upper_quantile=0.99):
    lower_bound = column.quantile(lower_quantile)
    upper_bound = column.quantile(upper_quantile)
    return np.clip(column, lower_bound, upper_bound)

# Z-Score Outlier Removal Function
def remove_outliers_zscore(df, col, threshold=3):
    """
    Removes outliers from a column based on Z-score.

    Parameters:
        df (pd.DataFrame): DataFrame containing the column.
        col (str): Name of the column to remove outliers from.
        threshold (float): Z-score threshold for outlier removal.

    Returns:
        pd.DataFrame: DataFrame with outliers removed.
    """
    # Compute Z-scores
    z_scores = zscore(df[col].fillna(0))
    z_scores = pd.Series(z_scores, index=df.index)
    
    # Filter out rows based on Z-score threshold
    return df[(np.abs(z_scores) < threshold)]
# IQR-based Outlier Removal Function
def remove_outliers_iqr(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return column[(column >= lower_bound) & (column <= upper_bound)]