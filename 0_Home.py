import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="Blog's Sang",
    page_icon="👋",
)
def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages
    def standardize_name(name: str) -> str:
            return name.lower().replace("_", " ")
    page_name = standardize_name(page_name)
    pages = get_pages("Home.py")  # OR whatever your main page is called
    for page_hash, config in pages.items():
            if standardize_name(config["page_name"]) == page_name:
                        raise _RerunException(
                                        _RerunData(
                                                            page_script_hash=page_hash,
                                                                                page_name=page_name,
                                                                                                )
                                                                                                            )
    page_names = [standardize_name(config["page_name"]) for config in pages.values()]
    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

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
    if st.button("Thơ"):
        switch_page("Thơ")
        
with col2:
    st.button("Truyện Ngắn")
with col3:
    st.button("Tiểu Thuyết")



st.markdown("""
    ### Liên hệ với mình?
    Email: tnsangtrng@gmail.com
"""

)
