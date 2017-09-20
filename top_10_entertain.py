import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import seaborn as sns
import os


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
    content_vod = csv.DictReader((line.replace('\0', '') for line in content_vod_file), delimiter=",")

    content_vod = csv.DictReader((line.replace('\0', '') for line in content_vod_file), delimiter=",")
    title = make_myDict(content_vod, 'programId', 'title')

    top_10_enter = {'나 혼자 산다':0, '라디오스타':0, '미운 우리 새끼':0, '김병만의 정글의 법칙':0, '팬텀싱어':0, '무한도전':0,
                '해피 투게더':0, '주간 아이돌':0, '자기야-백년손님':0, '거침없이 하이킥':0, '듀엣가요제':0, '아는 형님':0}
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
                    if previous_luid != luid:
                        if title[programId] in top_10_enter:
                            add_count = title[programId]
                            top_10_enter[add_count] = top_10_enter[add_count]+1

                        previous_luid = luid
            except Exception as e:
                pass

    print(top_10_enter)

main()




