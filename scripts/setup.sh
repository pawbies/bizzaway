#!/bin/bash

script_dir="$(dirname "$(readlink -f "$0")")"
cd "$script_dir/.."

pacman -S python

curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss-linux-x64
mv tailwindcss-linux-x64 tailwindcss

pip install django Pillow pytz
#./tailwindcss init
python manage.py makemigrations
python manage.py migrate
python manage.py test

cd static/games/connect/
make wasm