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

    deviceV = {'Android Phone':0, 'iOS Tablet':0, 'PC':0, 'Android Tablet':0, 'Chromecast':0,
               'Unocube OTT Device':0, 'Smart TV':0, 'iOS Phone':0}
    deviceM = {'Android Phone': 0, 'iOS Tablet': 0, 'PC': 0, 'Android Tablet': 0, 'Chromecast': 0,
               'Unocube OTT Device': 0, 'Smart TV': 0, 'iOS Phone': 0}
    deviceL = {'Android Phone': 0, 'iOS Tablet': 0, 'PC': 0, 'Android Tablet': 0, 'Chromecast': 0,
               'Unocube OTT Device': 0, 'Smart TV': 0, 'iOS Phone': 0}

    android_hour = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
    iphone_hour = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
    pc_hour = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                  '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                  '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}


    previous_luid = ''

    for file in data_list:
        f = open(file)
        data = csv.DictReader((line.replace('\0', '') for line in f), delimiter=",")
        print("starrrrrt")

        for line in data:
            try:
                if line['channeltype'] == 'V':
                    luid = line['uno']
                    if previous_luid != luid:
                        time = line['hour']
                        if line['devicetype'] == 'Android Phone':
                            android_hour[time] = android_hour[time] + 1
                        if line['devicetype'] == 'PC':
                            pc_hour[time] = pc_hour[time] + 1

                        previous_luid = luid
            except Exception as e:
                pass


    print(android_hour)
    print(pc_hour)


def graph():

    android_phone = {'16': 802950, '02': 789748, '19': 677844, '18': 657487, '04': 415353, '23': 1218412, '20': 699053, '00': 1006972, '10': 755826, '05': 338094, '17': 726879, '22': 1132782, '14': 826126, '01': 1019362, '08': 550817, '15': 821966, '06': 337785, '07': 413741, '12': 815477, '13': 835273, '21': 874637, '09': 663058, '03': 561973, '11': 803151}

    pc = {'16': 658314, '02': 497006, '19': 582023, '18': 552456, '04': 268781, '23': 854817, '20': 702322, '00': 691419, '10': 456387, '05': 211643, '17': 608690, '22': 912618, '14': 678097, '01': 646622, '08': 247493, '15': 679124, '06': 184873, '07': 194356, '12': 608962, '13': 656061, '21': 824472, '09': 344223, '03': 351393, '11': 544603}


    name_phone = list(android_phone.keys())
    name_pc = list(pc.keys())
    name_phone.sort()
    name_pc.sort()
    value_phone = []
    value_pc = []

    for i in name_phone:
        value_phone.append(android_phone[i])
    for i in name_pc:
        value_pc.append(pc[i])



    # print(name_total)
    # print(value_total)

    sns.set_style('whitegrid')

    plot1 = plt.plot(name_phone, value_phone, color='red', label='phone', marker='o')
    plot2 = plt.plot(name_pc, value_pc, color='blue', label='pc', marker='o')
    plt.axis(xmin=0, ymin=0, xmax=23)
    plt.title('Device usage')
    plt.xlabel('hour')
    plt.ylabel('count')


    plt.legend(['phone', 'pc'], loc='best')

    plt.show()

def graph_bar():
    vod = {'Unocube OTT Device': 10911, 'iOS Tablet': 4409119, 'Android Phone': 17744766, 'iOS Phone': 9230383,
           'Android Tablet': 2279564, 'Chromecast': 312878, 'PC': 12956755, 'Smart TV': 3202752}
    movie = {'Unocube OTT Device': 0, 'iOS Tablet': 36606, 'Android Phone': 170449, 'iOS Phone': 61599,
             'Android Tablet': 37825, 'Chromecast': 6744, 'PC': 173267, 'Smart TV': 96614}
    live = {'Unocube OTT Device': 0, 'iOS Tablet': 1870628, 'Android Phone': 4104463, 'iOS Phone': 1652893,
            'Android Tablet': 1011545, 'Chromecast': 156844, 'PC': 6261769, 'Smart TV': 0}

    name_vod = list(vod.keys())
    name_movie = list(movie.keys())
    name_live = list(live.keys())
    name_vod.sort()
    name_movie.sort()
    name_live.sort()
    value_vod = []
    value_movie = []
    value_live = []

    for i in name_vod:
        if vod[i] != 0 :
            value_vod.append((vod[i]/sum(vod.values()))*100)
        else:
            value_vod.append(vod[i])
    for i in name_movie:
        if movie[i] != 0:
            value_movie.append((movie[i]/sum(movie.values()))*100)
        else:
            value_movie.append(movie[i])
    for i in name_live:
        if live[i] != 0:
            value_live.append((live[i]/sum(live.values()))*100)
        else:
            value_live.append(live[i])

    w = 0.3

    pos = np.arange(len(name_vod))

    # fig = plt.figure()
    # ax = fig.add_subplot(111)

    plt.bar(range(len(name_vod)), value_vod, width=w, label='vod',color='red')
    plt.bar([i + w for i in range(len(name_movie))], value_movie, width=w, label='movie',color='green')
    plt.bar([i - w for i in range(len(name_live))], value_live, width=w, label='live', color='blue')

    # for i, rect in enumerate(rects1):
    #     ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(round(male[i], 2)), ha='center')
    #
    # for i, rect in enumerate(rects2):
    #     ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(round(female[i], 2)), ha='center')

    plt.ylabel('count')
    plt.xlabel('device type')
    plt.legend(loc='upper right')
    plt.title('Usage of Device')

    plt.xticks(pos, name_vod, rotation=45)

    plt.show()




graph()