import streamlit as st
from log import login
from app import main_app

login()

if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False
else:
    st.session_state['login_status'] = True

if st.session_state['login_status']:
    main_app()
