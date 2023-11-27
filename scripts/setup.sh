#!/bin/bash

script_dir="$(dirname "$(readlink -f "$0")")"
cd "$script_dir/.."

pacman -S python tailwindcss

pip install django Pillow pytz
tailwindcss init
python manage.py makemigrations
python manage.py migrate
python manage.py test