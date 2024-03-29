import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-hg5yp0xjud1o&!1_qj%8d*&ls*l3&i47g9kt5e&57o0n=@@7j_'

DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

CKEDITOR_CONFIGS = {
    'default':
        {
            'autoParagraph': False,
            'toolbar': 'basic',
            'allowedContent': True,
        },
}

AUTH_USER_MODEL = 'accounts.Account'

INSTALLED_APPS = [
    'modeltranslation',
    'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'payme',

    'accounts',
    'main',
    'duolar',
    'handbook',
    'place',
    'preperation',
    'orders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

GOOGLE_MAPS_API_KEY = 'AIzaSyAkkKvMyf8Tk3Q8s7MWXin6njbtjIjq2S4'

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
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (

    ('uz', 'Uzbek'),
    ('ky', 'Kyrgyz')
)

DEFAULT_LANGUAGE = 2
LANGUAGE_CODE = 'ky'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ky'
MODELTRANSLATION_LANGUAGES = ('ky', 'uz')
MODELTRANSLATION_TRANSLATION_FILES = (
    'duolar.translation',
    'handbook.translation',
    'main.translation',
    'place.translation',
    'preperation.translation'
)

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAYME: dict = {
    'PAYME_ID': '656d9a2694dc4293bdd4712d',
    'PAYME_KEY': 'txig0epiUPBMaY3c&#senn29SU4wh3ejQaO#',
    'PAYME_URL': 'my-psixolog.uz',
    'PAYME_CALL_BACK_URL': 'my-psixolog.uz',  # merchant api callback url
    'PAYME_MIN_AMOUNT': '10000',  # integer field
    'PAYME_ACCOUNT': 'order_id',
}
