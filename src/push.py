import json
from .func import *
import requests

# server chan 
# read json flie
push_json = 'config/push.json'

with open(push_json, 'r') as fw:
    push_dict = json.load(fw)

msg = list()
def build_msg(str):
    print(str)
    msg.append(str)

sc_response = None


def server_chan_run():
    server_chan_sckey = str(push_dict['sckey']) # http://sc.ftqq.com/3.version
    server_chan = {
        'url': 'https://sc.ftqq.com/{}.send'.format(server_chan_sckey)
    }

    #print("网站名：{name}, 地址 {date}".format(**s ))

    def server_chan_send(msg):
        """server chan push log to WeChat"""
        desp = ''
        for d in msg:
            desp += d + '\r' 

        #print(desp)

        params = {
            'text': '今日上报任务已完成!!',
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
            print('请检查 config/push.json 中的配置')

    server_chan_send(msg)
