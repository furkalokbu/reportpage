from .base import *
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k((9-_0t&p2s+%j4s9qc#xmdz+9k9^vs17oy%tibozrj-bysve'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'reportpage_dev',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgresdb.cqh8zx545xp6.eu-central-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
