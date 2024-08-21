import streamlit as st
from PIL import Image
import time

# Function to display the login form
def login_form():
    with st.form(key="login_form"):
        login_id = st.text_input("Login ID")
        password = st.text_input("Password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if login_id == "Sanidhya2468" and password == "pass2468":  # Replace with actual credentials
                st.success("Logged in successfully")
                
            else:
                st.error("Invalid Login ID or Password")

# Check if the user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_form()

    # Profile form for image upload and resize
st.text("Name:Sanidhya Srivastava")
st.text("Position:computer vision research engineer")
st.text("address:733, civil lines ,church road Sitapur UttarPradesh, 261001")
st.text("phone number:+918840445270")
st.text("UId:6753982561")

if 'image_file' in st.session_state:
    st.image(st.session_state.image_file, caption='Resized Passport Size Photo', use_column_width=True)

if st.button("generate letter"):
    st.warning("Dear Candidate your's joining letter is in progress  please wait for few hours")
