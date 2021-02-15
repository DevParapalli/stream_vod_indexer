release: python manage.py migrate
web: gunicorn --workers=3 --bind=0.0.0.0:$PORT server.wsgi