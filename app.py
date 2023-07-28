import streamlit as st


st.set_page_config(
    page_title="首页",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="auto",
)

# set_page_config配置Streamlit应用程序的页面设置。自定义应用程序的标题、图标、布局等方面，以提供更好的用户体验。
# 注意：set_page_config必须在应用程序的所有其他元素之前调用，否则会引发异常。
# 参数说明：
# page_title：可选参数，用于设置应用程序的标题，通常显示在浏览器的标签页上。
# page_icon：可选参数，用于设置应用程序的图标，通常显示在浏览器标签页和书签栏中。
# layout：可选参数，用于设置应用程序的布局方式，可以是"centered"（居中）或"wide"（宽屏）。
# initial_sidebar_state：可选参数，用于设置侧边栏的初始状态。可以是"auto"（自动展开）或"collapsed"（折叠）


def init_sidebar():
    """
    初始化侧边栏
    :return:
    """

    st.sidebar.title("About")

    markdown = """
    Web App URL: <https://geemap.streamlit.app>
    """
    st.sidebar.info(markdown)

    logo = "https://i.imgur.com/UbOXYAU.png"
    st.sidebar.image(logo)


def init_content():
    """
    初始化内容
    :return:
    """
    # Customize page title
    st.title("Earth Engine Web App")

    st.markdown(
        """
        This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [geemap](https://geemap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/giswqs/geemap-apps).
        """
    )

    st.header("Instructions")

    markdown = """
    1. For the [GitHub repository](https://github.com/giswqs/geemap-apps) or [use it as a template](https://github.com/new?template_name=geemap-apps&template_owner=giswqs) for your own project.
    2. Customize the sidebar by changing the sidebar text and logo in each Python files.
    3. Find your favorite emoji from https://emojipedia.org.
    4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.
    """

    st.markdown(markdown)



if __name__ == '__main__':
    init_sidebar()
    init_content()
    pass