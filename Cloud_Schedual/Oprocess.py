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
    up_rate = 0.012 * 0.1 * np.exp(0.0018 * int(ln)) / (
            0.1 + 0.012 * (np.exp(0.0018 * int(ln)) - 1))
    # print(up_rate)
    cost_spot_instance = int(sum(n)) * 7.5 * (0.03)
    # print("SP_cost "+str(cost_spot_instance))
    # cost = (cost_private + on_demand_cost + cost_spot_instance)/ 60 + int(int(max(n))/200)*10+50
    cost = (cost_private + on_demand_cost + cost_spot_instance)/ 60 + int(max(n)/20) * 0.3
    # print("cost "+str(cost))
    reward = 0.48 * (OD_time + sum(SP_time_1)+sum(SP_time_2)+ prta) / 60
    # print("reward "+str(reward))
    # print("OD: "+str(OD_time) + " SP: "+ str(sum(SP_time_1)+sum(SP_time_2)))
    for i in range(8):
        print(0.48*(forthepicOD[i]+SP_time_1[i]+SP_time_2[i]+prt[hour*8 + i])/60- (n[i]*7.5*0.03+forthepicOD[i]*0.1+prt[hour*8 + i]*0.02*0.05)/60-int(max(n)/200)*3/8)
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


# TODO:完成利润计算函数，spotinstance挣得钱按照其运行时间计算，spotinstance的花销按照成功运行的个数计算
# def Oprofit(hour, prt, a, b, np):
#     prt = sum(prt[hour * 8:hour * 8 + 8])
#
#     cost_private = 0.02 * 0.05 * prt / 60
#     on_demand_cost = 0.1 * a / 60
#
#     cost_spot_instance = 0
#     up_rate = price_up(np)
#     for num in range(8):
#         cost_spot_instance += np * 5 * (0.012 + up_rate * num)
#
#     cost = cost_private + on_demand_cost + cost_spot_instance / 60
#     reward = 0.48 * (a + b + prt) / 60
#
#     return reward - cost


if __name__ == '__main__':
    pkl_file = open('data_middle.pkl', 'rb')

    LIST = pickle.load(pkl_file)

    pn, prn = private_cloud(LIST)
    profit,OD,SP = ICOAO(LIST,0,pn,prn,1298.9442859466426,361.52079575239316,0)
    print(profit)
    print(OD)
    print(SP)
    # print("======================================================")
    # profit,OD,SP = ICOAO(LIST,0,pn,prn,870,0,0)
    # print(profit)
    # print(OD)
    # print(SP)
    # # _a_ = [701.2616067681188, 677.7488572878719, 727.9356096840606, 662.632381703391, 588.1993695485905,
    # #        846.7645340760077]
    # # _b_ = [5384.906545564749, 6332.2033312159665, 5022.614347773253, 5232.786207775275, 6898.162618489105,
    # #        4782.889296762429]
    # # a = [668, 5462]
    # # b = [0, 30000]
    # # TODO:此处要做一个辨识函数
    # OD_task = []
    # SP_task = []
    #
    # for num in range(6):
    #     if num == 0:
    #         ln = 0
    #     profit, ln, task_OD, task_SP = ICOAO(LIST,num,pn,prn,_a_[num],_b_[num],ln)
    #     OD_task +=task_OD
    #     SP_task +=task_SP
    #
    # reject = [0 for x in range(50)]
    # x = [x * 7.5 for x in range(48)]
    # x.insert(len(x),360.0)
    # x.insert(len(x),367.5)
    # OD_task.insert(0,0)
    # OD_task.insert(len(OD_task),0)
    # SP_task.insert(0,0)
    # SP_task.insert(len(SP_task),0)
    # pn.insert(0,0)
    # pn.insert(len(pn),0)
    #
    #
    # plt.plot(x, OD_task, color='r', marker='o', mec='r', mfc='r', label = 'on demand instance')
    # plt.plot(x, SP_task, color='blue', marker='o', mec='blue', mfc='blue', label = 'spot instance')
    # plt.plot(x, pn, color='green', marker='o', mec='green', mfc='green', label = 'private cloud')
    # plt.plot(x, reject, color='y', marker='o', mec='y', mfc='y', label = 'rejected')
    # plt.xlabel('time(min)',fontsize = 20)
    # plt.ylabel('number of scheduled tasks per 7.5 mins',fontsize = 15)
    # axs = plt.gca()
    # axs.set_ylim(0,2500)
    # plt.legend()
    # plt.savefig('number_pic')
    # plt.show()
    # # plt.savefig('number_pic')
    # plt.close()
    #
