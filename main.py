import streamlit as st
from log import login
from app import main_app

login()

if st.session_state['login_status']:
    main_app()
