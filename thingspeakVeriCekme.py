import urllib
from bs4 import BeautifulSoup
import requests


def bilgileriDondur():
    dataFromWebsite = requests.get("https://api.thingspeak.com/channels/1259624/feeds.json?results=2")
    sicaklikBilgisi = dataFromWebsite.json()['feeds'][0]['field1']
    sonGuncellemeTarihi = dataFromWebsite.json()['feeds'][0]['created_at']
    tarihVeSaat = str(sonGuncellemeTarihi).split("T")
    saatDakikaSaniye = tarihVeSaat[1][:-1].split(":")
    saatDakikaSaniye[0] = str(int(saatDakikaSaniye[0]) + 3)
    saatDakikaSaniye = ":".join(saatDakikaSaniye)
    cikti = str(tarihVeSaat[:-1][0]) + " tarihinde " + str(saatDakikaSaniye) + " zamanında ölçülen sıcaklık değeri " + str(sicaklikBilgisi) + " derecedir."
    return cikti