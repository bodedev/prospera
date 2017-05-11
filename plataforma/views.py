# -*- coding: utf-8 -*-


from django.views.generic import TemplateView


class LandingPageView(TemplateView):

    template_name = "pages/landing_page.html"


class LoginView(TemplateView):

    template_name = "pages/login.html"


class CreateAccountView(TemplateView):

    template_name = "pages/create_account.html"


class NosView(TemplateView):

    template_name = "pages/nos.html"


class NosDetailView(TemplateView):

    template_name = "pages/nos_detail.html"


class ObjectDetailView(TemplateView):

    template_name = "pages/object_detail.html"
