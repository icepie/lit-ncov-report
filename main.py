#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
import getopt
from src import mode

def usage():
    print('main.py -u <username> -p <password> [-m][-f <filename>]')

def main(argv):
    # default account
    #username = ''  # input your username
    #password = ''  # input your password
    try:
        opts, args = getopt.getopt(argv,"hmf:u:p:",["help","filename=","username=","password="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "-help", "--help") :
            usage()
            sys.exit()
        elif opt in ("-m", "--multi"):
            multi = 1
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-u", "--username"):
            username = arg
            print(username)
        elif opt in ("-p", "--password"):
            password = arg

    def normal_report():
        if 'password' in locals().keys() and 'password' in locals().keys():
            mode.normal_report(username,password)
        else:
            usage()

    if 'multi' in locals().keys():
        if 'password' in locals().keys() or 'password' in locals().keys():
            usage()
        else:
            # run a normal report (using the lasttemperature)
            if 'filename' in locals().keys():
                print('载入配置: ' + filename)
                json_dir = filename
            else:
                json_dir = "config/user.json"
            mode.multi_user_report(json_dir)
    else:
        normal_report()
        
if __name__ == "__main__":
   main(sys.argv[1:])