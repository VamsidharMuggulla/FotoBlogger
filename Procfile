web:python manage.py runserver
web: gunicorn fotoblogger.wsgi --log-file -
heroku ps:scale web=1
heroku buildpacks:set heroku/python
