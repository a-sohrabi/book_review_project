# Book Review Project

This is a simple Book Review API built with FastAPI. It allows users to register, log in, and manage books, reviews, and bookmarks.

## Features

- **User Registration & Authentication:** Users can register and log in with their email and password.
- **Book Management:** Admin users can add, edit, and delete books.
- **Review Management:** Users can add reviews for books.
- **Bookmark Management:** Users can bookmark books.
- **JWT Authentication:** Secure endpoints with JWT tokens.

## Project Structure

```plaintext
.
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── books.py
│   │   ├── reviews.py
│   │   ├── bookmarks.py
│   │   └── users.py
│   ├── schemas.py
│   └── crud.py
├── alembic/
├── alembic.ini
├── Dockerfile
├── .env
└── README.md
```

Prerequisites

    Docker: Make sure you have Docker installed on your machine.

Environment Variables

    Create a .env file at the root of the project with the following content:

env

    DATABASE_URL=sqlite:///./test.db
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30

Running the Application:

You can run the application using Docker.
Step 1: Build the Docker Image


    docker build -t book-review-app .

Step 2: Run the Docker Container


    docker run -d -p 8000:8000 --name book-review-container book-review-app

The application will be available at http://localhost:8000.
Step 3: Access the Swagger UI

You can access the Swagger UI for the API documentation at http://localhost:8000/docs.
Database Migrations

This project uses Alembic for database migrations.
Running Migrations


    alembic upgrade head