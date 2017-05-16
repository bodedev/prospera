# -*- coding: utf-8 -*-


from django.conf.urls import url
from plataforma.views import LandingPageView, LoginView, CreateAccountView, NosView, NosDetailView, ObjectDetailView


urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name="landing_page"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^create-account/$', CreateAccountView.as_view(), name="create_account"),
    url(r'^nos/$', NosView.as_view(), name="nos"),
    url(r'^nos/(?P<nos>[-\w]+)/detalhes/$', NosDetailView.as_view(), name="nos_detail"),
    url(r'^object/detalhes/$', ObjectDetailView.as_view(), name="object_detail"),
]
