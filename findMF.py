# -*- coding: UTF-8 -*-

import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import os


def allfiles(path):
    res = []

    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)

        for file in files:
            filepath = os.path.join(rootpath, file)
            res.append(filepath)

    return res


def classific_MF(luid, member):
    count = 2
    try:
        if member[luid] == 'M':
            count = 0
        elif member[luid] == 'F':
            count = 1
        else:
            count = 2
    except Exception as e:
        pass
    finally:
        return count


def make_memberDict(memberDict):
    newDict = {}
    for member in memberDict:
        newDict[member['uno']]= member['gender']

    return newDict
            


def main():
    font_name = font_manager.FontProperties(fname="/usr/share/fonts/truetype/NANUMGOTHIC.TTF").get_name()
    rc('font', family=font_name)
    data_list = allfiles("PATH")
    member_file = open("PATH", encoding='utf-8')
    memberDict = csv.DictReader(member_file, delimiter=",")
    member = make_memberDict(memberDict)

    Video_M = 0
    Video_F = 0
    Movie_M = 0
    Movie_F = 0
    Live_M = 0
    Live_F = 0

    previous_luid = ''

    #f = open("/home/hwang/Documents/POOQ/20170107/20170107_00_bookmark.csv","rb")

    for file in data_list:
        f = open(file)
        data = csv.DictReader((line.replace('\0', '') for line in f), delimiter=",")
        print("Starrrrrrt")

        for line in data:
            try:
                if line['channeltype'] == 'V':
                    luid = line['uno']
                    if previous_luid != luid:
                        temp = classific_MF(luid, member)
                        if temp == 1:
                            Video_F = Video_F + 1
                        elif temp == 0:
                            Video_M = Video_M + 1
                        previous_luid = luid

                elif line['channeltype'] == 'M':
                    luid = line['uno']
                    if previous_luid != luid:
                        temp = classific_MF(luid, member)
                        if temp == 1:
                            Movie_F = Movie_F + 1
                        elif temp == 0:
                            Movie_M = Movie_M + 1
                        previous_luid = luid

                elif line['channeltype'] == 'L':
                    luid = line['uno']
                    if previous_luid != luid:
                        temp = classific_MF(luid, member)
                        if temp == 1:
                            Live_F = Live_F + 1
                        elif temp == 0:
                            Live_M = Live_M + 1
                        previous_luid = luid
            except Exception as e:
                print(line)
                print(e)
                pass



    # mem_M = 1007520
    # mem_F = 1121167

    Video_G = Video_M+Video_F
    Movie_G = Movie_M+Movie_F
    Live_G = Live_F+Live_M

    print("Video_M: " + str(Video_M) + " Video_F: " + str(Video_F) + " Movie_M: " + str(Movie_M) + " Movie_F: " + str(
        Movie_F) + " Live_M: "
          + str(Live_M) + " Live_F: " + str(Live_F))

    name = ["Video_M", "Video_F", " Movie_M", " Movie_F", " Live_M", "Live_F"]
    data = [round((Video_M / Video_G) * 100,2), round((Video_F / Video_G) * 100,2),
            round((Movie_M / Movie_G) * 100,2), round((Movie_F / Movie_G) * 100,2),
            round((Live_M / Live_G) * 100,2), round((Live_F / Live_G) * 100,2)]

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)

    pos = np.arange(6)
    rects = plt.bar(pos, data, align='center', width=0.5)
    plt.xticks(pos, name)

    for i, rect in enumerate(rects):
        ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(data[i]), ha='center')

    plt.ylabel('명')
    plt.xlabel('성별')
    plt.title('채널에 따른 성별(하루)')

    plt.show()


main()





