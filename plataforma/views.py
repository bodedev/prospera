# -*- coding: utf-8 -*-


from braces.views import AjaxResponseMixin, JSONResponseMixin
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, TemplateView, UpdateView

from plataforma.constants import ETHER_DIVISOR
from plataforma.forms import ProsperaLoginForm, NodoForm, NodosForm, ObjetoForm, SignUpForm
from plataforma.models import Nodo, Nodos, Objeto, Saldo

import requests


class LandingPageView(TemplateView):

    template_name = "pages/landing_page.html"


class LandingLastOperationsByTokenView(TemplateView):

    template_name = "pages/partial_landing_history.html"

    def get_context_data(self, **kwargs):
        context = super(LandingLastOperationsByTokenView, self).get_context_data(**kwargs)
        context["transacoes"] = []
        try:
            r = requests.get("https://api.ethplorer.io/getTokenHistory/%s/?apiKey=freekey" % (settings.ETHERSCAN_CONTRACT_ADDRESS, ))
            if r.status_code == 200:
                data = r.json()
                for operation in data["operations"]:
                    context["transacoes"].append({
                        "date": datetime.fromtimestamp(float(operation["timestamp"])),
                        "value": int(operation["value"]) / float(ETHER_DIVISOR),
                        "from": operation["from"],
                        "to": operation["to"],
                    })
        except Exception, e:
            pass
        return context


class LandingBalanceByTokenView(ListView):

    model = Saldo
    ordering = ("-total", )
    template_name = "pages/partial_landing_balance.html"


@method_decorator(csrf_exempt, name='dispatch')
class LoginWithAjaxView(AjaxResponseMixin, JSONResponseMixin, LoginView):

    form_class = ProsperaLoginForm

    def post_ajax(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            login(self.request, form.get_user())
            return self.render_json_response({})
        else:
            return self.render_json_response(form.errors.as_json(), status=400)


@method_decorator(csrf_exempt, name='dispatch')
class NoCreateView(AjaxResponseMixin, JSONResponseMixin, FormView):

    form_class = SignUpForm
    template_name = "pages/no_create_form.html"

    def create_the_user(self, form):
        user = form.save()
        user.refresh_from_db()  # load the nodo instance created by the signal
        user.nodo.quem_sou = form.cleaned_data.get('quem_sou')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, u'Bem-vindo a Prospera!')
        return user

    def form_valid(self, form):
        user = self.create_the_user(form)
        return HttpResponseRedirect(reverse_lazy("no_detail_public", args=[user.id]))

    def post_ajax(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = self.create_the_user(form)
            return self.render_json_response({"next": reverse_lazy("no_detail_public", args=[user.id])})
        else:
            return self.render_json_response(form.errors.as_json(), status=400)


class NoDetailView(DetailView):

    fields = ["quem_sou"]
    template_name = "pages/no_detail.html"

    def get_object(self, queryset=None):
        if "pk" in self.kwargs:
            return get_object_or_404(Nodo, user__id=self.kwargs["pk"])
        return self.request.user.nodo


class NoDetailTransactionView(TemplateView):

    template_name = "pages/partial_no_transactions.html"

    def get_context_data(self, **kwargs):
        context = super(NoDetailTransactionView, self).get_context_data(**kwargs)
        context["transactions"] = []
        nodo = self.get_object()
        try:
            url = "https://api.ethplorer.io/getAddressHistory/%s?apiKey=freekey" % (nodo.carteira.lower())
            r = requests.get(url)
            data = r.json()
            for t in data["operations"]:
                context["transactions"].append(
                    {
                        "date": datetime.fromtimestamp(float(t["timestamp"])),
                        "value": int(t["value"]) / float(ETHER_DIVISOR),
                        "to": t["to"],
                        "from": t["from"],
                        "in_or_out": "in" if t["to"] == nodo.carteira.lower() else "out"
                    }
                )
        except:
            pass
        return context

    def get_object(self, queryset=None):
        try:
            nodo = Nodo.objects.get(user__id=self.kwargs["pk"])
            if nodo.carteira:
                return nodo
        except:
            pass
        return HttpResponseServerError


class NoDetailSummaryView(TemplateView):

    template_name = "pages/partial_no_status.html"

    def get_context_data(self, **kwargs):
        context = super(NoDetailSummaryView, self).get_context_data(**kwargs)
        nodo = self.get_object()
        context["nodo"] = nodo
        try:
            r = requests.get("https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=%s&address=%s&tag=latest&apikey=%s" % (settings.ETHERSCAN_CONTRACT_ADDRESS, nodo.carteira, settings.ETHERSCAN_APIKEY))
            if r.status_code == 200:
                data = r.json()
                if data["status"] == "1":
                    context["quanto_ganhou_com_a_prospera"] = float(data["result"]) / float(1000000000)
        except Exception, e:
            pass
        quanto_contribuiu_com_a_prospera = 0
        quanto_recebeu_como_nos = 0
        context["quanto_contribuiu_com_a_prospera"] = quanto_contribuiu_com_a_prospera
        context["quanto_recebeu_como_nos"] = quanto_recebeu_como_nos
        return context

    def get_object(self, queryset=None):
        try:
            nodo = Nodo.objects.get(user__id=self.kwargs["pk"])
            if nodo.carteira:
                return nodo
        except:
            pass
        return HttpResponseServerError


class TotalProsperEmitidosSummaryView(TemplateView):

    template_name = "pages/partial_landing_total.html"

    def get_context_data(self, **kwargs):
        context = super(TotalProsperEmitidosSummaryView, self).get_context_data(**kwargs)
        try:
            r = requests.get("https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=%s&apikey=%s" % (settings.ETHERSCAN_CONTRACT_ADDRESS, settings.ETHERSCAN_APIKEY))
            if r.status_code == 200:
                data = r.json()
                if data["status"] == "1":
                    context["total_emitido"] = int(data["result"]) / float(ETHER_DIVISOR)
        except:
            # Condição inicial
            context["total_emitido"] = 781.25
        return context


@method_decorator(login_required, name='dispatch')
class NoDeleteView(DeleteView):
    model = Nodo
    slug_url_kwarg = "no"
    template_name = "pages/no_delete_form.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user.is_active = False
        self.object.user.save()
        self.object.delete()

        logout(request)
        messages.success(request, u"Seu perfil foi excluído!")
        return HttpResponseRedirect(reverse_lazy("home"))

    def get_context_data(self, **kwargs):
        context = super(NoDeleteView, self).get_context_data(**kwargs)
        context["action"] = u'Excluir'
        context["comunidades_list"] = Nodos.objects.filter(criado_por=self.request.user)
        context["objetos_list"] = Objeto.objects.filter(criado_por=self.request.user)
        return context

    def get_object(self, queryset=None):
        self.object = super(NoDeleteView, self).get_object(queryset)
        if self.object.user != self.request.user:
            raise PermissionDenied
        return self.object


@method_decorator(login_required, name='dispatch')
class NoEditView(UpdateView):

    form_class = NodoForm
    model = Nodo
    slug_url_kwarg = "no"
    template_name = "pages/no_edit_form.html"

    def get_context_data(self, **kwargs):
        context = super(NoEditView, self).get_context_data(**kwargs)
        context["action"] = u'Salvar'
        return context

    def get_object(self, queryset=None):
        return self.request.user.nodo

    def get_success_url(self):
        return reverse_lazy("no_detail_public", args=[self.request.user.id])


class NoListView(ListView):

    model = Nodo
    template_name = "pages/no_list.html"

    def get_queryset(self):
        queryset = super(NoListView, self).get_queryset()
        return queryset.exclude(user__id__in=[4])


@method_decorator(login_required, name='dispatch')
class UserChangePassword(FormView):

    template_name = "pages/no_change_password.html"

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
        return HttpResponseRedirect(reverse_lazy('no_detail_public', args=[self.request.user.id]))


@method_decorator(login_required, name='dispatch')
class NosCreateView(CreateView):

    form_class = NodosForm
    model = Nodos
    template_name = "pages/nos_create_form.html"

    def form_valid(self, form):
        nos = form.save(commit=False)
        nos.criado_por = self.request.user
        nos.save()
        messages.success(self.request, u'Comunidade criada com sucesso!')
        return HttpResponseRedirect(reverse_lazy("nos_detail", args=[nos.slug]))


class NosListView(ListView):

    model = Nodos
    template_name = "pages/nos_list.html"


@method_decorator(login_required, name='dispatch')
class NosDeleteView(DeleteView):

    model = Nodos
    slug_url_kwarg = "nos"
    template_name = "pages/nos_delete_form.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, u"A Comunidade foi excluída!")
        return HttpResponseRedirect(reverse_lazy("nos_list"))

    def get_context_data(self, **kwargs):
        context = super(NosDeleteView, self).get_context_data(**kwargs)
        context["action"] = u'Excluir'
        context["objetos_list"] = Objeto.objects.filter(nodos=self.object)
        return context

    def get_object(self, queryset=None):
        self.object = super(NosDeleteView, self).get_object(queryset)
        if self.object.criado_por != self.request.user:
            raise PermissionDenied
        return self.object


class NosDetailView(DetailView):

    context_object_name = "nos"
    model = Nodos
    slug_url_kwarg = "nos"
    template_name = "pages/nos_detail.html"


@method_decorator(login_required, name='dispatch')
class NosEditView(UpdateView):

    form_class = NodosForm
    model = Nodos
    slug_url_kwarg = "nos"
    success_url = reverse_lazy("nos_list")
    template_name = "pages/nos_create_form.html"

    def get_context_data(self, **kwargs):
        context = super(NosEditView, self).get_context_data(**kwargs)
        context["action"] = u'Salvar'
        return context

    def get_object(self, queryset=None):
        self.object = super(NosEditView, self).get_object(queryset)
        if self.object.criado_por != self.request.user:
            raise PermissionDenied
        return self.object


@method_decorator(login_required, name='dispatch')
class ObjectCreateView(CreateView):

    form_class = ObjetoForm
    model = Objeto
    template_name = "pages/object_create_form.html"

    def form_valid(self, form):
        objeto = form.save(commit=False)
        objeto.nodos = Nodos.objects.get(slug=self.kwargs["nos"])
        objeto.criado_por = self.request.user
        objeto.save()
        messages.success(self.request, u'Objeto criado com sucesso!')
        return HttpResponseRedirect(reverse_lazy("object_detail", args=[objeto.nodos.slug, objeto.slug]))


@method_decorator(login_required, name='dispatch')
class ObjectDeleteView(DeleteView):

    model = Objeto
    slug_url_kwarg = "objeto"
    template_name = "pages/object_delete_form.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        comunidade_slug = self.object.nodos.slug
        self.object.delete()
        messages.success(request, u"O objeto foi excluído!")
        return HttpResponseRedirect(reverse_lazy("nos_detail", args=[comunidade_slug]))

    def get_context_data(self, **kwargs):
        context = super(ObjectDeleteView, self).get_context_data(**kwargs)
        context["action"] = u'Excluir'
        return context

    def get_object(self, queryset=None):
        self.object = super(ObjectDeleteView, self).get_object(queryset)
        if self.object.criado_por != self.request.user:
            raise PermissionDenied
        return self.object


class ObjectDetailView(DetailView):

    context_object_name = "objeto"
    model = Objeto
    slug_url_kwarg = "objeto"
    template_name = "pages/object_detail.html"


@method_decorator(login_required, name='dispatch')
class ObjectEditView(UpdateView):

    form_class = ObjetoForm
    model = Objeto
    slug_url_kwarg = "objeto"
    template_name = "pages/object_create_form.html"

    def get_context_data(self, **kwargs):
        context = super(ObjectEditView, self).get_context_data(**kwargs)
        context["action"] = u'Salvar'
        return context

    def get_object(self, queryset=None):
        self.object = super(ObjectEditView, self).get_object(queryset)
        if self.object.criado_por != self.request.user:
            raise PermissionDenied
        return self.object

    def get_success_url(self):
        return reverse_lazy("object_detail", kwargs={"nos": self.object.nodos.slug, "objeto": self.object.slug})


class ObjectListView(ListView):

    model = Objeto
    template_name = "pages/object_list.html"
