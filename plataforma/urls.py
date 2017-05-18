# -*- coding: utf-8 -*-


from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from plataforma.views import LandingPageView, LogoutView, NosCreateView, CreateAccountView, NoDetailView, NosView, NosDetailView, ObjectDetailView, UserChangePassword, ObjectCreateView


urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name="home"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^create-account/$', CreateAccountView.as_view(), name="create_account"),
    url(r'^no/$', NoDetailView.as_view(), name="no_detail"),
    url(r'^no/senha/$', UserChangePassword.as_view(), name="no_change_password"),
    url(r'^nos/$', NosView.as_view(), name="nos"),
    url(r'^nos/create/$', NosCreateView.as_view(), name="nos_create"),
    url(r'^nos/(?P<nos>[-\w]+)/detalhes/$', NosDetailView.as_view(), name="nos_detail"),
    url(r'^(?P<nos>[-\w]+)/objeto/create/$', ObjectCreateView.as_view(), name="object_create"),
    url(r'^(?P<nos>[-\w]+)/objeto/(?P<objeto>[-\w]+)/detalhes/$', ObjectDetailView.as_view(), name="object_detail"),
]
