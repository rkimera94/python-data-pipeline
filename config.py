import os
from os import environ 
DB_DETAILS = {
    'dev': {
        'DB_TYPE': 'mysql',
        'DB_NAME': '',
        'DB_HOST': '',
        'DB_NAME': '',
        'DB_USER': '',
        'DB_PASS': ''
    },
    'source': {
        'DB_TYPE': 'postgres',
        'DB_NAME': environ.get('DB_DATABASE_NAME'),
        'DB_HOST': environ.get('DB_HOST'),
        'DB_USER': environ.get('DB_USERNAME'),
        'DB_PASS': environ.get('DB_PASSWORD'),

    },
    'target': {
        'DB_TYPE': 'postgres',
        'DB_NAME': os.environ.get('DB_TARGET'),
        'DB_HOST': os.environ.get('DB_HOST'),
        'DB_PORT': os.environ.get('DB_PORT'),
        'DB_USER': os.environ.get('DB_USERNAME'),
        'DB_PASS': os.environ.get('DB_PASSWORD')
    },
}