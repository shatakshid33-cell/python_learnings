"""Reusable cleaning function built on Day 2."""
import pandas as pd
import numpy as np


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Clean a raw DataFrame: handle missing values, duplicates, whitespace,
    and inconsistent formatting.

    Fill in each step as you complete the Day 2 practice questions.
    """
    df = df.copy()

    # 1. Drop columns with >50% missing values
    # df = df.loc[:, df.isna().mean() < 0.5]

    # 2. Fill missing numeric values with median
    # num_cols = df.select_dtypes(include=np.number).columns
    # df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # 3. Fill missing categorical values with mode
    # cat_cols = df.select_dtypes(include='object').columns
    # for c in cat_cols:
    #     df[c] = df[c].fillna(df[c].mode()[0])

    # 4. Drop exact duplicates
    # df = df.drop_duplicates()

    # 5. Strip/lowercase string columns
    # for c in cat_cols:
    #     df[c] = df[c].str.strip().str.lower()

    return df
