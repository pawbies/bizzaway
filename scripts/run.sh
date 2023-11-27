#!/bin/bash

script_dir="$(dirname "$(readlink -f "$0")")"
cd "$script_dir/.."

./tailwindcss -i static/css/src_css.css -o static/css/out.css
python manage.py test -v 3 --timing
python manage.py check --force-color -v 3
python manage.py runserver --skip-checks