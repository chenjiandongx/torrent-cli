import requests
from bs4 import BeautifulSoup


def spider(kw=None, page=1, sort_by=None):

    domain = "http://bt2.bt87.cc"
    url = domain + "/index.php?r=files%2Findex&kw={kw}".format(kw=kw)
    resp = requests.get(url).text
    bs = BeautifulSoup(resp, "lxml").find("ul",class_="row list-group").find_all("li")
    urls = [domain + b.find("a")["href"] for b in bs]

    magnets = []
    for url in urls:
        resp = requests.get(url).text
        magnet = BeautifulSoup(resp, 'lxml').find("h4", id="magnet").text[8:]
        magnet_name = BeautifulSoup(resp, 'lxml').find("h3").text
        magnet_date, magnet_size = (
            str(BeautifulSoup(resp, 'lxml').find("h4").text).split(maxsplit=1))

        torrent = (magnet, magnet_name, magnet_date, magnet_size)
        magnets.append(torrent)

    from pprint import pprint
    pprint(magnets)
