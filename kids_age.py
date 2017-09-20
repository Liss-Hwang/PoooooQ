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
    member = csv.DictReader((line.replace('\0', '') for line in member_file), delimiter=",")

    genre = make_myDict(content_vod, 'programId', 'section')
    member_age = make_myDict(member, 'uno', 'ageGroup')


    age = {'5':0, '10':0, '15':0, '20':0, '25':0, '30':0, '35':0, '40':0, '45':0, '50':0, '55':0, '60':0}
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
                    if previous_luid != luid:
                        if genre[programId] == '키즈':
                            ages = member_age[luid]
                            age[ages] = age[ages]+1

                        previous_luid = luid
            except Exception as e:
                pass

    print(age)

def graph():
    age = {'50': 2617, '35': 51179, '55': 1185, '45': 10544, '15': 2553, '60': 1479, '5': 29, '10': 185, '30': 24191, '20': 3019, '25': 9981, '40': 27715}

    name_age = list(age.keys())
    name_age.sort()
    value_age = []

    for i in name_age:
        value_age.append(age[i])

    # print(name_total)
    # print(value_total)

    sns.set_style('whitegrid')

    plot1 = plt.bar(name_age, value_age)
    #plt.axis(xmin=5, ymin=0, xmax=60)
    plt.title('Age Group of Kids program viewer')
    plt.xlabel('age')
    plt.ylabel('count')

    plt.show()

graph()