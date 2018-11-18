from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_130356.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
num_sum = 0
for tag in tags:
    tag = tag.contents[0]
    num_sum = num_sum + int(tag)


print(num_sum)


