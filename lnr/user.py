#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import json

from lnr import endpoints
from lnr import util


class litUesr:
    """lit uesr object"""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = util.get_sha256(password)

        # login the acconut
        self.info = self.__login()
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
                url=endpoints['lg'], data=json.dumps(data), headers=headers)
            res = response.json()['data']
        except:
            res = None
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
                url=endpoints['lr'], params=data, headers=headers)
            res = response.json()['data']
        except:
            res = None

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
                url=endpoints['gi'], params=data, headers=headers)
            res = response.json()['data']
        except:
            res = None
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
                url=endpoints['fp'], params=data, headers=headers)
            res = response.json()['data']
        except:
            res = None
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
                url=endpoints['tp'], params=data, headers=headers)
            res = response.json()['data']
        except:
            res = None
        return res
