import streamlit as st
import pytesseract
import cv2
from PIL import Image
try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


uploaded_files = st.file_uploader("Choose a Image", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)