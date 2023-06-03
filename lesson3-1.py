import streamlit as st

def button_click():
    st.write(st.session_state)

if st.button("say hello!",key="mybutton",on_click=button_click):
    st.write("why hello there")
else:
    st.write("Goodbye")

import streamlit as st

agree = st.checkbox("我同意")

if agree:
    st.write("Great!")

import streamlit as st


genre = st.radio(
    "您喜歡的節目是什麼",
    ("卡通","戲劇","紀錄片")
)

if genre =="卡通":
    st.write("您選擇:卡通")
elif genre =="戲劇":
    st.write("您選擇:戲劇")
elif genre =="紀錄片":
    st.write("您選擇:紀錄片")
