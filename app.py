import streamlit as st
import pandas as pd

st.title("VIC Traffic Violations Dashboard")

# Load data from Google Sheets
sheet_url = https://drive.google.com/file/d/10kd48Lkcg-FCG7OFHRBhbrjOJcy4KPCz/view?usp=drive_link
csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")

df = pd.read_csv(csv_url)

st.subheader("Sample Data")
st.dataframe(df.head())
