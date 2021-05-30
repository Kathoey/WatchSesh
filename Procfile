web: gunicorn WatchSesh.wsgi --log-file -
worker: python manage.py runworker channel_layers --settings=WatchSesh.settings -v2