import os.path
from pathlib import Path
import platform

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sa!)g0we(5+9bz$@%#-z_8rdsg*sop37rqrr=+$r7h87%6$%_+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['geodjango.pythonanywhere.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.gis",
    "world",
    'leaflet.apps.LeafletConfig',
    'bootstrap4'
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

ROOT_URLCONF = 'geodjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'geodjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if platform.system() == "Windows":

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': "postgis",
            'USER': 'postgres',
            'PASSWORD': "Er880413",
            'HOST': "localhost",
            "PORT": "5432",
        },
    }

    GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, "OSGeo4W", "bin", "gdal307.dll")

    GEOS_LIBRARY_PATH = os.path.join(BASE_DIR, "OSGeo4W", "bin", "geos_c.dll")

elif platform.system() == "Linux":  # pythonanywhere

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.spatialite',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    GDAL_LIBRARY_PATH = r"/usr/local/lib/libgdal.so"
    GEOS_LIBRARY_PATH = r"/usr/lib/x86_64-linux-gnu/libgeos_c.so"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LEAFLET_CONFIG = {
    # conf here
    'DEFAULT_CENTER': (40, 38),
    'DEFAULT_ZOOM': 1,
    'MIN_ZOOM': 3,

    'DEFAULT_PRECISION': 6,
    'SCALE': 'both',
    'PLUGINS': {
        'name-of-plugin': {
            'css': [os.path.join(BASE_DIR, "static", "leaflet", "leaflet.css"),
                    os.path.join(BASE_DIR, "static", "leaflet", "leaflet_django.css")],
            'js': [os.path.join(BASE_DIR, "static", "leaflet", "leaflet.js"),
                   os.path.join(BASE_DIR, "static", "leaflet", "leaflet.extras.js"), ],
            'auto-include': True,
        },

    },
    'FORCE_IMAGE_PATH': True,
    'OVERLAYS': [('Cadastral', 'http://server/a/{z}/{x}/{y}.png', {'attribution': '&copy; IGN'})],
    'TILES': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
}
