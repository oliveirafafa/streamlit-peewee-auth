import time

from app.models.user import hash_password, User


class Login:
    def __init__(self, parent):
        st = parent.get_st()
        _, col2, _ = st.columns([0.25, 0.5, 0.25], gap='small')

        with col2:
            with st.form("Login"):
                email = st.text_input("Email")
                senha = st.text_input("Password", type="password")
                submit_button = st.form_submit_button("Sign in", type='primary')

                if submit_button:
                    senha_hash = hash_password(senha)
                    if user := User.check_user_login(email, senha_hash):
                        parent.update_user(user)
                        st.success('Login successful! Redirecting...')
                        time.sleep(1)
                        parent.navigate("landing")
                    else:
                        st.error("Login failed.")

            if st.button('Sign up'):
                parent.navigate('register')
