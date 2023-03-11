#!/bin/sh

set -e

python manage.py collectstatic --noinput

# uwsgi --socket :8090 --master --enable-threads --module jspedsRest.wsgi
# gunicorn jspedsRest.wsgi:application --bind 0.0.0.0:8090

exec "$@"