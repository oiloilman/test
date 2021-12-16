import streamlit as st

from PIL import Image

st.write("## Image example:- ")

img = Image.open(".jpeg")
st.image(img)
