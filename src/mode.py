import json

from .func import *
from .push import *
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
def multi_user_report(jf):
    with open(jf, 'r') as fw:
        user_dict = json.load(fw)

    count = 1
    while count - 1 < len(user_dict):
        n = 1
        print_color('#############################', fg = Color.RED.value)
        msg.append('\r')
        build_msg("组名: " + user_dict[str(count)]['name'])
        build_msg('=============================')
        while n  < len(user_dict[str(count)]):
            u = user_dict[str(count)][str(n)]['un']
            p = user_dict[str(count)][str(n)]['pw']
            normal_report(u,p)
            n = n + 1
        else:
            msg.append('\r')
            build_msg ("[s]状态: 该组成员已完成提交操作")
            print_color('#############################', fg = Color.RED.value)
            msg.append('\r')
        count = count + 1
    else:
        msg.append('# ')
        build_msg ("[s]所有群组提交操作已完成!")

def normal_report(u,p):
    if  login_web(u,p) == 1:
        build_msg("[s]登陆成功!")
        build_msg('姓名: ' + get_value('lg_response').json()['data']['name'])
        build_msg('学号: ' + get_value('lg_response').json()['data']['teamNo'])
        get_last_record()
        build_msg('            ---               ')
        if is_record_today() == 1:
            build_msg('[s]今日已提交!')
            print('-----------------------------')
        else:
            add_record()
            if add_record() == 1:
                msg.append('\r')
                build_msg("[s]提交成功!")
                build_msg('体温: ' + get_value('lr_response').json()['data']['temperature'] + '℃')
                build_msg('提交时间: ' + get_time('now'))
            else:
                build_msg("[e]提交失败!")
    else:
        build_msg("[e]登陆失败! 请检查学号和密码")
        msg.append('\r')
        print('-----------------------------')