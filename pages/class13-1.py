import streamlit as st
import os
from utils import init_page

init_page()

col_option, col_image = st.columns([1, 2])

with col_option:
    with st.expander("圖片設定"):
        image_folder = "image"
        image_files = os.listdir(image_folder)
        fruit = st.selectbox("請選擇水果", image_files)
        size = st.number_input("設定寬度", step=10, value=300, min_value=0)

with col_image:
    st.image(f"image/{fruit}", width=size)
