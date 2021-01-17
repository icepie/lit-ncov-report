#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import json

from litncov import endpoints
from litncov import util


class litUesr:
    """lit uesr object"""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = util.get_sha256(password)

        # login the acconut
        self.info = self.__login()['data']
        try:
            self.token = self.info['token']
            self.is_logined = True
        except:
            self.is_logined = False

    def __login(self):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }

        data = {
            'cardNo': self.username,
            'password': self.password
        }

        # login func
        try:
            response = requests.post(
                url=endpoints['login'], data=json.dumps(data), headers=headers)
        except:
            return None

        res = response.json()

        return res

    def get_last_record(self):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'token': self.token
        }

        data = {
            'teamId': self.info['teamId'],
            'userId': self.info['userId']
        }

        try:
            response = requests.get(
                url=endpoints['lastRecord'], params=data, headers=headers)
        except:
            return None

        res = response.json()

        return res

    def get_instructor(self):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token,
        }

        data = {
            'teamId': self.info['teamId'],
            'organizationName': self.info['organizationName'],
            'userOrganizationId': self.info['userOrganizationId']
        }
        try:
            response = requests.get(
                url=endpoints['getInstructor'], params=data, headers=headers)
        except:
            return None

        res = response.json()

        return res

    def get_familys(self):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token,
        }

        data = {
            'userId': self.info['userId'],
        }

        try:
            response = requests.get(
                url=endpoints['getFamilys'], params=data, headers=headers)
        except:
            return None

        res = response.json()

        return res

    def get_important_city(self):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token,
        }

        try:
            response = requests.get(
                url=endpoints['getImportantCity'], headers=headers)
        except:
            return None

        res = response.json()
        return res

    def get_trips(self):
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token,
        }

        data = {
            'userId': self.info['userId'],
            'teamId': self.info['teamId'],
        }

        try:
            response = requests.get(
                url=endpoints['getTrips'], params=data, headers=headers)
        except:
            return None

        res = response.json()

        return res

    def first_record(self, mode='last', times=1, temperature=36.6, temperatureTwo=36.3, temperatureThree=36.3):
        """
        the 'normal' will not record the temperatureTwo and temperatureThree values from last record
        and you can use the 'manual' for use your values, 'random' use random values
        """
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token,
        }

        # get the last record info
        last_record = self.get_last_record()

        data = {
            'mobile': self.info['mobile'],
            'nativePlaceProvince': self.info['nativePlaceProvince'],
            'nativePlaceCity': self.info['nativePlaceCity'],
            'nativePlaceDistrict': self.info['nativePlaceDistrict'],
            'nativePlaceAddress': self.info['nativePlaceAddress'],
            'localAddress': self.info['localAddress'],
            'currentProvince': last_record['currentProvince'],
            'currentCity': last_record['currentCity'],
            'currentDistrict': last_record['currentDistrict'],
            'currentLocation': util.current_location(last_record['currentDistrict'], last_record['currentCity']),
            'currentAddress': last_record['currentAddress'],
            'villageIsCase': last_record['villageIsCase'],
            'caseAddress': last_record['caseAddress'],
            'peerIsCase': last_record['peerIsCase'],
            'peerAddress': last_record['peerAddress'],
            'isInTeamCity': last_record['isInTeamCity'],
            'temperatureNormal': last_record['temperatureNormal'],
            'temperature': last_record['temperature'],
            'selfHealthy': last_record['selfHealthy'],
            'selfHealthyInfo': last_record['selfHealthyInfo'],
            'selfHealthyTime': last_record['selfHealthyTime'],
            'friendHealthy': last_record['friendHealthy'],
            'isolation': last_record['isolation'],
            'currentStatus': last_record['currentStatus'],
            'diagnosisTime': last_record['diagnosisTime'],
            'treatmentHospitalAddress': last_record['treatmentHospitalAddress'],
            'cureTime': last_record['cureTime'],
            'travelPatient': last_record['travelPatient'],
            'goHuBeiCity': last_record['goHuBeiCity'],
            'goHuBeiTime': last_record['goHuBeiTime'],
            'contactPatient': last_record['contactPatient'],
            'contactTime': last_record['contactTime'],
            'contactProvince': last_record['contactProvince'],
            'contactCity': last_record['contactCity'],
            'contactDistrict': last_record['contactDistrict'],
            'contactLocation': '',  # temporary emtpy
            'contactAddress': last_record['contactAddress'],
            'isAbroad':  last_record['isAbroad'],
            'abroadInfo': last_record['abroadInfo'],
            'seekMedical': last_record['seekMedical'],
            'seekMedicalInfo': last_record['seekMedicalInfo'],
            'exceptionalCase': last_record['exceptionalCase'],
            'exceptionalCaseInfo': last_record['exceptionalCaseInfo'],
            'isTrip':  last_record['isAbroad'],  # temporary use
            'userId': self.info['userId'],
            'teamId': self.info['teamId'],
            'healthyStatus': last_record['healthyStatus'],
            'temperatureTwo': '',
            'temperatureThree': '',
            'reportDate': util.get_time('today')
        }

        if mode == 'last':
            if times >= 2:
                data['temperatureTwo'] = last_record['temperatureTwo']
            if times == 3:
                data['temperatureThree'] = last_record['temperatureThree']
        elif mode == 'random':
            data['temperature'] = util.random_temp()
            if times >= 2:
                data['temperatureTwo'] = util.random_temp()
            if times == 3:
                data['temperatureThree'] = util.random_temp()
        elif mode == 'manual':
            data['temperature'] = temperature
            if times >= 2:
                data['temperatureTwo'] = temperatureTwo
            if times == 3:
                data['temperatureThree'] = temperatureThree
        else:
            return None

        try:
            response = requests.post(
                url=endpoints['firstRecord'], data=json.dumps(data), headers=headers)
            # res['data']['temperature'] = data['temperature']
            # res['data']['temperatureTwo'] = data['temperatureTwo']
            # res['data']['temperatureThree'] = data['temperatureThree']
            # {"success":true,"code":200,"msg":"请求成功","data":""}
        except:
            return None

        res = response.json()

        res['data'] = {'temperature': data['temperature']}
        if times >= 2:
            res['data']['temperatureTwo'] = data['temperatureTwo']
        if times == 3:
            res['data']['temperatureThree'] = data['temperatureThree']

        return res

    def second_record(self, mode='last', temperature=36.6):
        """
        mode: 'last', 'random' and 'manual'
        """
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token,
        }

        # get the last record info
        last_record = self.get_last_record()

        data = {
            'healthyRecordId': last_record['id'],
            'temperature': last_record['temperatureTwo'],
            'temperatureNormal': last_record['temperatureNormal']
        }

        if mode == 'last':
            pass
        elif mode == 'random':
            data['temperature'] = util.random_temp()
        elif mode == 'manual':
            data['temperature'] = temperature
        else:
            return None

        try:
            response = requests.put(
                url=endpoints['secondRecord'], params=data, headers=headers)
        except:
            return None

        res = response.json()
        res['data'] = {'temperature': data['temperature']}

        return res

    def third_record(self, mode='last', temperature=36.6):
        """
        mode: 'last', 'random' and 'manual'
        """
        headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'token': self.token,
        }

        # get the last record info
        last_record = self.get_last_record()

        data = {
            'healthyRecordId': last_record['id'],
            'temperature': last_record['temperatureThree'],
            'temperatureNormal': last_record['temperatureNormal']
        }

        if mode == 'last':
            pass
        elif mode == 'random':
            data['temperature'] = util.random_temp()
        elif mode == 'manual':
            data['temperature'] = temperature
        else:
            return None

        try:
            response = requests.put(
                url=endpoints['thirdRecord'], params=data, headers=headers)
        except:
            return None

        res = response.json()
        res['data'] = {'temperature': data['temperature']}

        return res
