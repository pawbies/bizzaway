default:
	npx tailwindcss -i static/src_css.css -o static/out.css
	python manage.py test
	python manage.py check
	python manage.py runserver

tailwind:
	npx tailwindcss -i static/src_css.css -o static/out.css --watch

compiletranslation:
	python manage.py compilemessages

updatetranslation:
	python manage.py makemessages -a

install:
	pip install django
	npm install -D tailwindcss postcss autoprefixer
	npx tailwindcss init
	python manage.py makemigrations
	python manage.py migrate
	python manage.py test