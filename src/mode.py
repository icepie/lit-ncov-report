import json
from .func import *
from enum import Enum

class Color(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

def print_color(text: str, fg: Color = Color.BLACK.value):
    print(f'\033[{fg}m{text}\033[0m')

# loding 
def multi_user_report(json_dir):
    with open(json_dir, 'r') as fw:
        user_dict = json.load(fw)

    count = 1
    while count - 1 < len(user_dict):
        n = 1
        print_color('#############################', fg = Color.RED.value)
        print ("组名: " + user_dict[str(count)]['name'])
        print('=============================')
        while n  < len(user_dict[str(count)]):
            u = user_dict[str(count)][str(n)]['un']
            p = user_dict[str(count)][str(n)]['pw']
            normal_report(u,p)
            n = n + 1
        else:
            print ("[s]状态: 该组成员已完成提交")
            print_color('#############################', fg = Color.RED.value)
        count = count + 1
    else:
        print ("[s]所有群组已提交完成!")

def normal_report(u,p):
    if  login_web(u,p) == 1:
        get_last_record()
        print('            ---               ')
        if is_record_today() == 1:
            print('[s]今日已提交!')
            print('-----------------------------')
        else:
            add_record()
    else:
        print('-----------------------------')