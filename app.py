import streamlit as st
import re

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

def check_password(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search("[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    return score, suggestions


if st.button("Check Password"):

    score, suggestions = check_password(password)

    if score <= 1:
        st.error("Weak Password")
    elif score == 2:
        st.warning("Medium Password")
    else:
        st.success("Strong Password")

    if suggestions:
        st.write("Suggestions:")
        for s in suggestions:
            st.write("-", s)