import streamlit as st
import os


def menu():
    st.sidebar.title("選單")
    st.sidebar.page_link(page="main.py", label="首頁", icon="🎪")
    st.sidebar.markdown("---")

    pages_files_path = os.listdir("pages")
    pages_files_path = [page for page in pages_files_path if "class" in page]
    page_path = st.sidebar.selectbox("選擇課程", pages_files_path)
    if st.sidebar.button("前往", key="go_to_page"):
        st.switch_page(f"pages/{page_path}")
    st.sidebar.markdown("---")
