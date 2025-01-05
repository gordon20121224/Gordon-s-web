import streamlit as st
from utils import init_page
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

init_page()
st.title("AI 聊天室")

if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if message := st.chat_input("請輸入你的訊息"):
    with st.chat_message("user"):
        st.write(message)

        st.session_state.message.append({"role": "user", "content": message})
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "You are a helpful assistant."}]
            + st.session_state.message,
        )

    assistant_response = completion.choices[0].message.content
    with st.chat_message("assistant"):
        st.write(assistant_response)
    st.session_state.message.append(
        {"role": "assistant", "content": assistant_response}
    )
