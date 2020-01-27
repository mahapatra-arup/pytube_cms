#ref :https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html
#import setting
from .base import *
from .tinymce_settings import *
from .django_jet_settings import *

INSTALLED_APPS += [
     #3rd prty
    'simple_pagination',
    'tinymce',
    

    #My app
    'organization',
    'post',
    'page',
    'app',
    'home',
    'staff',
]

#MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#install :- https://pypi.org/project/psycopg2/
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'pytube',
        'USER':     'postgres',
        'PASSWORD': '!dcuseronly',
        'HOST':     'localhost'
    }
}

#blog sign
BLOG_AUTHOR = "Arup Mahapatra || Pytube"


