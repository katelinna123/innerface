import requests
import json

# json.loads（）json字符串-》字典
# json.dumps（）字典-》json字符串
# json.load()json文件-》字典
# json.dump()-》字典-》json文件
req = {
    "method":"post",
    "url":"http://115.28.108.130:8080/gasStation/process",
    "json":'{"dataSourceId":"bHRz","methodId":"00A","CardInfo":{"cardNumber": "24545456"}}'
}
f = open('1.json', 'w')
json.dump(req, f)
f.close()
res = requests.request(**req)
print(res)

