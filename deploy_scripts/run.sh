#!/bin/bash

# shellcheck disable=SC2164
cd /var/www/husandev
source /var/www/husandev/venv/bin/activate
python3 manage.py runserver 0.0.0.0:8088