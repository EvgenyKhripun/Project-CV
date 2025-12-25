import streamlit as st

st.set_page_config(
    page_title="CV Project",
    layout="wide"
)

st.title("Computer Vision Project Dashboard")
st.markdown("""
Это мультистраничное приложение для:
- Семантической сегментации лесных снимков (UNet)
- Детекции лиц (YOLO)
- Детекции объектов (ветрогенераторы, YOLO)
""")
st.sidebar.success("Выберите страницу слева")
