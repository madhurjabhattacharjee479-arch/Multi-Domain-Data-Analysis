import pandas as pd

from src.data_validation import (
    check_missing_values,
    check_duplicate_rows,
    check_dataset_shape,
)


def test_stock_market_dataset_shape():
    df = pd.read_csv("data/raw/stock_market_data.csv")
    assert check_dataset_shape(df) == (252, 12)


def test_stock_market_no_unexpected_missing_values():
    df = pd.read_csv("data/raw/stock_market_data.csv")

    missing_by_column = df.isnull().sum()

    assert missing_by_column["Daily_Return"] <= 1
    assert missing_by_column["Cumulative_Return"] <= 1

    other_columns = [
        column
        for column in df.columns
        if column not in {"Daily_Return", "Cumulative_Return"}
    ]

    assert missing_by_column[other_columns].sum() == 0
    assert check_missing_values(df) == 2


def test_stock_market_no_duplicates():
    df = pd.read_csv("data/raw/stock_market_data.csv")
    assert check_duplicate_rows(df) == 0