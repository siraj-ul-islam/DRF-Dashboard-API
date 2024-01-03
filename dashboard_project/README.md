# Project Title: App Dashboard API

## Overview
The App Dashboard API is a Django Rest Framework (DRF) based backend service that enables users to manage applications under their account. Users can create, retrieve, update, and delete applications, associate subscriptions with pricing plans, and handle user authentication including registration, login, and password reset.

## Features
- **User Management:** Register and log in.
- **Application Management:** Allows users to maintain a list of applications.
- **Subscription Management:** Users can subscribe an application to a plan and update subscription details.
- **Plan Management:** Admin users can create and manage pricing plans.
- **Security:** Token-based authentication to secure API endpoints.
- **Swagger Documentation:** Auto-generated interactive API documentation using Swagger.

## Technical Requirements
Before you begin, ensure you have met the following requirements:

- Python 3.10
- Django 4.0
- Django Rest Framework 3.14.0
- DRF Authtoken
- drf-yasg for Swagger

You can install all the required packages using pip or pip install -r requirements.txt:

```sh
pip install django djangorestframework drf-yasg
```

## Installation
To set up the App Dashboard API on your local machine:

1. Clone this repository to your local machine.
2. Create a virtual environment.

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies.

```sh
pip install -r requirements.txt
```

4. Run migrations to create the database schema.

```sh
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser account for admin access.

```sh
python manage.py createsuperuser
```

6. Start the development server.

```sh
python manage.py runserver
```

7. Visit `http://localhost:8000/swagger/` in your browser to view the Swagger UI for the API documentation.

## Usage
Username:dashboard
Password: dashboard
Use the following endpoints to interact with the API:

- `/api/register/`: Register a new user account.
- `/api/login/`: Authenticate and receive a token.
- `/api/apps/`: List and create applications.
- `/api/apps/<id>/`: Retrieve, update, or delete specific applications.
- `/api/plans/`: List and create pricing plans (admin only).
- `/api/plans/<id>/`: Retrieve, update, or delete specific pricing plans (admin only).
- `/api/subscriptions/<id>/`: Retrieve and update subscription details.


