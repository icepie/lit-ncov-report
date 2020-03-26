
#_*_ coding:utf-8 _*_
import requests
import json
import hashlib

#login

username = ""
password = 123456

#md5
def get_md5(password):
    m = hashlib.md5()
    m.update(password)
    mpwd = m.hexdigest()
    return mpwd

print(get_md5(b'password'))

url="http://hmgr.sec.lit.edu.cn/wms/healthyLogin"

headers = {
 'Content-Type': 'application/json',
}

data = {
    'cardNo': username,
    'password': get_md5(b'password'),
}

response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
print(response.json())



