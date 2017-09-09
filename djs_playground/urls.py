from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from djs_playground.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
