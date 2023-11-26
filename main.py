import streamlit as st
from log import login
from app import main_app

# Check login status
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

if st.session_state['login_status']:
    # Hide the login form
    st.write("You are logged in!")
    main_app()
else:
    # Display the login form
    if login():
        st.session_state['login_status'] = True
        main_app()
