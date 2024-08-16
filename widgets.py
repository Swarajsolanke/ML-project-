import streamlit  as st
import pandas as pd
import numpy as np
st.title("Streamlit text input ")
name=st.text_input("Enter your name ")
age=st.slider("select  your age :",0,100,25)
st.write(f'your age is {age}')

options=['python','c','java','java-script9']
choice=st.selectbox("choose your language:",options)
st.write(f'you selected : {choice}')

if name:
    st.write(f'hello  :{name}')
data={
    "name":['john','mon','mahesh','rohan'],
    'age':[1,34,5,3],
    'city':['new york','los angeles','chicago','pune']
}


df=pd.DataFrame(data)     
df.to_csv('sample.csv')
st.write(df)

uploaded_files=st.file_uploader('choose a csv fiel',type='csv')
if uploaded_files is not None:
    df=pd.read_csv(uploaded_files)
    st.write(df)