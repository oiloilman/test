import streamlit as st

from PIL import Image

st.write("## Image example:- ")

img = Image.open("dogs.jpeg")
st.image(img)
