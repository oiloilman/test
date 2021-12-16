from PIL import Image
import requests
from io import BytesIO
import streamlit as st
url=st.write_input('url')
response = requests.get(url)
img = Image.open(BytesIO(response.content))
