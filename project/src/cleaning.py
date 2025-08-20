import pandas as pd

def fill_missing_median(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in numeric columns with their median.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe with missing values.

    Returns
    -------
    pd.DataFrame
        Dataframe with missing values filled.
    """
    df_filled = df.copy()
    median_values = df_filled.median(numeric_only=True)
    df_filled = df_filled.fillna(median_values)
    return df_filled


def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows with any missing values.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    return df.dropna()


def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize numeric columns to the range [0, 1].

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Dataframe with normalized numeric values.
    """
    df_normalized = df.copy()
    numeric = df_normalized.select_dtypes(include="number")
    df_normalized[numeric.columns] = (
        (numeric - numeric.min()) / (numeric.max() - numeric.min())
    )
    return df_normalized
