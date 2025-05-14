#!/bin/sh

if [ ! -f "/code/manage.py" ]; then
  echo "Creating new Django project..."
  django-admin startproject BizAuth .
fi

echo "Applying migrations..."
python manage.py migrate

echo "Running development server..."
python manage.py runserver 0.0.0.0:8000
