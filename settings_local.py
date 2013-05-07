# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG
# SALES_EMAIL = 'sales@nwclimate.ru'
SALES_EMAIL = 'antipov.serge@gmail.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
    	    'init_command': 'SET names utf8',
        }
    }
}

EMAIL_HOST = 'localhost'  # адрес smtp-сервера. например 'smtp.gmail.com' # # для локального хоста - 'localhost'
EMAIL_PORT = 1025  # порт smtp-сервера (обычно 587 или 25 для TLS или 465 для SSL)
# # для локального хоста - обычно порт 1025
EMAIL_HOST_USER = ''  # логин
EMAIL_HOST_PASSWORD = ''  # пароль
EMAIL_USE_TLS = False  # включить/отключить TLS (для тестового режима - False)
DEFAULT_FROM_EMAIL = 'no-reply@ex.ru'