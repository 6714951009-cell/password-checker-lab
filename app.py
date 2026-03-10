import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.write("Check how strong your password is")

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

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if len(password) >= 12:
        score += 1

    return score, suggestions


if st.button("Check Password"):

    if password:

        score, suggestions = check_password(password)

        st.subheader("Password Strength")

        # Progress bar
        st.progress(score / 5)

        st.write(f"Score: {score} / 5")

        if score <= 2:
            st.error("Weak Password")
        elif score == 3:
            st.warning("Medium Password")
        else:
            st.success("Strong Password")

        if suggestions:
            st.write("Suggestions to improve:")
            for s in suggestions:
                st.write("- ", s)

    else:
        st.warning("Please enter a password")