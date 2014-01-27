from __future__ import absolute_import
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from .common import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

