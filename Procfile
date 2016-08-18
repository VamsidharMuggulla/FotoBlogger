web:python manage.py makemigrations
web:python manage.py migrate
web:python manage.py runserver
web: gunicorn CodeSamples.wsgi --log-file -
heroku ps:scale web=1
heroku buildpacks:set heroku/python
heroku pg:psql --app fotoblogger DATABASE
heroku config:set DEBUG_COLLECTSTATIC=1
