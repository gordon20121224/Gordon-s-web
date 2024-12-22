import streamlit as st
from utils import init_page

init_page()
st.title("聊天室示範")

if "message" not in st.session_state:
    st.session_state.message = []

demo_messages = [
    {"role": "user", "content": "你好，請問要怎麼學python?"},
    {
        "role": "assistant",
        "content": "學習Python的基本步驟：\n1. 了解基礎語法\n2. 練習簡單程式\n3. 解決實際問題",
    },
    {"role": "user", "content": "看起來不難嘛"},
    {"role": "assistant", "content": "是的，Python是一種非常容易學習的語言"},
]


for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if message := st.chat_input("請輸入你的訊息"):
    with st.chat_message("user"):
        st.write(message)
    st.session_state.message.append({"role": "user", "content": message})
    assistant_response = f"你剛剛說了：{message}"
    with st.chat_message("assistant"):
        st.write(assistant_response)
    st.session_state.message.append(
        {"role": "assistant", "content": assistant_response}
    )
