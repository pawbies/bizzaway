default:
	npx tailwindcss -i static/src_css.css
	python manage.py runserver

tailwind:
	npx tailwindcss -i static/src_css.css -o static/output.css --watch

install:
	pip install django
	npm install -D tailwindcss
	npx tailwindcss init