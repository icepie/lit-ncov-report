# sha256 for password
import hashlib
import pytz
import time
import datetime
import gb2260
import random


def get_sha256(password: str):
    str = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return str


def get_now_time():
    return datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def get_today_time():
    return datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d")


def time_minus(d1: str, d2: str):
    # 2012-03-05 17:41:20
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
    delta = d1 - d2
    return delta.total_seconds()


def is_outdate_last_record(lr):

    try:
        ct = lr["tempTime"]
    except:
        return True

    if time_minus(get_now_time(), ct) > 10:
        return True

    return False


def is_valid_date(strdate):
    try:
        time.strptime(strdate, "%Y-%m-%d")
        return True
    except:
        return False


# def get_now_timestamp():
#     return int(time.time())


# def datetime_timestamp(dt):
#     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
#     ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
#     ts = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
#     return int(ts)


def cl_build(current_district):
    """ use gb2260 to build a CurrentLocation """
    div_result = []
    try:
        division = gb2260.get(current_district)
        for current in division.stack():
            temp = str(u"{0}".format(current.name))
            div_result.append(temp)
            # use "-" to split str
        return "-".join(str(i) for i in div_result)
    except:
        return None


def current_location(currentDistrict, currentCity):
    """ is not grace :( """
    cl = cl_build(currentDistrict)
    if cl == None:
        cl = cl_build(currentCity)
    if cl == None:
        return None
    return cl


def random_temp():
    """ build a random temp """
    return round(random.uniform(36.0, 37.2), 2)
