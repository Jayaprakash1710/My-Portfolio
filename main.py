import streamlit as st
import os

# Path to the HTML file
html_file_path = os.path.join("portfolio-website", "index.html")

# Read and display the HTML file in Streamlit
with open(html_file_path, "r") as f:
    html_content = f.read()

st.markdown(html_content, unsafe_allow_html=True)

