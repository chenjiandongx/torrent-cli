import requests
import re
from bs4 import BeautifulSoup


domain = "http://bt2.bt87.cc"
#
# url = "http://bt2.bt87.cc/index.php?r=files/index&kw="
# resp = requests.get(url).text
#
# url_pattern = re.compile(r'(/index.php\?r=files/view&infohash=\S+)"')
# urls = [domain + u for u in re.findall(url_pattern, resp)]
#
#
# resp = requests.get(url).text
# magnet_pattern = re.compile(r'(magnet:\?\S+)"')
# magnets = re.findall(magnet_pattern, resp)

# r = requests.get("http://bt2.bt87.cc/index.php?r=files/view&infohash=4952a2260099b88c1e84e33664c5df58eb542b1b").text
# magnet = BeautifulSoup(r, 'lxml').find("h4", id="magnet").text[8:]
# magnet_name = BeautifulSoup(r, 'lxml').find("h3").text
# magnet_date, magnet_size = (str(BeautifulSoup(r, 'lxml').find("h4").text).split(maxsplit=1))
#
# torrent = (magnet, magnet_name, magnet_date, magnet_size)
# print(torrent)

# urls = []
url = domain + "/index.php?r=files%2Findex&kw={kw}"
resp = requests.get(url).text
bs = BeautifulSoup(resp, "lxml").find("ul", class_="row list-group").find_all("li")

urls = [domain + b.find("a")["href"] for b in bs]