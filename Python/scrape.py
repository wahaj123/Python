# -*- coding: utf-8 -*-
# Used to make requests
import urllib.request
import urllib.parse
import re
from html.parser import HTMLParser


# # base_path = "/home/wahaj/Documents/Python/"
respData = urllib.request.urlopen(
    'https://www.mcdelivery.com.pk/pk/browse/menu.html')

resp = respData.read()
link = re.findall(r'<ul class="secondary-menu">(.*?)</ul>', str(resp))
# URLS
Urls = re.findall("href=[\"\'](.*?)[\"\']", str(link))
# remove amp from the urls
Url1 = [re.sub(r'amp;', '', item) for item in Urls]
# menu
deals = re.findall(r'<span>(.*?)</span>', str(link))
deal1 = [re.sub(r'x\S\d', ' ', s).replace('\\', '').strip() for s in deals]
print(deal1)
s = -1
# iterating over url1
for i in Url1:
    # iterating over deals
    s += 1
    # concatenation of base url with the url fetched from the tags through regex
    y = urllib.request.urlopen(
        'https://www.mcdelivery.com.pk/pk/browse/menu.html{}'.format(i))
    respdata = y.read()
    # find price
    price = re.findall(
        r'<span class="starting-price">(.*?)</span>', str(respdata))
    Title = re.findall(
        r'<h5 class="product.title">(.*?)</h5>', str(respdata))
    # Making file with the name of the data store in deals and storing the output of price and title in it
    output = '\n'.join([f'{i+1}.Title : {Title}\n  Price : {price}\n' for i,
                        Title, price in zip(range(len(Title)), Title, price)])
    # output = '\n'.join(
    #     [f'Title : {Title}\nPrice : {price}\n' for Title, price in zip(Title, price)])
    filename = open("%s.txt" % deal1[s], "a").write(output)
    # print(filename)
