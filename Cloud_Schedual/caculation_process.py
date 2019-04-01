"""
this is the main programme of the cloud caculation
there are some funcs
"""
import csv
import pickle
import random
from Cloud_Schedual.OPOS import *

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

import Cloud_Schedual.parameter_list

def price_up(num):
    '''
    :param num:number of the spot instance in the last time slot
    :return: the up rate of price in the next time slot with the same probability
    '''
    return 0.012 * 0.1 * np.exp(0.0018 * num) / (
            0.1 + 0.012 * (np.exp(0.0018 * num) - 1)) - 0.012

def get_the_list():
    '''
    get the whole list from the 48 csvs
    :return: the list of data in each time slot
    '''
    totel_list = []
    for num in range(1, 49):
        tmp = []
        csv_reader = csv.reader(open('data_base/data_set_' + str(num) + '.txt'))
        for index in csv_reader:
            a = index[0].split(" ")
            tmp.append([float(a[0]), float(a[1]), float(a[2])])
        totel_list.append(tmp)
    return totel_list

def limite(l,pn):
    all_time_list = []
    for index in l:
        all_time = 0
        for num in range(len(pn),len(index)):
            all_time += index[num][2]
        all_time_list.append(int(all_time/5))
    return all_time_list

def private_cloud(l):
    '''
    this func is to get the tasks works on the private cloud in each time slot
    :return:
    '''
    private_running_time = []
    private_num_list = []
    for index in l:

        num_tasks = 0
        time_of_task = 0
        core_record = 0
        mem_record = 0
        for member in index:
            core_record += member[0]
            mem_record += member[1]
            num_tasks += 1
            time_of_task += member[2]
            if core_record >= parameter_list.CPUmax or mem_record >= parameter_list.MEMmax:
                break
        private_num_list.append(num_tasks)
        private_running_time.append(time_of_task)
    return private_num_list, private_running_time


if __name__ == '__main__':
    pkl_file = open('data_middle.pkl', 'rb')

    LIST = pickle.load(pkl_file)

    print([len(x) for x in LIST])
    private_num_list, private_running_time = private_cloud(LIST)

    Limite = limite(LIST,private_num_list)
    Limite_ = [Limite[i:i+8] for i in range(0,len(Limite),8)]
    Limite__ = []
    for index in Limite_:
        Limite__.append(max(index))
    print(Limite__)

    last_num = 0
    a_list = []
    b_list = []
    profit = []
    for hour_num in range(0, 6):

        if hour_num == 0:
            last_num = 0

        a, b = OPOS(LIST, hour_num, private_num_list, private_running_time, last_num, Limite__)

        a_list.append(a)
        b_list.append(b)

        last_num = max(a.y1,a.y2,a.y3,a.y4,a.y5,a.y6,a.y7,a.y8)
        print(b)
    OD = []
    SI = []

    for index in a_list:
        OD.append(index.x)
        OD.append(index.x)
        OD.append(index.x)
        OD.append(index.x)
        OD.append(index.x)
        OD.append(index.x)
        OD.append(index.x)
        OD.append(index.x)
        SI.append(index.y1)
        SI.append(index.y2)
        SI.append(index.y3)
        SI.append(index.y4)
        SI.append(index.y5)
        SI.append(index.y6)
        SI.append(index.y7)
        SI.append(index.y8)


    print(OD)
    print(SI)
    print(b_list)
    index = np.arange(48)
    bar_width = 0.3
    plt.plot(index, OD, color='y',marker = 'o')
    plt.plot(index, SI, color='b',marker = 'x')
    plt.show()
