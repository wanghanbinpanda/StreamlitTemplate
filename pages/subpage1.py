import streamlit as st

st.set_page_config(
    page_title="子页",
    page_icon="✈",
    layout="centered",
    initial_sidebar_state="auto",
)

def init_content():

    st.title("子页")

    # 用于创建一个具有两列的布局，比例为4:1。第一个参数4表示第一列的宽度是第二列的4倍。
    col1, col2 = st.columns([4, 1])

    with col1:
        st.title("col1")



    with col2:
        st.title("col2")



if __name__ == '__main__':
    init_content()
