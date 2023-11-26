import streamlit as st

if st.button('Đăng nhập'):
    if username == 'admin' and password == '123':
        st.success('Đăng nhập thành công!')
        os.startfile('app.py')
    else:
        st.error('Tên người dùng hoặc mật khẩu không đúng.')
