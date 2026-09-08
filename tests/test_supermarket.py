import pandas as pd

from src.data_validation import (
    check_missing_values,
    check_duplicate_rows,
    check_dataset_shape,
)


def test_supermarket_dataset_shape():
    df = pd.read_csv("data/raw/supermarket_sales.csv")

    assert check_dataset_shape(df) == (2000, 14)


def test_supermarket_no_missing_values():
    df = pd.read_csv("data/raw/supermarket_sales.csv")

    assert check_missing_values(df) == 0


def test_supermarket_no_duplicates():
    df = pd.read_csv("data/raw/supermarket_sales.csv")

    assert check_duplicate_rows(df) == 0