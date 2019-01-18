"""
Django settings for Report project.

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
SECRET_KEY = '_vedw8cv1lrmf)h-c3(sxc@_+_sy4f^_!s3-traj8!d5__uvrx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_comments',
    'social_django',
    'social_widgets',
    'news',
    'user',
    'extras',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #Social login providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'robots',
    'fluent_dashboard',

    'admin_tools',     # for staticfiles in Django 1.3
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

)

SITE_ID = 2

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

)

ROOT_URLCONF = 'Report.urls'

WSGI_APPLICATION = 'Report.wsgi.application'


Database
https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3pbr0valabjun',
        'HOST': 'ec2-107-22-211-182.compute-1.amazonaws.com',
        'PORT': '5432',
        'USER': 'abvpzeprmithub',
        'PASSWORD': 'ad6e96f122ad54327a9e8db89bb1783a783e996b9486f61d862d65f95c234ccb',

    }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_2')

CELERY_BROKER_URL = 'amqp://localhost'


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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.request',

            ],
        },
    },
]


LOGIN_REDIRECT_URL = 'news:home'
LOGOUT_REDIRECT_URL = 'news:home'



DOMAIN = "https://reporternews.herokuapp.com"


# EMAIL CONFIGURATIONS

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER = 'thereportersnews@gmail.com'
EMAIL_HOST_PASSWORD = 'reportersnews'
EMAIL_USE_TLS = True


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'allauth.account.auth_backends.AuthenticationBackend',

)


#SOCIAL ACCOUNT SETTINGS

SOCIAL_AUTH_FACEBOOK_KEY = '489688774733419' # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '7a836b6dbb039e25979f17eb85acc191' # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =  '184919632724-tqr8tt08nbit4m0a0n5tllbbrtt88gge.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET =  'LDmvLlt1WSJlJRktSEsu1BKj'

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     }
# }

MANAGERS =[('Akhil', 'akhilanil.sayone@gmail.com'),('Akhil', 'thereportersnews@gmail.com')]
