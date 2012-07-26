import os
import sys
 
path = '/home/rita/chapter10'
if path not in sys.path:
    sys.path.insert(0, '/home/rita/chapter10')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'chapter10.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
