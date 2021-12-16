from PIL import Image
import requests
from io import BytesIO
import streamlit as st
url=st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None)('url')
response = requests.get(url)
img = Image.open(BytesIO(response.content))
show(img)
