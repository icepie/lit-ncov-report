# _*_ coding:utf-8 _*_
import requests
import json
import hashlib

# data
url = "http://hmgr.sec.lit.edu.cn/wms/healthyLogin"
username = "" #input your username
password = 123456

# sha256 for password
def get_sha256(data):
    s1 = hashlib.sha256()
    s1.update(json.dumps(data).encode())
    return s1.hexdigest()

# login
headers = {
    'Content-Type': 'application/json',
}

data = {
    'cardNo': username,
    'password': get_sha256(password),
}

response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)

# print(response.json())
if not 'True' in response.json():
    print("登陆成功!")
    print('学号: ' + response.json()['data']['teamNo'])
else:
    print("登陆失败! 请检查学号和密码.")
