import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="SHAP Explainer",
    layout="wide"
)


st.title("AI Fraud SHAP Explainer")

st.markdown(
    "Analyze which features most influenced the fraud prediction."
)


@st.cache_data
def load_data():

    return pd.read_csv(
        "shap_values.csv"
    )

df = load_data()


st.sidebar.header("Controls")

row_number = st.sidebar.slider(
    "Select Transaction Row",
    0,
    len(df)-1,
    0
)

row = df.iloc[row_number]


importance = pd.DataFrame({
    "Feature": row.index,
    "SHAP_Value": row.values
})

importance["ABS"] = (
    importance["SHAP_Value"].abs()
)

importance = importance.sort_values(
    by="ABS",
    ascending=False
)


TOP_N = 10

importance_top = importance.head(TOP_N)


c1, c2, c3 = st.columns(3)

c1.metric(
    "Selected Row",
    row_number
)

c2.metric(
    "Top Feature",
    importance_top.iloc[0]["Feature"]
)

c3.metric(
    "Highest SHAP",
    round(importance_top.iloc[0]["ABS"], 4)
)


st.subheader("Top Influencing Features")

fig = px.bar(
    importance_top[::-1],
    x="SHAP_Value",
    y="Feature",
    orientation='h',
    title="Feature Impact on Prediction",
    text="SHAP_Value"
)

fig.update_layout(
    height=500,
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader("Feature Contribution Distribution")

pie_fig = px.pie(
    importance_top,
    names="Feature",
    values="ABS",
    hole=0.5
)

pie_fig.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    pie_fig,
    use_container_width=True
)


st.subheader("Detailed SHAP Values")

st.dataframe(
    importance_top,
    use_container_width=True
)


st.subheader("Positive vs Negative Impact")

positive = importance[
    importance["SHAP_Value"] > 0
]["SHAP_Value"].sum()

negative = abs(
    importance[
        importance["SHAP_Value"] < 0
    ]["SHAP_Value"].sum()
)

impact_fig = go.Figure(
    data=[
        go.Bar(
            x=["Positive", "Negative"],
            y=[positive, negative]
        )
    ]
)

impact_fig.update_layout(
    title="Overall Prediction Push",
    template="plotly_dark"
)

st.plotly_chart(
    impact_fig,
    use_container_width=True
)