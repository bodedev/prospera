# -*- coding: utf-8 -*-


from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from plataforma.views import NoCreateView, NoEditView, LandingPageView, NoDetailView, UserChangePassword, NoDetailSummaryView, NoDetailTransactionView
from plataforma.views import NosCreateView, NosDetailView, NosEditView, NosListView
from plataforma.views import ObjectCreateView, ObjectDeleteView, ObjectDetailView, ObjectEditView, ObjectListView
from plataforma.views import LoginWithAjaxView
from plataforma.views import TotalProsperEmitidosSummaryView, LandingLastOperationsByTokenView, LandingBalanceByTokenView


urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name="home"),
    url(r'^historico/$', LandingLastOperationsByTokenView.as_view(), name="home_historico"),
    url(r'^saldos/$', LandingBalanceByTokenView.as_view(), name="home_saldos"),
    url(r'^login/$', LoginWithAjaxView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    url(r'^prosper/total/$', TotalProsperEmitidosSummaryView.as_view(), name="prosper_total"),
    url(r'^oauth/', include('social_django.urls', namespace="social")),
    url(r'^no/(?P<pk>\d+)/detalhes/$', NoDetailView.as_view(), name="no_detail_public"),
    url(r'^no/(?P<pk>\d+)/detalhes/resumo/$', NoDetailSummaryView.as_view(), name="no_detail_public_summary"),
    url(r'^no/(?P<pk>\d+)/detalhes/transacoes/$', NoDetailTransactionView.as_view(), name="no_detail_public_transactions"),
    url(r'^no/alterar-senha/$', UserChangePassword.as_view(), name="no_change_password"),
    url(r'^no/editar/$', NoEditView.as_view(), name="no_update"),
    url(r'^no/novo/$', NoCreateView.as_view(), name="no_create"),
    url(r'^comunidades/$', NosListView.as_view(), name="nos_list"),
    url(r'^comunidades/nova/$', NosCreateView.as_view(), name="nos_create"),
    url(r'^comunidades/(?P<nos>[-\w]+)/detalhes/$', NosDetailView.as_view(), name="nos_detail"),
    url(r'^comunidades/(?P<nos>[-\w]+)/editar/$', NosEditView.as_view(), name="nos_update"),
    url(r'^comunidades/(?P<nos>[-\w]+)/objeto/novo/$', ObjectCreateView.as_view(), name="object_create"),
    url(r'^comunidades/(?P<nos>[-\w]+)/objeto/(?P<objeto>[-\w]+)/detalhes/$', ObjectDetailView.as_view(), name="object_detail"),
    url(r'^comunidades/(?P<nos>[-\w]+)/objeto/(?P<objeto>[-\w]+)/editar/$', ObjectEditView.as_view(), name="object_update"),
    url(r'^comunidades/(?P<nos>[-\w]+)/objeto/(?P<objeto>[-\w]+)/excluir/$', ObjectDeleteView.as_view(), name="object_delete"),
    url(r'^objetos/$', ObjectListView.as_view(), name="object_list"),
]
