#!/bin/bash

script_dir="$(dirname "$(readlink -f "$0")")"
cd "$script_dir/.."

npx tailwindcss -i static/src_css.css -o static/out.css
python manage.py test -v 3 --timing
python manage.py check --force-color -v 3
python manage.py runserver --skip-checks