import streamlit as st

# App title
st.title(" Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")


operation = st.selectbox(
    "Select an operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)


if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed.")
