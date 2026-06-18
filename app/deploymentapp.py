import streamlit as st

st.set_page_config(
    page_title="Fraud Detection System",
    layout="wide"
)

st.title("💳 Fraud Detection System")

st.markdown(
    "Predict whether a transaction is potentially fraudulent."
)

transaction_amt = st.number_input(
    "Transaction Amount",
    min_value=0.0
)

device_type = st.selectbox(
    "Device Type",
    ["desktop", "mobile"]
)

card_type = st.selectbox(
    "Card Type",
    [
        "visa",
        "mastercard",
        "discover",
        "american express"
    ]
)

email_domain = st.text_input(
    "Email Domain"
)

if st.button("Predict Fraud"):
    
    st.success(
        "Prediction pipeline will be connected in the next step."
    )