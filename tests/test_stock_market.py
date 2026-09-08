import pandas as pd


def test_stock_market_dataset_shape():
    df = pd.read_csv("data/raw/stock_market_data.csv")

    assert df.shape == (252, 12)


def test_stock_market_no_unexpected_missing_values():
    df = pd.read_csv("data/raw/stock_market_data.csv")

    allowed_missing = {
        "Daily_Return": 1,
        "Cumulative_Return": 1
    }

    for column in df.columns:
        missing_count = df[column].isnull().sum()

        if column in allowed_missing:
            assert missing_count <= allowed_missing[column]
        else:
            assert missing_count == 0


def test_stock_market_no_duplicates():
    df = pd.read_csv("data/raw/stock_market_data.csv")

    assert df.duplicated().sum() == 0