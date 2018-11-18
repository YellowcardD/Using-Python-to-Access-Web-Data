import json
import urllib.request, urllib.parse

url = input('Enter- ')
print('Retrieving:', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

data = json.loads(data)
lst = data['comments']
print(len(lst))
print(lst)
num_sum = 0
for comment in lst:
    num_sum = num_sum + comment['count']
print(num_sum)
