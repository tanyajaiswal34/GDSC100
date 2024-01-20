import streamlit as st
st.write('this is demo app')
with st.sidebar:
  st.write('this is a sidebar')
col1,col2 = st.columns(2)
with col1:
  a = st.number_input('Enter a value')
with col2:
 b = st.text_input('enter a text')    
sub = st.button(label='submit')
