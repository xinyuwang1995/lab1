from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'productaste',
        'USER':'root',
        'PASSWORD':'8888',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS':{
            'charset':'utf8mb4',
        "init_command":"SET foreign_key_checks = 0;",
        },
    'TEST': {
            'NAME':'test',
        },
    }
}