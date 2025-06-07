# Blog System

Simple personal blog built with Django.

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

CSRF checks are disabled for simplicity. Log in to `/admin` to manage categories and articles, or use the home page to create and edit posts via AJAX.
