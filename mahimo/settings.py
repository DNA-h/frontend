"""
Django settings for mahimo project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import clients

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "3_dcc%ogq85%l2u0ils5#jvdk&2)tg1rzv9kp33w4)*7(mi9p5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['hussein-ubuntu', '127.0.0.1', 'localhost', '16a8a512.ngrok.io']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file-db': {
            'level': 'DEBUG',
            # 'class': 'logging.handlers.RotatingFileHandler',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'file-db.log/'),
            'formatter': 'verbose',
        },
        'file-app': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'file-app.log/'),
            'formatter': 'verbose',
        },
        'file-django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'file-django.log/'),
            'formatter': 'verbose',
        },
        'file-request': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR,'file-request.log/'),
            'formatter': 'verbose',
        },
        'console':{
            'level':'INFO',
            'filters': ['require_debug_true'],
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers':['console','file-django'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['console','file-db'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers':
            ['console', 'file-request','mail_admins','console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}


AUTH_USER_MODEL = 'clients.User'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.auth0',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'rest_framework',
    'corsheaders',
    'clients',
    'questionnaire',
    'djstripe',
    'drf_yasg',
    'constance',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mahimo.urls'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',

            ],
        },
    },
]

# AllAuth Configuration
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1


WSGI_APPLICATION = 'mahimo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mahimodb',
        'USER': 'postgres',
        'PASSWORD': 'zaq1@wsx',
        'HOST': 'localhost',
        'PORT': '5432',
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
        'OPTIONS': {
            'min_length': 9,
    }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# stripe

STRIPE_LIVE_PUBLIC_KEY = os.environ.get("STRIPE_LIVE_PUBLIC_KEY", "pk_test_sPNLxfW34KY7vtivoOH0XWj0")
STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "<your secret key>")
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_sPNLxfW34KY7vtivoOH0XWj0")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_bGzee5F6B77jQxNrK3eNl7Aq")
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_8kmPRhWcaNZEJB1FM2f5AdAYk29kqFNg"


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (os.path.join('static'), )

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES':
        (
	'rest_framework.authentication.BasicAuthentication',
	'rest_framework.authentication.SessionAuthentication',
	'rest_framework.authentication.TokenAuthentication',)
}


CONSTANCE_CONFIG = {
    'SITE_NAME': ('My Title', 'Website title'),
    'SITE_DESCRIPTION': ('', 'Website description'),
    'THEME': ('light-blue', 'Website theme'),
}
CONSTANCE_CONFIG_FIELDSETS = {
    'General Options': ('SITE_NAME', 'SITE_DESCRIPTION'),
    'Theme Options': ('THEME',),
}

CHOICES_SEPARATOR = ','

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:3001',
)

LOGIN_REDIRECT_URL = '/index/'

SWAGGER_SETTINGS = {
    'LOGIN_URL': '/accounts/login',
    'LOGOUT_URL': '/accounts/logout',
}


try:
    from local_settings import *
except ImportError:
    pass