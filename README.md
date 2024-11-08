# Banking System API

This is a banking API system developed with Python, Django, Django REST Framework, and SQLite as the database.

## Prerequisites

- Python 3.x
- Django
- Django REST Framework

## Instructions to Clone and Run the Project

### 1. Clone the Repository

Clone this repository and navigate into the project directory:

```bash
git https://github.com/IvnaFeitosa/bankingSystem.git
cd bankingSystem
````

### 2. Apply Migrations to Set Up the Database

Run the following commands to create the necessary database tables:

```bash
python manage.py makemigrations banking_system
python manage.py migrate
````

### 3. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
````
## Use an API testing to test and interact with the API

### Sugestions:

- Postman
- Insomnia

## Endpoints Options

- customers/register/
- customers/account/
- customers/deposit/
- customers/(account id)/
- customers/withdrawal/(account id)/
- customers/balance/(account id)/
