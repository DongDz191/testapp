import streamlit as st
from log import login
from app import main_app

# Create a placeholder for the login form
login_placeholder = st.empty()

# Check login status
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

if st.session_state['login_status']:
    main_app()
else:
    # Display the login form in the placeholder
    if login_placeholder.login():
        st.session_state['login_status'] = True
        login_placeholder.empty()  # Clear the login form
        main_app()
