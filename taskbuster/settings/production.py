# -*- coding: utf-8 -*-
from .base import *
DEBUG = False
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbuster_db',
        'USER': 'myusername',
        'PASSWORD': 'mypassword',
        'HOST': '',
        'PORT': '',
        }
    }