import requests
import sys

payload = {"id": 1049510487}

r = requests.get('https://baidu.com')
a = r.text
print(a)


