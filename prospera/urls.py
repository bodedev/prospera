# -*- coding: utf-8 -*-


from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from plataforma.urls import urlpatterns as plataforma_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += plataforma_urls

# server media files (only local)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

