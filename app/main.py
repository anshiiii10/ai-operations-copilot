import pandas as pd
import streamlit as st

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

    missing.columns = [
       "Column",
       "Missing Values"
    ]

    st.dataframe(missing)