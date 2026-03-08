"""
WSGI config for DevFlow project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# This line tells Django which settings file to use (devflow_core/settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devflow_core.settings')

# This is the actual application object the web server will talk to
application = get_wsgi_application()