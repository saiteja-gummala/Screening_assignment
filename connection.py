import numpy as np
import streamlit as st

def welcome():
    return "Welcome to Banker's App"

def predict_output(user_id, account_no, current_amount, withdraw_amount):       # Sql output

    prediction= classifier.predict([[user_id, account_no, current_amount, withdraw_amount]])
    print(prediction)
    return prediction

def main():
    st.title("Bank App")
    html_temp= """
    <div style = "background-color: tomato; padding: 10px">
    <h2 style = "color: white; text-align: center;" >Welcome to Banker's App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html= True)
    user_id= st.text_input(" Enter your user_id", "Type here")
    account_number= st.text_input("Enter your account_number", "Type here")
    withdraw_Amount= st.text_input("Enter your withdraw Amount", "Type here")
    # transaction_date= st.text_input(" Transaction_Date", "Type here")

    result= ""

    if st.button("Predict"):
        result= predict_output
    
    # if st.button("Output"):


if __name__ == "__main__":
    main()