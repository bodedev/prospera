# -*- coding: utf-8 -*-


from django.conf.urls import url
from plataforma.views import LandingPageView


urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name="landing_page"),
]
