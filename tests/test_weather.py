import pandas as pd

from src.data_validation import (
    check_missing_values,
    check_duplicate_rows,
    check_dataset_shape,
)


def test_weather_dataset_shape():
    df = pd.read_csv("data/raw/weather_data.csv")

    assert check_dataset_shape(df) == (365, 12)


def test_weather_no_missing_values():
    df = pd.read_csv("data/raw/weather_data.csv")

    assert check_missing_values(df) == 0


def test_weather_no_duplicates():
    df = pd.read_csv("data/raw/weather_data.csv")

    assert check_duplicate_rows(df) == 0