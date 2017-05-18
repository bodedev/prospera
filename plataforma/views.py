# -*- coding: utf-8 -*-


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, FormView, ListView, RedirectView, TemplateView, UpdateView
from social_django.models import UserSocialAuth

from plataforma.models import Nodos, Objeto


@method_decorator(login_required, name='dispatch')
class LogoutView(RedirectView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("home"))


class LandingPageView(TemplateView):

    template_name = "pages/landing_page.html"


class CreateAccountView(TemplateView):

    template_name = "pages/create_account.html"


@method_decorator(login_required, name='dispatch')
class NoDetailView(UpdateView):

    fields = ["quem_sou"]
    template_name = "pages/no_detail.html"
    success_url = reverse_lazy("no_detail")

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, u'Os dados do seu perfil foram salvos.')
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(NoDetailView, self).get_context_data(**kwargs)
        context["github_login"] = None
        try:
            context["github_login"] = self.request.user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            pass

        context["twitter_login"] = None
        try:
            context["twitter_login"] = self.request.user.social_auth.get(provider='twitter')
        except UserSocialAuth.DoesNotExist:
            pass

        context["facebook_login"] = None
        try:
            context["facebook_login"] = self.request.user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            pass

        context["can_disconnect"] = (self.request.user.social_auth.count() > 1 or self.request.user.has_usable_password())
        return context

    def get_object(self, queryset=None):
        return self.request.user.nodo


@method_decorator(login_required, name='dispatch')
class UserChangePassword(FormView):

    template_name = "pages/password.html"

    def get_form_class(self):
        if self.request.user.has_usable_password():
            return PasswordChangeForm
        return AdminPasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UserChangePassword, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, u'Sua senha foi alterada!')
        return HttpResponseRedirect(reverse_lazy('no_detail'))


class NosView(ListView):

    model = Nodos
    template_name = "pages/nos.html"


class NosDetailView(DetailView):

    context_object_name = "nos"
    model = Nodos
    slug_url_kwarg = "nos"
    template_name = "pages/nos_detail.html"


class ObjectDetailView(DetailView):

    context_object_name = "objeto"
    model = Objeto
    slug_url_kwarg = "objeto"
    template_name = "pages/object_detail.html"
