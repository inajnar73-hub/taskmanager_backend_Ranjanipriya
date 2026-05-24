# Task Manager Full Stack Application

## Backend Technologies
- Django REST Framework
- JWT Authentication
- SQLite / PostgreSQL
- SMTP Email Notification

## Features
- User Login Authentication
- Task Creation
- Task Assignment
- Email Notifications
- Protected APIs using JWT

## API Endpoints

### Login
POST /login/

### Create Task
POST /api/tasks/

### Get Tasks
GET /api/tasks/

## Environment Variables

Create a .env file:

EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

## Run Project

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver