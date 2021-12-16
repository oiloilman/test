import streamlit as st

from PIL import Image

st.text_input("## Image example:- ")

img = Image.open("dog.jpeg")
st.image(img)
