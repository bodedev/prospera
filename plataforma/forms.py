# -*- coding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

from plataforma import constants
from plataforma.models import Nodos, Objeto


class SignUpForm(UserCreationForm):

    quem_sou = forms.CharField(max_length=500, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'quem_sou', 'password1', 'password2', )


class NodosForm(forms.ModelForm):

    class Meta:

        model = Nodos
        exclude = ["created", "updated", "excluido", "excluido_por", "excluido_em", "criado_por"]

    def clean_imagem_listagem(self):
        picture = self.cleaned_data.get("imagem_listagem")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in constants.MIMETYPES_IMAGENS_ACEITOS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != constants.NODOS_TAMANHO_IMAGEM_LISTAGEM_LARGURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, constants.NODOS_TAMANHO_IMAGEM_LISTAGEM_LARGURA))
            if h != constants.NODOS_TAMANHO_IMAGEM_LISTAGEM_ALTURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, constants.NODOS_TAMANHO_IMAGEM_LISTAGEM_ALTURA))
        return picture

    def clean_imagem_detalhes(self):
        picture = self.cleaned_data.get("imagem_detalhes")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in constants.MIMETYPES_IMAGENS_ACEITOS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != constants.NODOS_TAMANHO_IMAGEM_DETALHES_LARGURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, constants.NODOS_TAMANHO_IMAGEM_DETALHES_LARGURA))
            if h != constants.NODOS_TAMANHO_IMAGEM_DETALHES_ALTURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, constants.NODOS_TAMANHO_IMAGEM_DETALHES_ALTURA))
        return picture


class ObjetoForm(forms.ModelForm):

    class Meta:

        model = Objeto
        exclude = ["created", "updated", "excluido", "excluido_por", "excluido_em", "criado_por", "nodos"]

    def clean_imagem_listagem(self):
        picture = self.cleaned_data.get("imagem_listagem")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in constants.MIMETYPES_IMAGENS_ACEITOS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != constants.OBJETO_TAMANHO_IMAGEM_LISTAGEM_LARGURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, constants.OBJETO_TAMANHO_IMAGEM_LISTAGEM_LARGURA))
            if h != constants.OBJETO_TAMANHO_IMAGEM_LISTAGEM_ALTURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, constants.OBJETO_TAMANHO_IMAGEM_LISTAGEM_ALTURA))
        return picture

    def clean_imagem_detalhes(self):
        picture = self.cleaned_data.get("imagem_detalhes")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in constants.MIMETYPES_IMAGENS_ACEITOS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != constants.OBJETO_TAMANHO_IMAGEM_DETALHES_LARGURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, constants.OBJETO_TAMANHO_IMAGEM_DETALHES_LARGURA))
            if h != constants.OBJETO_TAMANHO_IMAGEM_DETALHES_ALTURA:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, constants.OBJETO_TAMANHO_IMAGEM_DETALHES_ALTURA))
        return picture
