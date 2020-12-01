#!/bin/bash
cd /usr/src/app
# running migrations
flask db upgrade
# starting http server
uwsgi --ini /usr/src/app/uwsgi.ini