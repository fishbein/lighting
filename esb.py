from lxml import html
import requests
def today():
    page = requests.get("http://www.esbnyc.com/explore/tower-lights/calendar")
    tree = html.fromstring(page.content)
    print tree.xpath('//p[@class="lighting-desc"]/text()')[0]
    # check for h1#title, URL=http://www.esbnyc.com/tower-lighting-YYYY-MM-DD-000000
today()
