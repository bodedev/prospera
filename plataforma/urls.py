# -*- coding: utf-8 -*-


from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from plataforma.views import NoCreateView, LandingPageView, NoDetailView, UserChangePassword
from plataforma.views import NosCreateView, NosDetailView, NosEditView, NosListView
from plataforma.views import ObjectCreateView, ObjectDetailView, ObjectEditView


urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name="home"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    url(r'^oauth/', include('social_django.urls', namespace="social")),
    url(r'^no/$', NoDetailView.as_view(), name="no_detail"),
    url(r'^no/alterar-senha/$', UserChangePassword.as_view(), name="no_change_password"),
    url(r'^no/novo/$', NoCreateView.as_view(), name="no_create"),
    url(r'^nos/$', NosListView.as_view(), name="nos_list"),
    url(r'^nos/novo/$', NosCreateView.as_view(), name="nos_create"),
    url(r'^nos/(?P<nos>[-\w]+)/detalhes/$', NosDetailView.as_view(), name="nos_detail"),
    url(r'^nos/(?P<nos>[-\w]+)/editar/$', NosEditView.as_view(), name="nos_update"),
    url(r'^nos/(?P<nos>[-\w]+)/objeto/novo/$', ObjectCreateView.as_view(), name="object_create"),
    url(r'^nos/(?P<nos>[-\w]+)/objeto/(?P<objeto>[-\w]+)/detalhes/$', ObjectDetailView.as_view(), name="object_detail"),
    url(r'^nos/(?P<nos>[-\w]+)/objeto/(?P<objeto>[-\w]+)/editar/$', ObjectEditView.as_view(), name="object_update"),
]
