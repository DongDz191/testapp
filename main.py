import streamlit as st
from log import login
from app import main_app

def main():
    # Tạo placeholder
    login_placeholder = st.empty()

    # Hiển thị form login
    with login_placeholder:
        login_form = st.form(key='login')
        username = login_form.text_input('Tên đăng nhập')
        password = login_form.text_input('Mật khẩu', type='password')
        submit_button = login_form.form_submit_button('Đăng nhập')

    # Kiểm tra xem người dùng đã đăng nhập chưa
    if submit_button and username == 'admin' and password == '123':
        # Xóa placeholder
        login_placeholder.empty()

        # Hiển thị form main_app()
        with st.form(key='main_app'):
            # Thêm các thành phần của form main_app() vào đây
            pass
