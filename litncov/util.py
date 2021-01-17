# sha256 for password
import hashlib
import datetime
import gb2260
import random

def get_sha256(password: str):
    str = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return str

def get_time(type):
    if type == 'now':
        return str(datetime.datetime.now().replace(microsecond=0))
    elif type == 'today':
        return str(datetime.date.today())
    else:
        return None

def cl_build(current_district):
    div_result = []
    try:
        division = gb2260.get(current_district)
        for current in division.stack():
            temp = str(u'{0}'.format(current.name))
            div_result.append(temp)
            # use "-" to split str
        return("-".join(str(i) for i in div_result))
    except:
        return None

## not grace :(
def current_location(currentDistrict, currentCity):
    cl = cl_build(currentDistrict)
    if cl == None:
        cl = cl_build(currentCity)
    if cl == None:
        return None
    return cl

def random_temp():
    return round(random.uniform(36.0,37.2), 2)