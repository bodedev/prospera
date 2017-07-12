# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand
from django.conf import settings
from plataforma.models import Saldo
import requests


class Command(BaseCommand):

    help = u"Atualiza o saldo de todas as carteiras de um contrato."

    def handle(self, *args, **options):
        url = "https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=%s&toBlock=latest&address=%s&topic1=0x000000000000000000000000455f6c073f3898e53d9003b1d665d39d4b0d8cf8&apikey=%s" % (settings.ETHERSCAN_START_BLOCK_NUMBER, settings.ETHERSCAN_CONTRACT_ADDRESS, settings.ETHERSCAN_APIKEY)
        r = requests.get(url)
        data = r.json()
        for transacion in data["result"]:
            carteira = transacion["topics"][2].replace("0x000000000000000000000000", "0x")
            try:
                r = requests.get("https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=%s&address=%s&tag=latest&apikey=%s" % (settings.ETHERSCAN_CONTRACT_ADDRESS, carteira, settings.ETHERSCAN_APIKEY))
                if r.status_code == 200:
                    data = r.json()
                    if data["status"] == "1":
                        saldo = float(data["result"]) / float(1000000000)
                        _, created = Saldo.objects.update_or_create(carteira=carteira, defaults={"total": saldo})
                        print "%s: %0.6f (%s)" % (carteira, saldo, str(created))
            except Exception, e:
                print "Nao consegui pegar o saldo da carteira %s" % carteira
        print "Fim de processo!"
