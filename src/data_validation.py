import pandas as pd


def check_missing_values(df):
    """Return the total number of missing values in a DataFrame."""
    return df.isnull().sum().sum()


def check_duplicate_rows(df):
    """Return the total number of duplicate rows in a DataFrame."""
    return df.duplicated().sum()


def check_dataset_shape(df):
    """Return the number of rows and columns in a DataFrame."""
    return df.shape