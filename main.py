# _*_ coding:utf-8 _*_
import requests
import json
import hashlib

# data
url = "http://hmgr.sec.lit.edu.cn/wms/healthyLogin"
username = '' #input your username
password = '' #input your password

# sha256 for password
def get_sha256(password: str) -> str:
    s = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return s

# login
headers = {
    'Content-Type': 'application/json',
}

data = {
    'cardNo': username,
    'password': get_sha256(password),
}

response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)

#print(response.json())
if response.json()['code'] == 200:
    print("登陆成功!")
    print('学号: ' + response.json()['data']['teamNo'])
else:
    print("登陆失败! 请检查学号和密码.")
