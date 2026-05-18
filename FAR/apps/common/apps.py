# from django.apps import AppConfig


# class CommonConfig(AppConfig):
#     name = 'common'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'far',
        'USER': 'root', 
        'PASSWORD': 'root123',
        'HOST': '172.16.0.9',
        'PORT': '3307',   
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

from django.apps import AppConfig

class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.common'  
    label = 'common'