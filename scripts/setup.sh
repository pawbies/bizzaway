#!/bin/bash

script_dir="$(dirname "$(readlink -f "$0")")"
cd "$script_dir/.."

pip install django Pillow pytz
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
python manage.py makemigrations
python manage.py migrate
python manage.py test