import urllib.request, urllib.parse
import json


def get_value(list_or_dict):
    if type(list_or_dict) is type([]):
        for item in list_or_dict:
            return get_value(item)

    if type(list_or_dict) is type({}):
        if 'place_id' in list_or_dict:
            return list_or_dict['place_id']
        else:
            for k, v in list_or_dict.items():
                if type(v) is type({}) or type(v) is type([]):
                    return get_value(v)

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
while True:
    address = input('Enter Location:')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving: ', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    js = json.loads(data)
    place_id = get_value(js)
    print(place_id)