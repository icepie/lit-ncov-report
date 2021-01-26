# -*- coding: utf8 -*-
#  导入模块
from litncov.user import litUesr
def main_handler(event, context):
    # 新建实例
    testme = litUesr("username", "password")

    # 判断是否登陆成功
    if testme.is_logged:
        # 打印用户信息
        # print(testme.info)
        # 打印上次上报信息
        print(testme.get_last_record())
        # # 查询 2021-01-04 至今的上报信息
        # print(testme.query_record('2021-01-04'))
        # # 查询 2021-01-04 至 2021-01-18 的上报信息
        # print(testme.query_record('2021-01-04', '2021-01-18'))
        # # 打印学生学籍信息
        # print(testme.get_instructor())
        # # 打印用户家庭信息
        # print(testme.get_familys())
        # 打印用户外出信息
        print(testme.get_trips())
        # 打印疫情严重地区
        print(testme.get_important_city())
        # 判断今天是否上报过
        if not testme.is_record_today():
            # 进行当日第一次体温上报
            ## 模式：使用上一次上报信息， 次数： 只上报第一次
            print(testme.first_record(mode='last', rtimes=1))
        # 判断今天是否第二次上报过
        elif not testme.is_record_today(2):
            # 进行当日第二次体温上报
            ## 模式：手动填入， 温度： 36.6 摄氏度
            print(testme.second_record(mode='manual', temperature=36.6))
        # 判断今天是否第三次上报过
        elif not testme.is_record_today(rtime=3):
            # 进行当日第三次体温上报
            ## 模式：随机生成正常体温(36.0~37.2 摄氏度)
            print(testme.third_record(mode='random'))