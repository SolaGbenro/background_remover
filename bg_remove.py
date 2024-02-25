import streamlit as st
from rembg import remove
from io import BytesIO
from PIL import Image
import base64

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write("Try uploading an image to remove the background. :grin:")

st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024     # 5MB


def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)

    st.sidebar.markdown("\n")
    st.sidebar.download_button(
        label="Download fixed image",
        data=convert_image(fixed),
        file_name=f"fixed.png",
        mime="image/png")


col1, col2 = st.columns(2)
# uploaded_file = st.sidebar.file_uploader(label="Upload an image", type=["png", "jpg"])
uploaded_file = st.file_uploader(label="Upload an image", type=["png", "jpg"])

if uploaded_file is not None:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error(body="The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=uploaded_file)
else:
    # fix_image(upload="data/input/giraffe.jpg")
    fix_image(upload="data/input/parrot.jpg")

