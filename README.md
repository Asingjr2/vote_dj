# TODO_DJ

Web application using django functionality.

## Installation pt. 1

```bash
create directory
virtualenv venv
pip install -r requirements.txt
set  'GOOGLE_API_KEY' environment variable with personal key
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```

## Installation pt. 2

```bash
Application uses django-allauth to handle user signup, login, and logout.  Django-allauth has predefined urls and templates.  To read relevant documentation check out thier page at: https://django-allauth.readthedocs.io/en/latest/installation.html
```

## API

```bash
Application uses Google Maps API which requires login and user specific key.  For registration and to read documentation please check out: https://cloud.google.com/maps-platform/

Locations used in directions application represent "real" monuments in either Virgina or Washington, DC.
```
