# Online Library

This project is an online library application built with Django and Django REST Framework. It includes functionality for managing books, comments, ratings, and user authentication.

## Features

- User registration and authentication
- Book management (CRUD operations)
- Comment and rating system
- Add/remove books from favorites

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.10+
- PostgreSQL
- pip (Python package installer)
- Virtualenv (optional but recommended)

### 1. Clone the Repository with the following command

git clone 
cd online-library

### 2. Set Up a Virtual Environment

python -m venv myenv

<!-- acivate virtual environment -->
source myvenv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Up Environment Variables

Create a .env file in the root directory of the project and add your environment variables.

SECRET_KEY=your_secret_key_here
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port

### 5. Configure the Database

Make sure you have PostgreSQL installed and running. Create a database for the project with the following commands.

CREATE DATABASE your_database_name;
CREATE USER your_database_user WITH PASSWORD 'your_database_password';

### 6. Apply Migrations

Apply the Django migrations to set up your database schema with the following command.

python manage.py migrate

### 7. Create a Superuser

Create a superuser to access the Django admin.

python manage.py createsuperuser

### 8. Run the Development Server

Start the Django development server with the following command.

python manage.py runserver


