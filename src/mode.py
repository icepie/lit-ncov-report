import json
from .func import *

json_dir = "config/user.json"

# loding 
def multi_user_report():
    with open(json_dir, 'r') as fw:
        user_dict = json.load(fw)

    count = 1
    while count - 1 < len(user_dict):
        n = 1
        print ("组名: " + user_dict[str(count)]['name'])
        print('-----------------------------')
        while n  < len(user_dict[str(count)]):
            u = user_dict[str(count)][str(n)]['ur']
            p = user_dict[str(count)][str(n)]['pw']
            normal_report(u,p)
            n = n + 1
        else:
            print ("状态: 该组成员已完成提交")
            print('-----------------------------')
        count = count + 1
    else:
        print ("所有群组已提交完成!")

def normal_report(u,p):
    if  login_web(u,p) == 1:
        get_last_record()
        print('-----------------------------')
        if is_record_today() == 1:
            print('今日已提交!')
        else:
            add_record()
