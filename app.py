import streamlit as st
import boto3

# Tạo client S3
s3_client = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

def upload_file_to_s3(file, bucket, object_name):
    try:
        s3_client.upload_fileobj(file, bucket, object_name)
    except Exception as e:
        return False, str(e)
    return True, "File uploaded successfully"

# Giao diện người dùng để tải lên tệp tin
st.title('Tải Tệp lên AWS S3')

uploaded_file = st.file_uploader("Chọn một tệp tin")
if uploaded_file is not None:
    success, message = upload_file_to_s3(uploaded_file, 'your-bucket-name', uploaded_file.name)
    if success:
        st.success(message)
    else:
        st.error(message)
