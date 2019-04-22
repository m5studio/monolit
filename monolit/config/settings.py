"""
Django settings for monolit project.

Generated by 'django-admin startproject' using Django 2.2

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Django Environ https://github.com/joke2k/django-environ
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
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
    'location_field',
    'multiselectfield',
    'django_unused_media',
    'django_cleanup.apps.CleanupConfig',
    'imagekit',

    'apps.settings.apps.SettingsConfig',
    'apps.realty.apps.RealtyConfig',
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

                'apps.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
# TODO: setup producrion DB
if not DEBUG:
    print("!!! SET DB Settings for non-DEBUG mode")
    pass


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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


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
            ['NumberedList', 'BulletedList', '-', 'Image'],
            ['Link', 'Unlink'],
            ['ShowBlocks', 'SpecialChar', '-', 'RemoveFormat', 'Source']
        ],
        'removePlugins': 'stylesheetparser',
    }
}


# https://github.com/caioariede/django-location-field
# FIXME: API KEY is not OURS
GOOGLE_MAPS_API_KEY = 'AIzaSyC78BkEiMHHQLj5FrxlFUPUhUL0mmlcHIY'

LOCATION_FIELD_PATH = STATIC_URL + 'location_field'

LOCATION_FIELD = {
    'map.provider': 'google',
    # 'map.zoom': 17,
    'map.zoom': 8,

    'search.provider': 'google',
    'search.suffix': '',

    # Google
    'provider.google.api': '//maps.google.com/maps/api/js',
    'provider.google.api_key': GOOGLE_MAPS_API_KEY,
    'provider.google.map_type': 'ROADMAP',

    # Mapbox
    'provider.mapbox.access_token': '',
    'provider.mapbox.max_zoom': 18,
    'provider.mapbox.id': 'mapbox.streets',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 18,

    # misc
    'resources.root_path': LOCATION_FIELD_PATH,
    'resources.media': {
        'js': [
                LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
                LOCATION_FIELD_PATH + '/js/form.js',
            ],
    },
}


# https://github.com/matthewwithanm/django-imagekit
# IMAGEKIT_CACHEFILE_DIR = 'CACHE'
IMAGEKIT_CACHEFILE_DIR = 'cached-images'
