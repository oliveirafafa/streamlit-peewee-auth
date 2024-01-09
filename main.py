import streamlit as streamlit

from pages.landing import LandingPage
from pages.login import Login
from pages.register import Register

streamlit.set_page_config(
    initial_sidebar_state="collapsed",
    layout="wide"

)
streamlit.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


class App:
    __st = streamlit

    pages = {
        'login': Login,
        'register': Register,
        'landing': LandingPage
    }

    if 'page' not in __st.session_state and 'user' not in __st.session_state:
        __st.session_state.page = 'login'
        __st.session_state.user = None

    def get_st(self) -> streamlit:
        return self.__st

    def get_user(self):
        return self.__st.session_state.user.email

    def update_user(self, u):
        self.__st.session_state.user = u

    def navigate(self, page):
        self.__st.session_state.page = page
        self.__st.rerun()

    def run(self):
        self.pages[self.__st.session_state['page']](parent=self)


if __name__ == '__main__':
    app = App()
    app.run()
