import time

from app.models.user import hash_password, User, validate_email, validate_password


class Register:
    def __init__(self, parent):
        st = parent.get_st()
        _, col2, _ = st.columns([0.25, 0.5, 0.25], gap='small')

        with col2:
            with st.form("Register"):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                c_password = st.text_input("Confirm password", type="password")
                submit_button = st.form_submit_button("Create account", type='primary')

                if submit_button:
                    if not validate_email(email):
                        st.error("Invalid email.")
                    elif not validate_password(password):
                        st.error("The password must be at least 8 characters long.")
                    elif password != c_password:
                        st.error("Passwords do not match.")
                    elif User.user_exists(email):
                        st.error("User already exists!")
                    else:
                        user = User.create_user(email, hash_password(password))
                        st.success("User created successfully!")
                        with st.spinner('Redirecting you to the login screen...'):
                            time.sleep(2)
                            parent.navigate('login')

            if st.button("Sign in"):
                parent.navigate('login')
