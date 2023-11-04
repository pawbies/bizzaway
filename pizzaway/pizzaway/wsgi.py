#for apache later because i can't be bothered to look up how this works now

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaway.settings')

application = get_wsgi_application()
