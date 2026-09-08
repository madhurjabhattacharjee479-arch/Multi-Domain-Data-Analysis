import pandas as pd

from src.data_validation import (
    check_missing_values,
    check_duplicate_rows,
    check_dataset_shape,
)


def test_check_missing_values():
    df = pd.DataFrame({
        "A": [1, 2, None],
        "B": [4, 5, 6]
    })

    assert check_missing_values(df) == 1


def test_check_duplicate_rows():
    df = pd.DataFrame({
        "A": [1, 2, 2],
        "B": [3, 4, 4]
    })

    assert check_duplicate_rows(df) == 1


def test_check_dataset_shape():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    })

    assert check_dataset_shape(df) == (3, 2)