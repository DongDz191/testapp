import streamlit as st
import os

username = st.text_input('Tên người dùng')
password = st.text_input('Mật khẩu', type='password')

if st.button('Đăng nhập'):
    if username == 'admin' and password == '123':
        st.success('Đăng nhập thành công!')
        os.startfile('/app.py')
    else:
        st.error('Tên người dùng hoặc mật khẩu không đúng.')
