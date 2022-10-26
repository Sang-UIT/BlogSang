import streamlit as st
st.set_page_config(
    page_title="Thơ",
)
#Sidebar
st.sidebar.write("# Những bài thơ của Sang sẽ được tổng hợp ở đây")
st.sidebar.caption("2022")

st.sidebar.button("Chẳng biết phải đặt tên như thế nào")

st.sidebar.caption("2021")

st.sidebar.button("Con đã về đây, với mẹ thân yêu")
st.sidebar.button("Tấm gương")
st.sidebar.button("Sài gòn vắng em...")

st.sidebar.caption("2020")

st.sidebar.button("Mẹ...")
st.sidebar.button("[Dịch thơ] Do not stand at my grave and weep")
st.sidebar.button("Thơ về tác phẩm Vợ Nhặt")
st.sidebar.button("Thơ về Mị")

st.sidebar.caption("2019")

st.sidebar.button("Tôi lại bâng khuâng giữa mây ngàn")
st.sidebar.button("Gửi gió cùng những yêu thương")

st.sidebar.caption("2018")

st.sidebar.button("Hoa lục bình")

#main
def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages
    def standardize_name(name: str) -> str:
            return name.lower().replace("_", " ")
    page_name = standardize_name(page_name)
    pages = get_pages("Thơ.py")  # OR whatever your main page is called
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

st.write("# Thơ mới nhất")

st.write("# Những bài thơ của Sang sẽ được tổng hợp ở đây")
st.caption("2022")

b1=st.button("Chẳng biết phải đặt tên như thế nào.")
st.caption("2021")

b2=st.button("Con đã về đây, với mẹ thân yêu.")
b3=st.button("Tấm gương.")
b4=st.button("Sài gòn vắng em....")

st.caption("2020")

b5=st.button("Mẹ....")
b6=st.button("[Dịch thơ] Do not stand at my grave and weep.")
b7=st.button("Thơ về tác phẩm Vợ Nhặt.")
b8=st.button("Thơ về Mị.")

st.caption("2019")

b9=st.button("Tôi lại bâng khuâng giữa mây ngàn.")
b10=st.button("Gửi gió cùng những yêu thương.")

st.caption("2018")

st.button("Hoa lục bình.")