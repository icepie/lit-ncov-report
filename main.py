#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import requests
import json
import hashlib

# data
lg_url = 'http://hmgr.sec.lit.edu.cn/wms/healthyLogin'
username = '' #input your username
password = '' #input your password

# sha256 for password
def get_sha256(password: str) -> str:
    s = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return s

# login
lg_headers = {
    'Connection': 'application/json',
    'Content-Type': 'application/json',
}

lg_data = {
    'cardNo': username,
    'password': get_sha256(password),
}

lg_response = requests.post(url=lg_url, data=json.dumps(lg_data), headers=lg_headers, verify=False)

#print(lg_response.json())
if lg_response.json()['code'] == 200:
    print("登陆成功!")
    print('学号: ' + lg_response.json()['data']['teamNo'])
else:
    print("登陆失败! 请检查学号和密码.")


# get the last record
lr_url = 'http://hmgr.sec.lit.edu.cn/wms/lastHealthyRecord'

lr_headers = {
    'Connection': 'application/json',
    'Content-Type': 'application/json',
    'token': lg_response.json()['data']['token']
}

lr_data = {
    'teamId': lg_response.json()['data']['teamId'],
    'userId': lg_response.json()['data']['userId'],
}

lr_response = requests.get(url=lr_url, params=lr_data, headers=lr_headers)
#print(lr_response.json())
print('上次提交: ' + lr_response.json()['data']['createTime'])

