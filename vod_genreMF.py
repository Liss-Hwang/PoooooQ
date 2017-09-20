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

    member = make_myDict(member,'uno','gender')
    vod = make_myDict(content_vod,'programId','section')

    count_Male = {'해외드라마':0, '애니메이션':0, 'C3':0, '드라마':0, '예능':0, '키즈':0, '라디오':0, 'DN':0, '시사교양':0, '해외다큐':0, '스포츠':0, '뉴스':0}
    count_Female = {'해외드라마':0, '애니메이션':0, 'C3':0, '드라마':0, '예능':0, '키즈':0, '라디오':0, 'DN':0, '시사교양':0, '해외다큐':0, '스포츠':0, '뉴스':0}
    previous_luid = ''

    for file in data_list:
        f = open(file)
        data = csv.DictReader((line.replace('\0', '') for line in f), delimiter=",")
        print("starrrrrt")
        for line in data:
            try:
                if line['channeltype'] == 'V':
                    luid = line['uno']
                    contentId = line['programId']
                    if previous_luid != luid:
                        genre = vod[contentId]
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

    # for i, rect in enumerate(rects1):
    #     ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(round(male[i], 2)), ha='center')
    #
    # for i, rect in enumerate(rects2):
    #     ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(round(female[i], 2)), ha='center')

    plt.ylabel('명(%)')
    plt.xlabel('장르')
    plt.legend(loc='upper left')
    plt.title('장르와 성별')

    plt.xticks(pos, name_male, rotation=45)

    plt.show()


main()









