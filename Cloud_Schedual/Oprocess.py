from Cloud_Schedual.caculation_process import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import pickle


# TODO：现在基本的ICOA功能已经实现，但是在ICOA运算概率的时候还是使用硬编码方法

def ICOAO(l, hour, pn, prt, m, n, ln):
    '''

    :param l:
    :param hour:
    :param pn:
    :param m:
    :param n:
    :return: 返回在一小时的8个time slot中每一个time slot使用的spotintance时间和一个小时中使用的ondemand总时间
    '''
    divide = [l[i:i + 8] for i in range(0, len(l), 8)][hour]
    pn_divide = [pn[i:i + 8] for i in range(0, len(pn), 8)][hour]
    left = []  # 里面装的是所有在spotinstance里面剩下来的拼在一起

    OD_time = 0
    OD_num = []
    num_list = [0]  # 里面是spotinstance的标志位置
    num_SSP = []
    forthepicOD = []
    for num in range(8):
        OD_sum_time = 0
        OD_sum_number = 0
        for nn in divide[num][pn_divide[num]:]:

            OD_sum_time += nn[2]
            OD_sum_number += 1
            if OD_sum_time >= m * 7.5:
                OD_time += OD_sum_time - nn[2]
                OD_num.append(OD_sum_number - 1)
                forthepicOD.append(OD_sum_time-nn[2])
                break
        if len(OD_num) < num +1:
            OD_num.append(OD_sum_number)
            OD_time += OD_sum_time
            forthepicOD.append(OD_sum_time)
        num_list.append(num_list[-1] + len(divide[num]) - pn_divide[num] - OD_sum_number)
        left += divide[num][pn_divide[num] + OD_sum_number:]
        num_SSP.append(len(divide[num]) - pn_divide[num] - OD_sum_number)
    SP_time_1 = []
    SP_time_2 = []
    # SP_num = []
    num_record = 0  # 记录当前处理到什么位置了

    for num in range(8):
        #减去之后又加上真的是一波神奇操作
        SP_sum_time_1 = 0
        SP_sum_time_2 = 0
        # print(p*n)
        if num != 0 and num_record < num_list[num - 1]:
            # print('hour'+str(hour)+'time slot'+str(num+1)+'abandon number'+str(num_list[num-1] - num_record))
            num_record = num_list[num - 1]
        for index in left[num_record:num_list[num + 1]]:
            if num_record < num_list[num]:
                SP_sum_time_2 += index[2]
            else:
                SP_sum_time_1 += index[2]
            num_record += 1
            # SP_num_sum += 1
            if SP_sum_time_1 + SP_sum_time_2 >= 5 * n[num]:
                SP_time_1.append(SP_sum_time_1 - index[2])
                SP_time_2.append(SP_sum_time_2)
                # SP_num.append(SP_num_sum - 1)
                break
        if len(SP_time_1) < num + 1:
            SP_time_1.append(SP_sum_time_1)
            SP_time_2.append(SP_sum_time_2)


    prta = sum(prt[hour * 8:hour * 8 + 8])

    cost_private = 0.02 * 0.05 * prta
    on_demand_cost = 0.1 * OD_time
    up_rate = 0.01 * 0.1 * np.exp(0.0018 * int(ln)) / (
            0.1 + 0.01 * (np.exp(0.0018 * int(ln)) - 1))
    # print(up_rate)
    uprise = []
    for index in n:
        up_date_time_slot =0.01+ 0.01 * 0.1 * np.exp(0.0018 * int(index)) / (0.1 + 0.01 * (np.exp(0.0018 * int(index)) - 1))
        uprise.append(up_date_time_slot*int(index))

    # print("SP_cost "+str(cost_spot_instance))
    # cost = (cost_private + on_demand_cost + cost_spot_instance)/ 60 + int(int(max(n))/200)*10+50
    excost = 0
    if int(max(n)/20)<20: excost = int(max(n)/20)*0.8
    if 20<=int(max(n)/20)<40: excost = (int(max(n)/20)-20)*1.0+20*0.8
    if 40<=int(max(n)/20): excost = (int(max(n)/20)-40)*1.2+20*0.8+20*1.0

    cost = (cost_private + on_demand_cost + sum(uprise))/ 60 + excost
    # print("cost "+str(cost))
    reward = 0.48 * (OD_time + sum(SP_time_1)+sum(SP_time_2)+ prta) / 60
    # print("reward "+str(reward))
    # print("OD: "+str(OD_time) + " SP: "+ str(sum(SP_time_1)+sum(SP_time_2)))
    for i in range(8):
        print(0.48*(forthepicOD[i]+SP_time_1[i]+SP_time_2[i]+prt[hour*8 + i])/60- (uprise[i]*7.5*0.03+forthepicOD[i]*0.1+prt[hour*8 + i]*0.02*0.05)/60-excost/8)
    return reward - cost, OD_num, num_SSP



def ProC(price, num):
    f =  0.012 * 0.1 * np.exp(0.0018 * num) / (
            0.1 + 0.012 * (np.exp(0.0018 * num) - 1)) - 0.012
    low = 0.01 + f
    middle = 0.014 + f
    up = 0.02 + f
    x = symbols('x')
    probability = 0
    if price < low: price = low
    if price > up: price = up
    if price < middle:
        probability = integrate(2 * (x - 0.01 - f) / (0.01 * 0.004), (x, low, price))
    if price >= middle:
        probability = integrate(2 * (x - 0.02 - f) / (0.01 * - 0.006), (x, middle, price)) + 0.4

    return probability






