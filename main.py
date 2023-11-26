import streamlit as st
from log import login
from app import main_app

# Kiểm tra trạng thái đăng nhập
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

if st.session_state['login_status']:
    main_app()
else:
    if login():
        st.session_state['login_status'] = True
        main_app()
