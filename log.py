import streamlit as st

def login():
    st.title('Login Page')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    if st.button('Login'):
        if username == "admin" and password == "12345":
            return True
        else:
            st.error("Incorrect username or password")
            return False
