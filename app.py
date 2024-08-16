import streamlit as st
import numpy as np
import pandas as pd 

st.title("this is new app")
st.write('this is first time i am using streamlit')

df=pd.DataFrame({
    'first_column':[1,2,4,6],
    'second_column':[4,5,3,5]
})
st.title("here is the dataframe")
st.write(df)

chart=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']

)
st.line_chart(chart)