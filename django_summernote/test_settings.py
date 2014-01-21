DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_summernote.db',
    }
}

STATIC_URL = '/'
MEDIA_ROOT = 'test_media'

SECRET_KEY = 'django_summernote'

ROOT_URLCONF = 'django_summernote.urls'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django_summernote',
)
