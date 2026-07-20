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

    st.dataframe(df)
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")