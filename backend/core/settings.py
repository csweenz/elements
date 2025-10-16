from pathlib import Path
import os
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.environ.get('SECRET_KEY')

# run with debug turned off in production!
DEBUG = True
# specified further in production
ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:5173"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', 
    'corsheaders',
    'elemental',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'elements',
        'USER': os.environ.get('dbuser'),
        'PASSWORD': os.environ.get('dbpw'),
        'HOST': os.environ.get('dbhost'),
        'PORT': os.environ.get('dbport'),
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
        },
    }
}

import sys
if 'pytest' in sys.modules:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },
    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },
    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },
    {        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",  # CSRF-protected
        # todo token/JWT later
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 50,
}

# --- CELERY CONFIGURATION ---
CELERY_BROKER_URL = 'redis://127.0.0.1:6380/0' 
CELARY_RESULT_BACKEND = 'redis://127.0.0.1:6380/0' 
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC' 

CELERY_BEAT_SCHEDULE = {
    "ingest-worldbank-pink-sheet-daily-0915": {
        "task": "elemental.tasks.ingest_worldbank_pink_sheet",
        "schedule": crontab(hour=9, minute=15),  # server TZ
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Frontend Stuff for production
CORS_ALLOW_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:5173",
]
