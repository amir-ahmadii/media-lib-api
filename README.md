# MediaLib API

A robust RESTful API for managing a personal collection of books, movies, and music, built with Django and Django REST Framework. This project serves as a practical demonstration of building scalable and optimized backend services.

## Technology Stack

-   **Backend:** Python, Django, Django REST Framework
-   **Database:** PostgreSQL
-   **Containerization:** Docker, Docker Compose

## Getting Started

To run this project:

1.  **Build and run with Docker:**
    ```bash
    docker-compose up --build -d
    ```

2.  **Apply database migrations:**
    ```bash
    docker-compose exec web python manage.py migrate
    ```

3.  **Load fake data (Optional):**
    ```bash
    docker-compose exec web python manage.py seed_data --count 50
    ```

The API will be available at `http://localhost:8000/api/`.

### API Endpoints
- `/api/books/`
- `/api/movies/`
- `/api/albums/`