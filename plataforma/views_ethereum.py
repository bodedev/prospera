# -*- coding: utf-8 -*-


from braces.views import JSONResponseMixin
from django.conf import settings
from django.http import HttpResponseServerError
from django.views import View
import requests


class TotalEmitidoDetailView(View, JSONResponseMixin):

    template_name = "pages/landing_page.html"

    def get(self, request, *args, **kwargs):
        r = requests.get("https://api.etherscan.io/api?module=stats&action=tokensupply&tokenname=%s&apikey=%s" % (settings.EHTERSCAN_TOKENNAME, settings.ETHERSCAN_APIKEY))
        data = r.json()
        if data["status"] == "1":
            context_dict = {
                u"total": int(data["result"]) / float(1000000000),
            }
            return self.render_json_response(context_dict)
        return HttpResponseServerError()
