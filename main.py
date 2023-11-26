import streamlit as st
from log import login
from app import main_app

# Initialize login_status in session_state if not already present
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# Create a placeholder for the login page
login_placeholder = st.empty()

# If already logged in, show the main app
if st.session_state['login_status']:
    main_app()
else:
    # Show the login form in the placeholder
    with login_placeholder.container():
        if login():
            # On successful login, clear the placeholder and display the main app
            login_placeholder.empty()
            st.session_state['login_status'] = True
            main_app()
