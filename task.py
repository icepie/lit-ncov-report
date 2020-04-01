#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os, datetime
from src import crontab, crontab_run

# main
if __name__ == '__main__':
    # 每天00点00分10秒运行一次'executor script1 argv1'
    executor='python3'
    script1 = 'main.py'
    argv1 = '-m -t -s' 
    crontab.every('day').at(hour=0, minute=0, second=10).execute(script1,executor,argv1)
    
    # 每5分钟运行一次script2
    #script2 = '/opt/scrapy_news.py'
    #crontab.every('minute').interval(5).execute(script2)
    
    # 设置开始时间和结束时间
    #script3 = '/opt/scrapy_goods.py'
    #begin_time = datetime.datetime.strptime('2018-06-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    #end_time = datetime.datetime.strptime('2018-10-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    #crontab.every('minute').interval(5).begin(begin_time).end(end_time).execute(script3)
    
    # 每月最后一天运行script4
    #script4 = '/opt/scrapy_blog.py'
    #crontab.every('month').at(day=-1).execute(script4)
    
    # 开始运行crontab, 默认debug=False
    crontab_run(debug = False)
