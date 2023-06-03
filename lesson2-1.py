import streamlit as st

# 下面是magic的寫法
"#### Hello world Daisy"
"Hello ***徐得惠***"

st.markdown("Hello! **world**!")
st.divider()
st.title("這是app的title")
st.divider()
st.header("這是header")
st.divider()
st.subheader("這是subheader")
st.divider()
st.caption("這是caption")
st.divider()
st.code("a=123")


import numpy as np
import pandas as pd
import streamlit as st

scores_array = np.random.randint(50,high=101,size=(50,5))
student_dataFrame = pd.DataFrame(data=scores_array,
             columns=["國文","英文","數學","地理","社會"],
             index=range(1,51))

st.header("3年5班成績表")
#st.table(data=student_dataFrame)
st.dataframe(data=student_dataFrame)


import streamlit as st

st.metric(label="溫度", value="70 °F", delta="1.2 °F")