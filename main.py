import streamlit as st
import os

# Correct path to the HTML file directly in the root folder
html_file_path = "index.html"

# Check if the file exists and display the content
if os.path.exists(html_file_path):
    with open(html_file_path, "r") as f:
        html_content = f.read()

    st.markdown(html_content, unsafe_allow_html=True)
else:
    st.error("HTML file not found. Please check the file path.")

