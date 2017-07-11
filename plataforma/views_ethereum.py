# -*- coding: utf-8 -*-


from braces.views import JSONResponseMixin
from datetime import datetime
from django.conf import settings
from django.http import HttpResponseServerError
from django.views import View
import requests


class TotalEmitidoDetailView(View, JSONResponseMixin):

    def get(self, request, *args, **kwargs):
        r = requests.get("https://api.etherscan.io/api?module=stats&action=tokensupply&tokenname=%s&apikey=%s" % (settings.ETHERSCAN_TOKENNAME, settings.ETHERSCAN_APIKEY))
        data = r.json()
        if data["status"] == "1":
            context_dict = {
                u"total": int(data["result"]) / float(1000000000),
            }
            return self.render_json_response(context_dict)
        return HttpResponseServerError()


class UltimasTransacoesDetailView(View, JSONResponseMixin):

    def get(self, request, *args, **kwargs):
        r = requests.get("http://api.etherscan.io/api?module=account&action=txlist&address=%s&startblock=0&endblock=99999999&sort=asc&apikey=%s" % (kwargs["wallet"], settings.ETHERSCAN_APIKEY))
        data = r.json()
        if data["status"] == "1":
            context_dict = {
                u"transactions": [],
            }
            for t in data["results"]:
                context_dict["transactions"].append(
                    {
                        "date": datetime.fromtimestamp(t["timeStamp"]),
                        "value": int(t["value"]) / float(1000000000),
                        "to": t["to"],
                        "from": t["from"],
                        "in_or_out": "in" if t["to"] == kwargs["wallet"] else "out"
                    }
                )
            return self.render_json_response(context_dict)
        return HttpResponseServerError()
