# Simple_CMS

A small Django-based content management / personal weblog project (HMBlogs) implementing a simple blog with posts, images and basic admin management. This project was scaffolded with Django 6.0 and uses a SQLite database by default. It includes a simple Article model, templates for listing posts and viewing a single post, and an admin configuration to manage articles.

---

## Table of Content

- [Features](#Features)
- [Project structure](#Project-structure)
- [Requirements / Prerequisites](#Requirements\/\Prerequisites)
- [Quick start](#Quick-start)
- [Important configuration notes](#Important-configuration-notes)
- [Models & Admin](#Models-&-Admin)
- [License](#License)

---

## Features

- Create and manage blog articles via the Django admin.
- Article model with title, content, author, slug, image, status (draft/published), timestamps.
- Published manager to list only published posts.
- Templates for list and detail views with static assets and a responsive layout.
- Static and media handling configured (STATICFILES_DIRS and MEDIA_ROOT).
- Ready-to-run with SQLite for local development.

---

## Project structure

- personalWeblog/
  - manage.py
  - personalWeblog/
  - weblog/
- static/ — static assets referenced by templates (expected)
- media/ — uploaded images (configured by MEDIA_ROOT)
- LICENSE

---

## Requirements / Prerequisites

- Python 3.10+ (project generated with Django 6.0)
- pip
- virtualenv or venv recommended
- Pillow (for ImageField support)
- (Optional) gunicorn / uwsgi + nginx for production deployments

Note: The project’s settings currently include a SECRET_KEY and DEBUG=True. For production, replace SECRET_KEY and set DEBUG=False. See "Configuration & Security" below.

## Quick start

1. Clone the repository
   ```bash
   git clone https://github.com/HoomanMoradnia/Simple_CMS.git
   cd Simple_CMS
   ```

3. Create and activate a virtual environment
   ```bash
   python -m venv venv
   ```
   
   ### On macOS / Linux
     ```bash
     source venv/bin/activate
     ```
   
   ### On Windows (PowerShell)
     ```bash
     venv\Scripts\Activate.ps1
     ```

4. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access Django admin
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server
    ```bash
     python manage.py runserver
    ```

8. Visit
   - Main site: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin
  
---

## Important configuration notes

- Database: By default this project uses SQLite (configured in settings.py). For production, switch to PostgreSQL or another RDBMS and update DATABASES.
- SECRET_KEY: A secret key is currently present in settings.py — DO NOT use this value in production. Instead use an environment variable and load it in settings.
- DEBUG: Currently set to True in settings.py. Set DEBUG=False in production and properly configure ALLOWED_HOSTS.
- Static & Media:
  - STATICFILES_DIRS = [ BASE_DIR / 'static' ]
  - MEDIA_ROOT is configured to ./media/ and MEDIA_URL = '/media/' (development serves media via urlpatterns when DEBUG=True)
 
---

## Models & Admin

Article model (weblog/models.py) includes:
- title, content, author (ForeignKey to auth.User)
- created_at, updated_at
- status (draft|published)
- slug (unique)
- image (optional ImageField)

Admin registration (weblog/admin.py) includes a customized ArticleAdmin with:
- list_display, list_filter, search_fields, readonly_fields and basic fieldsets for easier management.

---

## License

This project is licensed under the MIT License — see the LICENSE file for details.
