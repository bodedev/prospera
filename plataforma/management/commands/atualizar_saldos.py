# -*- coding: utf-8 -*-


from django.conf import settings
from django.core.management.base import BaseCommand
from plataforma.constants import ETHER_DIVISOR
from plataforma.models import Saldo
import requests


def buscar_saldo(carteira):
    try:
        r = requests.get("https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=%s&address=%s&tag=latest&apikey=%s" % (settings.ETHERSCAN_CONTRACT_ADDRESS, carteira, settings.ETHERSCAN_APIKEY))
        if r.status_code == 200:
            data = r.json()
            if data["status"] == "1":
                saldo = float(data["result"]) / float(ETHER_DIVISOR)
                _, created = Saldo.objects.update_or_create(carteira=carteira, defaults={"total": saldo})
                print "%s: %0.6f (%s)" % (carteira, saldo, str(created))
                return True
        return False
    except Exception, e:
        print "Nao consegui pegar o saldo da carteira %s" % carteira
        return None


class Command(BaseCommand):

    help = u"Atualiza o saldo de todas as carteiras de um contrato."

    def handle(self, *args, **options):
        url = "https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=%s&toBlock=latest&address=%s&apikey=%s" % (settings.ETHERSCAN_START_BLOCK_NUMBER, settings.ETHERSCAN_CONTRACT_ADDRESS, settings.ETHERSCAN_APIKEY)
        r = requests.get(url)
        data = r.json()
        saldos_atualizados = []
        for transacion in data["result"]:
            carteira_from = transacion["topics"][1].replace("0x000000000000000000000000", "0x")
            if carteira_from not in saldos_atualizados:
                if buscar_saldo(carteira_from):
                    saldos_atualizados.append(carteira_from)
            if len(transacion["topics"]) >= 3:
                carteira_to = transacion["topics"][2].replace("0x000000000000000000000000", "0x")
                if carteira_to not in saldos_atualizados:
                    if buscar_saldo(carteira_to):
                        saldos_atualizados.append(carteira_to)
        print "Fim de processo!"
