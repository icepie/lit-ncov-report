# lit-ncov-report
洛阳理工学院 "健康状况管控平台" 的一个非官方`Python封装库`兼`CLI工具`与`拓展实现`

[![pypi version](https://img.shields.io/pypi/v/litncov)](https://pypi.org/project/litncov/)
[![pypi downloads per month](https://img.shields.io/pypi/dm/litncov)](https://pypi.org/project/litncov/)
[![Docker Pulls](https://img.shields.io/docker/pulls/icepie/litncov.svg)](https://hub.docker.com/r/icepie/litncov/)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![QQ Group](https://img.shields.io/badge/QQ%20Group-768887710-red.svg)](https://jq.qq.com/?_wv=1027&k=lz0XyN86)
[![TG Group](https://img.shields.io/badge/TG%20Group-lit_edu-blue.svg)](https://t.me/lit_edu)

> 如需旧版请前往 [v1](https://github.com/icepie/lit-ncov-report/tree/v1)

> Serverless(如云函数)请前往 [scf](https://github.com/icepie/lit-ncov-report/tree/scf)

## 安装

### Python

```bash
# Python3.6+ with pip
pip install litncov --upgrade
```

### Docker

```bash
docker run -it --rm icepie/litncov
```

## 封装库

### 范例

```python
#  导入模块
from litncov.user import litUesr

# 新建实例
testme = litUesr("username", "password")

# 判断是否登陆成功
if testme.is_logged:
    # 打印用户信息
    print(testme.info)
    # 打印上次上报信息
    print(testme.get_last_record())
    # 查询 2021-01-04 至今的上报信息
    print(testme.query_record('2021-01-04'))
    # 查询 2021-01-04 至 2021-01-18 的上报信息
    print(testme.query_record('2021-01-04', '2021-01-18'))
    # 打印学生学籍信息
    print(testme.get_instructor())
    # 打印用户家庭信息
    print(testme.get_familys())
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
    if not testme.is_record_today(2):
        # 进行当日第二次体温上报
        ## 模式：手动填入， 温度： 36.6 摄氏度
        print(testme.second_record(mode='manual', temperature=36.6))
    # 判断今天是否第三次上报过
    if not testme.is_record_today(rtime=3):
        # 进行当日第三次体温上报
        ## 模式：随机生成正常体温(36.0~37.2 摄氏度)
        print(testme.third_record(mode='random'))
```

## CLI工具

### 上报功能

#### 例子

- 使用上一条上报记录进行今天三次上报

```bash
$ litncov -u USERNAME -p PASSWORD report -a
# 不带 -a 参数则只进行今天第一次上报
```

- 使用随机温度进行今天第二次上报

```bash
$ litncov -u USERNAME -p PASSWORD report -r 2 -m random
```

- 手动输入温度进行今天第三次上报

```bash
$ litncov -u USERNAME -p PASSWORD report -r 3 -t 36.7
```

#### 帮助

```
$ litncov report -h
usage: litncov report [-h] [-a] [-f] [-r RTIME] [-m MODE] [-t TEMP]

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             do the all report tasks today
  -f, --force           forcely report
  -r RTIME, --rtime RTIME
                        the report time {1,2,3}
  -m MODE, --mode MODE  the report mode {last,random,manual}, default last
  -t TEMP, --temp TEMP  the body temperature (float), only use in manual
```

### 查询用户信息

#### 例子

- 主要个人信息

```bash
$ litncov -u USERNAME -p USERNAME info --user
```

- 外出信息

```bash
$ litncov -u USERNAME -p USERNAME info --trip
```

- 上次上报记录

```bash
$ litncov -u USERNAME -p USERNAME info -l
```

#### 帮助

```
$ litncov info -h
usage: litncov info [-h] [-u] [-l] [-f] [-i] [-t]

optional arguments:
  -h, --help         show this help message and exit
  -u, --user         the user main info
  -l, --last_record  the user last record info
  -f, --family       the user family info
  -i, --instructor   the user instructor info
  -t, --tirp         the user tirp info

```

### 查询上报记录

#### 例子
- 查询某日至今

```bash
$ litncov -u USERNAME -p PASSWORD query -s 2020-01-01
```

- 查询某日至某日

```bash
$ litncov -u USERNAME -p PASSWORD query -s 2020-01-01 -e 2020-01-15
```

#### 帮助

```
usage: litncov query [-h] -s START_TIME [-e END_TIME]

optional arguments:
  -h, --help            show this help message and exit
  -s START_TIME, --start_time START_TIME
                        the start time of the report history (Year-Month-Day)
  -e END_TIME, --end_time END_TIME
                        the end time of the report history, default Today (Year-Month-Day)
```
