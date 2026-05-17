import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Transaction Explorer",
    layout="wide"
)

st.title("Transaction Explorer")


@st.cache_data
def load_data():

    return pd.read_csv(
        "Data.csv.gz",
        compression="gzip"
    )

df = load_data()


df['TransactionID'] = (
    df['TransactionID']
    .astype(float)
    .astype(int)
    .astype(str)
)


@st.cache_resource
def load_model():

    return joblib.load("xg_model")

model = load_model()


st.sidebar.header("Filters")

fraud_filter = st.sidebar.selectbox(
    "Fraud Type",
    ["All", "Fraud", "Not Fraud"]
)


filtered_df = df

if fraud_filter == "Fraud":

    filtered_df = df[
        df['isFraud'] == 1
    ]

elif fraud_filter == "Not Fraud":

    filtered_df = df[
        df['isFraud'] == 0
    ]


st.subheader("Search Transaction")

transaction_id = st.text_input(
    "Enter TransactionID"
)


if st.button("Search"):

    if transaction_id.strip() != "":

        transaction_id = (
            transaction_id.strip()
        )

        row = df[
            df['TransactionID']
            == transaction_id
        ]


        if len(row) > 0:

            st.success(
                "Transaction Found"
            )

            st.subheader(
                "Transaction Details"
            )

            st.dataframe(
                row,
                use_container_width=True
            )


            try:

                drop_cols = [
                    c for c in ['isFraud', 'TransactionID']
                    if c in row.columns
                ]

                X = row.drop(columns=drop_cols)

                risk_score = (
                    model.predict_proba(X)
                    [:,1][0]
                )

                st.metric(
                    "Fraud Risk Score",
                    round(risk_score, 4)
                )

            except Exception as e:

                st.warning(
                    f"Prediction could not be generated: {e}"
                )


        else:

            st.error(
                "TransactionID not found"
            )


st.subheader("Transactions Table")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)