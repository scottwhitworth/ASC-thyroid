import sys
import os

# Place file at application base (ie. settings.py location)

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
