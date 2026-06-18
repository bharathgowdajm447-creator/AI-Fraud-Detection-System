import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AI Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

model = joblib.load("deployment_model.pkl")
encoder = joblib.load("card6_encoder.pkl")

st.title("💳 AI Fraud Detection System")

st.markdown(
    "Fraud Risk Prediction using Machine Learning"
)

col1, col2 = st.columns(2)

with col1:
    transaction_amt = st.number_input(
        "Transaction Amount",
        min_value=0.0
    )

    card1 = st.number_input(
        "Card1 ID",
        min_value=0
    )

    card2 = st.number_input(
        "Card2 ID",
        min_value=0
    )

    transaction_dt = st.number_input(
        "TransactionDT",
        min_value=0
    )

    d1 = st.number_input(
        "D1",
        min_value=0
    )

with col2:
    card1_frequency = st.number_input(
        "Card Usage Frequency",
        min_value=0
    )

    email_frequency = st.number_input(
        "Email Frequency",
        min_value=0
    )

    d2 = st.number_input(
        "D2",
        min_value=0
    )

    c1 = st.number_input(
        "C1",
        min_value=0
    )

    card6 = st.selectbox(
        "Card Type",
        [
            "credit",
            "debit",
            "charge card",
            "debit or credit"
        ]
    )

if st.button("Predict Fraud Risk"):

    card6_encoded = encoder.transform([card6])[0]

    input_df = pd.DataFrame({
        "TransactionAmt":[transaction_amt],
        "card1":[card1],
        "card2":[card2],
        "card6":[card6_encoded],
        "card1_frequency":[card1_frequency],
        "email_frequency":[email_frequency],
        "TransactionDT":[transaction_dt],
        "D1":[d1],
        "D2":[d2],
        "C1":[c1]
    })

    probability = model.predict_proba(input_df)[0][1]

    st.metric(
        "Fraud Probability",
        f"{probability*100:.2f}%"
    )

    if probability >= 0.50:
        st.error("🔴 HIGH FRAUD RISK")

    elif probability >= 0.20:
        st.warning("🟡 MEDIUM FRAUD RISK")

    else:
        st.success("🟢 LOW FRAUD RISK")