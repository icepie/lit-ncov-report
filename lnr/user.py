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
        self.password = password
        self.info = self.__login()
        #self.token = self.info()['token']
        print(self.info)

    def __login(self):
        lg_headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }

        lg_data = {
            'cardNo': self.username,
            'password': util.get_sha256(self.password)
        }

        # login func
        try:
            lg_response = requests.post(
                url=endpoints['lg'], data=json.dumps(lg_data), headers=lg_headers)
            if lg_response.text.json()['success'] == 'true':
                res = lg_response.text.json()['data']
            else:
                res = None
        except:
            res = None
        return res

