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


def classific(section, dataset, file):
    count = 0
    for movie in dataset:
        if movie['section'] == section:
            count = count+1
    return count


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
    content_movie_file = open("PATH", encoding='utf-8')

    member = csv.DictReader(member_file, delimiter=",")
    content_movie = csv.DictReader(content_movie_file, delimiter=",")


    member = make_myDict(member,'uno','gender')
    movie = make_myDict(content_movie,'movieId','section')

    count_Male = {'코미디':0,'드라마/가족':0,'성인':0,'기타':0,'SF/판타지':0,'액션/모험':0,'로맨스/멜로':0,'애니메이션':0,'공포/스릴러':0}
    count_Female = {'코미디': 0, '드라마/가족': 0, '성인': 0, '기타': 0, 'SF/판타지': 0, '액션/모험':0, '로맨스/멜로': 0, '애니메이션': 0,
                  '공포/스릴러': 0}
    previous_luid = ''

    for file in data_list:
        f = open(file)
        data = csv.DictReader((line.replace('\0', '') for line in f), delimiter=",")
        print("starrrrrt")
        for line in data:
            try:
                if line['channeltype'] == 'M':
                    luid = line['uno']
                    contentId = line['contentId']
                    if previous_luid != luid:
                        genre = movie[contentId]
                        if member[luid] == 'M':
                            count_Male[genre] = count_Male[genre] + 1

                        elif member[luid] == 'F':
                            count_Female[genre] = count_Female[genre] + 1

                        previous_luid = luid
            except:
                pass


    print(count_Male)
    print(count_Female)

    name_male = list(count_Male.keys())
    value_male = list(count_Male.values())
    name_female = list(count_Female.keys())
    value_female = list(count_Female.values())

    male = []
    female = []

    for i in value_male:
        male.append((i/sum(value_male))*100)

    for i in value_female:
        female.append((i/sum(value_female))*100)

    w = 0.3

    pos = np.arange(len(name_male))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.bar(range(len(name_male)), male, width=w, label='male')
    plt.bar([i + w for i in range(len(name_female))], female, width=w, label='female')


    plt.ylabel('명(%)')
    plt.xlabel('장르')
    plt.legend(loc='upper left')
    plt.title('장르와 성별')

    plt.xticks(pos, name_male, rotation=45)

    plt.show()


main()









