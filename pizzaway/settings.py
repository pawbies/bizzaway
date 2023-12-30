#here are all the settings
#some smart people might have figured that out already when they saw the filename
from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

#base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/ <- that's be imporant in the future


#key for hashing and stuff
SECRET_KEY = 'django-insecure-_^-x3)#wyp%1gvz!43q3w=q*8-+uesbt9g4-fq!y6*lbz9#dm#'


#what do you thing
DEBUG = True


#valid domain names
ALLOWED_HOSTS = []


#all the used apps
INSTALLED_APPS = [
    'webinterface.apps.WebinterfaceConfig',
    'employee.apps.EmployeeConfig',
    'game.apps.GameConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#stuff for altering IO 
#at least that's what the django website says
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


LOCALE_PATHS = [
    BASE_DIR / "pizzaway" / "locale",
    BASE_DIR / "webinterface" / "locale",
    BASE_DIR / "employee" / "locale",
    BASE_DIR / "game" / "locale",
]

#another thing you can probably guess is
ROOT_URLCONF = 'pizzaway.urls'

#settings for html templates
#better not to touch that stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# "Web Server Gateway Interface" for deploying with apache later
WSGI_APPLICATION = 'pizzaway.wsgi.application'

#database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#settings that controll validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#the language of the site
LANGUAGE_CODE = 'en'

#timezone of the server
TIME_ZONE = 'Europe/Berlin'

#this has also something to do with the language 
USE_I18N = True

#if i want time aware for the time zone
USE_TZ = True


#where the static files are
STATIC_URL = 'static/'

#other static directories that can be searched
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

#default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#where to redirect @login_required views to
LOGIN_URL = "/mitarbeiter/login"

#for user uploaded stuff (the pizza images in our case)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
    ("es", _("Spanish")),
]