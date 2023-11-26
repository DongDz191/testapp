import streamlit as st
from log import login
from app import main_app

# Kiểm tra trạng thái đăng nhập
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# Create a placeholder for the login page
login_placeholder = st.empty()

if st.session_state['login_status']:
    main_app()
else:
    # Use the placeholder to display the login page
    if login_placeholder.login():
        st.session_state['login_status'] = True
        # Clear the login page once the user logs in successfully
        login_placeholder.empty()
        main_app()
