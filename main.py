#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from src import func

# account
username = 'B1907XXXX'  # input your username
password = ''  # input your password

# run a normal report (using the lasttemperature)
def normal_report(u,p):
    func.login_web(u,p)
    func.get_last_record()
    print('-----------------------------')
    if func.is_record_today() == 1:
        print('今日已提交!')
        quit()
    else:
        func.add_record()

normal_report(username,password)