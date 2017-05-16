# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.contrib import admin
from plataforma.urls import urlpatterns as plataforma_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += plataforma_urls
