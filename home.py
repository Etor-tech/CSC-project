import streamlit as st
from savings_account import SavingsAccount
from current_account import CurrentAccount

# accounts
savings = SavingsAccount(20000)
current = CurrentAccount(1000)

st.set_page_config(page_title="Bank App", layout="centered")
st.title("Bank Account Operations")

# Choose account the account type
account_type = st.selectbox("Choose Account", ["Savings Account", "Current Account"])

if account_type == "Savings Account":
    with st.form("savings_form"):
        amount = st.number_input("Enter Amount to Save/Withdraw", min_value=1000)
        operation = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
        submit = st.form_submit_button("Submit")

        if submit:
            if operation == "Withdraw":
                try:
                    savings.withdraw(amount)
                    st.success(f"Withdrawal successful! New balance: {savings.balance}")
                except ValueError as e:
                    st.error(str(e))
            elif operation == "Deposit":
                savings.deposit(amount)
                st.success(f"Deposit successful! New balance: {savings.balance}")

elif account_type == "Current Account":
    with st.form("current_form"):
        amount = st.number_input("Enter Amount to Save/Withdraw", min_value=1000)
        operation = st.selectbox("Deposit or Withdraw", ("Deposit", "Withdraw"))
        submit = st.form_submit_button("Submit")

        if submit:
            if operation == "Withdraw":
                try:
                    current.withdraw(amount)
                    st.success(f"Withdrawal successful! New balance: {current.balance}")
                except ValueError as e:
                    st.error(str(e))
            elif operation == "Deposit":
                current.deposit(amount)
                st.success(f"Deposit successful! New balance: {current.balance}")