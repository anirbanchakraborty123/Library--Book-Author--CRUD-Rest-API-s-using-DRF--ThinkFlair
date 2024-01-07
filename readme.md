# Library-(AUTHOR+BOOK) CRUD REST APIS'S USING DRF Project
 
# This Django project provides simple APIs to manage a relationship between two    models - Author and Book.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/anirbanchakraborty123/Library--Book-Author--CRUD-Rest-API-s-using-DRF--ThinkFlair.git
   
   cd library

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

 - AUTHOUR:

- List all authors: `GET v1/api/authors/`
- Retrieve details of a specific author by ID: `GET v1/api/authors/<author_id>/`
- Create a new author: `POST v1/api/authors/`

 - BOOK:

- List all books: `GET v1/api/books/`
- Retrieve details of a specific book by ID: `GET v1/api/books/<book_id>/`
- Create a new book: `POST v1/api/books/`

## API documentation:




