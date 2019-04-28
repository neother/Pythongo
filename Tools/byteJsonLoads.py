import os
import sys
import requests
import json
r = requests.get('https://api.github.com/users/neother')
data_byte = r.content
data_str = data_byte.decode() #bytes to json
data_json = json.loads(data_str)# string(contain json) to a python object
data = data_json['html_url']
keys = data_json.keys()
value = data_json.values()
print(value)

