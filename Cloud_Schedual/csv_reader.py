"""
this programme is to divide the google data into the doc data as 48 pieses
these 48 piese has not been select by the random algorithm
"""
import csv
import pickle
import numpy as np

csv_reader = csv.reader(open("/home/hdl/PycharmProjects/yunjisuan/google-cluster-data-1.csv","r"))

time_slot = 0
num_list = []
totel_list = []
for index in csv_reader:
    if index[0].split(" ")[0] == 'Time':
        continue
    now_num = (int(index[0].split(" ")[0])-90000)/300
    if time_slot == now_num:
        pass
    else:
        time_slot = now_num
        totel_list.append(num_list)
        num_list = []
    core = index[0].split(" ")[4]
    mem = index[0].split(" ")[5]

    num_list.append([float(core),float(mem)])

for num in range(1,49):
    a = np.array(totel_list[num])
    np.savetxt('data/data_'+str(num)+'.txt',a)