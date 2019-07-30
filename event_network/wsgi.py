"""
WSGI config for event_network project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_network.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# from whitenoise import WhiteNoise
# application = WhiteNoise(application)