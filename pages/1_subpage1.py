import streamlit as st

st.set_page_config(
    page_title='서브페이지 1',
    layout='wide', # 'centered', 'wide'

)

st.header('서브페이지 헤더입니다.')
st.subheader('This is subheader')
st.write('This is write')