import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Fraud Dashboard",
    layout="wide"
)

st.title("Overview Dashboard")


@st.cache_data
def load_data():

    cols = [
        'TransactionAmt',
        'isFraud'
    ]

    return pd.read_csv(
        "Data.csv.gz",
        usecols=cols,
        compression="gzip"
    )

df = load_data()


total_transactions = len(df)

total_fraud = int(
    df['isFraud'].sum()
)

detection_rate = round(
    (total_fraud / total_transactions) * 100,
    2
)

avg_amount = round(
    df['TransactionAmt'].mean(),
    2
)


c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Transactions",
    f"{total_transactions:,}"
)

c2.metric(
    "Frauds",
    f"{total_fraud:,}"
)

c3.metric(
    "Fraud %",
    f"{detection_rate}%"
)

c4.metric(
    "Avg Amount",
    avg_amount
)

st.subheader("Fraud Distribution")

fraud_counts = df[
    'isFraud'
].value_counts()

st.bar_chart(fraud_counts)


@st.cache_data
def load_sample():

    return pd.read_csv(
        "Data.csv.gz",
        nrows=10,
        compression="gzip"
    )

sample_df = load_sample()


st.subheader("Dataset Sample")

st.dataframe(
    sample_df,
    use_container_width=True
)