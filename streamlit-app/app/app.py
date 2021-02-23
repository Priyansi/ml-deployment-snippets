import streamlit as st
from utils import get_prediction
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)

def predict(image_data):
    image = Image.open(image_data)
    prediction = get_prediction(image)
    return prediction


image_data = st.file_uploader("Upload file", type=["jpg", "png", "jpeg"])
dog_or_cat = st.button('Dog Or Cat?')

if image_data and dog_or_cat is not None:
    prediction = predict(image_data)
    st.write(prediction)
