from HTMLParser import HTMLParser
import sys
import urllib
from re import sub

# get html the data from url
class Crawler:
    def __init__(self, url):
        self.url = url

    def show_html(self):
        try:
            sock = urllib.urlopen(self.url)
            html_source = sock.read()
            sock.close()
        except:
            print "wrong url"
        try:
            parser = Parser()
            parser.feed(html_source)
            parser.close()
            print parser.text()

        except:
            print "parse error"


#parse data from html content
class Parser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []
        self.hide_output = False

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0 and not self.hide_output:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'br') and not self.hide_output:
            self.__text.append('\n')
        elif tag in ('script', 'style', 'head', 'noscript'):
            self.hide_output = True

    def handle_endtag(self, tag):
        if tag == 'p':
            self.__text.append('\n')
        elif tag in ('script', 'style', 'head', 'noscript'):
            self.hide_output = False

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()

url = sys.argv[1]
c = Crawler(url)
c.show_html()
