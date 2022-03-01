import dj_database_url
from dashplotly.settings import *




DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['projet-etic.herokuapp.com']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
