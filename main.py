#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from modules import mediawiki as mw
from modules import emojiapp_config as ec
import csv, sys, os, time
exit = sys.exit
ecname = "dawson783"
S = requests.Session()
csvpath = ec.get_root(ecname)+'/articles.csv'

def merge_two_dicts(x, y): # Backward compatibility
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def get_content():
    ret = {}
    try:
        with open(csvpath, newline='') as csvfile:
            rows = list(csv.reader(csvfile)).copy()
    except FileNotFoundError:
        print("Please create `"+csvpath+"` with article infomations!")
        return False
    count = 1
    for row in rows:
        # IndexError
        text = "{{User:SickManWP/沙盒/9"
        try:
            for x in range(24):
                text = text + "|" + str(row[x])
        except IndexError:
            print("Error in CSV file line "+str(count)+": Missing infomation")
            return False
        text = text + "}}"
        # merge_two_dicts(x, y)
        # 0,2,3
        title = row[0]+"_("+row[2]+row[3]+")"
        ret = merge_two_dicts(ret, {title:text})
        count = count + 1
    return ret

def run()
    uname = input("Please enter your bot username: ")
    passwd = input("Please enter your bot password: ")
    lgtoken = mw.token(S,"login")[0]
    lgstatus = mw.login(S,lgtoken,uname,passwd)
    if lgstatus == False
        print("error while login")
        exit(1)
    del passwd
    tmp = input("Please confirm `"+csvpath+"` have right content, then press enter to continue...")
    data = get_content()
    for title, content in data.items():
        time.sleep(5)
        etokenDATA = mw.token(S,"csrf")
        if etokenDATA == False:
            print("error while getting token to edit "+title)
            continue
        etoken = etokenDATA[0]
        mw.edit(S,etoken,title,content,"Auto creating [[WP:IOWA]] articles via [[https://zh.wikipedia.org/wiki/User:SickManWP/沙盒/9]]",True,True)

if __name__ == '__main__':
    run()
