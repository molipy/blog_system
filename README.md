# Blog System

Simple personal blog built with Django.

English instructions are provided below. For a Chinese version, see
[README.zh.md](README.zh.md).

## Setup

1. Install dependencies:
   ```bash
 pip install -r requirements.txt
  ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
4. Start the development server:
   ```bash
 python manage.py runserver
  ```

CSRF checks are disabled for simplicity. Log in to `/admin` to manage categories and articles using the beautiful **SimpleUI** interface.  Markdown editing is enabled in the admin so you can write posts more comfortably.  Posts can also be created and edited from the home page via AJAX.
