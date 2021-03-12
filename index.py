# -*- coding: utf8 -*-
#  导入模块
import os
import json
import csv
import datetime as dt
import litncov.util as util
from litncov.user import litUesr
from server.serverchan import ServerChan
from server.cqhttp import CQHTTP

# 读取主要设置
def conf_reader():
    current_path = os.path.abspath(__file__)
    config_file_path = os.path.join(
        os.path.abspath(os.path.dirname(current_path) + os.path.sep + "conf"),
        "conf.json",
    )
    with open(config_file_path, "r") as f:
        data = json.load(f)
    return data


# 读取用户配置
def users_reader():
    current_path = os.path.abspath(__file__)
    users_file_path = os.path.join(
        os.path.abspath(os.path.dirname(current_path) + os.path.sep + "conf"),
        "users.csv",
    )
    with open(users_file_path, "r") as f:
        f_csv = csv.reader(f)
        next(f_csv)
        data = [row for row in f_csv]
        return data


# 配置
main_conf = conf_reader()
users_conf = users_reader()


def push_msg(title: str, msg: str):
    # 推送功能设置
    if main_conf["push"]["serverchan"]["enabled"] == True:
        svc = ServerChan(main_conf["push"]["serverchan"]["sckey"])
        svc.send(title, msg)

    if main_conf["push"]["cqhttp"]["enabled"] == True:
        cq = CQHTTP(main_conf["push"]["cqhttp"]["url"])
        touser = main_conf["push"]["cqhttp"]["touser"]

        cqmsg = title + "\n" + msg

        if main_conf["push"]["cqhttp"]["isgroup"]:
            cq.send_group_msg(touser, cqmsg)
        else:
            cq.send_private_msg(touser, cqmsg)


def push_start_msg(t: str):

    title = "健康状况管控平台: 轮询任务准备执行"

    msg = "\t时间: " + t

    push_msg(title, msg)


def push_done_msg(
    first_count: int,
    second_count: int,
    third_count: int,
    done_count: int,
    fail_users: list,
    st,
):
    fail_count = len(fail_users)
    total_count = first_count + second_count + third_count + done_count + fail_count

    title = "健康状况管控平台: 本次上报结果"

    msg = """

\t总共: %s 人
\t失败: %s 人
\t用时: %s 秒

\t首次: %s 人
\t二次: %s 人
\t三次: %s 人
\t无需: %s 人

""" % (
        total_count,
        fail_count,
        st,
        first_count,
        second_count,
        third_count,
        done_count,
    )
    if fail_count != 0:
        msg += "\n失败列表: \n\n"
        # 失败列表
        for u in fail_users:
            msg += "\t" + u + "\n"

    push_msg(title, msg)


def report_all(username: str, password: str):
    # 新建实例
    litu = litUesr(username, password)
    # 判断是否登陆成功
    if litu.is_logged:
        # 判断今天是否上报过
        if not litu.is_record_today():
            # 读取第一次上报模式
            if main_conf["report"]["first"]["temperature"]:
                data = litu.first_record(
                    mode=main_conf["report"]["first"]["mode"],
                    temperature=main_conf["report"]["first"]["temperature"],
                    rtimes=1,
                )
            else:
                data = litu.first_record(
                    mode=main_conf["report"]["first"]["mode"], rtimes=1
                )
            if data:
                return 1

        # 判断今天是否第二次上报过
        elif not litu.is_record_today(2):
            # 读取第二次上报模式
            if main_conf["report"]["second"]["temperature"]:
                data = litu.second_record(
                    mode=main_conf["report"]["second"]["mode"],
                    temperature=main_conf["report"]["second"]["temperature"],
                )
            else:
                data = litu.second_record(
                    mode=main_conf["report"]["second"]["mode"]["temperature"]
                )
            if data:
                return 2

        # 判断今天是否第三次上报过
        elif not litu.is_record_today(rtime=3):
            # 读取第三次上报模式
            if main_conf["report"]["third"]["temperature"]:
                data = litu.third_record(
                    mode=main_conf["report"]["third"]["mode"],
                    temperature=main_conf["report"]["third"]["temperature"],
                )
            else:
                data = litu.third_record(
                    mode=main_conf["report"]["third"]["mode"]["temperature"]
                )
            if data:
                return 3
        else:
            return 0
    else:
        return -1

# 腾讯云 云函数 入口
def main_handler(event, context):

    start = dt.datetime.now()
    push_start_msg(util.get_now_time())

    # 计数器生成详情
    first_count = 0
    second_count = 0
    third_count = 0
    done_count = 0
    fail_users = []

    # 遍历帐号表进行上报
    for u in users_conf:
        rte = report_all(u[0], u[1])
        print("账号:" + u[0])
        if rte == 0:
            done_count += 1
            print("\t无需")
        elif rte == 1:
            first_count += 1
            print("\t第一次上报成功")
        elif rte == 2:
            second_count += 1
            print("\t第二次上报成功")
        elif rte == 3:
            third_count += 1
            print("\t第三次上报成功")
        else:
            fail_users.append(u[0])
            print("\t上报失败")

    end = dt.datetime.now()

    # 计算所用时间
    st = (end - start).seconds

    # print(first_count, second_count, third_count, done_count, fail_users)
    push_done_msg(
        first_count, second_count, third_count, done_count, fail_users, str(st)
    )

# 阿里云 函数计算 入口 
def handler(event, context):
    main_handler(event, context)
