#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os
import sys
import getopt

from src import func, push, mode

current_path = os.path.dirname(os.path.abspath(__file__))

# log system
def logger_run():
    class Logger(object):
        def __init__(self, filename="Default.log"):
            self.terminal = sys.stdout
            self.log = open(filename, "a")
        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)
        def flush(self):
            pass
    sys.stdout = Logger(os.path.join(current_path, 'log/run.log'))

def usage():
    print('usage: main.py -u <username> -p <password> [-f <filename>] [-l] ([-m] [-s] [-t] [-b]) ')

def version():
    print('lit-ncov-report v1.9, by icepie@github')

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hvmbstlf:u:p:",["help","version","multi","table","filename=","username=","password=","tgbot","serverchan","log"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help") :
            usage()
            sys.exit()
        elif opt in ("-v", "--version"):
            version()
            sys.exit()
        elif opt in ("-m", "--multi"):
            multi = 1
        elif opt in ("-b", "--table"):
            tab = 1
        elif opt in ("-s", "--serverchan"):
            serverchan = 1
        elif opt in ("-t", "--tgbot"):
            tgbot = 1
        elif opt in ("-l", "--log"):
            log = 1
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg

    def normal_report():
        if 'username' in locals().keys() and 'password' in locals().keys():
            mode.normal_report(username,password)
        else:
            usage()

    # if log mode
    if 'log' in locals().keys():
        logger_run()

    # judge run mode
    if 'multi' in locals().keys():
        # run a normal report (using the lasttemperature)
        if 'filename' in locals().keys():
            print('[c]载入用户配置: ' + filename)
            json_flie = filename
        else:
            json_flie = os.path.join(current_path, 'config/user.json')
        if 'tab' in locals().keys():
            push.table_tmp()
        mode.multi_user_report(json_flie)
    else:
        normal_report()

    # tab verification
    if 'tab' in locals().keys() and 'multi' not in locals().keys():
        print('[e]table must be run in multi-user mode')

    # push message
    if 'username' in locals().keys() and 'password' in locals().keys() or 'multi' in locals().keys():
        if 'serverchan' in locals().keys():
            push.server_chan_run()
        if 'tgbot' in locals().keys():
            push.tg_bot_run()

# main function
if __name__ == "__main__":
    main(sys.argv[1:])
