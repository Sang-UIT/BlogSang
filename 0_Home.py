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
    ## Nhấn vào nút phía bên trái để xem các tùy chọn hoặc nhấn vào đây 👇
    """)
col1,col2,col3,col4 = st.columns([1,2,2,5])
with col1:
    st.button("Thơ")
with col2:
    st.button("Truyện Ngắn")
with col3:
    st.button("Tiểu Thuyết")



st.markdown("""
    ### Liên hệ với mình?
    Email: tnsangtrng@gmail.com
"""

)