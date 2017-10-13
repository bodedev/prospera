# -*- coding: utf-8 -*-


from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from plataforma.urls import urlpatterns as plataforma_urls
from bode_error_pages.views import Error403View, Error404View, Error500View

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += plataforma_urls

# server media files (only local)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Bode Error Pages
handler403 = Error403View.as_view()
handler404 = Error404View.as_view()
handler500 = Error500View.as_view()

