import json

from .func import *
from .push import *
from enum import Enum
import prettytable as pt

# set prettytable
tb = pt.PrettyTable()
#tb.set_style(pt.MSWORD_FRIENDLY)
#tb.border = False
tb.field_names = ["编号", "学号", "姓名","上次","本次"]
tb.add_row(['----','----','----','----','----'])

# loding 
def multi_user_report(jf):
    with open(jf, 'r') as fw:
        user_dict = json.load(fw)

    ct1 = 1
    while ct1 - 1 < len(user_dict):
        n = 1
        build_msg('###############################')
        msg.append('\r')
        build_msg("组名: " + user_dict[str(ct1)]['name'])
        build_msg('===============================')
        while n  < len(user_dict[str(ct1)]):
            u = user_dict[str(ct1)][str(n)]['un']
            p = user_dict[str(ct1)][str(n)]['pw']
            # table mode set
            if normal_report(u,p) == 1:
                if is_record_today() == 1: 
                    tb.add_row([user_dict[str(ct1)]['name']+ ':' + str(n),user_dict[str(ct1)][str(n)]['un'],str(get_value('lg_response').json()['data']['name']),
                    str(get_value('lr_response').json()['data']['createTime']), '今日已提交'])
                else:
                    tb.add_row([user_dict[str(ct1)]['name']+ ':' + str(n),user_dict[str(ct1)][str(n)]['un'],str(get_value('lg_response').json()['data']['name']),
                    str(get_value('lr_response').json()['data']['createTime']), '成功! 体温:' + str(get_value('lr_response').json()['data']['temperature']) + '℃' ])                    
            else:
                tb.add_row([user_dict[str(ct1)]['name']+ ':' + str(n),user_dict[str(ct1)][str(n)]['un'], '登陆失败', '无法解析', '未知操作'])
            n += 1
        else:
            msg.append('\r')
            build_msg ("[f]状态: 该组成员已完成提交操作")
            build_msg('###############################')
            msg.append('\r')
        ct1 += 1
    else:
        msg.append('# ')
        build_msg ("[f]所有群组提交操作已完成!")
    if get_value('table') == 1:
        print(tb)
        print('[f]已生成结果表格')

def normal_report(u,p):
    if  login_web(u,p) == 1: 
        build_msg("[s]登陆成功!")
        build_msg('- 姓名: ' + get_value('lg_response').json()['data']['name'])
        build_msg('- 学号: ' + get_value('lg_response').json()['data']['teamNo'])
        get_last_record()
        build_msg('- 上次提交: ' + get_value('lr_response').json()['data']['createTime'])
        if is_record_today() == 1:
            build_msg('[s]今日已提交!')
            msg.append('\r')
            build_msg('-------------------------------')
        else:
            add_record()
            if add_record() == 1:
                msg.append('\r')
                build_msg("[s]提交成功!")
                build_msg('- 体温: ' + get_value('lr_response').json()['data']['temperature'] + '℃')
                build_msg('- 提交时间: ' + get_time('now'))
            else:
                build_msg("[e]提交失败!")
                msg.append('\r')
        return(1)
    else:
        build_msg("[e]登陆失败! 请检查学号和密码")
        msg.append('\n')
        build_msg('-------------------------------')
