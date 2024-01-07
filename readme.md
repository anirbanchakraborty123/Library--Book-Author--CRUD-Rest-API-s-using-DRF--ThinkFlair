# Library-(AUTHOR+BOOK) CRUD REST APIS'S USING DRF Project
 
# This Django project provides simple APIs to manage a relationship between two    models - Author and Book.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/anirbanchakraborty123/Library_CRUD_API.git
   
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
4. Create a superuser for accessing the Django admin:

   ```bash
    python manage.py createsuperuser
    ```
    
5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

 - AUTHOUR APIS:

- List all authors: `GET v1/api/authors/`
- Retrieve details of a specific author by ID: `GET v1/api/authors/<author_id>/`
- Create a new author: `POST v1/api/authors/`

 - BOOK APIS:

- List all books: `GET v1/api/books/`
- Retrieve details of a specific book by ID: `GET v1/api/books/<book_id>/`
- Create a new book: `POST v1/api/books/`

## API documentation:

- To access REST API's version-v1 docs:

 1. 'v1/swagger/'
 2. 'v1/redoc/'  


