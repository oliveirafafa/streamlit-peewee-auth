# Streamlit Authentication System with Peewee ORM

This project is a concept that demonstrates a simple authentication system using the Peewee ORM, Streamlit and MySQL. Users can register, log in, and access protected content.

The idea behind this project is to offer a straightforward authentication solution that can serve as a starting point for more complex systems. While this project is just a foundation, there is room for future enhancements, such as cookie handling, password reset and email confirmation via SMTP, etc.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/oliveirafafa/streamlit-peewee-auth.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your database configuration in `.env`.
    ```bash
   DB_NAME = 
   DB_USER = 
   DB_PASSWORD = 
   DB_HOST = 127.0.0.1
   DB_PORT = 3306
    ```

**NOTE**: The database will be created if it does not exist.

## Usage

1. Run the app.
    ```bash
   streamlit run main.py
   ```

2. Access the application in your web browser.
   
3. Register a new account with your email and password.

4. Log in with your registered credentials.

5. Access protected content and customize the authentication system as needed for your project.

## Features

- User registration with email and password.
- User login and session management.
- Easily extensible for additional features.

## Technologies Used

- [Python](https://www.python.org/)
- [Peewee ORM](http://docs.peewee-orm.com/en/latest/)
- [Streamlit](https://streamlit.io/)
- [MySQL](https://www.mysql.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

