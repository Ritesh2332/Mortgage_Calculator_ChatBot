import streamlit as st
from dotenv import load_dotenv
from mortgage_utils import calculate_mortgage_payment
from chatbot import get_mortgage_advice

load_dotenv()

st.title("🏠 Mortgage Calculator")

loan = st.number_input("Loan Amount (₹)", value=1000000)
rate = st.number_input("Annual Interest Rate (%)", value=7.5)
term = st.slider("Loan Term (years)", min_value=1, max_value=30, value=20)

if st.button("Calculate Monthly Payment"):
    monthly_payment = calculate_mortgage_payment(loan, rate, term)
    st.success(f"Your monthly payment is ₹{monthly_payment}")
    st.info(get_mortgage_advice(loan, rate, term))
