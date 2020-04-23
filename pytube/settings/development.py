#ref :https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html
#import setting
from .base import *
from .tinymce_settings import *
from .django_jet_settings import *
#messgage :Bootstrap Snippet
from django.contrib import messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# gives the root of the project: root/. This is THE ROOT OF THE PROJECT.
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

INSTALLED_APPS += [
     #3rd prty
    'simple_pagination',
    'tinymce',
    'mptt',

    #Newsletter
    'sorl.thumbnail',
    'newsletter',

    #My app
    'organization',
    'home',
    'page',
    'post',
    'app',
    'staff',

    #SHOP
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',

    'shop',

    
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Allauth ----------

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

SITE_ID = 1

# after login redirect to
LOGIN_REDIRECT_URL = '/'

# Make it false if you don't need email varfication
ACCOUNT_EMAIL_VERIFICATION = 'none'


#MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#install :- https://pypi.org/project/psycopg2/
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',#'django.db.backends.postgresql_psycopg2', 
        'NAME':     'pytube',
        'USER':     'postgres',
        'PASSWORD': '!dcuseronly',
        'HOST':     'localhost'
    }
}

# #Heroku DATABASES['default']
# import dj_database_url
# DATABASES =  {'default':dj_database_url.config(default='postgres://xmwffnfspuwngf:f47eaaf1142777a89bec380253fd498c938c38639ee2ddd13c320cfa88a4a6a2@ec2-52-45-14-227.compute-1.amazonaws.com:5432/d9k5asqgavu083')}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases



#blog sign
BLOG_AUTHOR = "Arup Mahapatra || Pytube"


#Newsletter
NEWSLETTER_CONFIRM_EMAIL = True
# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1

# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60

# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100

# Using django-tinymce
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"


#Email Details

EMAIL_HOST = 'mail.pytube.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
