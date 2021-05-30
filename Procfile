web: gunicorn WatchSesh.wsgi --log-file -
worker: python manage.py runworker channel_layer --settings=WatchSesh.settings -v2