#!/bin/bash

python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

cd alltext
exec gunicorn app.wsgi:application \
	--bind 0.0.0.0:8000 \
	--workers 3
