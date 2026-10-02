import streamlit as st
import pickle
import pandas as pd

                                                                                                                                
# Load trained model
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)


# Page configuration
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="centered"
)


# Title
st.title("💰 Loan Approval Prediction System")

st.write(
    "Enter applicant details to predict whether the loan will be Approved or Rejected."
)


# Input fields

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

income = st.number_input(
    "Annual Income",
    min_value=0,
    value=50000,
    step=1000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=200000,
    step=5000
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=700
)

employment_years = st.number_input(
    "Employment Years",
    min_value=0,
    max_value=50,
    value=5
)

existing_loans = st.number_input(
    "Existing Loans",
    min_value=0,
    max_value=20,
    value=1
)

debt_to_income = st.number_input(
    "Debt to Income (%)",
    min_value=0.0,
    max_value=100.0,
    value=30.0
)


# Prediction button
if st.button("🔍 Predict Loan Status"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "age": [age],
        "income": [income],
        "loan_amount": [loan_amount],
        "credit_score": [credit_score],
        "employment_years": [employment_years],
        "existing_loans": [existing_loans],
        "debt_to_income": [debt_to_income]
    })

    # Prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:

        st.success("✅ Loan Approved")

        st.write(
            f"Approval Probability: {probability[1] * 100:.2f}%"
        )

    else:

        st.error("❌ Loan Rejected")

        st.write(
            f"Rejection Probability: {probability[0] * 100:.2f}%"
        )