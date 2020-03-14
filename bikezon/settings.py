"""
Django settings for bikezon project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files path
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Automatically find templates DIR to avoid hard-coding paths
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Email auth creds
gmail_server = True
if os.path.exists('email.json'):
    print("found email server")
    EMAIL_AUTH_PATH = os.path.join(BASE_DIR, 'email.json')
else:
    print("did not find email server")
    gmail_server = False
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tqbagvz-mhdh2##rop@(2g$_na^*g07m-tor3mnh8%e#=+w+=r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'phone_field',
    'captcha',
    'bootstrap4',
    'crispy_forms',
    'coverage',
    'selenium',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bikezon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bikezon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR, ]

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# CAPTCHA Settings
RECAPTCHA_PUBLIC_KEY = '6LcWyN4UAAAAALfrAGuuoRR6V0m9Dck1u4YAWoE2'
RECAPTCHA_PRIVATE_KEY = '6LcWyN4UAAAAAJd7i-5YETqS2OzOilH-IdB6vRrD'
RECAPTCHA_DOMAIN = 'www.recaptcha.net'

# Email setting
if gmail_server:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # Email server settings
    with open(EMAIL_AUTH_PATH, 'r') as f:
        email_data = json.load(f)

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = email_data["email"]
    EMAIL_HOST_PASSWORD = email_data["password"]
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
