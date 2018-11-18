import urllib.request, urllib.parse
import xml.etree.ElementTree as ET

#serviceurl = 'http://py4e-data.dr-chuck.net/comments_130358.xml'

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
# print(type(data))
#print(data.decode())
tree = ET.fromstring(data)

# results = tree.findall('.//count')
# num_sum = 0
# for num in results:
#     print(num.text)
#     num_sum = num_sum + int(num.text)
#
# print(num_sum)

results = tree.findall('comments/comment/count')
num_sum = 0
for num in results:
    num_sum = num_sum + int(num.text)
print(num_sum)