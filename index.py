# -*- coding: utf8 -*-
#  导入模块
from litncov.user import litUesr
from server.serverchan import ServerChan


# 推送功能设置
svc = ServerChan("SCKEY")

# 新建实例
litu = litUesr("username", "password")


def main_handler(event, context):
    # 判断是否登陆成功
    if litu.is_logged:
        last_record = litu.get_last_record()
        # 判断今天是否上报过
        if not litu.is_record_today():
            # 进行当日第一次体温上报
            # 模式：使用上一次上报信息， 次数： 只上报第一次
            data = litu.first_record(mode="last", rtimes=1)
            print(data)
            if data != None:
                status = "成功"
            else:
                status = "失败"
            svc.send(("健康状况管控平台: 第一次上报" + status), ("温度: " + str(data["data"]["temperature"]) ))
        # 判断今天是否第二次上报过
        elif not litu.is_record_today(2):
            # 进行当日第二次体温上报
            # 模式：手动填入， 温度： 36.6 摄氏度
            data = litu.second_record(mode="manual", temperature=36.6)
            if data != None:
                status = "成功"
            else:
                status = "失败"
            svc.send(("健康状况管控平台: 第二次上报" + status), ("温度: " + str(data["data"]["temperature"]) ))
        # 判断今天是否第三次上报过
        elif not litu.is_record_today(rtime=3):
            # 进行当日第三次体温上报
            # 模式：随机生成正常体温(36.0~37.2 摄氏度)
            data = litu.third_record(mode="random")
            if data != None:
                status = "成功"
            else:
                status = "失败"
            svc.send(("健康状况管控平台: 第三次上报" + status), ("温度: " + str(data["data"]["temperature"]) ))
        else:
            svc.send("健康状况管控平台: 已完成今日上报任务", "温度一: " + str(last_record["data"]["temperature"]) +  " 温度二: " + str(last_record["data"]["temperatureTwo"]) + " 温度三: " +  str(last_record["data"]["temperatureThree"]))
    else:
        svc.send("健康状况管控平台: 登陆失败", "学号: " + litu.username + " 该用户无法登陆" )