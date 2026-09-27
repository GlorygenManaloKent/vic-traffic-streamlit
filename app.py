import streamlit as st
import pandas as pd

st.title("VIC Traffic Violations Dashboard")

# Load data
file_id = "10kd48Lkcg-FCG7OFHRBhbrjOJcy4KPCz"
csv_url = f"https://drive.google.com/uc?export=download&id={file_id}"

df = pd.read_csv(csv_url)


# Sidebar Filters
st.sidebar.header("Filters")

violation_filter = st.sidebar.multiselect(
    "Select Violation Type:",
    options=df["Violation Type"].unique(),
    default=df["Violation Type"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Select Payment Status:",
    options=df["Payment Status"].unique(),
    default=df["Payment Status"].unique()
)

month_filter = st.sidebar.multiselect(
    "Select Month:",
    options=sorted(df["Violation Month"].unique()),
    default=sorted(df["Violation Month"].unique())
)

# Apply filters
filtered_df = df[
    (df["Violation Type"].isin(violation_filter)) &
    (df["Payment Status"].isin(payment_filter)) &
    (df["Violation Month"].isin(month_filter))
]


st.subheader("Sample Data")
st.dataframe(df.head())


st.subheader("Bar Chart: Violations by Type")

fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.countplot(data=filtered_df, x="Violation Type", palette="viridis", ax=ax1)
ax1.set_title("Number of Violations by Type")
ax1.tick_params(axis='x', rotation=45)

st.pyplot(fig1)

st.markdown("**Interpretation:** Speeding appears as the most frequent violation, suggesting it is a key focus area for enforcement.")

st.subheader("Pie Chart: Payment Status")

payment_counts = filtered_df["Payment Status"].value_counts()

fig2, ax2 = plt.subplots(figsize=(4, 4))
ax2.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%", colors=["#4CAF50", "#FF5252"])
ax2.set_title("Payment Status Distribution")

st.pyplot(fig2)

st.markdown("**Interpretation:** A high proportion of unpaid fines may indicate the need for better follow-up or reminder systems.")

st.subheader("Trend Analysis: Violations by Month")

monthly_counts = filtered_df.groupby("Violation Month").size()

fig3, ax3 = plt.subplots(figsize=(8, 4))
monthly_counts.plot(kind="line", marker="o", ax=ax3, color="blue")
ax3.set_title("Trend of Violations by Month")
ax3.set_xlabel("Month")
ax3.set_ylabel("Number of Violations")
ax3.grid(True)

st.pyplot(fig3)

st.markdown("**Interpretation:** Peaks in certain months (e.g., March–April) may reflect seasonal travel patterns or enforcement campaigns.")


