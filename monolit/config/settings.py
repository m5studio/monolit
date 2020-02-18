"""
Django settings for monolit project.

Generated by 'django-admin startproject' using Django 2.2

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Django Environ https://github.com/joke2k/django-environ
import environ
env = environ.Env(
    # Set casting, default value
    DEBUG=(bool, False)
)
# Reading .env file
PATH_TO_ENV = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_file=PATH_TO_ENV)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

if DEBUG:
    ALLOWED_HOSTS = ['*']
if not DEBUG:
    ALLOWED_HOSTS = env('ALLOWED_HOSTS').split('|')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'ckeditor',
    'django_unused_media',
    'django_cleanup.apps.CleanupConfig',
    'imagekit',

    'apps.core.apps.CoreConfig',
    'apps.realty.apps.RealtyConfig',
    'apps.news.apps.NewsConfig',
    'apps.mortgage.apps.MortgageConfig',
    'apps.company.apps.CompanyConfig',
    'apps.pages.apps.PagesConfig',
    'apps.forms.apps.FormsConfig',

    'apps.favorites.apps.FavoritesConfig',
    'apps.api.apps.ApiConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'apps.core.context_processors.settings',
                'apps.core.context_processors.monolit_objects',
                'apps.core.context_processors.monolit_company_age',
                'apps.core.context_processors.current_month_rus',
                'apps.core.context_processors.compleated_objects',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DB local
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
# DB production
if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': env("DB_USER"),
            'NAME': env("DB_NAME"),
            'PASSWORD': env("DB_PASSWORD"),
            'HOST': env("DB_HOST"),
            'PORT': env("DB_PORT"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

# USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'layout/dist'),

    ('css', os.path.join(BASE_DIR, 'layout/dist/css')),
    ('js', os.path.join(BASE_DIR, 'layout/dist/js')),
    ('favicons', os.path.join(BASE_DIR, 'layout/dist/images/favicons')),
]


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Sessions https://docs.djangoproject.com/en/2.2/ref/settings/#sessions
# default value
# SESSION_COOKIE_AGE = 1209600


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False


# Datetime settngs
DATETIME_FORMAT = 'd/m/Y H:i:s'
SHORT_DATETIME_FORMAT = 'd/m/Y H:i'

# TODO: Setup Django Сaching https://docs.djangoproject.com/en/2.2/topics/cache/

""" [ Additional modules Settings ] """

# Custom settings
MAX_IMG_WIDTH = 1980
IMG_QUALITY = 70


# CKEditor https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', '-', 'Undo', 'Redo'],
            # ['NumberedList', 'BulletedList', '-', 'Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['ShowBlocks', 'SpecialChar', '-', 'RemoveFormat', 'Source']
        ],
        'removePlugins': 'stylesheetparser',
    }
}


# https://github.com/matthewwithanm/django-imagekit
IMAGEKIT_CACHEFILE_DIR = 'cache-images'
