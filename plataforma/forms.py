# -*- coding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

from plataforma import constants
from plataforma.models import Nodo, Nodos, Objeto


class SignUpForm(UserCreationForm):

    quem_sou = forms.CharField(max_length=2000, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'quem_sou', 'password1', 'password2', )


class ImageValidator():

    def validar_imagem(self, imagem, mimetypes_aceitos, largura, altura):
        if imagem:
            if hasattr(imagem, "content_type") and imagem.content_type not in constants.MIMETYPES_IMAGENS_ACEITOS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            largura_imagem, altura_imagem = get_image_dimensions(imagem)
            if largura_imagem != largura:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (largura_imagem, largura))
            if altura_imagem != altura:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (altura_imagem, altura))
        return imagem


class NodoForm(forms.ModelForm, ImageValidator):

    quem_sou = forms.CharField(max_length=2000, required=False)

    def clean_imagem(self):
        imagem = self.cleaned_data.get("imagem")
        return self.validar_imagem(imagem, constants.MIMETYPES_IMAGENS_ACEITOS, constants.NODO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, constants.NODO_TAMANHO_IMAGEM_LISTAGEM_ALTURA)

    class Meta:
        model = Nodo
        fields = ('quem_sou', 'carteira', 'contato_facebook', 'contato_whatsapp', 'contato_zoom', 'imagem')


class NodosForm(forms.ModelForm, ImageValidator):

    class Meta:

        model = Nodos
        exclude = ["created", "updated", "excluido", "excluido_por", "excluido_em", "criado_por"]

    def clean_imagem(self):
        imagem = self.cleaned_data.get("imagem")
        return self.validar_imagem(imagem, constants.MIMETYPES_IMAGENS_ACEITOS, constants.NODOS_TAMANHO_IMAGEM_LISTAGEM_LARGURA, constants.NODOS_TAMANHO_IMAGEM_LISTAGEM_ALTURA)


class ObjetoForm(forms.ModelForm, ImageValidator):

    class Meta:

        model = Objeto
        exclude = ["created", "updated", "excluido", "excluido_por", "excluido_em", "criado_por", "nodos"]

    def clean_imagem(self):
        imagem = self.cleaned_data.get("imagem")
        return self.validar_imagem(imagem, constants.MIMETYPES_IMAGENS_ACEITOS, constants.OBJETO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, constants.OBJETO_TAMANHO_IMAGEM_LISTAGEM_ALTURA)
