import json
import requests

f = open("3.json")
data = json.load(f)
print(data)
print(type(data))
res = requests.request(**data)
print(res)
r = res.text
print(r)
f.close()