"""Streamlit about page for the Image Analyzer app."""

import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="./app/images/object.png",
    layout="centered",
)

st.title("About the App")

st.write(
    """
    This application showcases the object detection capabilities of the YOLOv5 model by
    allowing you to analyze images or a webcam feed directly from your browser. It features:

    - fast model loading optimized in the ONNX format;
    - analysis of local images or live streams to identify up to 20 categories;
    - a straightforward Streamlit interface to visualize detections and their details.

    Whether you are exploring computer vision or presenting a proof of concept, the app
    offers a ready-to-use experience for testing YOLOv5.
    """
)
