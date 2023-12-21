import urllib.request, urllib.parse, urllib.error
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xml = input('Enter XML: ')
html = urllib.request.urlopen(xml, context=ctx)
data = html.read().decode()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

sum = 0
for item in lst:
    count = int(item.find('count').text)
    sum += count

print(sum)
