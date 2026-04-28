web: python manage.py migrate && python manage.py populate_questions && gunicorn quizproject.wsgi:application --bind 0.0.0.0:$PORT
