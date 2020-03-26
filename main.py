#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import requests
import json
import hashlib
import datetime
import time

# data
lg_url = 'http://hmgr.sec.lit.edu.cn/wms/healthyLogin'
username = 'B1907xxxx' #input your username
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
    time.sleep(1)
    quit()


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

print('-----------------------------')

# add a new record
ar_url = 'http://hmgr.sec.lit.edu.cn/wms/addHealthyRecord'

today = datetime.date.today()
now = datetime.datetime.now().replace(microsecond=0)

ar_data = {
    'userId': lg_response.json()['data']['teamId'], 
    'teamId': lg_response.json()['data']['userId'], 
    'currentProvince': lr_response.json()['data']['currentProvince'], 
    'currentCity': lr_response.json()['data']['currentCity'], 
    'currentDistrict': lr_response.json()['data']['currentDistrict'], 
    'currentAddress': lr_response.json()['data']['currentAddress'], 
    'isInTeamCity': lr_response.json()['data']['currentCity'], 
    'healthyStatus': lr_response.json()['data']['healthyStatus'], 
    'temperatureNormal': lr_response.json()['data']['temperatureNormal'], 
    'temperature': lr_response.json()['data']['temperature'], 
    'temperatureTwo': lr_response.json()['data']['temperatureTwo'], 
    'selfHealthy': lr_response.json()['data']['selfHealthy'], 
    'selfHealthyInfo': lr_response.json()['data']['selfHealthyInfo'], 
    'selfHealthyTime': lr_response.json()['data']['selfHealthyTime'], 
    'friendHealthy': lr_response.json()['data']['friendHealthy'], 
    'travelPatient': lr_response.json()['data']['travelPatient'], 
    'contactPatient': lr_response.json()['data']['contactPatient'], 
    'isolation': lr_response.json()['data']['isolation'], 
    'seekMedical': lr_response.json()['data']['seekMedical'], 
    'seekMedicalInfo': lr_response.json()['data']['seekMedicalInfo'], 
    'exceptionalCase': lr_response.json()['data']['exceptionalCase'], 
    'exceptionalCaseInfo': lr_response.json()['data']['exceptionalCaseInfo'], 
    'reportDate': str(today), 
    'currentStatus': lr_response.json()['data']['currentStatus'], 
    'villageIsCase': lr_response.json()['data']['villageIsCase'], 
    'caseAddress': lr_response.json()['data']['caseAddress'], 
    'peerIsCase': lr_response.json()['data']['peerIsCase'], 
    'peerAddress': lr_response.json()['data']['peerAddress'], 
    'goHuBeiCity': lr_response.json()['data']['goHuBeiCity'], 
    'goHuBeiTime': lr_response.json()['data']['goHuBeiTime'], 
    'contactProvince': lr_response.json()['data']['contactProvince'], 
    'contactCity': lr_response.json()['data']['contactCity'], 
    'contactDistrict': lr_response.json()['data']['contactDistrict'], 
    'contactAddress': lr_response.json()['data']['contactAddress'], 
    'contactTime': lr_response.json()['data']['contactTime'], 
    'diagnosisTime': lr_response.json()['data']['diagnosisTime'], 
    'treatmentHospitalAddress': lr_response.json()['data']['treatmentHospitalAddress'], 
    'cureTime': lr_response.json()['data']['cureTime'], 
    'isTrip': 0, 
    'tripList': [ ], 
    'peerList': [ ], 
    'mobile': lg_response.json()['data']['mobile']
}

ar_response = requests.post(url=ar_url,data=json.dumps(ar_data), headers=lr_headers)
#print(ar_response.json())
if ar_response.json()['code'] == 200:
    print("提交成功!")
    print('提交时间: ' + str(now))
else:
    print("提交失败!")