import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import pandas as pd
import streamlit as st

from src.cleaning import remove_duplicates, fill_missing_values

st.title("AI Operations Copilot")

st.write("Welcome to the AI Operations Copilot!")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

# Store dataframe only the first time
    if "df" not in st.session_state:
        st.session_state.df = df

# From now on, always use the dataframe stored in session state
    df = st.session_state.df

    st.subheader("Data Preview")

    st.dataframe(df.head(10))
    col1, col2 = st.columns(2)
    st.subheader("Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    col4.metric("Duplicate Rows", df.duplicated().sum())
    st.subheader("Column Information")

    st.dataframe(df.dtypes.reset_index().rename(
        columns={
           "index":"Column",
           0:"Data Type"
        }
    ))
    st.subheader("Missing Values by Column")

    missing = (
        df.isnull()
            .sum()
            .reset_index()
    )

    missing.columns = ["Column", "Missing Values"]

    missing = missing[missing["Missing Values"] > 0]

    missing.columns = [
       "Column",
       "Missing Values"
    ]

    st.dataframe(missing)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Remove Duplicate Rows"):

            before = len(st.session_state.df)

            st.session_state.df = remove_duplicates(st.session_state.df)

            after = len(st.session_state.df)

            removed = before - after

            st.success(f"Removed {removed} duplicate rows.")

    with col2:
        if st.button("Fill Missing Values"):

            st.session_state.df = fill_missing_values(st.session_state.df)

            st.success("Missing values filled.")
