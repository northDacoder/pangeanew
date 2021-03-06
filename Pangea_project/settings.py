"""
Django settings for Pangea_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '89ic7zu@^q)_0u_z*7%uk18tnt^p=!_#o8m)brf1k_22el%rdc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'charity_app',
    'registration',
    'giver_app',
    'jquery'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Pangea_project.urls'

WSGI_APPLICATION = 'Pangea_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pangea_project_databse',
        'USER': "root",
        'PASSWORD':"",
        "HOST":"127.0.0.1",
        "PORT": ""
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/static/'
STATIC_URL  = '/static/'

LOGIN_REDIRECT_URL = "index"
import smtplib
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
smtp=smtplib.SMTP(host=EMAIL_HOST,port=EMAIL_PORT)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "yash.saxena1217@gmail.com"
EMAIL_HOST_PASSWORD = 'FEDERERKOBE123456'

ACCOUNT_ACTIVATION_DAYS=7