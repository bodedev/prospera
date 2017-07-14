# -*- coding: utf-8 -*-


import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '*%+t3h%v7kcr!*ql3t!c9%99u0&2objrcx)$a(btq2rn#r^fqf'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'simple_history',
    'social_django',
    'common',
    'plataforma',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'prospera.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'prospera.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
]

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'plataforma.pipelines.save_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

# Configurações do Django Social Auth

SOCIAL_AUTH_GITHUB_KEY = '00019165722992da6704'
SOCIAL_AUTH_GITHUB_SECRET = 'd7ba3679d1381db6da0b51f2cb9050677ca06186'

SOCIAL_AUTH_TWITTER_KEY = 'a471yvGqyszzdcAdL7Hu7A9it'
SOCIAL_AUTH_TWITTER_SECRET = 'rbht3obVrKD8dsuvFY7kVl6fhzhcMdUiFFoefMEI5IObTlCqv7'

SOCIAL_AUTH_FACEBOOK_KEY = '1840103436255351'
SOCIAL_AUTH_FACEBOOK_SECRET = '0e15e15c8ff756a51dca2c9d467cc93f'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '715506321226-t5te2ue0tdkp14bca0gfr4t7oka7c5mg.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'rIVQ9_gE6tET-J2lQd3jAxn3'

SOCIAL_AUTH_LOGIN_ERROR_URL = 'home'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'home'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

ETHERSCAN_APIKEY = "TI3JTME844UTC71TFZ2YQD35F75GHQNQN7"
ETHERSCAN_CONTRACT_ADDRESS = "0x0c04d4f331da8df75f9e2e271e3f3f1494c66c36"
ETHERSCAN_START_BLOCK_NUMBER = 3965050
ETHERSCAN_TOKENNAME = "DGD"
MAX_TRANSACTIONS_PROFILE = 5

if not os.path.exists(os.path.join(BASE_DIR, 'prospera', 'local.py')):
    raise Exception("Couldn't import the local configuration file!")
else:
    from local import *
