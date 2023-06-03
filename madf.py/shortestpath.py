import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Shortest Path",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

# lottie file
lottie_code=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_0lvdwxbc.json")

#--header
st.title("Shortest Path")
st.write("The algorithm uses advance image recognisition system to identify the note and the path between them and uses it to calculate and identify the shortest path")
st.write("[click to learn more](https://youtu.be/BBJa32lCaaY)")
st_lottie(lottie_code,height=300, key="coding")


# Create a centered button to accept images
st.markdown(
    """
    <div style='display: flex; justify-content: center;'>
        <label for="file-upload" class="btn btn-primary">
          **UPLOAD IMAGE**
        </label>
    </div>
    """,
    unsafe_allow_html=True
)

# Process the uploaded image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Do something with the uploaded image
    st.image(uploaded_file, caption="Uploaded Image")

