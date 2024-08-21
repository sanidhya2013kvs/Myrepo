import streamlit as st
from PIL import Image
import time

# Function to display the login form


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
