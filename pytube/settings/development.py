#ref :https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html
#import setting
from .base import *
from .tinymce_settings import *
from .django_jet_settings import *

# gives the root of the project: root/. This is THE ROOT OF THE PROJECT.
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

INSTALLED_APPS += [
     #3rd prty
    'simple_pagination',
    'tinymce',
    # All your other apps here
    'versatileimagefield',
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


#Field
# VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
#     "products": [
#         ("product_gallery", "thumbnail__540x540"),
#         ("product_gallery_2x", "thumbnail__1080x1080"),
#         ("product_small", "thumbnail__60x60"),
#         ("product_small_2x", "thumbnail__120x120"),
#         ("product_list", "thumbnail__255x255"),
#         ("product_list_2x", "thumbnail__510x510"),
#     ],
#     "background_images": [("header_image", "thumbnail__1080x440")],
#     "user_avatars": [("default", "thumbnail__445x445")],
# }

# VERSATILEIMAGEFIELD_SETTINGS = {
#     # Images should be pre-generated on Production environment
#     "create_images_on_demand": get_bool_from_env("CREATE_IMAGES_ON_DEMAND", DEBUG)
# }
VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 2592000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    'cache_name': 'versatileimagefield_cache',
    # The save quality of modified JPEG images. More info here:
    # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    'jpeg_resize_quality': 70,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    'sized_directory_name': '__sized__',
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    'filtered_directory_name': '__filtered__',
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    'placeholder_directory_name': '__placeholder__',
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    'create_images_on_demand': True,
    # A dot-notated python path string to a function that processes sized
    # image keys. Typically used to md5-ify the 'image key' portion of the
    # filename, giving each a uniform length.
    # `django-versatileimagefield` ships with two post processors:
    # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
    #    md5 hash of `image_key`.
    # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
    #    of the 32 character md5 hash of `image_key`.
    # By default, image_keys are unprocessed. To write your own processor,
    # just define a function (that can be imported from your project's
    # python path) that takes a single argument, `image_key` and returns
    # a string.
    'image_key_post_processor': None,
    # Whether to create progressive JPEGs. Read more about progressive JPEGs
    # here: https://optimus.io/support/progressive-jpeg/
    'progressive_jpeg': False
}

#blog sign
BLOG_AUTHOR = "Arup Mahapatra || Pytube"


#Newsletter
NEWSLETTER_CONFIRM_EMAIL = False
# Using django-tinymce
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"


