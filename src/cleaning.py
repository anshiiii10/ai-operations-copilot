import pandas as pd


def remove_duplicates(df):
    return df.drop_duplicates()


def fill_missing_values(df):
    cleaned_df = df.copy()

    for column in cleaned_df.columns:

        if cleaned_df[column].dtype in ["int64", "float64"]:
            cleaned_df[column] = cleaned_df[column].fillna(
                cleaned_df[column].median()
            )

        else:
            cleaned_df[column] = cleaned_df[column].fillna("Unknown")

    return cleaned_df