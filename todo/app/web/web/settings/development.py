"""Django development settings"""
import os

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


# https://github.com/twoscoops/django-twoscoops-project/tree/develop/project_name/project_name/settings
def get_env_setting(setting):
    """Get the environment setting or return exception"""
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2erjkl!^vj(v8jga*bh$kaima5i=(2^b)ob=dmwj5uvwectv1l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_ENV_DB'],
        'USER': os.environ['DB_ENV_USER'],
        'PASSWORD': os.environ['DB_ENV_PASS'],
        'HOST': os.environ['DB_PORT_5432_TCP_ADDR'],
        'PORT': os.environ['DB_PORT_5432_TCP_PORT'],
    }
}
