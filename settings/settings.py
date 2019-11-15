from .base import *

if os.getenv('BUILD_ON_TRAVIS', None):
    SECRET_KEY = "SecretKeyForUseOnTravis"
    DEBUG = False
    TEMPLATE_DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test',
            'USER': 'travis',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
        }
    }
