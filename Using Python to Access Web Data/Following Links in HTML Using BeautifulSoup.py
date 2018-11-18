from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
cnt = input('Enter count')
pos = input('Enter position')
print('Enter count:' + cnt)
print('Enter position' + pos)
for i in range(int(cnt)):
    #url = 'http://py4e-data.dr-chuck.net/known_by_Zohair.html'
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    cnt = 1
    for tag in tags:
        if cnt == int(pos):
            url = re.findall('href="(.+)"', str(tag))[0]
            print("Retrieving:" + url)
        cnt = cnt + 1




