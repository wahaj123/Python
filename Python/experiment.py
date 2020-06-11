from html.parser import HTMLParser
import urllib.request
import html.parser
# Import HTML from a URL
url = urllib.request.urlopen(
    "https://www.mcdelivery.com.pk/pk/browse/menu.html")
html = url.read().decode()
url.close()


class MyParser(html.parser.HTMLParser):
    def __init__(self, html):
        self.matches = []
        self.match_count = 0
        super().__init__()

    # Defining what the method should output when called by HTMLParser.

    # def handle_starttag(self, tag, attrs):
    #     # Only parse the 'anchor' tag.
    #     if tag == "div":
    #         for name, link in attrs:
    #             if name == "class" and link.startswith("http"):
    #                 print(link)

    def handle_data(self, data):
        self.matches.append(data)
        self.match_count += 1

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "div":
            if attrs.get("product-cost"):
                self.handle_data()
            else:
                return


# p = Parse()
# p.feed(html)
#request_html = the_request_method(url, ...)


parser = MyParser()
parser.feed(html)

for item in parser.matches:
    print(item)
