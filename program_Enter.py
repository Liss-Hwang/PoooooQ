import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import os
import seaborn as sns


def allfiles(path):
    res = []

    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)

        for file in files:
            filepath = os.path.join(rootpath, file)
            res.append(filepath)

    return res


def make_myDict(Dict,var1,var2):
    newDict = {}
    for line in Dict:
        newDict[line[var1]]= line[var2]

    return newDict


def main():
    font_name = font_manager.FontProperties(fname="/usr/share/fonts/truetype/NANUMGOTHIC.TTF").get_name()
    rc('font', family=font_name)
    data_list = allfiles("PATH")
    member_file = open("PATH", encoding='utf-8')
    content_vod_file = open("PATH", encoding='utf-8')

    #member = csv.DictReader(member_file, delimiter=",")
    content_vod = csv.DictReader((line.replace('\0', '') for line in content_vod_file), delimiter=",")


    section = make_myDict(content_vod, 'programId','section')
    content_vod_file = open("/home/hwang/Documents/POOQ/content/vod.csv", encoding='utf-8')

    # member = csv.DictReader(member_file, delimiter=",")
    content_vod = csv.DictReader((line.replace('\0', '') for line in content_vod_file), delimiter=",")
    title = make_myDict(content_vod, 'programId', 'title')

    title_list = []
    previous_luid = ""

    for file in data_list:
        f = open(file)
        data = csv.DictReader((line.replace('\0', '') for line in f), delimiter=",")
        print("starrrrrt")

        for line in data:
            try:
                if line['channeltype'] == 'V':

                    luid = line['uno']
                    programId = line['programId']
                    time = line['hour']
                    #total_hour[time] = total_hour[time]+1
                    if previous_luid != luid:
                        genre = section[programId]
                        if genre == '예능':
                            pro = title[programId]
                            title_list.append(pro)


                        previous_luid = luid
            except Exception as e:
                pass


    print(title_list)
    remove_overlap = list(set(title_list))

    dic = {}

    for list_name in remove_overlap:
        dic[list_name] = 0

    for list_count in title_list:
        dic[list_count] = dic[list_count] + 1

    print(dic)

main()
