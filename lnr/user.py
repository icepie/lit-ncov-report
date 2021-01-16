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
        self.info = self.__login()
        try:
            self.token = self.info['token']
            self.is_logined = True
        except:
            self.is_logined = False

    def __login(self):
        lg_headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }

        lg_data = {
            'cardNo': self.username,
            'password': self.password
        }

        # login func
        try:
            lg_response = requests.post(
                url=endpoints['lg'], data=json.dumps(lg_data), headers=lg_headers)
            res = lg_response.json()['data']
        except:
            res = None
        return res