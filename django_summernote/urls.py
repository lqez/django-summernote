from django.conf.urls import patterns, url
from django_summernote.views import editor, upload_attachment

urlpatterns = patterns(
    'django_summernote.views',
    url(r'^editor/(?P<id>.+)/$', editor,
        name='django_summernote-editor'),
    url(r'^upload_attachment/$', upload_attachment,
        name='django_summernote-upload_attachment'),
)
