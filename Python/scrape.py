# Used to make requests
import urllib.request
import urllib.parse
import re
from html.parser import HTMLParser
import os

base_path = "/home/wahaj/Documents/Python/"
respData = urllib.request.urlopen(
    'https://www.mcdelivery.com.pk/pk/browse/menu.html')

resp = respData.read()

link = re.findall(r'<ul class="secondary-menu">(.*?)</ul>', str(resp))
# URLS
Urls = re.findall("href=[\"\'](.*?)[\"\']", str(link))
# menu
# print(Urls)
Url1 = [re.sub(r'amp;', '', item) for item in Urls]
deals = re.findall(r'<span>(.*?)</span>', str(link))
price = re.findall(r'<span class="starting-price">(.*?)</span>', str(resp))
Title = re.findall(r'<h5 class="product.title">(.*?)</h5>', str(resp))

for i in Url1:
    for t in deals:
        # print(deals)
        y = urllib.request.urlopen(
            'https://www.mcdelivery.com.pk/pk/browse/menu.html{}'.format(i))
        respdata = y.read()
        price = re.findall(
            r'<span class="starting-price">(.*?)</span>', str(respdata))
        Title = re.findall(
            r'<h5 class="product.title">(.*?)</h5>', str(respdata))
        output = '\n'.join(
            [f'Title : {Title}\nPrice : {price}\n' for Title, price in zip(Title, price)])
        filename = open("%s.txt" % t, "w").write(output)
        # print(filename)
