import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="Blog's Sang",
    page_icon="👋",
)

st.write("# Chào mừng đến với blog của Sang! 👋")

st.sidebar.success("Chọn chỉ mục muốn xem.")

st.markdown(
    """
    Blog này là gì?
    **Đây là blog để mình đăng tải thơ, văn và các dự án cá nhân của bản thân**
    ### Liên hệ với mình?
    Email: tnsangtrng@gmail.com
"""

)