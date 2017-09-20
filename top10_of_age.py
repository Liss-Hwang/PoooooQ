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

def list_to_dict(newlist):
    remove_overlap = list(set(newlist))

    dic = {}

    for list_name in remove_overlap:
        dic[list_name] = 0

    for list_count in newlist:
        dic[list_count] = dic[list_count] + 1

    return dic

def top10(dic):
    sort_dic = list(dic.values())
    sort_dic.sort(reverse=True)

    top_ten = []
    i = 0
    new_Dict = {}

    while i < 10:
        for title, count in dic.items():
            if count == sort_dic[i]:
                #top_ten.append(title)
                new_Dict[title] = count
                i = i + 1

    return new_Dict


def main():
    font_name = font_manager.FontProperties(fname="/usr/share/fonts/truetype/NANUMGOTHIC.TTF").get_name()
    rc('font', family=font_name)
    data_list = allfiles("PATH")
    member_file = open("PATH", encoding='utf-8')
    content_vod_file = open("PATH", encoding='utf-8')
    content_vod = csv.DictReader((line.replace('\0', '') for line in content_vod_file), delimiter=",")
    member = csv.DictReader((line.replace('\0', '') for line in member_file), delimiter=",")

    title = make_myDict(content_vod, 'programId', 'title')
    member_age = make_myDict(member, 'uno', 'ageGroup')

    age10 = []
    age20 = []
    age30 = []
    age40 = []
    age50 = []

    #age = {'5': 0, '10': 0, '15': 0, '20': 0, '25': 0, '30': 0, '35': 0, '40': 0, '45': 0, '50': 0, '55': 0, '60': 0}
    # age = {'10':0, '20':0, '30':0, '40':0, '50':0, '60':0}
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
                        if member_age[luid] == '10' or member_age[luid] == '15':
                            age10.append(title[programId])
                        elif member_age[luid] == '20' or member_age[luid] == '25':
                            age20.append(title[programId])
                        elif member_age[luid] == '30' or member_age[luid] == '35':
                            age30.append(title[programId])
                        elif member_age[luid] == '40' or member_age[luid] == '45':
                            age40.append(title[programId])
                        elif member_age[luid] == '50' or member_age[luid] == '55':
                            age50.append(title[programId])
                        previous_luid = luid
            except Exception as e:
                pass


    print("Finish")

    age10_dict = list_to_dict(age10)
    age20_dict = list_to_dict(age20)
    age30_dict = list_to_dict(age30)
    age40_dict = list_to_dict(age40)
    age50_dict = list_to_dict(age50)

    print(age10_dict)
    print(age20_dict)
    print(age30_dict)
    print(age40_dict)
    print(age50_dict)

    top_age10 = top10(age10_dict)
    top_age20 = top10(age20_dict)
    top_age30 = top10(age30_dict)
    top_age40 = top10(age40_dict)
    top_age50 = top10(age50_dict)

    print(top_age10)
    print(top_age20)
    print(top_age30)
    print(top_age40)
    print(top_age50)



def graph():
    age10 = {'나 혼자 산다': 68744, '낭만닥터 김사부': 35095, '푸른 바다의 전설': 65094, '무한도전': 101052, '미운 우리 새끼': 39775, '태양의 후예': 30292,
     '역도요정 김복주': 145686, '우리 결혼했어요': 60276, '라디오스타': 39843, '김병만의 정글의 법칙': 28231, '아는 형님': 31048}
    age20 = {'나 혼자 산다': 1507152, '낭만닥터 김사부': 404809, '우리 결혼했어요': 374269, '푸른 바다의 전설': 901390, '무한도전': 1702633,
     '김병만의 정글의 법칙': 396178, '미운 우리 새끼': 1248942, '역도요정 김복주': 754430, '라디오스타': 897435, '썰전': 260495, '해피 투게더': 373825}
    age30 = {'나 혼자 산다': 1875455, '낭만닥터 김사부': 504817, '썰전': 669262, '푸른 바다의 전설': 964065, '무한도전': 1798539, '김병만의 정글의 법칙': 753689,
     '미운 우리 새끼': 2498895, '팬텀싱어': 461594, '역도요정 김복주': 515562, '라디오스타': 1028857}
    age40 = {'썰전': 303147, '무한도전': 450873, '역도요정 김복주': 276237, '라디오스타': 281543, '나 혼자 산다': 590384, '낭만닥터 김사부': 283739,
     '월계수 양복점 신사들': 190415, '푸른 바다의 전설': 438900, '미운 우리 새끼': 1135678, '김병만의 정글의 법칙': 420452, '팬텀싱어': 355225,
     '솔로몬의 위증': 194391}
    age50 = {'썰전': 90300, '무한도전': 229302, '역도요정 김복주': 132078, '라디오스타': 138844, '나 혼자 산다': 270851, '낭만닥터 김사부': 112347,
     '월계수 양복점 신사들': 90513, '푸른 바다의 전설': 180336, '미운 우리 새끼': 400712, '김병만의 정글의 법칙': 141282, '팬텀싱어': 118136,
     '솔로몬의 위증': 79966}

    name_age = list(age10.keys())

    value_age = []

    for i in name_age:
        value_age.append(age10[i])

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