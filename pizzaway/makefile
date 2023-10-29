default:
	npx tailwindcss -i static/src_css.css -o static/out.css
	python manage.py runserver

tailwind:
	npx tailwindcss -i static/src_css.css -o static/out.css --watch

install:
	pip install django
	npm install -D tailwindcss postcss autoprefixer
	npx tailwindcss init
	python manage.py makemigrations
	python manage.py migrate