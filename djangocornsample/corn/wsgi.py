"""
WSGI config for corn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'corn.settings')

os.environ["SCRIPT_NAME"] = "/a/b/c/d/e"
print("Prefix: ", os.environ["SCRIPT_NAME"])

application = get_wsgi_application()
