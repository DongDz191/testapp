import streamlit as st
from log import log
from app import app

# Kiểm tra trạng thái đăng nhập
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

if st.session_state['login_status']:
    app()
else:
    if log():
        st.session_state['login_status'] = True
        app()
