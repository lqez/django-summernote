from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'django_summernote.views',
    url(r'^editor/(?P<id>.+)/$', 'editor', name='django_summernote-editor'),
)
