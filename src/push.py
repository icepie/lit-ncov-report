import os
import json
import telebot
import requests

from .func import *
from .mode import *

# tg push proxy
#telebot.apihelper.proxy = {'https':'socks5://127.0.0.1:1080'}

current_path = os.path.dirname(os.path.abspath(__file__))

# server chan 
# read json flie
push_json = os.path.join(current_path, '../config/push.json')

with open(push_json, 'r') as fw:
    push_dict = json.load(fw)

msg = list()

def table_tmp():
    print('[s]程序运行中...')
    print('[s]正在生成结果...')
    set_value('table',1)
    return (1)

def build_msg(self):
    if get_value('table') != 1:
        print(self)
    msg.append(self)

sc_response = None

def server_chan_run():
    server_chan_sckey = str(push_dict['sckey']) # http://sc.ftqq.com/3.version
    server_chan = {
        'url': 'https://sc.ftqq.com/{}.send'.format(server_chan_sckey)
    }

    def server_chan_send():
        """server chan push log to WeChat"""

        desp = '#### 结果如下' + '\n'
        desp += '~~~~'  + '\n'

        if get_value('table') == 1:
            desp += get_value('tbw')
        else:
            for d in msg:
                desp += d + '\n' +'\n'
            desp += '~~~~'  + '\n'
            desp += '[项目](https://github.com/icepie/lit-ncov-report)'  + '\n'
           
        params = {
            'text': '今日上报任务已完成',
            'desp': desp
        }

        sc_response = requests.get(server_chan['url'], params=params)

        if 'errno' in sc_response.json():
            if sc_response.json()['errno'] == 0:
                print('[s]server酱 推送成功!')
            else:
                print('[e]server酱 推送失败!')    
                print(sc_response.json())
        else:
            print('[e]请检查 config/push.json 中的配置')

    server_chan_send()

# tgbot push 
def tg_bot_run():
    # check tg token
    if not push_dict['tgtoken']:
        print('[e]tgtoken未找到')
        print('[e]请检查 config/push.json 中的配置')
        quit()
    tgtoken = str(push_dict['tgtoken'])

    # check tg chat id
    if not push_dict['tgid']:
        print('[e]tgid未找到')
        print('[e]请检查 config/push.json 中的配置')
        quit()
    tgid = str(push_dict['tgid'])
    
    bot = telebot.TeleBot(tgtoken)

    desp = '#lnr ' + '\n'

    if get_value('table') == 1: 
        desp +=  '<pre>' + '-------------- 今日上报任务已完成! ------------' + '\n' + get_value('tbt') + '</pre>'
        tg_response = bot.send_message(chat_id=tgid, text=desp, parse_mode='HTML')
    else:
        desp +=  '-------------- 今日上报任务已完成! ------------' + '\n'
        desp += '+++++++++++++++++++++++++++++++' + '\n'
        for d in msg:
            desp += d + '\n'
        tg_response = bot.send_message(chat_id=tgid, text=desp)

    if tg_response:
        print('[s]Telegram Bot 推送成功!')
    else:
        print('[e]Telegram Bot 推送失败!') 
        print('[e]请检查 config/push.json 中的配置')
