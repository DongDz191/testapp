import s3fs
import streamlit as st

# Khởi tạo S3FileSystem
fs = s3fs.S3FileSystem(key='YOUR_ACCESS_KEY', secret='YOUR_SECRET_KEY')

def upload_file_to_s3(file, bucket_name, file_path):
    with fs.open(f'{bucket_name}/{file_path}', 'wb') as f:
        f.write(file.getvalue())
    return f's3://{bucket_name}/{file_path}'

# Giao diện người dùng để tải lên tệp tin
st.title('Tải Tệp lên AWS S3')

uploaded_file = st.file_uploader("Chọn một tệp tin")
if uploaded_file is not None:
    file_path = upload_file_to_s3(uploaded_file, 'your-bucket-name', uploaded_file.name)
    st.write(f"Tệp tin đã được tải lên thành công: {file_path}")
