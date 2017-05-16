# -*- coding: utf-8 -*-


from django.views.generic import DetailView, ListView, TemplateView

from plataforma.models import Nodos


class LandingPageView(TemplateView):

    template_name = "pages/landing_page.html"


class LoginView(TemplateView):

    template_name = "pages/login.html"


class CreateAccountView(TemplateView):

    template_name = "pages/create_account.html"


class NosView(ListView):

    model = Nodos
    template_name = "pages/nos.html"


class NosDetailView(DetailView):

    model = Nodos
    template_name = "pages/nos_detail.html"
    slug_url_kwarg = "nos"


class ObjectDetailView(TemplateView):

    template_name = "pages/object_detail.html"
