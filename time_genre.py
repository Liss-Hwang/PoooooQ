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

    member = csv.DictReader(member_file, delimiter=",")
    content_vod = csv.DictReader(content_vod_file, delimiter=",")

    # f = open("/home/hwang/Documents/POOQ/20170107/20170107_00_bookmark.csv")
    # data = csv.DictReader((line.replace('\0', '') for line in f), delimiter=",")

    vod = make_myDict(content_vod, 'programId','section')
    drama_hour = {'00':0,'01':0, '02':0, '03':0, '04':0, '05':0, '06':0, '07':0, '08':0, '09':0, '10':0, '11':0, '12':0, '13':0, '14':0, '15':0,
            '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0}
    culture_hour = {'00':0,'01':0, '02':0, '03':0, '04':0, '05':0, '06':0, '07':0, '08':0, '09':0, '10':0, '11':0, '12':0, '13':0, '14':0, '15':0,
            '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0}
    sport_hour = {'00':0,'01':0, '02':0, '03':0, '04':0, '05':0, '06':0, '07':0, '08':0, '09':0, '10':0, '11':0, '12':0, '13':0, '14':0, '15':0,
            '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0}
    enter_hour = {'00':0,'01':0, '02':0, '03':0, '04':0, '05':0, '06':0, '07':0, '08':0, '09':0, '10':0, '11':0, '12':0, '13':0, '14':0, '15':0,
            '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0}

    previous_luid = ''
    count = 0

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
                        genre = vod[programId]
                        if genre == '드라마':
                            drama_hour[time] = drama_hour[time]+1
                        elif genre == '시사교양':
                            culture_hour[time] = culture_hour[time]+1
                        elif genre == '예능':
                            enter_hour[time] = enter_hour[time]+1
                        elif genre == '스포츠':
                            sport_hour[time] = sport_hour[time]+1

                        previous_luid = luid
            except Exception as e:
                pass

    print(drama_hour)
    print(enter_hour)
    print(culture_hour)
    print(sport_hour)



main()



