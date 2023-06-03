import streamlit as st

option = st.selectbox(
    "您想要如何聯絡?",
    ("Email","電話","手機")
)

st.write("You selected:",option)

import streamlit as st

options = st.multiselect(
    "請選擇您喜歡的顏色",
    ["Green","Yellow","Red","Blue"],
    ["Yellow","Red"]
)

st.write("您選擇:",options)