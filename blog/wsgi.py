"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from dj_static import Cling

# Cling verifica se cada requisição é arquivo estático, se não
# for entrega pro django e se for ele cuida
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = Cling(get_wsgi_application())
