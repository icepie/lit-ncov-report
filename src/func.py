import requests
import json
import hashlib
import datetime
import time

# set url
url = {
    'lg': 'http://hmgr.sec.lit.edu.cn/wms/healthyLogin',
    'lr': 'http://hmgr.sec.lit.edu.cn/wms/lastHealthyRecord',
    'ar': 'http://hmgr.sec.lit.edu.cn/wms/addHealthyRecord',
}

# set time
def get_time(t):
    if t == 'now':
        return str(datetime.datetime.now().replace(microsecond=0))
    elif t == 'today':
        return str(datetime.date.today())
    else:
        return None
           
# global
_global_dict = None

def _init():
    global _global_dict
    _global_dict = {}

def set_value(key,value):
    """ set global variable """
    _global_dict[key] = value


def get_value(key,defValue=None):
    """ to obtain a global variable, if does not exist, it returns the default value """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue

# sha256 for password
def get_sha256(password: str) -> str:
    s = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return s

# login web
def login_web(username, password):
    lg_headers = {
        'Connection': 'application/json',
        'Content-Type': 'application/json',
    }

    lg_data = {
        'cardNo': username,
        'password': get_sha256(password),
    }

    set_value('lg_response',requests.post(url=url['lg'], data=json.dumps(lg_data), headers=lg_headers, verify=False))

    #print(get_value('lg_response').json())

    if get_value('lg_response').json()['code'] == 200:
        return(1)
    else:
        return(0)
        
# get the last record
def get_last_record():

    lr_headers = {
        'Connection': 'application/json',
        'Content-Type': 'application/json',
        'token': get_value('lg_response').json()['data']['token']
    }

    set_value('ar_headers',lr_headers)

    lr_data = {
        'teamId': get_value('lg_response').json()['data']['teamId'],
        'userId': get_value('lg_response').json()['data']['userId'],
    }

    set_value('lr_response',requests.get(url=url['lr'], params=lr_data, headers=lr_headers))

    #print(get_value('lr_response').json())


def is_record_today():
    if str(get_value('lr_response').json()['data']['createTime'])[0:10] == str(get_time('today')):
        return(1)
    else:
        return(0)

def add_record():
    ar_data = {
        'userId': get_value('lg_response').json()['data']['teamId'], 
        'teamId': get_value('lg_response').json()['data']['userId'], 
        'currentProvince': get_value('lr_response').json()['data']['currentProvince'], 
        'currentCity': get_value('lr_response').json()['data']['currentCity'], 
        'currentDistrict': get_value('lr_response').json()['data']['currentDistrict'], 
        'currentAddress': get_value('lr_response').json()['data']['currentAddress'], 
        'isInTeamCity': get_value('lr_response').json()['data']['currentCity'], 
        'healthyStatus': get_value('lr_response').json()['data']['healthyStatus'], 
        'temperatureNormal': get_value('lr_response').json()['data']['temperatureNormal'], 
        'temperature': get_value('lr_response').json()['data']['temperature'], 
        'temperatureTwo': get_value('lr_response').json()['data']['temperatureTwo'], 
        'selfHealthy': get_value('lr_response').json()['data']['selfHealthy'], 
        'selfHealthyInfo': get_value('lr_response').json()['data']['selfHealthyInfo'], 
        'selfHealthyTime': get_value('lr_response').json()['data']['selfHealthyTime'], 
        'friendHealthy': get_value('lr_response').json()['data']['friendHealthy'], 
        'travelPatient': get_value('lr_response').json()['data']['travelPatient'], 
        'contactPatient': get_value('lr_response').json()['data']['contactPatient'], 
        'isolation': get_value('lr_response').json()['data']['isolation'], 
        'seekMedical': get_value('lr_response').json()['data']['seekMedical'], 
        'seekMedicalInfo': get_value('lr_response').json()['data']['seekMedicalInfo'], 
        'exceptionalCase': get_value('lr_response').json()['data']['exceptionalCase'], 
        'exceptionalCaseInfo': get_value('lr_response').json()['data']['exceptionalCaseInfo'], 
        'reportDate': get_time('today'), 
        'currentStatus': get_value('lr_response').json()['data']['currentStatus'], 
        'villageIsCase': get_value('lr_response').json()['data']['villageIsCase'], 
        'caseAddress': get_value('lr_response').json()['data']['caseAddress'], 
        'peerIsCase': get_value('lr_response').json()['data']['peerIsCase'], 
        'peerAddress': get_value('lr_response').json()['data']['peerAddress'], 
        'goHuBeiCity': get_value('lr_response').json()['data']['goHuBeiCity'], 
        'goHuBeiTime': get_value('lr_response').json()['data']['goHuBeiTime'], 
        'contactProvince': get_value('lr_response').json()['data']['contactProvince'], 
        'contactCity': get_value('lr_response').json()['data']['contactCity'], 
        'contactDistrict': get_value('lr_response').json()['data']['contactDistrict'], 
        'contactAddress': get_value('lr_response').json()['data']['contactAddress'], 
        'contactTime': get_value('lr_response').json()['data']['contactTime'], 
        'diagnosisTime': get_value('lr_response').json()['data']['diagnosisTime'], 
        'treatmentHospitalAddress': get_value('lr_response').json()['data']['treatmentHospitalAddress'], 
        'cureTime': get_value('lr_response').json()['data']['cureTime'], 
        'isTrip': 0, 
        'tripList': [ ], 
        'peerList': [ ], 
        'mobile': get_value('lg_response').json()['data']['mobile']
    }

    set_value('ar_response',requests.post(url=url['ar'],data=json.dumps(ar_data), headers= get_value('ar_headers')))

    #print(get_value('ar_response').json())

    if get_value('ar_response').json()['code'] == 200:
        return(1)
    else:
        return(0)

# initialize
_init()