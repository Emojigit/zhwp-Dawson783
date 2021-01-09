#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from modules import mediawiki
from modules import emojiapp_config as ec
import csv, sys, os
exit = sys.exit
ecname = "dawson783"
S = requests.Session()

def merge_two_dicts(x, y): # Backward compatibility
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def get_content():
    csvpath = ec.get_root(ecname)+'/articles.csv'
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
