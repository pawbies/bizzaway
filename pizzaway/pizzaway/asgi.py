#i think this is an alternative to wsgi
#i think i've read about that in the django docs
#but i could be wrong i didn't need it so far

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaway.settings')

application = get_asgi_application()
