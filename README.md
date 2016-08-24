# django-apiary

## Housekeeping

    pip install Django Pillow django-filer
    python manage.py migrate
    python manage.py collectstatic

You'll also need to copy `apiary/example-settings.py` to `apiary/settings.py` and update `SECRET_KEY`, `ALLOWED_HOSTS`, `DATABASES`, `STATIC_ROOT` and `MEDIA_ROOT` accordingly.
