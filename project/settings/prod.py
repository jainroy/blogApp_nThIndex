from .base import *
from decouple import config

SECRET_KEY = config('THE_SECRET_KEY')
DEBUG = config('MY_DEBUG', cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT', default='5432'),
    }
}

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')