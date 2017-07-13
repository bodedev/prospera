# -*- coding: utf-8 -*-


from django.core.files.base import ContentFile
from requests import request, HTTPError


def save_profile(backend, user, response, *args, **kwargs):
    # salvando foto :)
    if backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        try:
            response = request('GET', url, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            user.nodo.imagem.save('{0}_social.jpg'.format(user.username), ContentFile(response.content))
            user.nodo.save()
