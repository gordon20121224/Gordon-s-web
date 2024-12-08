import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用`st.write`顯示的文字，可以處理多種格式， 例如:數字、文字、markdown、數據框等。"
)
st.text("這是一個用`st.write`顯示的純文字，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
這是一個用`st.markdown`顯示的markdown文字，可以處理多種格式， 例如:數字、文字、markdown、數據框等。
例如:

* **這是粗體**
* *這是斜體*
* [這是超連結](https://www.google.com)
    
```python
print("這是一個程式碼")
``` 
"""
)
st.write("#expander 展開元件")
with st.expander("這是一個展元件"):
    st.write("這是一個展開的內容")

st.write("這是展開元件的外面")

st.write("---")

st.write("# number_input 數字輸入元件")
number = st.number_input("輸入一個數字", min_value=0, max_value=100, value=50, step=5)
st.write(f"你輸入的數字是:{number}")


st.write("---")
st.write("# text_input 文字輸入元件")
text = st.text_input("輸入一個文字", value="Hello World")
st.write(f"你輸入的文字是:{text}")

st.write("---")
st.write("# st.button 按鈕元件")
if st.button("点击我", key="btn1"):
    st.write("你点击了我")
    st.balloons()


st.write("---")
st.write("# st.columns 欄位元件")
col1, col2 = st.columns(2)
col1.write("這是第一欄")

if col1.button("点击我", key="btn2"):
    col1.balloons()

col2.write("這是第二欄")
if col2.button("点击我", key="btn3"):
    col2.balloons()


col1, col2 = st.columns([1, 2])
col1.button("点击我", key="btn3-1")
col2.button("点击我", key="btn4")


col1, col2, col3 = st.columns([1, 2, 3])
col1.button("点击我", key="btn5")
col2.button("点击我", key="btn6")
col3.button("点击我", key="btn7")
