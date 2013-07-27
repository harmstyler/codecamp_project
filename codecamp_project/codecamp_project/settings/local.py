# settings/local.py
from .base import *
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_DIR, '../../'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/codecamp.db',
    }
}

INSTALLED_APPS += ("debug_toolbar", )

INTERNAL_IPS = ("127.0.0.1", )

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)