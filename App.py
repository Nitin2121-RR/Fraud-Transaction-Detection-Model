import streamlit as st

st.set_page_config(
    page_title="Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #58A6FF;
}

div[data-testid="metric-container"] {
    background-color: #161B22;
    padding: 15px;
    border-radius: 10px;
}

.box {
    background-color: #161B22;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    border-left: 5px solid #58A6FF;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("💳 Fraud Detection Dashboard")


st.divider()

# Metrics
col1, col2 = st.columns(2)

col1.metric("Transactions", "590K")
col2.metric("Fraud Cases", "20K")

st.divider()

# Overview Box
st.markdown("""
<div class="box">

<h2>📌 Model Overview</h2>

<ul>
<li><b>Recall:</b> 65% for Fraud Cases</li>
<li><b>Precision:</b> 93% for Fraud Cases</li>
<li><b>F1-Score:</b> 76% for Fraud Cases</li>
<li><b>Model Used:</b> XGBoost Classifier</li>
<li><b>Purpose:</b> Detect fraudulent financial transactions</li>
<li><b>Explainability:</b> SHAP-based prediction interpretation</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.divider()

st.caption("Built by Nitin Kumar Patel ")