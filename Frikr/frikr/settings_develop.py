# -*- coding:utf-8 -*-
from  settings import *

#En consola python manage.py migrate --settings=frikr.settings_develop
#en el server runserver 192.168.1.x:8000 --settings=frikr.settings_develop   ... Poner tu IP, no x
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_DEVELOP.sqlite3'),
    }
}