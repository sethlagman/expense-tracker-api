
# **Expense Tracker API**

An API for tracking all your expenses

![Demo Image](https://github.com/sethlagman/expense-tracker-api/blob/main/demo.png?raw=true)

## Features

- Sign up as new user
- Login as user
- Generate and validate JWTs for handling authentication and user session
- Create expense
- Retrieve expense
- Update expense
- Delete expense
- Filter expense by date:
    - Past week
    - Past month
    - Past three months
    - Custom date

## Installation

- [X]  [Download Python 3.13.0](https://www.python.org/downloads/release/python-3130/)
- [X]  Clone or download this repository
- [X]  Go to the project directory via CLI or any IDE of your choice
- [X]  Create a virtual environment
    - For Linux or macOS: `python3 -m venv venv`
    - For Windows: `python -m venv venv`
- [X]  Activate the virtual environment
    - For Linux or macOS: `source venv/bin/activate`
    - For Windows: `venv\Scripts\activate`
- [X]  Install the dependencies
    - `pip install -r requirements.txt`
- [X]  Set up environment variables
    - Create .env file
    - Input your keys
    ```
    SECRET_KEY=<django key>
    DB_USER=<db username>
    DB_PASSWORD=<db password>
    DB_NAME=<db name>
    DB_HOST=<db host>
    DB_PORT=<db port>
    ```
- [X]  Change directory to expense app
    - `cd expense`
- [X]  Run the django app
    - `python manage.py runserver`
- [X]  Navigate to
    - http://127.0.0.1:8000/ or http://127.0.0.1:8000/docs/
- [X]  To deactivate virtual environment
    - `deactivate`

## Setup PostgreSQL

- [X]  Install PostgreSQL
    - For Linux: Use your package manager (e.g., `sudo apt-get install postgresql postgresql-contrib`)
    - For macOS: Use Homebrew (`brew install postgresql`)
    - For Windows: Download the installer from the [official PostgreSQL website](https://www.postgresql.org/download/windows/)
- [X]  Start the PostgreSQL service
    - For Linux: `sudo service postgresql start`
    - For macOS: `brew services start postgresql`
    - For Windows: Start the PostgreSQL service from the Services application or via command line.
- [X]  Access the PostgreSQL shell
    - `psql -U postgres`
- [X]  Create a new database
    - `CREATE DATABASE <db name>;`
- [X]  Create a new user
    - `CREATE USER <db username> WITH PASSWORD '<db password>';`
- [X]  Grant privileges to the user
    - `GRANT ALL PRIVILEGES ON DATABASE <db name> TO <db username>;`
- [X]  Exit the PostgreSQL shell
    - `\q`
- [X]  Update your `.env` file with the database credentials
    - Input your keys
    ```
    SECRET_KEY=<django key>
    DB_USER=<db username>
    DB_PASSWORD=<db password>
    DB_NAME=<db name>
    DB_HOST=<db host>
    DB_PORT=<db port>
    ```
- [X]  Change directory to expense app
    - `cd expense`
- [X]  Run database migrations
    - `python manage.py makemigrations`
    - `python manage.py migrate`

## Creation

- Python
- [Django REST](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
- [PostgreSQL](https://www.postgresql.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)