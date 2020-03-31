#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
import getopt

from src import func, push, mode

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
    sys.stdout = Logger('run.log')

def usage():
    print('usage: main.py -u <username> -p <password> [-f <filename>] [-l] ([-m] [-s] [-t] [-b]) ')

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hmbstlf:u:p:",["help","filename=","username=","password="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "-help", "--help") :
            usage()
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
        if 'password' in locals().keys() and 'password' in locals().keys():
            mode.normal_report(username,password)
        else:
            usage()

    # if log mode
    if 'log' in locals().keys():
        logger_run()

    # judge run mode
    if 'multi' in locals().keys():
        if 'password' in locals().keys() or 'password' in locals().keys():
            usage()
        else:
            # run a normal report (using the lasttemperature)
            if 'filename' in locals().keys():
                print('[c]载入用户配置: ' + filename)
                json_flie = filename
            else:
                if 'tab' in locals().keys():
                    push.table_tmp()
                json_flie = "config/user.json"
                mode.multi_user_report(json_flie)
                if 'serverchan' in locals().keys():
                    push.server_chan_run()
                if 'tgbot' in locals().keys():
                    push.tg_bot_run()
    else:
        normal_report()
if __name__ == "__main__":
    main(sys.argv[1:])