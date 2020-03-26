
#_*_ coding:utf-8 _*_
import requests
import json
import hashlib

#login
username = ""
password = 123456

#sha256 for password
def get_sha256(data) :
    s1 = hashlib.sha256()
    s1.update(json.dumps(data).encode())
    return  s1.hexdigest()

url="http://hmgr.sec.lit.edu.cn/wms/healthyLogin"

headers = {
 'Content-Type': 'application/json',
}

data = {
    'cardNo': username,
    'password': get_sha256(password),
}

response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
print(response.json())



