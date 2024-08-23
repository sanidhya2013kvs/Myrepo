import streamlit as st
from PIL import Image
import time

# Function to display the login form

image_path = "./IMG.JPG"  # Replace with your image path

# Display the image with a specified width
st.image(image_path, width=150)  # Adjust width to your desired size
    # Profile form for image upload and resize
st.text("Name:Sanidhya Srivastava")
st.text("Location:Gurugram,Haryana,India")
st.text("Apple ID:8532584")
st.text("Position:computer vision research engineer")
st.text("address:733, civil lines ,church road Sitapur UttarPradesh, 261001")


if st.button("generate letter"):
    st.warning("Dear Candidate your's joining letter has been in process and will recived by mail shotrtly")
