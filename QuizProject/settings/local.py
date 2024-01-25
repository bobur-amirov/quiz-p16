from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': '../db.sqlite3', # This is where you put the name of the db file.
#                  # If one doesn't exist, it will be created at migration time.
#     }
# }

DATABASES = {
    "default": {
        "SQL_ENGINE": "django.db.backends.postgresql",
        "SQL_DATABASE": "quizdb",
        "SQL_USER": "quiz",
        "SQL_PASSWORD": "QuizProject123",
        "SQL_HOST": "localhost",
        "SQL_PORT": "5432",
    }
}