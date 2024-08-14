import streamlit as st
from PIL import Image
import time

# Function to display the login form
def login_form():
    with st.form(key="login_form"):
        login_id = st.text_input("Login ID")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if login_id == "Sanidhya Srivastava" and password == "password":  # Replace with actual credentials
                st.success("Logged in successfully")
                st.session_state.logged_in = True
                st.session_state.name = "Sanidhya Srivastava"  # Replace with actual user data
                st.session_state.address = "733,civil lines church road Sitapur UttarPradesh, India, 261001"
                st.session_state.phone = "+91 8840445270"
                st.session_state.uid = "98436732368"
                st.experimental_rerun()
            else:
                st.error("Invalid Login ID or Password")

# Check if the user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_form()
else:
    # Profile form for image upload and resize
    

    # Display profile information
    st.text(f"Name: {st.session_state.name}")
    st.text(f"Address: {st.session_state.address}")
    st.text(f"Phone Number: {st.session_state.phone}")
    st.text(f"UID: {st.session_state.uid}")

    if 'image_file' in st.session_state:
        st.image(st.session_state.image_file, caption='Resized Passport Size Photo', use_column_width=True)

    if st.button("generate letter"):
        st.warning("Dear Candidate your's joining letter is in progress  please wait for few hours")
