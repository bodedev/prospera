# -*- coding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

from plataforma.models import Nodos, Objeto


class SignUpForm(UserCreationForm):

    quem_sou = forms.CharField(max_length=500, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'quem_sou', 'password1', 'password2', )


class NodosForm(forms.ModelForm):

    VALID_IMAGE_FORMATS = ["image/jpeg", "image/png"]
    LIST_IMAGE_WIDTH = 300
    LIST_IMAGE_HEIGHT = 300
    DETAILS_IMAGE_WIDTH = 500
    DETAILS_IMAGE_HEIGHT = 300

    class Meta:

        model = Nodos
        exclude = ["created", "updated", "excluido", "excluido_por", "excluido_em"]

    def clean_imagem_listagem(self):
        picture = self.cleaned_data.get("imagem_listagem")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in self.VALID_IMAGE_FORMATS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != self.LIST_IMAGE_WIDTH:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, self.LIST_IMAGE_WIDTH))
            if h != self.LIST_IMAGE_HEIGHT:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, self.LIST_IMAGE_HEIGHT))
        return picture

    def clean_imagem_detalhes(self):
        picture = self.cleaned_data.get("imagem_detalhes")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in self.VALID_IMAGE_FORMATS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != self.DETAILS_IMAGE_WIDTH:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, self.DETAILS_IMAGE_WIDTH))
            if h != self.DETAILS_IMAGE_HEIGHT:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, self.DETAILS_IMAGE_HEIGHT))
        return picture


class ObjetoForm(forms.ModelForm):

    VALID_IMAGE_FORMATS = ["image/jpeg", "image/png"]
    LIST_IMAGE_WIDTH = 50
    LIST_IMAGE_HEIGHT = 50
    DETAILS_IMAGE_WIDTH = 800
    DETAILS_IMAGE_HEIGHT = 244

    class Meta:

        model = Objeto
        exclude = ["created", "updated", "excluido", "excluido_por", "excluido_em"]

    def clean_imagem_listagem(self):
        picture = self.cleaned_data.get("imagem_listagem")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in self.VALID_IMAGE_FORMATS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != self.LIST_IMAGE_WIDTH:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, self.LIST_IMAGE_WIDTH))
            if h != self.LIST_IMAGE_HEIGHT:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, self.LIST_IMAGE_HEIGHT))
        return picture

    def clean_imagem_detalhes(self):
        picture = self.cleaned_data.get("imagem_detalhes")
        if picture:
            if hasattr(picture, "content_type") and picture.content_type not in self.VALID_IMAGE_FORMATS:
                raise forms.ValidationError(u'O formato informado não é suportado.')
            w, h = get_image_dimensions(picture)
            if w != self.DETAILS_IMAGE_WIDTH:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de largura. Ela necessita ter %i pixels." % (w, self.DETAILS_IMAGE_WIDTH))
            if h != self.DETAILS_IMAGE_HEIGHT:
                raise forms.ValidationError("A imagem enviada tem %i pixel(s) de altura. Ela necessita ter %i pixels." % (w, self.DETAILS_IMAGE_HEIGHT))
        return picture
