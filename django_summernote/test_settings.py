DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_summernote.db',
    }
}

SECRET_KEY = 'django_summernote'

ROOT_URLCONF = 'django_summernote.urls'

INSTALLED_APPS = (
    'django_summernote',
)
