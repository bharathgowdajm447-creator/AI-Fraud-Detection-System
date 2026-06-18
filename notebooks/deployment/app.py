import streamlit as st

st.set_page_config(
    page_title="AI Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

st.title("💳 AI Fraud Detection System")

st.markdown("""
This application predicts fraud risk for online transactions using the IEEE-CIS Fraud Detection project pipeline.
""")

st.sidebar.header("Transaction Input")

col1, col2 = st.columns(2)

with col1:
    transaction_amt = st.number_input("Transaction Amount", min_value=0.0)
    card1 = st.number_input("Card1 ID", min_value=0)
    card2 = st.number_input("Card2 ID", min_value=0)

with col2:
    card1_frequency = st.number_input("Card Usage Frequency", min_value=0)
    email_frequency = st.number_input("Email Frequency", min_value=0)
    card6 = st.selectbox("Card Type", ["credit", "debit", "charge card", "debit or credit"])

if st.button("Predict Fraud Risk"):
    st.info("Model prediction will be connected in the next step.")