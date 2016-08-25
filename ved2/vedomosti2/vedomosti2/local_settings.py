import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ved2',
        'USER': 'root',
        'PASSWORD': '0013Tau',
        'HOST': 'localhost',
        'PORT': '3306',

    }
}

DEBUG = True