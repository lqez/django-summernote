DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_summernote.db',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

STATIC_URL = '/'
MEDIA_ROOT = 'test_media'

SECRET_KEY = 'django_summernote'

ROOT_URLCONF = 'django_summernote.urls'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django_summernote',
)
