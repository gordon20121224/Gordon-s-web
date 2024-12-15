import streamlit as st
import os

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("按鈕", key="btn8"):
        st.balloons()
    st.write("這是col1")
with col2:
    st.button("按鈕", key="btn9")
    st.write("這是col2")

col_num = st.number_input("輸入想要幾個col", step=1, value=4)
cols = st.columns(col_num)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")

col1, col2 = st.columns(2)
with col1:
    st.button("按鈕", key="1")
    st.button("按鈕", key="2")
    st.button("按鈕", key="3")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.markdown("---")
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"{i+4}")
    with col2:
        st.write(f"這是col2_{i+1}")

ans = 1
if st.button("点击我ans加1", key="ans1"):
    ans = ans + 1
st.write(f"ans:{ans}")

if "ans" not in st.session_state:
    st.session_state.ans = 1
if st.button("点击我ans加1", key="ans2"):
    st.session_state.ans = st.session_state.ans + 1
st.write(f"ans:{st.session_state.ans}")
image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)

st.title("圖片原件")

st.image("image/apple.png", width=300)

fruit = st.selectbox("請選擇水果", ["苹果", "橘子", "香蕉"])
st.write("你選擇的水果是:", {fruit})
