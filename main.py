import streamlit as st
from log import login
from app import main_app

# Initialize login_status in session_state if not already present
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# If already logged in, show the main app
if st.session_state['login_status']:
    main_app()
else:
    # Create a separate container for the login
    with st.container():
        if login():
            # On successful login, update login_status and rerun the app
            st.session_state['login_status'] = True
            st.experimental_rerun()

    # You can add additional content below the login container if needed
