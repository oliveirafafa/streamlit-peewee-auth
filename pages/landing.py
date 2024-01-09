class LandingPage:
    def __init__(self, parent):
        st = parent.get_st()
        _, col2, _ = st.columns([0.25, 0.5, 0.25], gap='small')

        with col2:
            st.markdown(f'Hello, {parent.get_user()}')
