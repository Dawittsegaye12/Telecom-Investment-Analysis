import pandas as pd
import numpy as np

def fill_numeric_missing_values(df):
    """
    Fill missing values in numeric columns using the mean of each column.

    Parameters:
    - df: DataFrame containing the data

    Returns:
    - DataFrame with missing values filled in numeric columns
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        mean_value = df[col].mean()
        df[col] = df[col].fillna(mean_value)
    return df


def fill_categorical_missing_values(df):
    """
    Fill missing values in categorical columns with the mode of each column.

    Parameters:
    - df: DataFrame containing the data

    Returns:
    - DataFrame with missing values filled in categorical columns
    """
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        mode_value = df[col].mode()[0]
        df[col] = df[col].fillna(mode_value)
    return df