# -*- coding: UTF-8 -*-

import csv
import matplotlib as plt


data00_file = open("log_datafile_PATH", encoding='utf-8')


data00 = csv.DictReader((line.replace('\0', '') for line in data00_file))

count_m, count_v, count_l = 0, 0, 0

previous_uno = ''

for line in data00:
    if line.get('uno') != previous_uno:
        if line.get('channeltype') == 'V':
            count_v = count_v+1
        elif line.get('channeltype') == 'M':
            count_m = count_m+1
        elif line.get('channeltype') == 'L':
            count_l = count_l+1
        previous_uno = line.get('uno')

print("VOD: "+str(count_v)+" Movie: "+str(count_m)+" Live: "+str(count_l))



data00_file.close()
