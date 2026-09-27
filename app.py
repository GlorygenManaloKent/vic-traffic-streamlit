import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("VIC Traffic Violations Dashboard")

data = [
    ["D1001", "Sarah Lopez", "Speeding", 15, 350, "2026-03-12", 3, "Paid", 1, "O455"],
    ["D1002", "Mark Tan", "Red Light", 0, 450, "2026-01-22", 1, "Unpaid", 0, "O322"],
    # ... you will paste all 50 records here later ...
]

columns = [
    "Driver ID", "Driver Name", "Violation Type", "Speed Over Limit",
    "Fine Amount", "Violation Date", "Violation Month",
    "Payment Status", "Previous Violations", "Officer ID"
]

df = pd.DataFrame(data, columns=columns)

st.subheader("Sample Data")
st.dataframe(df.head())
