from .base import *
import os
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME','productaste'),
        'USER':os.getenv('DB_USER','root'),
        'PASSWORD':os.getenv('DB_PASSWORD','8888'),
        'HOST':os.getenv('DB_HOST','127.0.0.1'),
        'PORT':os.getenv('DB_PORT','3306'),
        'OPTIONS':{
            'charset':'utf8mb4'
        }
    }
}