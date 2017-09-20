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
    data_list = allfiles("/home/hwang/Documents/POOQ/20170107/")
    member_file = open("/home/hwang/Documents/POOQ/member/member.csv", encoding='utf-8')
    content_vod_file = open("/home/hwang/Documents/POOQ/content/vod.csv", encoding='utf-8')

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
                        if genre == '뉴스':
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

def title():
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

    previous_luid = ""

    jtbc_hour = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                 '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                 '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
    kbs_hour = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                 '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                 '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}

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
                        if genre == '뉴스':
                            pro = title[programId]
                            if pro == 'JTBC 뉴스룸 (On-Air VOD 19:55 ~ )':
                                jtbc_hour[time] = jtbc_hour[time] + 1
                            elif pro == 'KBS 뉴스9':
                                kbs_hour[time] = kbs_hour[time]+1

                        previous_luid = luid
            except Exception as e:
                pass


    print(jtbc_hour)
    print("")
    print(kbs_hour)

def graph():
    font_name = font_manager.FontProperties(fname="/usr/share/fonts/truetype/NANUMGOTHIC.TTF").get_name()
    rc('font', family=font_name)

    jtbc = {'15': 26, '11': 65, '02': 208, '14': 34, '05': 258, '00': 11677, '03': 253, '23': 8213, '21': 14609,
            '10': 19, '01': 4984, '16': 14, '13': 79, '12': 123, '22': 13078, '07': 88, '20': 11934, '04': 107, '18': 0,
            '09': 34, '08': 170, '06': 160, '19': 770, '17': 1}

    kbs = {'15': 191, '11': 845, '02': 1593, '14': 282, '05': 700, '00': 2041, '03': 1255, '23': 964, '21': 1658,
           '10': 505, '01': 1817, '16': 212, '13': 575, '12': 519, '22': 1719, '07': 712, '20': 254, '04': 645,
           '18': 225, '09': 681, '08': 840, '06': 601, '19': 415, '17': 187}

    name_jtbc= list(jtbc.keys())
    name_kbs = list(kbs.keys())
    name_jtbc.sort()
    name_kbs.sort()
    value_jtbc = []
    value_kbs = []

    for i in name_jtbc:
        value_jtbc.append(jtbc[i])
    for i in name_kbs:
        value_kbs.append(kbs[i])

    # print(name_total)
    # print(value_total)

    sns.set_style('whitegrid')

    plot1 = plt.plot(name_jtbc, value_jtbc, color='red', label='Drama', marker='o')
    plot2 = plt.plot(name_kbs, value_kbs, color='blue', label='Entertainment', marker='o')
    plt.axis(xmin=1, ymin=0, xmax=23)
    plt.title('Vod Top2 News Viewership Graph over time')
    plt.xlabel('hour')
    plt.ylabel('count')

    plt.legend(['jtbc news 8', 'kbs news 9'], loc='best')

    plt.show()

main()
